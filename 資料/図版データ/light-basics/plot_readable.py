"""Readable spectral panels and TRT figure; 7-inch canvas, >=11.5 pt type."""
import os,re
os.environ.setdefault('MPLCONFIGDIR','/tmp/skin-orchestra-mpl')
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Circle, Rectangle
B=Path(__file__).resolve().parent;R=B.parents[2]
f='/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc';fm.fontManager.addfont(f)
plt.rcParams.update({'font.family':fm.FontProperties(fname=f).get_name(),'font.size':11.5,'svg.fonttype':'path','axes.spines.top':False,'axes.spines.right':False})
hb=np.array([[float(x) for x in m] for m in re.findall(r'^\s*(\d+)\s+(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)\s*$',(B/'hemoglobin.html').read_text(),re.M)])
w=np.array([[float(x) for x in l.split()] for l in (B/'hale73.txt').read_text().splitlines() if re.match(r'^\s*\d+(?:\.\d+)?\s+[0-9.eE+\-]+\s*$',l)])
su=np.array([[float(v) for v in l.split()] for l in (B/'bloodSuzaki.dat').read_text().splitlines() if re.match(r'^\d+\s+[0-9.eE+\-]+\s+[0-9.eE+\-]+\s*$',l)])
def save(fig,name):
 fig.savefig(R/'figures'/f'{name}.svg',facecolor='white')
 fig.savefig('/tmp/'+name+'_700.png',dpi=100,facecolor='white')
 plt.close(fig)
fig=plt.figure(figsize=(7,6.0))
a=fig.add_axes([.14,.40,.83,.49]);t=fig.add_axes([.14,.09,.83,.19],sharex=a)
x=np.arange(400,1101)
a.semilogy(x,1.7e12*x**-3.48,c='#1c1d23',lw=2.2)
m=(hb[:,0]>=400)&(hb[:,0]<=1000)
for j,ls in [(1,'-'),(2,'--')]:
 a.plot(hb[m,0],hb[m,j]*2.303*150/64500,c='#a34b40',lw=2,ls=ls)
 m2=(su[:,0]>=1000)&(su[:,0]<=1100);a.plot(su[m2,0],su[m2,j],c='#a34b40',lw=2,ls=ls)
a.plot(w[:,0],w[:,1],c='#1d4f91',lw=2)
a.set(xlim=(400,1100),ylim=(1e-4,1e4),ylabel='吸収係数（1/cm）')
a.set_yticks([1e-4,1e-2,1,100,10000]);a.set_xticks([400,600,800,1000]);a.minorticks_off();a.grid(axis='y',alpha=.15)
a.text(850,800,'メラニン',fontsize=13)
a.annotate('酸素化Hb',xy=(920,5.5),xytext=(845,30),fontsize=12,color='#a34b40',arrowprops={'arrowstyle':'-','lw':.8,'color':'#a34b40'})
a.annotate('脱酸素化Hb',xy=(880,3),xytext=(760,.12),fontsize=12,color='#a34b40',arrowprops={'arrowstyle':'-','lw':.8,'color':'#a34b40'})
a.text(570,.00045,'水',fontsize=13,color='#1d4f91')
for start,end,label,col in [(400,700,'可視光線（400〜700 nm）','#e9edf4'),(700,1100,'近赤外線','#f2f4f7')]:
 a.add_patch(Rectangle((start,1.055),end-start,.09,transform=a.get_xaxis_transform(),facecolor=col,clip_on=False,lw=0))
 a.text((start+end)/2,1.10,label,transform=a.get_xaxis_transform(),ha='center',va='center',fontsize=12)
fig.text(.97,.34,'波長（nm）',ha='right',fontsize=11.5)
t.set_ylim(-.45,2.2);t.axis('off')
t.text(0,1.15,'主な治療標的',transform=t.transAxes,fontsize=12)
for y,name,col in [(1,'メラニン','#1c1d23'),(0,'血管','#a34b40')]:
 t.axhline(y,c='#d5dbe3',lw=.8)
 t.text(-.025,y,name,transform=t.get_yaxis_transform(),ha='right',va='center',fontsize=11.5,color=col)
for v in [532,595,694,755,810,1064]:
 t.text(v,1.8,str(v),ha='center',fontsize=11.5)
 t.plot([v,v],[-.15,1.5],ls=':',c='#b4bcc7',lw=.8,zorder=0)
for v in [532,694,755,810,1064]:t.plot(v,1,'o',c='#1c1d23',ms=7)
for v in [532,595,1064]:t.plot(v,0,'o',c='#a34b40',ms=7)
save(fig,'light-basics_吸収曲線_可視近赤外_本文幅')
fig=plt.figure(figsize=(7,2.9));a=fig.add_axes([.14,.23,.83,.61])
a.loglog(w[:,0],w[:,1],c='#1d4f91',lw=2.3)
a.set(xlim=(1100,12000),ylim=(.1,1e5),ylabel='吸収係数（1/cm）',xlabel='波長（nm）')
a.set_xticks([1500,3000,10000],labels=['1500','3000','10000']);a.set_yticks([.1,100,100000]);a.minorticks_off();a.grid(axis='y',alpha=.15)
for x,label,y in [(2940,'Er:YAG 2940',1.07),(10600,'CO₂ 10600',1.07)]:
 a.axvline(x,c='#9ba7b7',ls=':',lw=1)
 a.text(x,y,label,transform=a.get_xaxis_transform(),ha='center',fontsize=11.5)
a.text(4400,4,'水',fontsize=13,color='#1d4f91')
save(fig,'light-basics_吸収曲線_赤外水_本文幅')
# TRT: aligned time axes, equal pulse energy shown by equal rectangular areas.
fig=plt.figure(figsize=(7,4.6));ax=fig.add_axes([.05,.06,.90,.88]);ax.set(xlim=(0,10),ylim=(0,6));ax.axis('off')
ax.text(.1,5.65,'パルス幅と熱緩和時間（TRT）',fontsize=15)
ax.text(7.65,5.1,'照射終了時',ha='center',fontsize=11.5)
for base,width,height,label,long in [(3.1,.8,.95,'TRTより短い',False),(1.0,3.8,.2,'TRTより長い',True)]:
 ax.text(.1,base+1.43,label,fontsize=12)
 ax.annotate('',xy=(5.8,base),xytext=(.9,base),arrowprops={'arrowstyle':'->','color':'#64748b'})
 ax.add_patch(Rectangle((1,base),width,height,facecolor='#1d4f91',alpha=.9))
 ax.plot([3,3],[base-.1,base+1.0],ls='--',c='#64748b',lw=1)
 ax.text(3,base-.33,'TRT',ha='center',fontsize=11.5)
 ax.text(1,base-.33,'0',ha='center',fontsize=11.5)
 ax.text(5.75,base-.33,'時間',ha='right',fontsize=11.5)
 ax.text(1+width/2,base+height+.1,'照射',ha='center',fontsize=11.5)
 for rad,col in ([(.68,'#fbf2f0'),(.5,'#f3dbd5'),(.34,'#e3b4a8')] if long else [(.31,'#f3dbd5')]):
  ax.add_patch(Circle((7.65,base+.55),rad,facecolor=col))
 ax.add_patch(Circle((7.65,base+.55),.23,facecolor='#a34b40'))
 ax.text(7.65,base-.43,'周囲へ熱が広がる' if long else '標的に熱が集中',ha='center',fontsize=11.5)
ax.text(.1,.05,'青：照射パルス　　赤茶：標的と周囲の熱',fontsize=11.5)
save(fig,'light-basics_熱緩和_時間軸')
