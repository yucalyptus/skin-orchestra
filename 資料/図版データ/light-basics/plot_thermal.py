import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/skin-orchestra-mpl')
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Circle
root=Path(__file__).resolve().parents[3]
f='/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc';fm.fontManager.addfont(f)
plt.rcParams.update({'font.family':fm.FontProperties(fname=f).get_name(),'svg.fonttype':'path'})
fig=plt.figure(figsize=(10,5.5),facecolor='white')
fig.text(.05,.93,'パルス幅と熱の広がり',fontsize=23,color='#1d4f91')
fig.text(.05,.85,'同じ標的・同じ吸収エネルギーで、照射中の熱拡散を比較',fontsize=13)
for left,long in [(.05,False),(.53,True)]:
 ax=fig.add_axes([left,.23,.42,.50]);ax.set(xlim=(-1,1),ylim=(-1,1));ax.set_aspect('equal');ax.axis('off')
 if long:
  for r,c in [(.74,'#fbf2f0'),(.58,'#f3dbd5'),(.42,'#e3b4a8')]:ax.add_patch(Circle((0,0),r,color=c))
 else:ax.add_patch(Circle((0,0),.36,color='#fbf2f0'))
 ax.add_patch(Circle((0,0),.27,color='#a34b40'))
 fig.text(left+.21,.76,'TRTより長いパルス' if long else 'TRTより短いパルス',ha='center',fontsize=18,color='#1d4f91')
 fig.text(left+.21,.20,'照射中に周囲へ熱が広がる' if long else '照射中の熱拡散が少ない',ha='center',fontsize=15)
fig.text(.05,.095,'TRT（熱緩和時間）は、標的が熱を失う時間の目安です。',fontsize=13)
fig.text(.05,.04,'照射後はどちらも冷却します。',fontsize=13)
fig.savefig(root/'figures/light-basics_熱緩和_改訂.svg',bbox_inches='tight')
fig.savefig('/tmp/light-thermal-fixed.png',dpi=140,bbox_inches='tight')
