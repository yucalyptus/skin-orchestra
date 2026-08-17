#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — 本文/*.md を、1章＝1ページの静的サイトにビルドする。

出力は docs/index.html（表紙＋全章の目次）と、章ごとの docs/ch01.html … docs/final.html。
全57章を1ページに積むと1.2MBになり読み進められないので、ページを分けている。
左ナビ・本文中の「→ 第N章」リンク・章末の前後リンクは、すべて下の MANIFEST の並び順から作る。

使い方:
    python3 build.py
    ※ Pillow が無いと PNG→WebP 変換が黙って効かず docs/images が肥大する。README の一時venvを使う。
"""
import datetime
import io
import os
import re
import shutil
import subprocess
import sys

try:
    from PIL import Image
except ImportError:
    # Pillow が無いと、図が WebP に変換されず PNG のまま docs/ に出る。
    # 以前これに気づかず公開してしまったので、黙って続行させない。
    # Pillow を持つ別の python が居れば、そちらへ入れ替えて実行し直す。
    _CANDIDATES = [
        "/opt/homebrew/opt/python@3.13/bin/python3.13",
        "/opt/homebrew/opt/python@3.12/bin/python3.12",
        "/opt/homebrew/opt/python@3.11/bin/python3.11",
        "/usr/local/opt/python@3.11/bin/python3.11",
        "/usr/bin/python3",
    ]
    _found = None
    for _cand in _CANDIDATES:
        if os.path.exists(_cand) and _cand != sys.executable:
            _probe = subprocess.run(
                [_cand, "-c", "import PIL"],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            if _probe.returncode == 0:
                _found = _cand
                break
    if _found:
        sys.stderr.write(
            "この python には Pillow がありません（%s）。\n"
            "図を WebP に変換できないので、%s で実行し直します。\n\n"
            % (sys.executable, _found)
        )
        os.execv(_found, [_found] + sys.argv)
    sys.stderr.write(
        "エラー：Pillow がありません（%s）。\n"
        "このまま続けると、図が WebP にならず PNG のまま docs/ に出力され、\n"
        "公開サイトの画像が全点入れ替わります。ビルドを中止しました。\n\n"
        "  対処： python3 -m pip install --user Pillow\n"
        "         （Homebrew の python で PEP 668 に弾かれる場合は --break-system-packages を付けるか、\n"
        "           Pillow の入った別の python3 で build.py を実行してください）\n"
        % sys.executable
    )
    sys.exit(1)

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(ROOT, "chapters")      # 本文。章の正体は front matter の id
FIG_DIR = os.path.join(ROOT, "figures")       # 図のソースPNG
TOC_FILE = os.path.join(ROOT, "目次.yml")     # 並び順の正典。順番を持つのはここだけ

# --preview のときだけ _preview/ へ出し、未承認の章も入れる（gitignore 済み）。
PREVIEW = "--preview" in sys.argv
OUT_DIR = os.path.join(ROOT, "_preview" if PREVIEW else "docs")
OUT = os.path.join(OUT_DIR, "index.html")

# 公開先。canonical・OGP・sitemap.xml の絶対URLを組むのに使う。
BASE_URL = "https://yucalyptus.github.io/skin-orchestra/"
OG_DEFAULT = "images/巻頭_本教材が守る切り分け.webp"

# 公開・更新から何日「NEW」「更新」バッジを出すか。
NEW_DAYS = 14

# ▼▼▼ 感想フォームのURLはここに入れる（Googleフォームの共有リンク）▼▼▼
# 空のままにすると、フッターの感想欄そのものが出力されない。
FEEDBACK_URL = "https://docs.google.com/forms/d/e/1FAIpQLSd8Cw6652qaE6gRcVhSjbDO0HoRwTkypatWEvGkLonF3Fk9cA/viewform"

# ---------------------------------------------------------------------------
# 定数ブロック（docs/index.html からそのまま再利用）
# ---------------------------------------------------------------------------

PAGE_HEAD = '''<!DOCTYPE html>
<html lang="ja"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noai, noimageai">
<meta name="author" content="Yuka Aoki, MD">
<title>{{TITLE}}</title>
<meta name="description" content="{{DESC}}">
<link rel="canonical" href="{{URL}}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="生化学で見る美容医療">
<meta property="og:locale" content="ja_JP">
<meta property="og:title" content="{{TITLE}}">
<meta property="og:description" content="{{DESC}}">
<meta property="og:url" content="{{URL}}">
<meta property="og:image" content="{{IMAGE}}">
<meta name="twitter:card" content="summary_large_image">
<style>
:root{
--bg:#f4f3f0;--paper:#ffffff;--ink:#1c1d23;--sub:#494c54;--faint:#6b6e77;
--line:#e7e5df;--rule:#cdcbc4;--accent:#1d4f91;--accent-line:#b9cde8;--accent-bg:#f2f6fc;--soft:#f1f2f4;
--col-bg:#fdf1f4;--col-line:#edc9d5;--col-ink:#b5476a;
--serif:"Hiragino Mincho ProN","Yu Mincho",YuMincho,"Noto Serif JP",serif;
--sans:-apple-system,BlinkMacSystemFont,"Hiragino Kaku Gothic ProN","Noto Sans JP",sans-serif;
--mono:ui-monospace,SFMono-Regular,Menlo,"Courier New",monospace;
}
@media(prefers-color-scheme:dark){:root{
--bg:#15161a;--paper:#1b1d21;--ink:#eceae6;--sub:#b6b9c0;--faint:#9a9da5;
--line:#2c2e34;--rule:#3b3d44;--accent:#82b1e8;--accent-line:#33506f;--accent-bg:#1b2330;--soft:#24272d;
--col-bg:#2c2126;--col-line:#4d3740;--col-ink:#f0a0b8;}}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--serif);
font-size:17px;line-height:2.0;letter-spacing:.02em;-webkit-font-smoothing:antialiased}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
a.chref{border-bottom:1px solid var(--accent-line);white-space:nowrap}

/* ---- 骨格 ---- */
.wrap{display:flex;max-width:1180px;margin:0 auto}
.side{width:272px;flex:none;position:sticky;top:0;height:100vh;overflow:auto;
padding:28px 16px 48px;background:var(--paper);border-right:1px solid var(--line);font-family:var(--sans)}
.brand{display:block;font-size:13.5px;font-weight:700;line-height:1.55;color:var(--ink)}
.brand:hover{text-decoration:none;color:var(--accent)}
.brand small{display:block;font-weight:400;font-size:11px;color:var(--sub);margin-top:4px;letter-spacing:.02em}
.toc{margin-top:22px;font-size:13px;line-height:1.65}
.toc .part{margin:22px 0 6px;padding:0 8px;color:var(--faint);font-size:11px;font-weight:700;letter-spacing:.09em}
.toc a{display:block;padding:4px 8px;border-radius:5px;color:var(--sub)}
.toc a:hover{background:var(--soft);text-decoration:none}
.toc a.active{background:var(--soft);color:var(--accent);font-weight:700}
.main{flex:1;min-width:0;background:var(--paper);padding:56px clamp(18px,5vw,64px) 88px}
.col{max-width:40em;margin:0 auto;counter-reset:fig}

/* ---- 見出し ---- */
.kicker{font-family:var(--sans);font-size:12px;font-weight:700;letter-spacing:.1em;
color:var(--accent);margin:0 0 12px}
h1{font-family:var(--sans);font-size:clamp(21px,2.8vw,26px);font-weight:700;line-height:1.55;
margin:0 0 30px;padding-bottom:20px;border-bottom:1px solid var(--rule);letter-spacing:.01em}
h2{font-family:var(--sans);font-size:16.5px;font-weight:700;line-height:1.65;margin:58px 0 14px;
color:var(--accent);padding-bottom:9px;border-bottom:1px solid var(--accent-line)}
h3{font-family:var(--sans);font-size:14.5px;font-weight:700;line-height:1.7;margin:34px 0 8px;color:var(--ink)}
p{margin:17px 0}
strong{font-weight:700}

/* ---- 引用（章の入口・この章の一言） ---- */
blockquote{margin:28px 0;padding:2px 0 2px 20px;border-left:2px solid var(--rule);color:var(--sub)}
blockquote.lead{border-left:3px solid var(--accent);color:var(--ink);background:var(--accent-bg);
padding:18px 22px;border-radius:0 6px 6px 0;margin:26px 0}

/* ---- 矢印フロー ---- */
.flow{display:flex;flex-wrap:wrap;align-items:center;gap:7px;margin:28px 0;font-family:var(--sans);font-size:13.5px;line-height:1.75}
.flow .node{background:var(--paper);border:1px solid var(--accent-line);border-radius:4px;padding:6px 11px}
.flow .arr{color:var(--accent);font-size:14px}
.flow.vert{flex-direction:column;align-items:flex-start;gap:3px}
.flow.vert .arr{margin-left:16px}
.flow.diagram{background:var(--accent-bg);border-radius:8px;padding:18px 20px}
.flow.vert.diagram .node{display:flex;align-items:baseline;width:100%;max-width:34em}
.flow .num{display:inline-flex;align-items:center;justify-content:center;width:18px;height:18px;
border-radius:50%;background:var(--accent);color:#fff;font-size:10.5px;font-weight:700;margin-right:9px;flex:none}

/* ---- 図 ---- */
figure.book-figure{margin:36px 0;counter-increment:fig}
.book-figure img{display:block;width:100%;height:auto;margin:0 auto;border:1px solid var(--line);cursor:zoom-in}
.book-figure.tall img{max-width:420px}
.book-figure.square img{max-width:600px}
.book-figure.zoom img{max-width:100%;cursor:zoom-out}
.book-figure figcaption{margin-top:11px;font-family:var(--sans);font-size:13px;line-height:1.85;color:var(--sub)}
/* まとめ図は帯を付けて、章の締めであることをHTML側で示す */
.book-figure.summary{background:var(--accent-bg);border:1px solid var(--accent-line);border-radius:8px;
overflow:hidden;padding-bottom:14px}
.book-figure.summary .fig-label{margin:0 0 14px;padding:9px 16px;background:var(--accent);color:#fff;
font-family:var(--sans);font-size:11px;font-weight:700;letter-spacing:.14em}
.book-figure.summary img{border:none;border-radius:0}
.book-figure.summary figcaption{padding:0 16px}
.book-figure figcaption::before{content:"図" counter(fig) "　";font-weight:700;color:var(--accent)}
.figslot{margin:32px 0;padding:18px 20px;border:1px dashed var(--rule);border-radius:6px;
font-family:var(--sans);font-size:12.5px;line-height:1.8;color:var(--sub)}
.figslot .fs-icon{display:none}
.fs-path{color:var(--faint)}
.inlineslot{font-family:var(--sans);font-size:12.5px;color:var(--sub);border-bottom:1px dashed var(--rule)}

/* ---- 表 ---- */
.tblwrap{overflow-x:auto;margin:30px 0}
table{border-collapse:collapse;width:100%;min-width:400px;font-family:var(--sans);font-size:14px;line-height:1.85}
th,td{padding:11px 14px 11px 0;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}
th:not(:last-child),td:not(:last-child){padding-right:20px}
thead th{background:var(--accent-bg);border-top:1px solid var(--accent-line);
border-bottom:1px solid var(--accent-line);color:var(--accent);font-size:13px;font-weight:700;
letter-spacing:.03em;padding:11px 14px}
tbody tr:last-child td{border-bottom:1px solid var(--rule)}

/* ---- リスト ---- */
ul,ol{padding-left:1.5em;margin:17px 0}
li{margin:7px 0}
ul.goal,ol.goal{background:var(--accent-bg);border-radius:8px;padding:22px 26px 22px 46px;margin:30px 0}
ul.goal li::marker,ol.goal li::marker{color:var(--accent);font-weight:700}
ul.goal li,ol.goal li{margin:8px 0}
ul.evidence{list-style:none;padding:18px 0;margin:30px 0;border-top:2px solid var(--accent-line);border-bottom:2px solid var(--accent-line)}
ul.evidence li{margin:9px 0;padding-left:0;font-size:15px;line-height:1.85}

/* ---- その他の要素 ---- */
code{font-family:var(--mono);background:var(--soft);border-radius:3px;padding:1px 5px;font-size:.85em}
pre.code{font-family:var(--sans);background:var(--soft);border-radius:8px;padding:16px 18px;
font-size:12.5px;line-height:1.95;overflow-x:auto;margin:28px 0}
hr{border:none;border-top:1px solid var(--line);margin:36px 0}

/* ---- 前後の章 ---- */
.pager{display:flex;gap:20px;margin:72px 0 0;padding-top:26px;border-top:1px solid var(--rule);
font-family:var(--sans);font-size:13.5px;line-height:1.75}
.pager a{display:block;max-width:46%;color:var(--sub)}
.pager a:hover{color:var(--accent);text-decoration:none}
.pager .lbl{display:block;font-size:11.5px;color:var(--accent);margin-bottom:4px;letter-spacing:.06em;font-weight:700}
.pager .next{margin-left:auto;text-align:right}

/* ---- 扉（表紙） ---- */
/* 囲みは使わない。紙の上に、字と余白と五線だけで組む。*/
.cover{position:relative;text-align:center;
padding:clamp(40px,8vw,92px) 0 clamp(40px,6vw,64px);margin-bottom:clamp(36px,5vw,58px)}
/* 背景の五線 ―― 副題（オーケストラ）に掛けた譜面。中央は伏せて題字を邪魔しない。*/
.cover::before{content:"";position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
width:min(880px,104%);height:168px;pointer-events:none;
background:repeating-linear-gradient(to bottom,var(--accent) 0 1px,transparent 1px 27px);
-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 16%,#000 84%,transparent 100%);
mask-image:linear-gradient(90deg,transparent 0,#000 16%,#000 84%,transparent 100%);opacity:.45}
.cover > *{position:relative}
/* 文字の幅ぶんだけ紙を抜いて、五線が字に重ならないようにする（囲みではない）*/
.cover-en,.cover-title,.cover-sub,.cover-author{background:var(--paper);display:table;
margin-left:auto;margin-right:auto}
.cover-en{font-family:var(--sans);font-size:11.5px;font-weight:700;letter-spacing:.34em;
text-transform:uppercase;color:var(--accent);margin:0 auto clamp(26px,4vw,40px);padding:2px 22px 2px calc(22px + .34em)}
.cover-title{font-family:var(--serif);font-weight:400;font-size:clamp(28px,5.8vw,50px);line-height:1.45;
letter-spacing:.12em;color:var(--ink);margin:0 auto;border:none;padding:8px .55em 8px calc(.55em + .12em)}
.cover-sub{margin:clamp(18px,3vw,28px) auto 0;font-size:clamp(14.5px,2.2vw,19px);
font-weight:400;letter-spacing:.2em;color:var(--accent);padding:6px 1.1em 6px calc(1.1em + .2em)}
.cover-sub::before{content:"";display:block;width:44px;height:1px;background:var(--accent-line);
margin:0 auto clamp(18px,3vw,28px)}
.cover-author{font-family:var(--sans);font-size:12px;font-weight:700;letter-spacing:.2em;
color:var(--faint);margin:clamp(34px,5vw,48px) auto 0;padding:4px 20px 4px calc(20px + .2em)}

/* ---- 表紙の説明・目次 ---- */
.hero{margin:0 0 8px}
.hero .lede{color:var(--ink);margin:0;font-size:16.5px}
.flowline{display:block;margin-top:26px;padding:16px 0;border-top:1px solid var(--line);
border-bottom:1px solid var(--line);font-family:var(--sans);font-size:12px;letter-spacing:.06em;
color:var(--sub);text-align:center}
.note{font-family:var(--sans);font-size:13.5px;line-height:1.95;color:var(--sub);margin-top:22px}
.contents{margin-top:64px}
.part-block{margin:0 0 36px}
.part-title{font-family:var(--sans);font-size:11.5px;font-weight:700;letter-spacing:.09em;color:var(--faint);
padding-bottom:9px;border-bottom:1px solid var(--rule);margin-bottom:2px}
.toc-list{list-style:none;padding:0;margin:0}
.toc-list li{margin:0}
.toc-list a{display:block;padding:11px 6px;border-bottom:1px solid var(--line);color:var(--ink);
font-size:15px;line-height:1.75}
.toc-list a:hover{background:var(--soft);text-decoration:none}
.sec-rule{margin:72px 0 0;padding-top:8px;border-top:1px solid var(--rule)}
.disc{margin:72px 0 0;padding-top:24px;border-top:1px solid var(--line);
font-family:var(--sans);font-size:12.5px;line-height:1.95;color:var(--sub)}

/* ---- 根拠表示の付け方の注記。本文より一段控えめに ---- */
.scope-note{margin-top:26px;padding:14px 18px;background:var(--accent-bg);
border-left:2px solid var(--accent-line);font-size:15px;line-height:1.9}

/* ---- 「はじめに」の案内欄。本文より一段控えめに ---- */
.notice{margin:38px 0 0;padding:16px 20px;background:var(--soft);
border-left:2px solid var(--rule);font-family:var(--sans);
font-size:14px;line-height:1.95;color:var(--sub)}
.notice p{margin:0 0 10px}
.notice p:last-child{margin:0}
.notice-t{font-weight:700;color:var(--ink)}

/* ---- 全ページ共通フッター ---- */
.sitefoot{margin:72px 0 0}
.feedback{padding:22px 24px;background:var(--soft);border:1px solid var(--line);
border-radius:8px;font-family:var(--sans);font-size:14px;line-height:1.9;color:var(--sub)}
.feedback p{margin:0 0 12px}
.fb-t{font-size:15px;font-weight:700;color:var(--ink)}
.fb-btn{display:inline-block;max-width:100%;padding:9px 20px;
border:1px solid var(--accent);border-radius:6px;
color:var(--accent);font-size:13.5px;font-weight:700}
.fb-btn:hover{background:var(--accent);color:var(--paper);text-decoration:none}
.fb-btn:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.fb-note{margin:0;font-size:12px;color:var(--faint)}
.sitefoot .stamp{margin:24px 0 0}
.sitefoot .disc{margin:6px 0 0}

/* ---- モバイル ---- */
.menubtn{display:none;position:fixed;left:14px;top:14px;z-index:60;font-family:var(--sans);font-size:13px;
background:var(--paper);color:var(--ink);border:1px solid var(--rule);border-radius:6px;padding:8px 13px;
box-shadow:0 2px 12px rgba(0,0,0,.10)}
@media(max-width:900px){
.wrap{display:block}
.side{position:fixed;left:0;top:0;z-index:50;width:min(84vw,300px);transform:translateX(-100%);
transition:transform .22s;box-shadow:2px 0 18px rgba(0,0,0,.12)}
.side.open{transform:none}
.menubtn{display:block}
.main{padding:66px 20px 64px}
body{font-size:16px;line-height:1.95}
h2{margin-top:46px}
}
/* ---- 文献への外部リンク ---- */
a.ext{border-bottom:1px dotted var(--accent-line);white-space:nowrap}
a.ext::after{content:"↗";font-size:.75em;vertical-align:.35em;margin-left:.15em;opacity:.7}

/* ---- 章内目次 ---- */
.chaptoc{margin:34px 0 8px;padding:14px 18px;background:var(--soft);
border-left:3px solid var(--accent-line);font-family:var(--sans)}
.chaptoc-t{margin:0 0 6px;font-size:12px;font-weight:700;color:var(--faint);letter-spacing:.08em}
/* 横並びにすると、和文の長い節タイトルが折り返して項目の切れ目が見えなくなる。1行1節。 */
.chaptoc ul{margin:0;padding:0;list-style:none;display:grid;gap:2px}
.chaptoc li{font-size:13.5px;line-height:1.7;padding-left:0}
.chaptoc a{color:var(--sub)}
.chaptoc a:hover{color:var(--accent)}

/* ---- 左ナビの凡例と絞り込み ---- */
.legend{margin:2px 0 12px;font-size:11.5px;line-height:1.65;color:var(--faint)}
.navfilter{width:100%;margin:0 0 12px;padding:7px 10px;font-family:var(--sans);font-size:13px;
color:var(--ink);background:var(--bg);border:1px solid var(--line);border-radius:5px}
.navfilter:focus{outline:2px solid var(--accent-line);outline-offset:1px}
.toc a.hide,.toc .part.hide{display:none}

/* ---- キーボード操作の可視化 ---- */
figure.book-figure:focus-visible,.menubtn:focus-visible,.toc a:focus-visible{
outline:2px solid var(--accent);outline-offset:2px}

/* ---- 平易版／専門版の切り替え ---- */
.readmode{display:flex;align-items:center;gap:8px;margin:0 0 26px;
font-family:var(--sans);font-size:12.5px;color:var(--faint)}
.readmode-sw{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden}
.readmode-sw button{appearance:none;border:0;padding:5px 14px;cursor:pointer;
font-family:var(--sans);font-size:12.5px;color:var(--sub);background:var(--paper)}
.readmode-sw button[aria-pressed="true"]{background:var(--accent);color:#fff;font-weight:700}
.readmode-sw button:focus-visible{outline:2px solid var(--accent);outline-offset:-2px}
.easy{display:none}
body.mode-easy .easy{display:block}
body.mode-easy .pro{display:none}

/* ---- 用語のツールチップ ---- */
.term{border-bottom:1px dotted var(--accent);cursor:help}
.term:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:2px}
#tip{position:absolute;z-index:60;max-width:340px;padding:12px 15px;
background:var(--paper);border:1px solid var(--accent-line);border-radius:8px;
box-shadow:0 8px 28px rgba(0,0,0,.16);font-family:var(--sans);
font-size:13.5px;line-height:1.8;color:var(--ink);display:none}
#tip.on{display:block}
#tip .tip-t{font-weight:700;font-size:14px;margin-bottom:5px}
#tip .tip-l{display:block;margin-top:9px;font-size:12px;color:var(--accent)}
.g-ch{font-family:var(--sans);font-size:12.5px;color:var(--sub);white-space:normal}

/* ---- 版と最終更新 ---- */
.stamp{margin:0 0 6px;font-family:var(--sans);font-size:11.5px;color:var(--faint)}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;
clip:rect(0 0 0 0);white-space:nowrap;border:0}
@media(max-width:900px){
.feedback{padding:18px 16px}
}
@media print{
.side,.menubtn,.pager,.chaptoc,.navfilter,.feedback{display:none}
.wrap{display:block}.main{padding:0;background:#fff}
body{background:#fff;font-size:10.5pt;line-height:1.8}
h2{margin-top:24pt}
}

/* ---- セクションと部の扉（目次） ---- */
.sec-block{margin:0 0 42px}
.sec-title{font-family:var(--sans);font-size:19px;font-weight:700;letter-spacing:.02em;
  margin:0 0 4px;padding:0 0 8px;border-bottom:2px solid var(--ink)}
.sec-title small{display:block;font-size:12px;font-weight:400;color:var(--faint);
  letter-spacing:.06em;margin-top:4px}
.sec-intro{margin:10px 0 20px;font-size:13.5px;line-height:1.8;color:var(--sub)}
.part-intro{margin:2px 0 9px;padding:0 6px;font-size:12.5px;line-height:1.75;color:var(--faint)}
/* ---- 左ナビのセクション見出し ---- */
.toc .sec{margin:26px 0 2px;padding:0 8px;color:var(--ink);font-size:11.5px;
  font-weight:700;letter-spacing:.09em;border-bottom:1px solid var(--line);padding-bottom:5px}
/* ---- NEW / 更新 / 準備中 ---- */
.badge{display:inline-block;margin-left:6px;padding:1px 6px;border-radius:3px;
  font-family:var(--sans);font-size:9.5px;font-weight:700;letter-spacing:.06em;vertical-align:middle}
.badge.bnew{background:var(--accent);color:#fff}
.badge.bupd{background:#fff;color:var(--accent);border:1px solid var(--accent)}
.badge.bst{background:#f4f1e8;color:#8a7a52;border:1px solid #ddd3b4}
.toc-list li.soon{display:block;padding:11px 6px;border-bottom:1px solid var(--line);color:var(--faint)}
.toc .soon{display:block;padding:4px 8px;font-size:13px;color:var(--faint)}
.soon em{font-style:normal;margin-left:8px;font-size:10.5px;letter-spacing:.06em;opacity:.85}
/* ---- 最近の更新・更新履歴 ---- */
.recent{margin:24px 0 32px;padding:16px 18px;background:var(--soft);border-radius:8px}
.rc-t{margin:0 0 10px;font-family:var(--sans);font-size:11.5px;font-weight:700;
  letter-spacing:.09em;color:var(--faint)}
.recent ul,.cl{list-style:none;margin:0;padding:0}
.recent li,.cl li{display:flex;flex-wrap:wrap;align-items:baseline;gap:9px;padding:7px 0;
  font-size:13.5px;line-height:1.65;border-bottom:1px solid var(--line)}
.recent li:last-child,.cl li:last-child{border-bottom:0}
.recent time,.cl time{font-family:var(--sans);font-size:11.5px;color:var(--faint);white-space:nowrap}
.k{font-family:var(--sans);font-size:10px;font-weight:700;letter-spacing:.06em;
  padding:1.5px 6px;border-radius:3px;white-space:nowrap}
.k.new{background:var(--accent);color:#fff}
.k.upd{background:#fff;color:var(--accent);border:1px solid var(--accent)}
.recent .note,.cl .note{flex:1 1 100%;font-size:12.5px;color:var(--sub);line-height:1.7}
.rc-more{margin:11px 0 0;font-size:12.5px}
.cl-date{font-family:var(--sans);font-size:13px;letter-spacing:.04em;margin:28px 0 6px;color:var(--sub)}
/* ---- 章の見出し・日付・更新 ---- */
.ch-title{margin:2px 0 6px}
.ch-title small{display:block;font-family:var(--sans);font-size:12.5px;font-weight:400;
  color:var(--faint);letter-spacing:.04em;margin-top:6px}
.dateline{margin:0 0 24px;font-family:var(--sans);font-size:11.5px;color:var(--faint)}
.ch-history{margin:32px 0 0;padding:14px 18px;background:var(--soft);border-radius:8px}
.chh-t{margin:0 0 7px;font-family:var(--sans);font-size:11.5px;font-weight:700;
  letter-spacing:.08em;color:var(--faint)}
.ch-history ul{list-style:none;margin:0;padding:0}
.ch-history li{display:flex;gap:11px;font-size:12.5px;line-height:1.75;padding:3px 0}
.ch-history time{font-family:var(--sans);font-size:11.5px;color:var(--faint);white-space:nowrap}
@media print{.recent,.ch-history,.dateline .badge{display:none}}

/* ---- コラム ---- */
/* 本筋から外れる話の受け皿。読み飛ばしても筋は通る。
   地の文は明朝なので、ここだけゴシックにして「別の声」であることを書体で示す。
   色は装飾（ラベル・見出し左の縦線）にだけ持たせ、読む文字は地の文と同じ濃さを保つ。 */
.column{margin:40px 0;padding:22px 26px 20px;background:var(--col-bg);
  border:1px solid var(--col-line);border-radius:10px;font-family:var(--sans)}
.col-t{margin:0 0 10px;font-size:10.5px;font-weight:700;letter-spacing:.2em;
  color:var(--col-ink)}
.col-h{margin:0 0 14px;padding-left:13px;font-size:16.5px;font-weight:700;
  line-height:1.6;color:var(--ink);border-left:3px solid var(--col-ink);
  text-wrap:balance}
.column p{margin:0 0 14px;font-size:13.5px;line-height:1.95;color:var(--sub)}
.column p:last-child{margin-bottom:0}
.column strong{color:var(--ink);font-weight:700}
.column ul,.column ol{margin:0 0 14px;padding-left:1.25em;font-size:13.5px;
  line-height:1.95;color:var(--sub)}
.column li{margin:0 0 5px}
.column a.chref{color:var(--col-ink);text-decoration-color:var(--col-line)}
.column figure.book-figure{margin:18px 0}
.column .tblwrap{margin:16px 0;font-size:13px}
@media(max-width:600px){.column{padding:18px 18px 16px}}
@media print{.column{background:none;border:1px solid var(--rule)}}

/* ---- 公開の状況（スコア表） ---- */
/* 章は増え続けるので、本数ぶん場所を取る表現（マス・帯）は避け、数字だけで見せる。
   数字は等幅にして桁を揃える——増えたことが一目で分かるのは、桁が動くときなので。 */
.score{margin:26px 0 30px;padding:16px 20px 14px;border:1px solid var(--line);border-radius:8px}
.sc-t{margin:0 0 10px;font-family:var(--sans);font-size:11.5px;font-weight:700;
  letter-spacing:.09em;color:var(--faint)}
/* 本文用の table は min-width:400px と行の下線を持っている（.tblwrap で横スクロール
   させる前提）。この表は囲んでいないので、狭い画面ではみ出さないよう打ち消す。 */
.score table{width:100%;min-width:0;border-collapse:collapse}
.score th,.score td{border:0;padding:6px 0;vertical-align:baseline}
.score th{text-align:left;font-family:var(--sans);font-size:13.5px;font-weight:400;
  color:var(--sub);padding-right:12px}
.sc-n{text-align:right;font-family:var(--sans);
  font-variant-numeric:tabular-nums;white-space:nowrap;width:1%}
.sc-n strong{font-size:17px;font-weight:700;color:var(--ink)}
.sc-n span{font-size:12.5px;color:var(--faint);margin-left:1px}
.score .sc-total th,.score .sc-total td{border-top:1px solid var(--line);padding-top:9px}
.sc-total th{font-weight:700;color:var(--ink)}
.sc-total .sc-n strong{color:var(--accent)}
.sc-note{margin:11px 0 0;font-size:12.5px;color:var(--sub)}
@media print{.score{display:none}}
</style></head><body>'''

HERO = '''<header class="cover">
<p class="cover-en">An Orchestra Beneath the Skin</p>
<h1 class="cover-title">生化学で見る美容医療<span class="cover-sub">皮膚の下のオーケストラ</span></h1>
<p class="cover-author">Yuka Aoki, MD</p>
</header>
<div class="hero">
<p class="lede">美容施術の刺激を受けたあと、皮膚・脂肪・筋の細胞が、どのようにエネルギーを使い、傷んだものを除去し、新しい組織を作るのか。臨床でふだん意識しない基礎を思い出し、施術と結びつけて理解するための教材です。</p>
<div class="flowline">細胞の構造　→　エネルギー代謝　→　品質管理　→　加齢変化　→　美容施術への応答</div>
<p class="note">確認できた章から少しずつ公開しています。基礎が一本の筋を作り、そのうえに個々の施術を乗せます。</p>
</div>'''

INTRO = '''<section class="intro sec-rule">
<h1>はじめに ― なぜこれを作ったか</h1>
<blockquote class="lead">医学部で学んだ基礎は、いまの臨床に地続きでつながっている。そこまでイメージできると、より良い治療の選択ができるようになる。</blockquote>
<p>私は美容医療に長く携わってきました。でも正直に言うと、最初は「レーザーでコラーゲンを増やす」と言葉で説明しながら、その裏で細胞が実際に何をしているのかを、うまくイメージできていませんでした。</p>
<p>線維芽細胞（fibroblast）が細胞の中でコラーゲンを合成して外へ出し、それが細胞のまわりに積み上がって<strong>細胞外マトリックス（ECM）という土台</strong>になる。そしてその土台が、こんどは細胞の側に働きかける。<strong>ひとつひとつの単語は知っていました。でもそれが、細胞の実際の働きとして結びついていませんでした。</strong></p>
<p>一つの細胞の中でも、いくつものオルガネラが順に噛み合って、ようやく一本のタンパク質ができます。組織では、線維芽細胞も免疫細胞も血管内皮も、ECMまでが互いに働きかけ合っている。<strong>どれか一つが主役なのではなく、全体が噛み合ったときに結果が出る。</strong>タイトルに「皮膚の下のオーケストラ」と付けたのは、そういう意味です。生命というのは神秘に溢れていて、とても精巧に作られていて、感動しますね。</p>
<p>医学部で習った生化学や細胞生物学は、日々の臨床からは遠ざかりがちです。そこまで立ち返らなくても、現場の仕事は回る。<strong>けれど、細胞・生化学のレベルまでイメージできると、治療の選び方が変わってきます。</strong></p>
<p>これは新しい知識の詰め込みではなく、<strong>「学び直し」</strong>です。臨床で働く仲間が、施術の裏側を細胞から見直すための手がかりになればうれしいです。</p>
<aside class="notice">
<p class="notice-t">制作と利用について</p>
<p>本教材の制作過程では、文章の整理・推敲や図版の作成などに生成AIを使用しています。内容は文献と照らし合わせながら確認していますが、誤りや不十分な点を含む可能性があります。</p>
<p>本教材は学習を目的としたものであり、個別の診療判断に代わるものではありません。診療にあたっては、最新のガイドライン、添付文書、原著論文などをご確認ください。</p>
</aside>
</section>'''

CRITERIA = '''<section id="criteria" class="sec-rule">
<h1>この教材の立ち方 ― 限られた根拠から、どう判断するか</h1>
<blockquote class="lead">美容医療に、質の高い臨床試験がそろっている領域はほとんどありません。それでも私たちは毎日、治療を選んでいます。<strong>この教材は、限られた材料をつないで地図を作り、つないだところに「どのくらい確かか」を書き添えます。</strong></blockquote>
<p>「エビデンスがないから何も言えない」で止めてしまうと、<strong>手元に残るのは経験談と広告だけ</strong>になります。美容医療で厳密な対照試験が組まれることは少なく、多くは小規模・単群・企業主導です。それを理由に、考えることをやめるわけにはいきません。</p>
<p>使える材料は三つあります。<strong>①いま臨床で見えていること　②確立した細胞生物学・生化学　③確度はまちまちだが、報告されていること。</strong>よりよく治療するには、この三つをつなぐしかありません。</p>
<p>三つをつなぐには、推論が要ります。<strong>推論は、私たちが日々の診療でしていることそのものです。</strong>問題になるのは推論すること自体ではなく、<strong>推論を確かめられた事実と取り違えること</strong>だけです。だからこの教材は、<strong>どこまでが確立していて、どこからが推論か</strong>を、つないだ矢印ごとに示したまま進みます。それが分かれば、あとは読者が自分の臨床で判断できます——「ヒトでは未確認だが、機序は筋が通っていてリスクも低いなら試す」も、「未確認だから患者さんには断定的に説明しない」も、どちらも成り立ちます。</p>
<p>下の六つが、その目印です。<strong>主張を却下するためのふるいではなく、いま自分がどの段に立っているかを確かめるためのもの</strong>です。</p>
{FIG_CRITERIA}
<div class="tblwrap"><table><thead><tr><th>ここまでは来ている</th><th></th><th>ここから先はまだ推論</th></tr></thead><tbody>
<tr><td>血液の値が動いた</td><td>→</td><td>標的組織の値が動いた</td></tr>
<tr><td>経路が動いた（target engagement）</td><td>→</td><td>臨床効果が出た</td></tr>
<tr><td>欠乏を是正すると改善する</td><td>→</td><td>足りている人に上乗せしても改善する</td></tr>
<tr><td>経口で効いた</td><td>→</td><td>外用で効く ／ 皮内注入で効く</td></tr>
<tr><td>全身に供給した</td><td>→</td><td>その組織で使われた</td></tr>
<tr><td>前臨床（動物・in vitro）で示された</td><td>→</td><td>ヒトで示された</td></tr>
</tbody></table></div>
<p>図では、確立した反応を実線、間接的な連結を破線、ヒトで未検証の仮説を点線で描き分けています。<strong>点線が多い章は「怪しい章」ではありません。</strong>機序までは描けるけれど、ヒトでの確認がこれからという領域だということ。そこを知って使うのと、知らずに使うのは、患者さんへの説明も次の一手もまるで変わります。そして<strong>この位置づけは、現時点のものです。</strong>報告が増えれば、点線が破線や実線に変わることも、その逆もあります。</p>
<p>本当のことを言えば、真実の側にはまだ限界があります。それでも、<strong>いま分かっていること・言われていることを知っておくことは必要で、それがより良い治療につながることがある。</strong>この教材はその前提で書かれています。</p>
<p class="scope-note"><strong>根拠表示の付け方について。</strong>第1〜7部（細胞の地図からエネルギー・品質管理・加齢まで）は、標準的な教科書レベルの基礎です。ここは確度が争点にならないので、章末の Evidence meter と個別の参考文献は置いていません。<strong>それらを付けているのは、確度そのものが論点になる第8部以降の各論</strong>——個別の製剤・デバイス・臨床エビデンスを扱う章です。</p>
</section>'''

# 感想欄。FEEDBACK_URL が空なら、この節ごと出力しない。
FEEDBACK = '''<section class="feedback" aria-labelledby="fb-t">
<p class="fb-t" id="fb-t">ご意見・ご感想をお聞かせください</p>
<p>内容の誤りやわかりにくい点、追加するとよさそうな内容、読んだ感想などがありましたら、ぜひお聞かせください。みなさまのお力も借りながら、より充実した教材に育てていけたらうれしいです。</p>
<p><a class="fb-btn" href="{{FEEDBACK_URL}}" target="_blank" rel="noopener noreferrer">ご意見・感想を送る</a></p>
<p class="fb-note">※個別の医療相談には回答できません。患者さんを特定できる情報は入力しないでください。</p>
</section>'''

# 全ページ共通のフッター。章から直接来た読者は「はじめに」を読んでいないので、
# 利用条件と医学的注意はここにも置く（「はじめに」の案内欄と内容が重なるのは承知のうえ）。
FOOTER = '''<footer class="sitefoot">{{FEEDBACK}}
<p class="stamp">{{STAMP}}</p>
<div class="disc">© 2026 Yuka Aoki, MD.　営利目的での利用、改変しての再配布、著者名を外した転載、生成AIの学習データとしての利用は認めません。執筆と図版の作成過程では生成AIを使用しています。引用文献は一次文献を確認したものを載せ、未照合の箇所は本文に「要確認」と表示しています。本教材は生化学・細胞学の教育目的の資料であり、特定製品の効能保証や医療行為の指示ではありません。実際の適応・用量・安全性は、最新の一次情報と各国の規制に従ってご判断ください。</div>
</footer>'''

SCRIPT = '''<script>
const side=document.getElementById('side');
const mbtn=document.querySelector('.menubtn');
function setMenu(open){
  side.classList.toggle('open',open);
  if(mbtn)mbtn.setAttribute('aria-expanded',open?'true':'false');
  if(open){const f=side.querySelector('.navfilter');if(f)f.focus();}
  else if(mbtn&&innerWidth<=900)mbtn.focus();
}
function toggleMenu(){setMenu(!side.classList.contains('open'));}
document.querySelectorAll('.toc a').forEach(a=>a.addEventListener('click',()=>{if(innerWidth<=900)setMenu(false);}));
/* 背景（本文）を触ったら閉じる。狭い画面でナビが本文に重なるため。*/
document.addEventListener('click',e=>{
  if(innerWidth>900||!side.classList.contains('open'))return;
  if(!side.contains(e.target)&&e.target!==mbtn&&!mbtn.contains(e.target))setMenu(false);
});
document.addEventListener('keydown',e=>{
  if(e.key!=='Escape')return;
  if(side.classList.contains('open'))setMenu(false);
  document.querySelectorAll('figure.zoom').forEach(f=>{f.classList.remove('zoom');f.setAttribute('aria-expanded','false');});
});
/* 図の拡大。クリックだけでなくEnter/Spaceでも開閉できるようにする。*/
document.querySelectorAll('figure.book-figure').forEach(f=>{
  const flip=()=>{const on=f.classList.toggle('zoom');f.setAttribute('aria-expanded',on?'true':'false');};
  f.addEventListener('click',flip);
  f.addEventListener('keydown',e=>{
    if(e.key==='Enter'||e.key===' '){e.preventDefault();flip();}
  });
});
/* 章名の絞り込み。56章を目で追わずに目的の章へ行けるようにする。*/
const filt=side&&side.querySelector('.navfilter');
if(filt)filt.addEventListener('input',()=>{
  const q=filt.value.trim().toLowerCase();
  const items=side.querySelectorAll('.toc a, .toc .part');
  let lastPart=null,shown=0;
  items.forEach(el=>{
    if(el.classList.contains('part')){
      if(lastPart)lastPart.classList.toggle('hide',shown===0);
      lastPart=el;shown=0;el.classList.remove('hide');return;
    }
    const hit=!q||el.textContent.toLowerCase().includes(q);
    el.classList.toggle('hide',!hit);
    if(hit)shown++;
  });
  if(lastPart)lastPart.classList.toggle('hide',shown===0);
});
/* 平易版／専門版の切り替え。選んだ読み方は他の章へ移っても保つ。*/
(function(){
  const KEY='readmode';
  function apply(m){
    document.body.classList.toggle('mode-easy',m==='easy');
    document.querySelectorAll('.readmode-sw button').forEach(b=>
      b.setAttribute('aria-pressed',b.dataset.m===m?'true':'false'));
  }
  let mode='pro';
  try{mode=localStorage.getItem(KEY)||'pro';}catch(e){}
  apply(mode);
  document.querySelectorAll('.readmode-sw button').forEach(b=>{
    b.addEventListener('click',()=>{
      apply(b.dataset.m);
      try{localStorage.setItem(KEY,b.dataset.m);}catch(e){}
    });
  });
})();
/* 用語のツールチップ。ページを移動せずにその場で定義を出す。*/
(function(){
  const terms=document.querySelectorAll('.term');
  if(!terms.length)return;
  const tip=document.createElement('div');
  tip.id='tip';document.body.appendChild(tip);
  let cur=null;
  function show(el){
    cur=el;
    tip.innerHTML='<div class="tip-t"></div><div class="tip-b"></div>'+
      '<a class="tip-l" href="glossary.html">用語集で見る →</a>';
    tip.querySelector('.tip-t').textContent=el.dataset.t;
    tip.querySelector('.tip-b').textContent=el.dataset.d;
    tip.classList.add('on');
    const r=el.getBoundingClientRect(),w=tip.offsetWidth,h=tip.offsetHeight;
    let x=r.left+scrollX+r.width/2-w/2;
    x=Math.max(scrollX+8,Math.min(x,scrollX+innerWidth-w-8));
    /* 下に入らなければ上に出す */
    let y=r.bottom+scrollY+8;
    if(r.bottom+8+h>innerHeight)y=r.top+scrollY-h-8;
    tip.style.left=x+'px';tip.style.top=Math.max(scrollY+8,y)+'px';
  }
  function hide(){tip.classList.remove('on');cur=null;}
  terms.forEach(el=>{
    el.addEventListener('mouseenter',()=>show(el));
    el.addEventListener('focus',()=>show(el));
    el.addEventListener('mouseleave',e=>{if(!tip.matches(':hover'))hide();});
    el.addEventListener('blur',hide);
    /* スマホ：タップで開閉 */
    el.addEventListener('click',e=>{e.preventDefault();cur===el?hide():show(el);});
  });
  tip.addEventListener('mouseleave',hide);
  document.addEventListener('click',e=>{
    if(cur&&!e.target.closest('.term')&&!e.target.closest('#tip'))hide();
  });
  addEventListener('scroll',()=>{if(cur)hide();},{passive:true});
  document.addEventListener('keydown',e=>{if(e.key==='Escape')hide();});
})();
/* いま読んでいる章を左ナビの中央に出す。ページ本体は動かさない（scrollIntoViewだと本文まで飛ぶ）。*/
const cur=document.querySelector('.toc a.active');
if(cur&&side)side.scrollTop=cur.offsetTop-side.clientHeight/2;
</script>'''

# ---------------------------------------------------------------------------
# 構成のデータ層 ―― 目次.yml と front matter
#   並び順の正典は 目次.yml だけ。章の正体は front matter の id。
#   PyYAML には依存しない（目次.yml は決まった形しか取らないので自前で読む）。
# ---------------------------------------------------------------------------

def load_toc():
    """目次.yml を [{section, subtitle, intro, parts: [{part, intro, chapters: [id]}]}] に読む。

    part を持たない section は章を直下に置ける（美容内科・おわりに）。
    その場合も内部では part=None の1ブロックにまとめ、部の扉は出さない。
    """
    sections, sec, part = [], None, None
    for raw in io.open(TOC_FILE, encoding="utf-8"):
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"  - section: (.+)$", line)
        if m:
            sec = {"section": m.group(1).strip(), "subtitle": "", "intro": "", "parts": []}
            sections.append(sec)
            part = None
            continue
        if sec is None:
            continue
        m = re.match(r"    subtitle: (.+)$", line)
        if m:
            sec["subtitle"] = m.group(1).strip(); continue
        m = re.match(r"    intro: (.+)$", line)
        if m:
            sec["intro"] = m.group(1).strip(); continue
        m = re.match(r"      - part: (.+)$", line)
        if m:
            part = {"part": m.group(1).strip(), "intro": "", "chapters": []}
            sec["parts"].append(part); continue
        m = re.match(r"        intro: (.+)$", line)
        if m and part is not None:
            part["intro"] = m.group(1).strip(); continue
        m = re.match(r"\s+- ([a-z0-9-]+)\s*(?:#.*)?$", line)
        if m:
            if part is None:                       # section 直下に章を置く形
                part = {"part": None, "intro": "", "chapters": []}
                sec["parts"].append(part)
            part["chapters"].append(m.group(1))
    if not sections:
        sys.exit("ERROR: 目次.yml が読めない（sections が空）")
    return sections


FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
HIST_RE = re.compile(r"\s*-\s*\{date:\s*([0-9][0-9-]*),\s*note:\s*(.+?)\}\s*$")


def parse_front_matter(text):
    """front matter を (dict, 本文) に分ける。history だけリスト、他は文字列。"""
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm, hist = {}, []
    for line in m.group(1).split("\n"):
        h = HIST_RE.match(line)
        if h:
            hist.append({"date": h.group(1), "note": h.group(2).strip()}); continue
        kv = re.match(r"([^\s:]+):\s*(.*)$", line)
        if kv:
            fm[kv.group(1)] = kv.group(2).strip()
    if hist:
        fm["history"] = hist
    return fm, text[m.end():]


def days_since(datestr):
    """ISO日付から今日までの日数。読めなければ None。"""
    try:
        y, mo, d = (int(x) for x in datestr.split("-"))
        return (datetime.date.today() - datetime.date(y, mo, d)).days
    except Exception:
        return None


# ---------------------------------------------------------------------------
# インライン変換
# ---------------------------------------------------------------------------

WIKI_RE = re.compile(r"\[\[([a-z0-9-]+)(?:\|([^\]\n]+))?\]\]")
CHAPTERS = {}       # id -> 章dict（build時に作る）
CURRENT_ID = None   # いま組み立てている章。自分自身へのリンクは張らない
ORPHANS = []        # md はあるのに 目次.yml に無い章。ビルドの最後に必ず知らせる


def slug_for(cid):
    """章id -> 公開ページのファイル名。id がそのまま公開URLになる。"""
    return cid + ".html"


def resolve_wikilinks(s):
    """本文の [[id]] / [[id|表示文字]] を、その章へのリンクにする。

    章をまたぐ参照は教材の骨格なので、飛べないと読者は目次まで戻ることになる。
    - 解決できない id があればビルドを止める（リンク切れを黙って公開しない）
    - 自分自身への参照はリンクにしない
    - 未公開章への参照は、公開ビルドではリンクを外して章題だけ残す
    """
    def rep(m):
        cid, label = m.group(1), m.group(2)
        ch = CHAPTERS.get(cid)
        if ch is None:
            sys.exit("ERROR: 解決できない章参照 [[%s]]（%s の本文）"
                     % (cid, CURRENT_ID or "?"))
        text = label or ch["title"]
        if cid == CURRENT_ID or not ch["visible"]:
            return text
        return '<a class="chref" href="%s">%s</a>' % (ch["slug"], text)
    return WIKI_RE.sub(rep, s)


def strip_wikilinks(s):
    """図のキャプション用。[[id]] を章題に開くが、リンクは張らない。

    figure 全体が拡大トグルなので、中にリンクを置くと1クリックで2つ動いてしまう。
    """
    def rep(m):
        cid, label = m.group(1), m.group(2)
        ch = CHAPTERS.get(cid)
        if ch is None:
            sys.exit("ERROR: 解決できない章参照 [[%s]]（図のキャプション：%s）"
                     % (cid, CURRENT_ID or "?"))
        return label or ch["title"]
    return WIKI_RE.sub(rep, s)


def esc(s):
    """HTMLの特殊文字を無害化する。

    本文には pH<pKa・パルス幅<TRT のような不等号が出てくる。これを素通しすると
    ブラウザがタグの開始と読んで、そこから先が公開ページから消える。
    だから変換の一番最初に必ずここを通す。
    """
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def decorate(s):
    """エスケープ済みの文字列に、許可したMarkdown記法だけを適用する。

    **bold** -> <strong>、*italic*（誌名・学名）-> <em>、`code` -> <code>。
    **を先に処理してから単独の*を見るので、太字が斜体に食われることはない。
    """
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*([^*\n]+?)\*", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+?)`", r"<code>\1</code>", s)
    return s


def strip_marks(s):
    """Markdownの装飾記号だけを落とす（alt属性など、タグを置けない場所用）。"""
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"\*([^*\n]+?)\*", r"\1", s)
    s = re.sub(r"`([^`]+?)`", r"\1", s)
    return s


def alt_text(s, limit=90):
    """図のalt。figcaptionが詳細を持つので、altは短い要約に留める。

    altとcaptionに同じ長文を入れると、スクリーンリーダーが同じ説明を二度読む。
    """
    t = strip_marks(s).strip()
    head = re.split(r"(?<=[。．])", t)[0].strip() or t
    if len(head) > limit:
        head = head[:limit].rstrip() + "…"
    return esc(head)


PMID_RE = re.compile(r"PMID:?\s*(\d{4,9})")
DOI_RE = re.compile(r"DOI:?\s*(10\.\d{4,9}/[^\s　、。（）()<>「」]+)")


def linkify_refs(s):
    """PMID・DOIを一次文献へのリンクにする。

    根拠を追えることがこの教材の値打ちなので、番号を読者に手で検索させない。
    """
    def pmid(m):
        return ('<a class="ext" href="https://pubmed.ncbi.nlm.nih.gov/%s/"'
                ' target="_blank" rel="noopener">%s</a>' % (m.group(1), m.group(0)))

    def doi(m):
        # 「DOI: 10.1234/abc.」の末尾ピリオドは文末であってDOIの一部ではない。
        raw = m.group(1)
        body = raw.rstrip(".")
        tail = raw[len(body):]
        label = m.group(0)[:len(m.group(0)) - len(tail)]
        return ('<a class="ext" href="https://doi.org/%s"'
                ' target="_blank" rel="noopener">%s</a>%s' % (body, label, tail))

    return DOI_RE.sub(doi, PMID_RE.sub(pmid, s))


def inline(s):
    """本文のインライン変換。エスケープ -> 装飾 -> 文献リンク -> 「第N章」リンク。"""
    return resolve_wikilinks(linkify_refs(decorate(esc(s))))


def heading_id(txt):
    """節見出しのid。「## 3　適応 ―― …」なら #s3。

    節番号を使うので、見出しの文言を直してもリンクは生きたまま。番号のない
    「この章の一言」「到達点」にはidを振らない（章内目次にも出さない）。
    """
    m = re.match(r"(\d+(?:\.\d+)?)[　 ]", txt)
    return ' id="s%s"' % m.group(1).replace(".", "-") if m else ""


def chapter_toc(body_html):
    """章内目次。長い章でも節へ直接飛べるようにする（スマホで効く）。"""
    items = re.findall(r'<h2 id="(s[\d\-]+)">(.*?)</h2>', body_html, flags=re.S)
    if len(items) < 3:
        return ""
    lis = "".join('<li><a href="#%s">%s</a></li>'
                  % (i, re.sub(r"<[^>]+>", "", t)) for i, t in items)
    return ('<nav class="chaptoc" aria-label="この章の節"><p class="chaptoc-t">この章の節</p>'
            '<ul>%s</ul></nav>' % lis)


def is_flow_text(text):
    """段落/引用が「純粋な矢印フロー」か判定。→か↓を含み、文らしい句読点(。「、)を含まない。"""
    if "→" not in text and "↓" not in text:
        return False
    for ch in "。「、":
        if ch in text:
            return False
    return True


def flow_div(nodes, cls, arr):
    inner = []
    for k, n in enumerate(nodes):
        inner.append('<span class="node">%s</span>' % n)
        if k < len(nodes) - 1:
            inner.append('<span class="arr">%s</span>' % arr)
    return '<div class="%s">%s</div>' % (cls, "".join(inner))


def strip_wrapping_bold(text):
    """フロー全体を包む **…** を外す。

    「**A → B → C**」を矢印で割ると **A と C** に分断され、対にならない
    アスタリスクがそのまま画面に出る。分割の前に外して、後で各節点に掛け直す。
    """
    t = text.strip()
    if t.startswith("**") and t.endswith("**") and t.count("**") == 2:
        return t[2:-2], True
    return text, False


def inline_flow(text):
    """段落/引用由来の矢印フロー。↓があれば縦(flow vert)、なければ横(flow)。"""
    text, bold = strip_wrapping_bold(text)
    node = (lambda s: "<strong>%s</strong>" % inline(s)) if bold else inline
    if "↓" in text:
        nodes = [node(p.strip()) for p in text.split("↓") if p.strip()]
        return flow_div(nodes, "flow vert", "↓")
    nodes = [node(p.strip()) for p in text.split("→") if p.strip()]
    return flow_div(nodes, "flow", "→")


# ---------------------------------------------------------------------------
# ブロック単位のレンダラ
# ---------------------------------------------------------------------------

def render_blockquote(lines, lead):
    joined_space = " ".join(lines)
    if is_flow_text(joined_space):
        return inline_flow(joined_space)
    cls = ' class="lead"' if lead else ""
    body = "<br>".join(inline(l) for l in lines)
    return "<blockquote%s>%s</blockquote>" % (cls, body)


def render_paragraph(lines):
    joined_space = " ".join(lines)
    if is_flow_text(joined_space):
        return inline_flow(joined_space)
    body = "<br>".join(inline(l) for l in lines)
    return "<p>%s</p>" % body


def render_list(items, list_class):
    """items: [(indent, 'ul'|'ol', content), ...]（1段のネストまで対応）。"""
    top_tag = "ol" if items[0][1] == "ol" else "ul"
    cls = ' class="%s"' % list_class if list_class else ""
    out = []
    i = 0
    while i < len(items):
        indent, _typ, content = items[i]
        li = inline(content)
        # 子（より深いインデント）を集める
        children = []
        j = i + 1
        while j < len(items) and items[j][0] > indent:
            children.append(items[j])
            j += 1
        if children:
            ctag = "ol" if children[0][1] == "ol" else "ul"
            li += "<%s>%s</%s>" % (
                ctag,
                "".join("<li>%s</li>" % inline(c[2]) for c in children),
                ctag,
            )
        out.append("<li>%s</li>" % li)
        i = j
    return "<%s%s>%s</%s>" % (top_tag, cls, "".join(out), top_tag)


def _cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def render_table(rows):
    header = _cells(rows[0])
    body = rows[2:]  # rows[1] は区切り行
    thead = "<thead><tr>%s</tr></thead>" % "".join(
        "<th>%s</th>" % inline(c) for c in header
    )
    tb = "<tbody>%s</tbody>" % "".join(
        "<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in _cells(r))
        for r in body
    )
    return '<div class="tblwrap"><table>%s%s</table></div>' % (thead, tb)


def render_figslot(alt, src):
    # 本文は figures/<id>_図名.png（ソースPNG）を指す。公開側は images/ へ WebP で出す。
    # 流れは figures/ → ビルド → <出力先>/images/ の一方向。
    source_path = os.path.join(ROOT, src)
    if os.path.isfile(source_path):
        base = os.path.basename(src)
        if Image is not None and base.lower().endswith(".png"):
            public_src = "images/" + os.path.splitext(base)[0] + ".webp"
        else:
            public_src = "images/" + base
        output_path = os.path.join(OUT_DIR, public_src)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        if public_src.lower().endswith(".webp"):
            with Image.open(source_path) as im:
                im.convert("RGB").save(output_path, "WEBP", quality=85, method=4)
        else:
            shutil.copy2(source_path, output_path)
        caption = alt.strip() or os.path.splitext(os.path.basename(src))[0]
        caption = strip_wikilinks(caption)
        # 縦長の図を横幅いっぱいに出すと、縦に1000px以上占領して読みにくい。
        # 縦横比でクラスを振り、CSS側で上限幅を決める（クリックで拡大できる）。
        shape = ""
        if Image is not None:
            try:
                with Image.open(source_path) as im:
                    w, h = im.size
                if h / w > 1.15:
                    shape = " tall"
                elif h / w > 0.72:
                    shape = " square"
            except Exception:
                pass
        # 図の中に章番号を書かない方針にしたので、「まとめ」であることは
        # 画像ではなくHTML側の帯で示す（章が動いても作り直さずに済む）。
        is_summary = "まとめ" in os.path.basename(src)
        label = '<p class="fig-label">この章のまとめ</p>' if is_summary else ""
        cls = "book-figure" + shape + (" summary" if is_summary else "")
        # captionは装飾を効かせる（章リンクは張らない。figure全体が拡大トグルなので、
        # 中にリンクを置くと1クリックで2つ動いてしまう）。altは短い要約に分ける。
        # 拡大の開閉はJS側（Enter/Spaceでも動かすため）。ここでは役割と状態だけ持たせる。
        return (
            '<figure class="%s" role="button" tabindex="0" aria-expanded="false"'
            ' aria-label="図を拡大／縮小">'
            '%s<img src="%s" alt="%s" loading="lazy">'
            '<figcaption>%s</figcaption></figure>'
        ) % (cls, label, public_src, alt_text(caption), decorate(esc(caption)))
    return (
        '<div class="figslot"><div class="fs-icon">🖼️</div>'
        '<div class="fs-txt"><strong>画像スロット（画像は未配置）</strong><br>'
        '%s<br><span class="fs-path">予定ファイル: %s</span></div></div>'
    ) % (decorate(esc(alt)), esc(src))


def render_flow_fence(buf):
    # フェンス内は行ごとに独立したフロー行。ただし「→」で始まる行は
    # 直前行の続き（分岐・折り返し）とみなして連結する。
    rows = []
    for b in buf:
        s = b.strip()
        if not s:
            continue
        if s.startswith("→") and rows:
            rows[-1] = rows[-1] + " " + s
        else:
            rows.append(s)
    divs = []
    for row in rows:
        nodes = [inline(p.strip()) for p in row.split("→") if p.strip()]
        divs.append(flow_div(nodes, "flow diagram", "→"))
    return "\n".join(divs)


def render_steps_fence(buf):
    steps = [b.strip() for b in buf if b.strip()]
    inner = []
    for k, s in enumerate(steps):
        inner.append(
            '<span class="node"><span class="num">%d</span>%s</span>' % (k + 1, inline(s))
        )
        if k < len(steps) - 1:
            inner.append('<span class="arr">↓</span>')
    return '<div class="flow vert diagram">%s</div>' % "".join(inner)


def render_code_fence(buf):
    return '<pre class="code">%s</pre>' % "<br>".join(esc(b) for b in buf)


# ---------------------------------------------------------------------------
# 行パーサ
# ---------------------------------------------------------------------------

LI_RE = re.compile(r"^(\s*)([-]|\d+\.)\s+(.*)$")
IMG_RE = re.compile(r"^!\[(.*?)\]\((.*?)\)\s*$")


def is_blank(l):
    return l.strip() == ""


def parse_markdown(text):
    """Markdown 本文 -> ブロック HTML 文字列のリスト。"""
    lines = text.split("\n")
    blocks = []
    i = 0
    n = len(lines)
    pending_list_class = None  # 次のリストに付けるクラス（goal / evidence）
    pending_lead = False       # 次の引用を lead にするか

    def clear_pending():
        nonlocal pending_list_class, pending_lead
        pending_list_class = None
        pending_lead = False

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if is_blank(line):
            i += 1
            continue

        # 平易版のブロック ::: easy … :::
        #   直前のブロックが専門版、この中身が平易版。どちらも無い段落は両版に共通で出る。
        if stripped.startswith("::: easy"):
            j = i + 1
            buf = []
            while j < n and lines[j].strip() != ":::":
                buf.append(lines[j])
                j += 1
            if blocks:
                blocks[-1] = '<div class="pro">%s</div>' % blocks[-1]
            inner = parse_markdown("\n".join(buf))
            blocks.append('<div class="easy">%s</div>' % "\n".join(inner))
            clear_pending()
            i = j + 1
            continue

        # コラム ::: column タイトル … :::
        #   章の骨から外れるが面白い話・背景の話を置く受け皿。
        #   「骨は1本、全節をそれに奉仕させる」を守ったまま余談を置けるようにする。
        #   本文と視覚的に切り離すので、読者は本筋と区別して読める。
        if stripped.startswith("::: column"):
            title = stripped[len("::: column"):].strip()
            j = i + 1
            buf = []
            while j < n and lines[j].strip() != ":::":
                buf.append(lines[j])
                j += 1
            inner = parse_markdown("\n".join(buf))
            head = '<p class="col-t">コラム</p>'
            if title:
                head += '<p class="col-h">%s</p>' % decorate(esc(title))
            blocks.append('<aside class="column">%s%s</aside>' % (head, "\n".join(inner)))
            clear_pending()
            i = j + 1
            continue

        # フェンス ```lang ... ```
        if stripped.startswith("```"):
            lang = stripped[3:].strip()
            j = i + 1
            buf = []
            while j < n and not lines[j].strip().startswith("```"):
                buf.append(lines[j])
                j += 1
            if lang == "flow":
                blocks.append(render_flow_fence(buf))
            elif lang == "steps":
                blocks.append(render_steps_fence(buf))
            elif lang == "html":
                # 旧版のインラインSVGは、直前の完成PNGと内容が重複するため公開版では省略。
                pass
            else:
                blocks.append(render_code_fence(buf))
            clear_pending()
            i = j + 1
            continue

        # 見出し
        if stripped.startswith("### "):
            txt = stripped[4:].strip()
            blocks.append("<h3>%s</h3>" % inline(txt))
            clear_pending()
            if txt == "Evidence meter":
                pending_list_class = "evidence"
            i += 1
            continue
        if stripped.startswith("## "):
            txt = stripped[3:].strip()
            blocks.append('<h2%s>%s</h2>' % (heading_id(txt), inline(txt)))
            clear_pending()
            if "到達点" in txt:
                pending_list_class = "goal"
            if txt == "この章の一言":
                pending_lead = True
            i += 1
            continue
        if stripped.startswith("# "):
            txt = line[2:]  # 本文先頭 # 行はそのまま
            blocks.append("<h1>%s</h1>" % txt)
            clear_pending()
            i += 1
            continue

        # 水平線
        if re.match(r"^-{3,}$", stripped):
            blocks.append("<hr>")
            clear_pending()
            i += 1
            continue

        # 画像スロット
        m = IMG_RE.match(stripped)
        if m:
            blocks.append(render_figslot(m.group(1), m.group(2)))
            clear_pending()
            i += 1
            continue

        # 生HTML（<svg> / <div> など）は素通し
        if stripped.startswith("<"):
            blocks.append(line)
            clear_pending()
            i += 1
            continue

        # 引用（連続する > 行）
        if line.startswith(">"):
            bq = []
            while i < n and lines[i].startswith(">"):
                content = lines[i][1:]
                if content.startswith(" "):
                    content = content[1:]
                bq.append(content)
                i += 1
            if not (bq and bq[0].lstrip().startswith("制作メモ")):
                blocks.append(render_blockquote(bq, pending_lead))
            clear_pending()
            continue

        # テーブル（連続する | 行）
        if stripped.startswith("|"):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(lines[i])
                i += 1
            if len(rows) >= 2:
                blocks.append(render_table(rows))
            clear_pending()
            continue

        # リスト（連続するリスト項目）
        lm = LI_RE.match(line)
        if lm:
            items = []
            while i < n:
                m2 = LI_RE.match(lines[i])
                if not m2:
                    break
                indent = len(m2.group(1))
                typ = "ol" if m2.group(2)[0].isdigit() else "ul"
                items.append((indent, typ, m2.group(3)))
                i += 1
            blocks.append(render_list(items, pending_list_class))
            clear_pending()
            continue

        # 段落（連続する平文行を <br> で結合）
        para = []
        while i < n:
            cur = lines[i]
            s = cur.strip()
            if (
                is_blank(cur)
                or s.startswith("```")
                or s.startswith("#")
                or re.match(r"^-{3,}$", s)
                or IMG_RE.match(s)
                or cur.startswith(">")
                or s.startswith("|")
                or cur.startswith("<")
                or LI_RE.match(cur)
            ):
                break
            para.append(cur)
            i += 1
        if para:
            blocks.append(render_paragraph(para))
            clear_pending()
        else:
            i += 1  # 安全弁（通常到達しない）

    return blocks


# ---------------------------------------------------------------------------
# ビルド
# ---------------------------------------------------------------------------

def first_heading(text):
    for l in text.split("\n"):
        if l.startswith("# "):
            return l[2:]
    return ""



def criteria_html():
    """巻頭「この教材の立ち方」。図があればfigure、無ければプレースホルダを差し込む。"""
    fig = render_figslot("手持ちの三つ（臨床・生化学・報告）をつなぎ、つないだ矢印に確かさのラベルを付ける", "figures/巻頭_本教材が守る切り分け.png")
    return CRITERIA.replace("{FIG_CRITERIA}", fig)


def build_stamp():
    """最終更新日と版。規制・製品情報を含む教材なので、鮮度が読者に見えるようにする。"""
    date = datetime.date.today().isoformat()
    try:
        rev = subprocess.check_output(
            ["git", "-C", ROOT, "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL).decode().strip()
        return "最終更新 %s ／ 版 %s" % (date, rev)
    except Exception:
        return "最終更新 %s" % date


def chapter_desc(text, fallback):
    """meta description。章の「この章の一言」を使う（無ければ章タイトル）。"""
    m = re.search(r"^##\s*この章の一言\s*$(.*?)(?=^##\s|\Z)", text, flags=re.M | re.S)
    body = m.group(1) if m else ""
    for line in body.split("\n"):
        l = line.strip().lstrip(">").strip()
        if not l or l.startswith(("#", "!", "|", "```")):
            continue
        l = re.sub(r"\s+", " ", strip_marks(strip_wikilinks(l)))
        return l[:110] + "…" if len(l) > 110 else l
    return fallback


def first_figure(text):
    """OGP画像。章の最初の図を使う（無ければ巻頭図）。"""
    m = re.search(r"^!\[[^\]]*\]\(figures/([^)]+)\)", text, flags=re.M)
    if not m:
        return OG_DEFAULT
    return "images/" + re.sub(r"\.png$", ".webp", m.group(1), flags=re.I)


# ---------------------------------------------------------------------------
# 用語集 ―― ページとツールチップ
# ---------------------------------------------------------------------------

GLOSSARY_MD = os.path.join(ROOT, "資料", "用語集.md")

# 表示名から検索パターンを作れない語だけ、ここで上書きする。
# （gen_glossary_candidates.py の ALIAS と同じ思想。あちらは章の集計、こちらは本文への印付け）
TERM_ALIAS = {
    "NAD⁺・NADH": ["NAD⁺", "NADH"],
    "mTOR・mTORC1": ["mTORC1", "mTOR"],
    "TCA cycle": ["TCA回路", "TCA cycle"],
    "salvage pathway": ["salvage pathway", "salvage経路"],
    "YAP/TAZ": ["YAP/TAZ"],
    "ubiquitin–proteasome": ["ubiquitin–proteasome"],
    "PBM": ["PBM"],
}

GLOSSARY = []       # [(表示名, 定義, 登場章, [検索パターン]), ...]
TERMS_SEEN = set()  # 1章のなかで既に印を付けた語。章ごとにリセットする


def load_glossary():
    """用語集.md の表を読む。定義が空の語はまだ書けていないので飛ばす。"""
    GLOSSARY.clear()
    if not os.path.exists(GLOSSARY_MD):
        return
    for line in open(GLOSSARY_MD, encoding="utf-8"):
        cells = line.split("|")
        if len(cells) != 5:
            continue
        term, defi, chaps = (c.strip() for c in cells[1:4])
        if not term or not defi or term == "用語" or set(term) <= set("-: "):
            continue
        pats = TERM_ALIAS.get(term) or [re.sub(r"（.*?）", "", term).strip()]
        GLOSSARY.append((term, defi, chaps, pats))
    # 長い語から先に印を付ける（HSP47 を HSP に食われないように）
    GLOSSARY.sort(key=lambda g: -max(len(p) for p in g[3]))


def _boundary_re(pat):
    """英数字の語は前後が英数字でないときだけ拾う（AGE が damage に食われないように）。"""
    if re.match(r"^[A-Za-z0-9]", pat) and re.search(r"[A-Za-z0-9]$", pat):
        return re.compile(r"(?<![A-Za-z0-9])%s(?![A-Za-z0-9])" % re.escape(pat))
    return re.compile(re.escape(pat))


TAG_SPLIT = re.compile(r"(<[^>]+>)")


def _mark_text(text):
    """テキスト片に用語の印を付ける。

    印を入れた部分は確定させ、残りだけを見ていく。こうしないと、いま挿入した
    ツールチップの定義文（属性値）の中を次の語が走査してしまう。
    """
    done, rest = [], text
    while True:
        best = None
        for term, defi, _chaps, pats in GLOSSARY:
            if term in TERMS_SEEN:
                continue
            for pat in pats:
                m = _boundary_re(pat).search(rest)
                if m and (best is None or m.start() < best[0].start()):
                    best = (m, term, defi)
                break
        if best is None:
            break
        m, term, defi = best
        TERMS_SEEN.add(term)
        done.append(rest[:m.start()])
        done.append('<span class="term" tabindex="0" data-t="%s" data-d="%s">%s</span>'
                    % (esc(term), esc(strip_marks(defi)), m.group(0)))
        rest = rest[m.end():]
    done.append(rest)
    return "".join(done)


def mark_terms(html):
    """本文に用語のツールチップを仕込む。1章につき各語1回だけ（初出）。

    青い印が本文中に何度も出ると読めなくなるので、章ごとに最初の1回に絞る。
    タグの中身（属性値）とリンクの内側は触らない。
    """
    if not GLOSSARY:
        return html
    out, in_link = [], False
    for part in TAG_SPLIT.split(html):
        if part.startswith("<"):
            if part.startswith("<a "):
                in_link = True
            elif part.startswith("</a>"):
                in_link = False
            out.append(part)
        elif in_link or not part.strip():
            out.append(part)
        else:
            out.append(_mark_text(part))
    return "".join(out)


def glossary_body():
    """用語集ページ。分類の見出しごとに、用語・定義・登場章の3列で出す。"""
    blocks = ['<article class="chapter">', '<p class="kicker">用語集</p>',
              "<h1>用語集</h1>",
              '<blockquote class="lead">章をまたいで出てくる用語を集めました。'
              '臨床で日常的に使う語ではなく、<strong>基礎で習ったが日常では使っていない語</strong>を選んでいます。'
              '本文中では、各章の初出に点線を引いてあります——触れるとその場に定義が出ます。</blockquote>']
    section, rows = None, []

    def flush():
        if rows:
            blocks.append('<div class="tblwrap"><table><thead><tr>'
                          "<th>用語</th><th>定義</th><th>登場章</th></tr></thead>"
                          "<tbody>%s</tbody></table></div>" % "".join(rows))
            rows.clear()

    for line in open(GLOSSARY_MD, encoding="utf-8"):
        if line.startswith("## "):
            title = line[3:].strip()
            if title in ("語の選び方", "定義を書くときのルール", "表示のしかた（実装はこれから）"):
                section = None
                continue
            flush()
            blocks.append('<h2 id="g-%d">%s</h2>' % (len(blocks), esc(title)))
            section = title
            continue
        if section is None:
            continue
        cells = line.split("|")
        if len(cells) != 5:
            continue
        term, defi, chaps = (c.strip() for c in cells[1:4])
        if not term or not defi or term == "用語" or set(term) <= set("-: "):
            continue
        rows.append("<tr><td><strong>%s</strong></td><td>%s</td><td class=\"g-ch\">%s</td></tr>"
                    % (esc(term), decorate(esc(defi)), resolve_wikilinks(esc(chaps))))
    flush()
    blocks.append("</article>")
    return "\n".join(blocks)


def footer_html():
    """全ページ共通のフッター。感想欄→最終更新→著作権の順に1つの footer へまとめる。"""
    fb = FEEDBACK.replace("{{FEEDBACK_URL}}", FEEDBACK_URL) if FEEDBACK_URL else ""
    return FOOTER.replace("{{FEEDBACK}}", fb).replace("{{STAMP}}", build_stamp())


def page(title, nav, body, desc="", url="", image=""):
    """1ページ分のHTML。章ページも目次ページも同じ骨格を使う。"""
    head = (PAGE_HEAD
            .replace("{{TITLE}}", esc(title))
            .replace("{{DESC}}", esc(desc))
            .replace("{{URL}}", BASE_URL + url)
            .replace("{{IMAGE}}", BASE_URL + (image or OG_DEFAULT)))
    return "\n".join([
        head,
        '<button class="menubtn" onclick="toggleMenu()" aria-controls="side"'
        ' aria-expanded="false">目次</button>',
        '<div class="wrap">',
        nav,
        '<main class="main"><div class="col">',
        body,
        footer_html(),
        "</div></main></div>",
        SCRIPT,
        "</body></html>",
    ]) + "\n"


def strip_authoring_comments(text):
    """本文の HTML コメント（制作メモ）を落とす。公開ページに残さないため。"""
    return re.sub(r"<!--.*?-->\n?", "", text, flags=re.S)


def collect_chapters():
    """目次.yml と front matter から章の並びを作る。

    返すのは章dictの平坦なリスト（並び順は 目次.yml のとおり）。
    section / part を各章が持つので、ナビも目次もこの1本から組める。
    """
    toc = load_toc()
    by_id = {}
    for name in sorted(os.listdir(SRC_DIR)):
        if not name.endswith(".md"):
            continue
        text = io.open(os.path.join(SRC_DIR, name), encoding="utf-8").read()
        fm, body = parse_front_matter(text)
        if not fm.get("id"):
            sys.exit("ERROR: front matter に id が無い: chapters/%s" % name)
        if fm["id"] in by_id:
            sys.exit("ERROR: id が重複している: %s" % fm["id"])
        by_id[fm["id"]] = (fm, strip_authoring_comments(body), name)

    out, seen = [], set()
    for sec in toc:
        for part in sec["parts"]:
            for cid in part["chapters"]:
                if cid not in by_id:
                    sys.exit("ERROR: 目次.yml の %s に対応する md が chapters/ に無い" % cid)
                fm, body, name = by_id[cid]
                seen.add(cid)
                hist = fm.get("history") or []
                dates = [h["date"] for h in hist]
                out.append({
                    "id": cid,
                    "slug": slug_for(cid),
                    "title": fm.get("title") or cid,
                    "subtitle": fm.get("subtitle", ""),
                    "kind": fm.get("kind", ""),
                    "status": fm.get("status", "draft"),
                    "published": fm.get("published", ""),
                    "history": hist,
                    "latest": max(dates) if dates else fm.get("published", ""),
                    "first": min(dates) if dates else fm.get("published", ""),
                    "section": sec["section"],
                    "sec_subtitle": sec["subtitle"],
                    "sec_intro": sec["intro"],
                    "part": part["part"],
                    "part_intro": part["intro"],
                    "text": body,
                    "file": name,
                })
    ORPHANS[:] = sorted(set(by_id) - seen)
    return out


def mark_visibility(chapters):
    """公開ビルドでは approved だけをページにする。ほかは目次に「準備中」で出る。"""
    for ch in chapters:
        ch["visible"] = PREVIEW or ch["status"] == "approved"


def badge_of(ch):
    """NEW / 更新 バッジ。最終更新から NEW_DAYS 以内のときだけ出す。手では貼らない。"""
    if not ch.get("visible") or not ch["latest"]:
        return ""
    d = days_since(ch["latest"])
    if d is None or d > NEW_DAYS:
        return ""
    is_new = (ch["latest"] == ch["first"])
    return '<span class="badge %s">%s</span>' % ("bnew" if is_new else "bupd",
                                                 "NEW" if is_new else "更新")


def status_badge(ch):
    """プレビュー専用。著者が「どれがまだ未承認か」を一目で見るための印。"""
    if not PREVIEW or ch["status"] == "approved":
        return ""
    return '<span class="badge bst">%s</span>' % esc(ch["status"])


def dateline_html(ch):
    """章ページの日付。規制・製品情報を含む教材なので、鮮度が読者に見えるようにする。"""
    bits = []
    if ch["published"]:
        bits.append("公開 %s" % ch["published"])
    if ch["latest"] and ch["latest"] != ch["published"]:
        bits.append("最終更新 %s" % ch["latest"])
    return '<p class="dateline">%s</p>' % esc("　／　".join(bits)) if bits else ""


def history_html(ch):
    """この章の更新。初公開だけのときは出さない。"""
    if len(ch["history"]) < 2:
        return ""
    items = "".join(
        "<li><time>%s</time>%s</li>" % (esc(h["date"]), decorate(esc(h["note"])))
        for h in sorted(ch["history"], key=lambda h: h["date"], reverse=True))
    return ('<section class="ch-history"><p class="chh-t">この章の更新</p>'
            "<ul>%s</ul></section>" % items)


def changelog_rows(chapters):
    """(日付, 章, 内容, 新規か) を新しい順に。表紙の「最近の更新」と更新履歴の共通の元。"""
    rows = []
    for ch in chapters:
        if not ch["visible"]:
            continue
        for h in ch["history"]:
            rows.append((h["date"], ch, h["note"], h["date"] == ch["first"]))
    rows.sort(key=lambda r: (r[0], r[1]["title"]), reverse=True)
    return rows


def _cl_item(date, ch, note, is_new, with_date=True):
    return ('<li>%s<span class="k %s">%s</span>'
            '<a href="%s">%s</a><span class="note">%s</span></li>'
            % ("<time>%s</time>" % esc(date) if with_date else "",
               "new" if is_new else "upd", "新規" if is_new else "改訂",
               ch["slug"], esc(ch["title"]), decorate(esc(note))))


def recent_html(chapters, limit=5):
    """表紙の「最近の更新」。増えていく教材なので、まずここが見えるようにする。"""
    rows = changelog_rows(chapters)
    if not rows:
        return ""
    items = "".join(_cl_item(*r) for r in rows[:limit])
    return ('<section class="recent"><p class="rc-t">最近の更新</p><ul>%s</ul>'
            '<p class="rc-more"><a href="changelog.html">すべての更新履歴</a></p></section>'
            % items)


def changelog_body(chapters):
    rows = changelog_rows(chapters)
    blocks = ['<section class="sec-rule"><h1>更新履歴</h1>',
              '<blockquote class="lead">確認できた章から順に公開しています。'
              '新しく公開した章と、あとから直した内容が新しい順に並びます。</blockquote>']
    if not rows:
        blocks.append("<p>まだ公開した章がありません。</p>")
    cur = None
    for date, ch, note, is_new in rows:
        if date != cur:
            if cur is not None:
                blocks.append("</ul>")
            cur = date
            blocks.append('<h2 class="cl-date">%s</h2><ul class="cl">' % esc(date))
        blocks.append(_cl_item(date, ch, note, is_new, with_date=False))
    if cur is not None:
        blocks.append("</ul>")
    blocks.append("</section>")
    return "\n".join(blocks)


def nav_html(chapters, active_slug):
    """全ページ共通の左ナビ。セクション > 部の2階層。いま開いている章に active を付ける。"""
    lines = [
        '<nav class="side" id="side">',
        '<a class="brand" href="index.html">生化学で見る美容医療'
        "<small>皮膚の下のオーケストラ</small></a>",
        '<label class="sr-only" for="navfilter">しぼり込む</label>',
        '<input class="navfilter" id="navfilter" type="search" autocomplete="off"'
        ' placeholder="しぼり込む（例：NAD、レーザー）">',
        '<div class="toc">',
        '<div class="part">はじめに</div>',
        '<a href="index.html"%s>表紙と目次</a>' % ("" if active_slug else ' class="active"'),
        '<a href="index.html#criteria">この教材の立ち方</a>',
        '<a href="changelog.html"%s>更新履歴</a>'
        % (' class="active"' if active_slug == "changelog.html" else ""),
        '<a href="glossary.html"%s>用語集</a>'
        % (' class="active"' if active_slug == "glossary.html" else ""),
    ]
    sec = part = None
    for ch in chapters:
        if ch["section"] != sec:
            sec, part = ch["section"], None
            lines.append('<div class="sec">%s</div>' % esc(sec))
        if ch["part"] != part:
            part = ch["part"]
            if part:
                lines.append('<div class="part">%s</div>' % esc(part))
        if ch["visible"]:
            cls = ' class="active"' if ch["slug"] == active_slug else ""
            lines.append('<a href="%s"%s>%s%s%s</a>'
                         % (ch["slug"], cls, esc(ch["title"]), badge_of(ch), status_badge(ch)))
        else:
            lines.append('<span class="soon">%s<em>準備中</em></span>' % esc(ch["title"]))
    lines.append("</div></nav>")
    return "\n".join(lines)


def pager_html(chapters, i):
    """読み進める線。公開されている章だけをつなぐ（未公開は飛ばす）。

    「次に何を読むか」は本文に書かない。並び順は 目次.yml だけが持つので、ここで作る。
    """
    def near(step):
        j = i + step
        while 0 <= j < len(chapters):
            if chapters[j]["visible"]:
                return chapters[j]
            j += step
        return None
    items = []
    prev, nxt = near(-1), near(1)
    if prev:
        items.append('<a class="prev" href="%s"><span class="lbl">前へ</span>%s</a>'
                     % (prev["slug"], esc(prev["title"])))
    if nxt:
        items.append('<a class="next" href="%s"><span class="lbl">次へ</span>%s</a>'
                     % (nxt["slug"], esc(nxt["title"])))
    return '<nav class="pager">%s</nav>' % "".join(items) if items else ""


def progress_html(chapters):
    """公開の状況をスコア表で出す。

    章はこれからも増えるので、マスや帯のように「本数だけ場所を取る」形は使わない。
    数字なら何本になっても崩れない。数は 目次.yml と front matter から毎回数え直す。
    """
    order, agg = [], {}
    for ch in chapters:
        k = ch["section"]
        if k not in agg:
            agg[k] = [0, 0]
            order.append(k)
        agg[k][1] += 1
        if ch["visible"]:
            agg[k][0] += 1
    rows = "".join(
        '<tr><th>%s</th><td class="sc-n"><strong>%d</strong> <span>/ %d</span></td></tr>'
        % (esc(k), agg[k][0], agg[k][1]) for k in order)
    done = sum(a[0] for a in agg.values())
    total = sum(a[1] for a in agg.values())
    rows += ('<tr class="sc-total"><th>合計</th>'
             '<td class="sc-n"><strong>%d</strong> <span>/ %d</span></td></tr>'
             % (done, total))
    return ('<section class="score"><p class="sc-t">公開の状況</p>'
            '<table>%s</table>'
            '<p class="sc-note">確認できたものから、ひとつずつ増やしています。</p>'
            '</section>' % rows)


def index_body(chapters):
    blocks = [HERO, progress_html(chapters), recent_html(chapters), INTRO, criteria_html(),
              '<section class="contents sec-rule">', "<h1>目次</h1>"]
    sec = part = None
    for ch in chapters:
        if ch["section"] != sec:
            if part is not None:
                blocks.append("</ul></div>")
            if sec is not None:
                blocks.append("</div>")
            sec, part = ch["section"], None
            blocks.append('<div class="sec-block"><h2 class="sec-title">%s%s</h2>'
                          % (esc(ch["section"]),
                             "<small>%s</small>" % esc(ch["sec_subtitle"])
                             if ch["sec_subtitle"] else ""))
            if ch["sec_intro"]:
                blocks.append('<p class="sec-intro">%s</p>' % decorate(esc(ch["sec_intro"])))
        if ch["part"] != part:
            if part is not None:
                blocks.append("</ul></div>")
            part = ch["part"]
            blocks.append('<div class="part-block">')
            if part:
                blocks.append('<div class="part-title">%s</div>' % esc(part))
                if ch["part_intro"]:
                    blocks.append('<p class="part-intro">%s</p>'
                                  % decorate(esc(ch["part_intro"])))
            blocks.append('<ul class="toc-list">')
        if ch["visible"]:
            blocks.append('<li><a href="%s">%s%s%s</a></li>'
                          % (ch["slug"], esc(ch["title"]), badge_of(ch), status_badge(ch)))
        else:
            blocks.append('<li class="soon"><span>%s</span><em>準備中</em></li>'
                          % esc(ch["title"]))
    if part is not None:
        blocks.append("</ul></div>")
    if sec is not None:
        blocks.append("</div>")
    blocks.append("</section>")
    return "\n".join(blocks)


def build():
    global CURRENT_ID
    os.makedirs(OUT_DIR, exist_ok=True)
    img_dir = os.path.join(OUT_DIR, "images")
    os.makedirs(img_dir, exist_ok=True)
    # 出力は毎回作り直す（章を減らした・未承認に戻したときに古いページを残さない）。
    for name in os.listdir(img_dir):
        if name.lower().endswith((".png", ".webp")):
            os.unlink(os.path.join(img_dir, name))
    for name in os.listdir(OUT_DIR):
        if name.endswith(".html"):
            os.unlink(os.path.join(OUT_DIR, name))

    chapters = collect_chapters()
    mark_visibility(chapters)
    CHAPTERS.clear()
    for ch in chapters:
        CHAPTERS[ch["id"]] = ch
    load_glossary()

    written = 0
    for i, ch in enumerate(chapters):
        if not ch["visible"]:
            continue
        CURRENT_ID = ch["id"]
        TERMS_SEEN.clear()          # 用語の印は章ごとに数え直す
        body = mark_terms("\n".join(parse_markdown(ch["text"])))
        CURRENT_ID = None
        # 章内目次は「この章の一言」の後・§1の前に置く（章の顔を先に見せる）。
        toc = chapter_toc(body)
        if toc:
            body = re.sub(r'(?=<h2 id="s)', toc, body, count=1)
        article = "\n".join([
            '<article class="chapter">',
            '<p class="kicker">%s%s</p>'
            % (esc(ch["section"]), "　／　" + esc(ch["part"]) if ch["part"] else ""),
            '<h1 class="ch-title">%s%s</h1>'
            % (esc(ch["title"]),
               "<small>%s</small>" % esc(ch["subtitle"]) if ch["subtitle"] else ""),
            dateline_html(ch),
            body,
            history_html(ch),
            "</article>",
            pager_html(chapters, i),
        ])
        with io.open(os.path.join(OUT_DIR, ch["slug"]), "w", encoding="utf-8") as f:
            f.write(page("%s ― 生化学で見る美容医療" % ch["title"],
                         nav_html(chapters, ch["slug"]), article,
                         desc=chapter_desc(ch["text"], ch["title"]),
                         url=ch["slug"],
                         image=first_figure(ch["text"])))
        written += 1

    with io.open(OUT, "w", encoding="utf-8") as f:
        f.write(page("生化学で見る美容医療 ― 皮膚の下のオーケストラ",
                     nav_html(chapters, None), index_body(chapters),
                     desc="美容施術の刺激を受けたあと、皮膚・脂肪・筋の細胞は"
                          "どのようにエネルギーを使い、傷んだものを除去し、"
                          "新しい組織を作るのか。美容医療に携わる医師のための"
                          "細胞生物学・生化学の教材です。",
                     url="index.html"))
    with io.open(os.path.join(OUT_DIR, "changelog.html"), "w", encoding="utf-8") as f:
        f.write(page("更新履歴 ― 生化学で見る美容医療",
                     nav_html(chapters, "changelog.html"), changelog_body(chapters),
                     desc="新しく公開した章と、あとから直した内容の一覧です。",
                     url="changelog.html"))
    if GLOSSARY:
        with io.open(os.path.join(OUT_DIR, "glossary.html"), "w", encoding="utf-8") as f:
            f.write(page("用語集 ― 生化学で見る美容医療",
                         nav_html(chapters, "glossary.html"), glossary_body(),
                         desc="この教材で章をまたいで出てくる用語を、"
                              "1語＝定義2〜3行と登場章つきでまとめました。",
                         url="glossary.html"))
    if not PREVIEW:
        write_sitemap(OUT_DIR, [c for c in chapters if c["visible"]])
    sys.stderr.write("Wrote %s（%s）: %d / %d 章\n"
                     % (OUT_DIR, "プレビュー・全章" if PREVIEW else "公開・approved のみ",
                        written, len(chapters)))
    if not PREVIEW and written == 0:
        sys.stderr.write("  ※ status: approved の章がまだありません。"
                         "著者が読んでOKを出した章だけが公開されます。\n")
    if ORPHANS:
        # 目次に入れ忘れると、その章は黙って無視される。いちばん気づきにくい事故なので最後に出す。
        sys.stderr.write(
            "\n" + "!" * 62 + "\n"
            "!! 目次.yml に登録されていない章が %d本あります。\n"
            "!! **この章はサイトに出ません**（ビルドは無視しています）。\n"
            % len(ORPHANS))
        for cid in ORPHANS:
            sys.stderr.write("!!   - %s\n" % cid)
        sys.stderr.write(
            "!! 目次.yml の入れたい部に id を1行足してください。\n"
            + "!" * 62 + "\n")


def write_sitemap(out_dir, chapters):
    """sitemap.xml。1ページ1章なので、公開した章の場所を検索エンジンに知らせる。"""
    today = datetime.date.today().isoformat()
    urls = ["index.html", "changelog.html"] + [ch["slug"] for ch in chapters]
    items = "".join(
        "<url><loc>%s%s</loc><lastmod>%s</lastmod></url>" % (BASE_URL, u, today)
        for u in urls)
    with io.open(os.path.join(out_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                + items + "</urlset>\n")


if __name__ == "__main__":
    build()
