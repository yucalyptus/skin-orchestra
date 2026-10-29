"""吸収曲線（本文幅・v3）。文字の重なりを除き、標的の段を曲線の直下に寄せる。データと換算は plot_readable.py と同じ。"""
import os, re
os.environ.setdefault('MPLCONFIGDIR', '/tmp/skin-orchestra-mpl')
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle
B = Path(__file__).resolve().parent; R = B.parents[2]
f = '/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc'; fm.fontManager.addfont(f)
plt.rcParams.update({'font.family': fm.FontProperties(fname=f).get_name(), 'font.size': 13, 'svg.fonttype': 'path',
                     'axes.spines.top': False, 'axes.spines.right': False})
INK, RED, BLUE, GRAY, LINE = '#1c1d23', '#a34b40', '#1d4f91', '#64748b', '#c5cdd6'
hb = np.array([[float(x) for x in m] for m in re.findall(r'^\s*(\d+)\s+(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)\s*$', (B/'hemoglobin.html').read_text(), re.M)])
w = np.array([[float(x) for x in l.split()] for l in (B/'hale73.txt').read_text().splitlines() if re.match(r'^\s*\d+(?:\.\d+)?\s+[0-9.eE+\-]+\s*$', l)])
su = np.array([[float(v) for v in l.split()] for l in (B/'bloodSuzaki.dat').read_text().splitlines() if re.match(r'^\d+\s+[0-9.eE+\-]+\s+[0-9.eE+\-]+\s*$', l)])

def save(fig, name):
    fig.savefig(R/'figures'/f'{name}.svg', facecolor='white')
    fig.savefig(f'/tmp/{name}.png', dpi=100, facecolor='white')
    plt.close(fig)

# 可視〜近赤外
fig = plt.figure(figsize=(7, 5.6))
a = fig.add_axes([.15, .38, .78, .52]); t = fig.add_axes([.15, .03, .78, .22], sharex=a)
x = np.arange(400, 1101)
a.semilogy(x, 1.7e12 * x**-3.48, c=INK, lw=2.4)
m = (hb[:, 0] >= 400) & (hb[:, 0] <= 1000)
for j, ls in [(1, '-'), (2, '--')]:
    a.plot(hb[m, 0], hb[m, j] * 2.303 * 150 / 64500, c=RED, lw=2.2, ls=ls)
    m2 = (su[:, 0] >= 1000) & (su[:, 0] <= 1100); a.plot(su[m2, 0], su[m2, j], c=RED, lw=2.2, ls=ls)
a.plot(w[:, 0], w[:, 1], c=BLUE, lw=2.4)
a.set(xlim=(400, 1100), ylim=(1e-4, 1e4)); a.set_ylabel('吸収係数（1/cm、対数）', fontsize=12.5)
a.set_yticks([1e-4, 1e-2, 1, 1e2, 1e4]); a.set_xticks([400, 500, 600, 700, 800, 900, 1000, 1100]); a.minorticks_off()
a.grid(axis='y', alpha=.15); a.tick_params(labelsize=12)
a.set_xlabel('波長（nm）', fontsize=12.5, labelpad=2)
a.text(760, 350, 'メラニン', fontsize=14, color=INK)
from matplotlib.lines import Line2D
a.legend([Line2D([], [], c=RED, lw=2.2), Line2D([], [], c=RED, lw=2.2, ls='--')], ['酸素化ヘモグロビン', '脱酸素化ヘモグロビン'], loc='lower right', frameon=False, fontsize=12.5, labelcolor=RED, handlelength=2.6)
a.text(450, 1.6e-3, '水', fontsize=14, color=BLUE)
for start, end, label, col in [(400, 700, '可視光線', '#e9edf4'), (700, 1100, '近赤外線', '#f2f4f7')]:
    a.add_patch(Rectangle((start, 1.03), end - start, .08, transform=a.get_xaxis_transform(), facecolor=col, clip_on=False, lw=0))
    a.text((start + end) / 2, 1.07, label, transform=a.get_xaxis_transform(), ha='center', va='center', fontsize=12.5)
t.set_ylim(-.5, 2.6); t.axis('off')
t.text(400, 2.35, '代表的な治療波長（nm）と標的', ha='left', va='center', fontsize=12, color=GRAY)
for y, name, col in [(1, 'メラニン', INK), (0, '血管', RED)]:
    t.axhline(y, c=LINE, lw=.9)
    t.text(-.02, y, name, transform=t.get_yaxis_transform(), ha='right', va='center', fontsize=12.5, color=col)
for v in [532, 595, 694, 755, 810, 1064]:
    t.text(v, 1.6, str(v), ha='center', fontsize=12)
    a.axvline(v, ls=':', c='#b4bcc7', lw=.9, zorder=0)
for v in [532, 694, 755, 810, 1064]: t.plot(v, 1, 'o', c=INK, ms=8)
for v in [532, 595, 1064]: t.plot(v, 0, 'o', c=RED, ms=8)
save(fig, 'light-basics_吸収曲線_可視近赤外_v3')

# 赤外の水
fig = plt.figure(figsize=(7, 3.0)); a = fig.add_axes([.15, .2, .78, .66])
a.loglog(w[:, 0], w[:, 1], c=BLUE, lw=2.4)
a.set(xlim=(1100, 12000), ylim=(.1, 1e5)); a.set_ylabel('吸収係数（1/cm、対数）', fontsize=12.5); a.set_xlabel('波長（nm、対数）', fontsize=12.5)
a.set_xticks([1500, 2000, 3000, 5000, 10000], labels=['1500', '2000', '3000', '5000', '10000']); a.set_yticks([.1, 10, 1000, 100000]); a.minorticks_off()
a.grid(axis='y', alpha=.15); a.tick_params(labelsize=12)
for v, label in [(2940, 'Er:YAG 2940 nm'), (10600, 'CO₂ 10600 nm')]:
    a.axvline(v, c='#9ba7b7', ls=':', lw=1)
    a.text(v, 1.04, label, transform=a.get_xaxis_transform(), ha='right' if v > 5000 else 'center', fontsize=12.5)
a.text(1250, 3000, '水', fontsize=14, color=BLUE)
save(fig, 'light-basics_吸収曲線_赤外水_v3')
print('ok')
