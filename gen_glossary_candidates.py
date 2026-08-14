#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用語集を作るための候補抽出。

本文に英語のまま埋め込まれている専門用語（このプロジェクトの表記方針）を拾い、
    - 何回出てくるか
    - どの章で初めて出てくるか
    - いくつの章にまたがるか
を出す。用語集に載せるべきなのは「何章にもまたがって出てくるのに、
初出の章でしか説明されていない語」なので、その判断材料にする。

    python3 gen_glossary_candidates.py > /tmp/glossary_candidates.tsv

定義文は書かない（それは人／エージェントの仕事）。ここは候補出しまで。
"""

import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from build_site import MANIFEST  # noqa: E402

ORDER = [stem for _, chs in MANIFEST for stem, _, _ in chs]

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

    for stem in ORDER:
        path = os.path.join(ROOT, "本文", stem + ".md")
        if not os.path.exists(path):
            continue
        txt = open(path, encoding="utf-8").read()
        # 図の参照・リンク・コードブロックは対象外
        txt = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", txt)
        txt = re.sub(r"\[[^\]]*\]\([^)]*\)", " ", txt)
        txt = re.sub(r"```.*?```", " ", txt, flags=re.S)
        txt = re.sub(r"`[^`]*`", " ", txt)

        ch = re.match(r"(第[\d.]+[a-z]?章|最終章)", stem).group(1)
        for raw in TERM.findall(txt):
            t = norm(raw)
            if len(t) < 3 or t.lower() in STOP:
                continue
            if t.isdigit():
                continue
            count[t] += 1
            chapters[t].add(ch)
            first.setdefault(t, ch)

    rows = [(t, count[t], len(chapters[t]), first[t]) for t in count]
    # 章をまたぐ数 → 出現数 の順。用語集の優先度そのもの。
    rows.sort(key=lambda r: (-r[2], -r[1]))

    print("用語\t出現数\t登場章数\t初出章")
    for t, c, nch, f in rows:
        if nch < 2 and c < 3:
            continue
        print("%s\t%d\t%d\t%s" % (t, c, nch, f))




# ---------------------------------------------------------------------------
# 用語集.md の「登場章」列を更新する（--update）
#
# 章を足す・分ける・並べ替えても追従できるよう、章の一覧は手で書かず、
# 本文を実際に検索して埋める。定義の列には触らない。
# ---------------------------------------------------------------------------

GLOSSARY = os.path.join(ROOT, "用語集.md")

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
}


def _chapter_label(stem):
    m = re.match(r"(第[\d.]+[a-z]?章|最終章)", stem)
    return m.group(1) if m else stem


def _word_re(pat):
    """英数字で始まり英数字で終わる語は、前後が英数字でないときだけ拾う。"""
    if re.match(r"^[A-Za-z0-9]", pat) and re.search(r"[A-Za-z0-9]$", pat):
        return re.compile(r"(?<![A-Za-z0-9])%s(?![A-Za-z0-9])" % re.escape(pat))
    return re.compile(re.escape(pat))


def _compact(labels):
    """「第1章 第2章 第3章 第7章」→「第1〜3章, 第7章」。列が長くなりすぎないように。"""
    nums, out = [], []
    for l in labels:
        m = re.match(r"第(\d+)章$", l)
        nums.append(int(m.group(1)) if m else None)
    i = 0
    while i < len(labels):
        if nums[i] is None:
            out.append(labels[i]); i += 1; continue
        j = i
        while j + 1 < len(labels) and nums[j + 1] == nums[j] + 1:
            j += 1
        if j - i >= 2:
            out.append("第%d〜%d章" % (nums[i], nums[j]))
        else:
            out.extend(labels[i:j + 1])
        i = j + 1
    return ", ".join(out)


def update_glossary():
    order = [stem for _, chs in MANIFEST for stem, _, _ in chs]
    texts = []
    for stem in order:
        p = os.path.join(ROOT, "本文", stem + ".md")
        if os.path.exists(p):
            body = open(p, encoding="utf-8").read()
            body = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", body)   # 図の説明は除く
            texts.append((_chapter_label(stem), body))

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
        pats = ALIAS.get(term) or [re.sub(r"（.*?）", "", term).strip()]
        # 部分一致だと M1 が別語に食われるので、英数字の語は前後の境界を見る。
        res = [_word_re(p) for p in pats]
        hits = [lab for lab, body in texts if any(r.search(body) for r in res)]
        new = _compact(hits) if hits else "—"
        if cells[3].strip() != new:
            updated += 1
        cells[3] = " %s " % new
        return "|".join(cells)

    out = "\n".join(fix(l) for l in src.split("\n"))
    open(GLOSSARY, "w", encoding="utf-8").write(out)
    sys.stderr.write("用語集.md: %d語の「登場章」を更新（変更 %d語）\n" % (rows, updated))


if __name__ == "__main__":
    if "--update" in sys.argv:
        update_glossary()
    else:
        main()
