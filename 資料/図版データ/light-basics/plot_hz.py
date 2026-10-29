"""Generate a pedagogical pulse-count diagram, not a device waveform."""
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/skin-orchestra-mpl')
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle
ROOT=Path(__file__).resolve().parents[3]
f='/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc'
fm.fontManager.addfont(f)
plt.rcParams.update({'font.family':fm.FontProperties(fname=f).get_name(),'svg.fonttype':'path','font.size':16})
fig=plt.figure(figsize=(10,7.5),facecolor='white')
fig.text(.06,.86,'Hzは「1秒間に何発照射するか」',fontsize=24,color='#1d4f91')
blue='#1d4f91';gray='#64748b'
for y,hz,positions in [(.57,2,[.1,.6]),(.29,5,[.1,.3,.5,.7,.9])]:
 ax=fig.add_axes([.23,y,.7,.18]);ax.set_xlim(0,1);ax.set_ylim(0,1.4)
 for sp in ['left','right','top']:ax.spines[sp].set_visible(False)
 ax.spines['bottom'].set_color(gray);ax.set_yticks([]);ax.set_xticks([0,.5,1],['0','0.5','1秒']);ax.tick_params(axis='x',labelsize=14)
 for i,x in enumerate(positions):
  ax.add_patch(Rectangle((x,.0),.025,.65,facecolor=blue));ax.text(x+.0125,.75,str(i+1),ha='center',fontsize=15,color=blue)
 a,b=positions[:2];ax.annotate('',xy=(a,1.12),xytext=(b,1.12),arrowprops={'arrowstyle':'|-|','color':gray})
 ax.text((a+b)/2,1.25,f'{1/hz:g}秒間隔',ha='center',fontsize=15)
 fig.text(.06,y+.07,f'{hz} Hz',fontsize=25,color=blue)
 fig.text(.06,y+.015,f'1秒間に{hz}発',fontsize=16)
fig.text(.23,.22,'両段とも同じ1秒間。1発の幅と高さはそろえています。',fontsize=13,color=gray)
fig.lines.append(plt.Line2D([.06,.94],[.18,.18],transform=fig.transFigure,color='#c5cdd6'))
ax=fig.add_axes([.09,.055,.26,.10]);ax.set_xlim(0,1);ax.set_ylim(-.35,1.1);ax.axis('off')
ax.plot([.05,.3,.3,.7,.7,.95],[0,0,.9,.9,0,0],color=blue,lw=2.5)
ax.annotate('',xy=(.3,-.23),xytext=(.7,-.23),arrowprops={'arrowstyle':'|-|','color':gray})
fig.text(.40,.12,'1発を拡大すると…',fontsize=16,color=blue)
fig.text(.40,.073,'光を出している長さが「パルス幅」',fontsize=17)
fig.text(.06,.012,'模式図：パルスの幅・高さは実際の機器の値ではありません。',fontsize=12,color=gray)
fig.savefig(ROOT/'figures/light-basics_Hzの比較.svg',bbox_inches='tight')
fig.savefig('/tmp/light-hz.png',dpi=140,bbox_inches='tight')
