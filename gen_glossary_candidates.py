#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用語集を作るための候補抽出と、「登場章」列の更新。

本文に英語のまま埋め込まれている専門用語（このプロジェクトの表記方針）を拾い、
    - 何回出てくるか
    - どの章で初めて出てくるか
    - いくつの章にまたがるか
を出す。用語集に載せるべきなのは「何章にもまたがって出てくるのに、
初出の章でしか説明されていない語」なので、その判断材料にする。

    python3 gen_glossary_candidates.py            # 候補を TSV で出す
    python3 gen_glossary_candidates.py --update   # 資料/用語集.md の「登場章」列を埋める

章の並び順の正典は 目次.yml、章の正体は front matter の id。
このスクリプトはどちらも実際に読むので、章を足す・分ける・並べ替えても追従する。
定義文は書かない（それは人／エージェントの仕事）。
"""

import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(ROOT, "chapters")
TOC_FILE = os.path.join(ROOT, "目次.yml")
GLOSSARY = os.path.join(ROOT, "資料", "用語集.md")


# ---------------------------------------------------------------------------
# 章の一覧 ―― 目次.yml の並び順で [(id, 本文), ...] を返す
# ---------------------------------------------------------------------------

def toc_order():
    """目次.yml に登場する章 id を、並び順のまま返す。"""
    ids = []
    with open(TOC_FILE, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\s*-\s+([a-z0-9\-]+)\s*(?:#.*)?$", line)
            if m:
                ids.append(m.group(1))
    if not ids:
        sys.exit("ERROR: 目次.yml から章 id が読めない")
    return ids


def chapter_texts():
    """[(id, 本文テキスト), ...] を 目次.yml の順で返す。図の説明は除く。"""
    by_id = {}
    for name in os.listdir(SRC_DIR):
        if not name.endswith(".md"):
            continue
        path = os.path.join(SRC_DIR, name)
        text = open(path, encoding="utf-8").read()
        m = re.search(r"^id:\s*([a-z0-9\-]+)\s*$", text, re.M)
        if m:
            by_id[m.group(1)] = text

    out = []
    for cid in toc_order():
        if cid not in by_id:
            continue                      # 目次にあって md が無い章は黙って飛ばす
        body = by_id[cid]
        body = re.sub(r"\A---\n.*?\n---\n", "", body, flags=re.S)   # front matter は本文ではない
        body = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", body)   # 図の説明は対象外
        out.append((cid, body))
    return out


# 英字の語（ハイフン・ドット・数字を含む）。日本語文中に埋まった専門用語を拾う。
TERM = re.compile(r"[A-Za-zα-ωΑ-Ω][A-Za-zα-ωΑ-Ω0-9\-–/]*(?:\s[A-Za-z][a-z]+){0,2}")

# 専門用語ではないもの
STOP = {
    "a", "an", "and", "the", "of", "in", "to", "or", "vs", "is", "are", "be",
    "for", "with", "by", "on", "at", "as", "it", "this", "that", "from",
    "not", "no", "yes", "e", "g", "i", "ie", "eg", "etc", "et", "al",
    "png", "md", "py", "html", "webp", "images", "http", "https", "www",
    "com", "org", "doi", "pmid", "pmc", "true", "false",
}


def norm(t):
    return t.strip(" -–/").rstrip(".")


def main():
    count = defaultdict(int)
    chapters = defaultdict(set)
    first = {}

    for cid, txt in chapter_texts():
        txt = re.sub(r"\[[^\]]*\]\([^)]*\)", " ", txt)
        txt = re.sub(r"```.*?```", " ", txt, flags=re.S)
        txt = re.sub(r"`[^`]*`", " ", txt)
        txt = re.sub(r"\[\[[^\]]*\]\]", " ", txt)           # 相互参照は語ではない
        for raw in TERM.findall(txt):
            t = norm(raw)
            if len(t) < 3 or t.lower() in STOP or t.isdigit():
                continue
            count[t] += 1
            chapters[t].add(cid)
            first.setdefault(t, cid)

    rows = [(t, count[t], len(chapters[t]), first[t]) for t in count]
    rows.sort(key=lambda r: (-r[2], -r[1]))     # 章をまたぐ数 → 出現数

    print("用語\t出現数\t登場章数\t初出章")
    for t, c, nch, f in rows:
        if nch < 2 and c < 3:
            continue
        print("%s\t%d\t%d\t%s" % (t, c, nch, f))


# ---------------------------------------------------------------------------
# 資料/用語集.md の「登場章」列を更新する（--update）
#   章を足す・分ける・並べ替えても追従できるよう、章の一覧は手で書かず、
#   本文を実際に検索して埋める。定義の列には触らない。
# ---------------------------------------------------------------------------

# 表示名から検索パターンを作れない語だけ、ここで上書きする。
ALIAS = {
    "NAD⁺・NADH": ["NAD⁺", "NADH"],
    "mTOR・mTORC1": ["mTOR"],
    "TCA cycle": ["TCA"],
    "salvage pathway": ["salvage"],
    "ubiquitin–proteasome": ["ubiquitin"],
    "YAP/TAZ": ["YAP"],
    "M1": ["M1"],
    "M2": ["M2"],
    "PBM": ["PBM", "photobiomodulation"],
    "AGE": ["AGE"],
    "DEJ": ["DEJ"],
    "HSP": ["HSP"],
    "ubiquinone (CoQ10)": ["ubiquinone", "CoQ10"],
}


def _word_re(pat):
    """英数字で始まり英数字で終わる語は、前後が英数字でないときだけ拾う。"""
    if re.match(r"^[A-Za-z0-9]", pat) and re.search(r"[A-Za-z0-9]$", pat):
        return re.compile(r"(?<![A-Za-z0-9])%s(?![A-Za-z0-9])" % re.escape(pat))
    return re.compile(re.escape(pat))


def _compact(ids, order):
    """目次の並びで3章以上続いたら「[[a]]〜[[b]]」にまとめる。列が長くなりすぎないように。"""
    pos = {cid: i for i, cid in enumerate(order)}
    ids = sorted(ids, key=lambda c: pos[c])
    out, i = [], 0
    while i < len(ids):
        j = i
        while j + 1 < len(ids) and pos[ids[j + 1]] == pos[ids[j]] + 1:
            j += 1
        if j - i >= 2:
            out.append("[[%s]]〜[[%s]]" % (ids[i], ids[j]))
        else:
            out.extend("[[%s]]" % c for c in ids[i:j + 1])
        i = j + 1
    return ", ".join(out)


def update_glossary():
    texts = chapter_texts()
    order = [cid for cid, _ in texts]

    src = open(GLOSSARY, encoding="utf-8").read()
    rows = updated = 0

    def fix(line):
        nonlocal rows, updated
        cells = line.split("|")
        if len(cells) != 5:
            return line
        term = cells[1].strip()
        if not term or term in ("用語", "---"):
            return line
        rows += 1
        pats = ALIAS.get(term) or [re.sub(r"（.*?）|\(.*?\)", "", term).strip()]
        res = [_word_re(p) for p in pats]
        hits = [cid for cid, body in texts if any(r.search(body) for r in res)]
        new = _compact(hits, order) if hits else "—"
        if cells[3].strip() != new:
            updated += 1
        cells[3] = " %s " % new
        return "|".join(cells)

    out = "\n".join(fix(l) for l in src.split("\n"))
    open(GLOSSARY, "w", encoding="utf-8").write(out)
    sys.stderr.write("資料/用語集.md: %d語の「登場章」を更新（変更 %d語）\n" % (rows, updated))


if __name__ == "__main__":
    if "--update" in sys.argv:
        update_glossary()
    else:
        main()
