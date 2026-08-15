#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""章を1本足す。front matter 付きのひな形を作り、目次.yml にも登録する。

    python3 new_chapter.py --id sunscreen --title 日焼け止め --part 外用
    python3 new_chapter.py --id glp1 --title GLP-1受容体作動薬 --section 美容内科
    python3 new_chapter.py --id peel-deep --title 深いピーリング --part 外用 --after chemical-peel

章を足すときに落ちやすいのは「md は書いたが 目次.yml に入れ忘れる」ことで、
そうなるとビルドがその章を黙って無視する。だから2つを必ず同時にやる。

ひな形は CLAUDE.md の「章の型」に合わせてある。骨を1本決めて、それだけを通す。
"""

import argparse
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(ROOT, "chapters")
TOC_FILE = os.path.join(ROOT, "目次.yml")

TEMPLATE = """---
id: {id}
title: {title}{subtitle_line}
kind: {kind}
status: draft
---

> **この章の前提**：{prereq}

（臨床の入口。読者が実際に見聞きしていること——業者資料・添付文書・自分が説明に
使っている言い回し・扱っている製剤や機器——から入る。**疑問からは入らない。**
**エピソードを作らない**。淡々と事実だけを短く置く。）

## この章の一言

> （この章の骨を1本、ここで宣言する。以降の節はすべてこれに奉仕させる。）

## 1　なぜこの見方が必要か

（いきなり各論の数字や分類から始めない。まず「なぜこの読み替えが要るか」を置く。
図があるなら先に出し、本文は図にないことだけ書く。）

## 2

## この章の到達点

1.
2.
3.
"""


def load_toc_lines():
    return io.open(TOC_FILE, encoding="utf-8").read().split("\n")


def existing_ids(lines):
    return {m.group(1) for m in
            (re.match(r"\s+- ([a-z0-9-]+)\s*(?:#.*)?$", l) for l in lines) if m}


def find_container(lines, part=None, section=None):
    """指定した部（または部を持たないセクション）の章リストの範囲を返す。

    戻り値は (最初の章の行番号, 最後の章の行番号, インデント)。
    """
    cur_sec, cur_part, start, indent = None, None, None, None
    hit = None
    for i, l in enumerate(lines):
        m = re.match(r"  - section: (.+)$", l)
        if m:
            cur_sec, cur_part = m.group(1).strip(), None
            continue
        m = re.match(r"      - part: (.+)$", l)
        if m:
            cur_part = m.group(1).strip()
            continue
        m = re.match(r"(\s+)- ([a-z0-9-]+)\s*(?:#.*)?$", l)
        if m:
            want = (part is not None and cur_part == part) or \
                   (section is not None and cur_sec == section and cur_part is None)
            if want:
                if hit is None:
                    hit = [i, i, len(m.group(1))]
                else:
                    hit[1] = i
            continue
    return hit


def list_places(lines):
    out, cur_sec, cur_part = [], None, None
    for l in lines:
        m = re.match(r"  - section: (.+)$", l)
        if m:
            cur_sec = m.group(1).strip(); cur_part = None
            out.append(("section", cur_sec))
            continue
        m = re.match(r"      - part: (.+)$", l)
        if m:
            cur_part = m.group(1).strip()
            out.append(("part", cur_part))
    return out


def main():
    ap = argparse.ArgumentParser(description="章を1本足す（ひな形＋目次.yml 登録）")
    ap.add_argument("--id", required=True, help="公開URLになる英字id。一度公開したら変えない")
    ap.add_argument("--title", required=True, help="章題（日本語）")
    ap.add_argument("--subtitle", default="", help="英語または短い副題（任意）")
    ap.add_argument("--part", help="入れる部の名前（例: 外用／注射／デバイス）")
    ap.add_argument("--section", help="部を持たないセクションに入れるとき（例: 美容内科）")
    ap.add_argument("--kind", default="", help="basic / applied / conclusion（既定は部から推測）")
    ap.add_argument("--after", help="この id の直後に入れる（既定は部の末尾）")
    ap.add_argument("--file", help="ファイル名（既定は 章題.md）")
    ap.add_argument("--prereq", default="", help="前提章の id をカンマ区切りで（[[id]] に展開）")
    args = ap.parse_args()

    if not re.match(r"^[a-z][a-z0-9-]*$", args.id):
        sys.exit("ERROR: id は英小文字・数字・ハイフンだけにする: %s" % args.id)
    if not args.part and not args.section:
        sys.exit("ERROR: --part か --section のどちらかが要る")

    lines = load_toc_lines()
    ids = existing_ids(lines)
    if args.id in ids:
        sys.exit("ERROR: id が既にある: %s" % args.id)

    hit = find_container(lines, args.part, args.section)
    if hit is None:
        places = list_places(lines)
        sys.exit("ERROR: 「%s」が目次.yml に無い。\n入れられる場所:\n%s"
                 % (args.part or args.section,
                    "\n".join("  %-8s %s" % (k, v) for k, v in places)))
    first, last, indent = hit

    at = last
    if args.after:
        if args.after not in ids:
            sys.exit("ERROR: --after の id が無い: %s" % args.after)
        for i in range(first, last + 1):
            if re.match(r"\s+- %s\s*(?:#.*)?$" % re.escape(args.after), lines[i]):
                at = i
                break
        else:
            sys.exit("ERROR: --after の id は「%s」の中に無い" % (args.part or args.section))

    # ファイルを先に作る（目次だけ更新して md が無い状態を作らない）
    fname = args.file or (args.title + ".md")
    if not fname.endswith(".md"):
        fname += ".md"
    path = os.path.join(SRC_DIR, fname)
    if os.path.exists(path):
        sys.exit("ERROR: ファイルが既にある: chapters/%s" % fname)

    kind = args.kind or ("basic" if (args.part or "") in
                         ("細胞の地図", "情報をどう読むか", "エネルギー", "材料を感知し作る",
                          "掃除と作り直し", "傷つくとどうなるか", "加齢で何が変わるか",
                          "皮膚・脂肪・筋の生化学") else "applied")
    prereq = "・".join("[[%s]]" % x.strip() for x in args.prereq.split(",") if x.strip()) \
        or "[[id]]（この章を読む前に押さえておくもの）"
    body = TEMPLATE.format(
        id=args.id, title=args.title,
        subtitle_line=("\nsubtitle: " + args.subtitle) if args.subtitle else "",
        kind=kind, prereq=prereq)
    io.open(path, "w", encoding="utf-8").write(body)

    # 目次.yml に1行足す。コメントの位置は既存の行に合わせる
    width = 28
    m = re.match(r"(\s+- )([a-z0-9-]+)(\s*)#", lines[first])
    if m:
        width = len(m.group(2)) + len(m.group(3))
    entry = "%s- %s%s# %s" % (" " * indent, args.id,
                              " " * max(1, width - len(args.id)), args.title)
    lines.insert(at + 1, entry)
    io.open(TOC_FILE, "w", encoding="utf-8").write("\n".join(lines))

    print("作成: chapters/%s" % fname)
    print("登録: 目次.yml の「%s」%s" % (args.part or args.section,
                                        ("（%s の直後）" % args.after) if args.after else "（末尾）"))
    print("")
    print("次に:")
    print("  1. chapters/%s を書く（骨を1本決めて、それだけを通す）" % fname)
    print("  2. 図は figures/%s_<図名>.png に置き、本文から ![キャプション](figures/…) で参照" % args.id)
    print("  3. python3 gen_index.py     … 章一覧・図版台帳を更新")
    print("  4. .venv/bin/python build.py --preview  … プレビューで確認")
    print("  5. 確定したら status: approved にし、published と history を入れる")


if __name__ == "__main__":
    main()
