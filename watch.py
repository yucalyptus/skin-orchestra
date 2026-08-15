#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""figures/ と chapters/ と 目次.yml を見張って、変わったら自動でプレビューを作り直す。

    python3 watch.py            # プレビュー（_preview/）だけ作り直す
    python3 watch.py --docs     # 公開版（docs/）も一緒に作り直す

図を差し替えたり本文を直したりするたびに手でビルドを流すのは忘れる。
走らせっぱなしにしておけば、保存した数秒後にはプレビューが最新になっている。
止めるのは Ctrl+C。

WebP への変換は build.py がやる。**figures/ に置くのは常にPNGだけ**でよく、
公開用のWebPを人が作る必要はない（両方を人が持つと必ず食い違う）。
"""

import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
WATCH = [os.path.join(ROOT, "chapters"),
         os.path.join(ROOT, "figures")]
WATCH_FILES = [os.path.join(ROOT, "目次.yml")]
INTERVAL = 2.0          # 秒。これくらいなら保存してすぐ反映される
SETTLE = 1.0            # 保存直後はまだ書き込み中のことがあるので少し待つ

PY = os.path.join(ROOT, ".venv", "bin", "python")
if not os.path.exists(PY):
    sys.exit("ERROR: .venv がありません。先に作ってください：\n"
             "  python3 -m venv .venv && .venv/bin/pip install -q Pillow")


def snapshot():
    """見張る対象の (パス, 更新時刻, サイズ) の集合。中身の変更も名前の増減も拾う。"""
    state = {}
    for d in WATCH:
        if not os.path.isdir(d):
            continue
        for name in os.listdir(d):
            if name.startswith("."):
                continue
            p = os.path.join(d, name)
            try:
                st = os.stat(p)
                state[p] = (st.st_mtime, st.st_size)
            except OSError:
                pass
    for p in WATCH_FILES:
        try:
            st = os.stat(p)
            state[p] = (st.st_mtime, st.st_size)
        except OSError:
            pass
    return state


def diff(old, new):
    added = sorted(set(new) - set(old))
    removed = sorted(set(old) - set(new))
    changed = sorted(p for p in set(old) & set(new) if old[p] != new[p])
    return added, removed, changed


def run(with_docs):
    """索引を作り直してからビルドする。順番が逆だと台帳が古いまま残る。"""
    ok = True
    for cmd in ([sys.executable, os.path.join(ROOT, "gen_index.py")],
                [PY, os.path.join(ROOT, "build.py"), "--preview"]) + \
               ((([PY, os.path.join(ROOT, "build.py")]),) if with_docs else ()):
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        out = (r.stdout + r.stderr).strip()
        if out:
            print("\n".join("   " + l for l in out.split("\n")))
        if r.returncode != 0:
            ok = False
            print("   → 失敗（%s）。直すまでプレビューは前のままです。" % os.path.basename(cmd[-1]))
            break
    return ok


def main():
    with_docs = "--docs" in sys.argv
    print("見張っています： chapters/ figures/ 目次.yml")
    print("出力先        ： _preview/%s" % ("　＋　docs/（公開版）" if with_docs else ""))
    print("止めるとき    ： Ctrl+C")
    print("-" * 62)
    state = snapshot()
    run(with_docs)
    print("-" * 62)
    try:
        while True:
            time.sleep(INTERVAL)
            new = snapshot()
            added, removed, changed = diff(state, new)
            if not (added or removed or changed):
                continue
            time.sleep(SETTLE)              # 書き込み途中を掴まないように
            new = snapshot()
            added, removed, changed = diff(state, new)
            state = new
            stamp = time.strftime("%H:%M:%S")
            for label, items in (("追加", added), ("削除", removed), ("変更", changed)):
                for p in items:
                    print("[%s] %s: %s" % (stamp, label, os.path.relpath(p, ROOT)))
            run(with_docs)
            print("-" * 62)
    except KeyboardInterrupt:
        print("\n終了しました。")


if __name__ == "__main__":
    main()
