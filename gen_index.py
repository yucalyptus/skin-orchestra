#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""資料/章一覧.md と 資料/図版台帳.md を実データから生成する。

手書きの索引は57本・図326点の規模では維持できないので、
    - 章の一覧 … 目次.yml（並び順の正典）＋ 各章の front matter
    - 図の一覧 … chapters/*.md の ![キャプション](figures/…) 記法
を唯一のソースとして毎回作り直す。

    python3 gen_index.py

生成物は成果物なので手編集しない。章を足したら 目次.yml に id を1行足してから流す。
build.py には依存しない（Pillow が無い python でも動く）。
"""

import datetime
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(ROOT, "chapters")
FIG_DIR = os.path.join(ROOT, "figures")
TOC_FILE = os.path.join(ROOT, "目次.yml")
OUT_CHAPTERS = os.path.join(ROOT, "資料", "章一覧.md")
OUT_FIGURES = os.path.join(ROOT, "資料", "図版台帳.md")

IMG_RE = re.compile(r"!\[(.*?)\]\(figures/([^)]+)\)")
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
HIST_RE = re.compile(r"\s*-\s*\{date:\s*([0-9][0-9-]*),\s*note:\s*(.+?)\}\s*$")

# 本文mdではなく build.py が巻頭へ自動で差し込む固定図。未参照扱いにしない。
FIXED_FIGURES = {"巻頭_本教材が守る切り分け.png"}


# ---------------------------------------------------------------------------
# 読み込み
# ---------------------------------------------------------------------------

def load_toc():
    """目次.yml を [{section, subtitle, parts: [{part, chapters: [id]}]}] に読む。"""
    sections, sec, part = [], None, None
    for raw in io.open(TOC_FILE, encoding="utf-8"):
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"  - section: (.+)$", line)
        if m:
            sec = {"section": m.group(1).strip(), "subtitle": "", "parts": []}
            sections.append(sec)
            part = None
            continue
        if sec is None:
            continue
        m = re.match(r"    subtitle: (.+)$", line)
        if m:
            sec["subtitle"] = m.group(1).strip()
            continue
        if re.match(r"    intro: ", line) or re.match(r"        intro: ", line):
            continue
        m = re.match(r"      - part: (.+)$", line)
        if m:
            part = {"part": m.group(1).strip(), "chapters": []}
            sec["parts"].append(part)
            continue
        m = re.match(r"\s+- ([a-z0-9-]+)\s*(?:#.*)?$", line)
        if m:
            if part is None:
                part = {"part": None, "chapters": []}
                sec["parts"].append(part)
            part["chapters"].append(m.group(1))
    if not sections:
        sys.exit("ERROR: 目次.yml が読めない")
    return sections


def parse_front_matter(text):
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm, hist = {}, []
    for line in m.group(1).split("\n"):
        h = HIST_RE.match(line)
        if h:
            hist.append({"date": h.group(1), "note": h.group(2).strip()})
            continue
        kv = re.match(r"([^\s:]+):\s*(.*)$", line)
        if kv:
            fm[kv.group(1)] = kv.group(2).strip()
    if hist:
        fm["history"] = hist
    return fm, text[m.end():]


def collect():
    """目次.yml の順に章を並べる。図も本文に出てくる順で拾う。"""
    by_id = {}
    for name in sorted(os.listdir(SRC_DIR)):
        if not name.endswith(".md"):
            continue
        text = io.open(os.path.join(SRC_DIR, name), encoding="utf-8").read()
        fm, body = parse_front_matter(text)
        if not fm.get("id"):
            sys.exit("ERROR: front matter に id が無い: chapters/%s" % name)
        by_id[fm["id"]] = (fm, body, name)

    rows, seen = [], set()
    for sec in load_toc():
        for part in sec["parts"]:
            for cid in part["chapters"]:
                if cid not in by_id:
                    sys.stderr.write("WARNING: 目次.yml の %s に対応する md が無い\n" % cid)
                    rows.append({"id": cid, "missing": True, "section": sec["section"],
                                 "part": part["part"]})
                    continue
                fm, body, name = by_id[cid]
                seen.add(cid)
                rows.append({
                    "id": cid,
                    "missing": False,
                    "title": fm.get("title") or cid,
                    "subtitle": fm.get("subtitle", ""),
                    "kind": fm.get("kind", ""),
                    "status": fm.get("status", "draft"),
                    "published": fm.get("published", ""),
                    "history": fm.get("history") or [],
                    "section": sec["section"],
                    "sec_subtitle": sec["subtitle"],
                    "part": part["part"],
                    "file": name,
                    "figures": [(m.group(1), m.group(2)) for m in IMG_RE.finditer(body)],
                })
    extra = sorted(set(by_id) - seen)
    if extra:
        sys.stderr.write("WARNING: 目次.yml に載っていない章: %s\n" % "、".join(extra))
    return rows


# ---------------------------------------------------------------------------
# 章一覧
# ---------------------------------------------------------------------------

def write_chapter_index(rows):
    out = [
        "# 章一覧（自動生成）",
        "",
        "**このファイルは `gen_index.py` の成果物。手で編集しない。**",
        "並び順を変えるのは `目次.yml`、章題を変えるのは各章の front matter。",
        "",
        "status: `draft`（執筆中）→ `review`（著者確認中）→ `approved`（**公開される**）",
        "",
    ]
    sec = part = None
    n = 0
    for r in rows:
        if r["section"] != sec:
            sec, part = r["section"], None
            sub = r.get("sec_subtitle") or ""
            out += ["", "## %s%s" % (sec, " ― " + sub if sub else ""), ""]
        if r["part"] != part:
            part = r["part"]
            if part:
                out += ["### %s" % part, ""]
            out += ["| | 章題 | id | status | 図 | ファイル |",
                    "|---|---|---|---|---|---|"]
        n += 1
        if r["missing"]:
            out.append("| %d | **mdが無い** | `%s` | | | |" % (n, r["id"]))
            continue
        title = r["title"] + ("<br><small>%s</small>" % r["subtitle"] if r["subtitle"] else "")
        out.append("| %d | %s | `%s` | %s | %d | [%s](../chapters/%s) |"
                   % (n, title, r["id"], r["status"], len(r["figures"]),
                      r["file"], r["file"]))
    done = sum(1 for r in rows if not r["missing"] and r["status"] == "approved")
    out += ["", "**計 %d本**（うち公開済み %d本）" % (n, done), "",
            "生成: %s" % datetime.date.today().isoformat(), ""]
    io.open(OUT_CHAPTERS, "w", encoding="utf-8").write("\n".join(out))
    return n, done


# ---------------------------------------------------------------------------
# 図版台帳
# ---------------------------------------------------------------------------

def write_figure_ledger(rows):
    have = {f for f in os.listdir(FIG_DIR) if f.lower().endswith(".png")}
    used, missing = set(), []
    body = ["# 図版台帳（自動生成）", "",
            "**このファイルは `gen_index.py` の成果物。手で編集しない。**",
            "元は `chapters/*.md` の `![キャプション](figures/…)` 記法と `figures/` の中身。",
            "図を足す・差し替えるのは `figures/`、参照を書くのは本文。", "",
            "命名規則は `<章id>_<図名>.png`。図名は日本語でよい。", ""]

    total = 0
    for r in rows:
        if r["missing"]:
            continue
        body += ["", "## %s　`%s`" % (r["title"], r["id"]), ""]
        if not r["figures"]:
            body.append("図なし。")
            continue
        body += ["| # | キャプション（本文の `![…]`） | ファイル | |",
                 "|---|---|---|---|"]
        for i, (cap, fn) in enumerate(r["figures"], 1):
            total += 1
            used.add(fn)
            ok = fn in have
            if not ok:
                missing.append((r["id"], fn))
            cap = re.sub(r"\s+", " ", cap).strip()
            if len(cap) > 90:
                cap = cap[:90] + "…"
            # 命名規則から外れた図は目で気づけるようにする
            pref = "" if fn.startswith(r["id"] + "_") else " ⚠️id不一致"
            body.append("| %d | %s | `%s` | %s%s |"
                        % (i, cap, fn, "" if ok else "⚠️**画像なし**", pref))

    orphan = sorted(have - used - FIXED_FIGURES)
    head = ["", "## 集計", "",
            "| | |", "|---|---|",
            "| 本文が参照する図 | %d点 |" % total,
            "| `figures/` にあるPNG | %d点 |" % len(have),
            "| 本文が参照するのに `figures/` に無い | %d点 |" % len(missing),
            "| `figures/` にあるのに本文から参照されていない | %d点 |" % len(orphan),
            ""]
    if missing:
        head += ["### ⚠️ 本文が参照するのに画像が無い", ""]
        head += ["- `%s`（%s）" % (fn, cid) for cid, fn in missing] + [""]
    if orphan:
        head += ["### `figures/` にあるが本文から参照されていない", "",
                 "章を削った・図を差し替えた名残の可能性がある。", ""]
        head += ["- `%s`" % f for f in orphan] + [""]
    head += ["生成: %s" % datetime.date.today().isoformat(), ""]

    io.open(OUT_FIGURES, "w", encoding="utf-8").write(
        "\n".join(body[:6] + head + body[6:]) + "\n")
    return total, len(have), len(missing), len(orphan)


def main():
    rows = collect()
    n, done = write_chapter_index(rows)
    total, have, miss, orph = write_figure_ledger(rows)
    sys.stderr.write(
        "資料/章一覧.md    : %d本（公開済み %d本）\n"
        "資料/図版台帳.md  : 参照%d点 / 実体%d点 / 欠け%d点 / 未参照%d点\n"
        % (n, done, total, have, miss, orph))


if __name__ == "__main__":
    main()
