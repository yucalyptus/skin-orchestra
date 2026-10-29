"""Rebuild spectral figures from saved OMLC tables; run from repository root."""
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/skin-orchestra-mpl')
from pathlib import Path
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[2]
font=Path('/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc')
if font.exists():
 fm.fontManager.addfont(str(font)); plt.rcParams['font.family']=fm.FontProperties(fname=font).get_name()
plt.rcParams.update({'font.size':14,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'path','axes.labelcolor':'#1c1d23','text.color':'#1c1d23'})
hb=np.array([[float(x) for x in m] for m in re.findall(r'^\s*(\d+)\s+(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)\s*$',(BASE/'hemoglobin.html').read_text(),re.M)])
w=np.array([[float(x) for x in line.split()] for line in (BASE/'hale73.txt').read_text().splitlines() if re.match(r'^\s*\d+(?:\.\d+)?\s+[0-9.eE+\-]+\s*$',line)])
assert hb.shape[0]>300 and w.shape[0]>200
np.savetxt(BASE/'hemoglobin.csv',hb,delimiter=',',header='wavelength_nm,oxyHb_molar_extinction,deoxyHb_molar_extinction')
def finish(fig,name):
 fig.savefig(ROOT/'figures'/f'{name}.svg',bbox_inches='tight',facecolor='white')
 fig.savefig('/tmp/'+name+'.png',dpi=140,bbox_inches='tight',facecolor='white')
 plt.close(fig)
fig,ax=plt.subplots(figsize=(11,6.4));fig.subplots_adjust(bottom=.26,top=.8,left=.12,right=.96)
x=np.linspace(400,1000,601)
ax.semilogy(x,1.7e12*x**-3.48,color='#1c1d23',lw=2.8,label='メラニン（メラノソーム内・近似）')
mask=(hb[:,0]>=400)&(hb[:,0]<=1000)
ax.semilogy(hb[mask,0],hb[mask,1]*2.303*150/64500,color='#a34b40',lw=2.5,label='酸素化ヘモグロビン')
ax.semilogy(hb[mask,0],hb[mask,2]*2.303*150/64500,color='#a34b40',lw=2.5,ls='--',label='脱酸素化ヘモグロビン')
mask=(w[:,0]>=400)&(w[:,0]<=1000)
ax.semilogy(w[mask,0],w[mask,1],color='#1d4f91',lw=2.8,label='水')
ax.set(xlim=(400,1000),ylim=(1e-4,1e4),xlabel='波長（nm）',ylabel='吸収係数（1/cm・対数目盛）')
ax.set_yticks([1e-4,1e-2,1,100,10000]);ax.grid(axis='y',alpha=.2)
for v,label in [(532,'532'),(595,'595'),(694,'694'),(755,'755')]:
 ax.axvline(v,color='#64748b',lw=.8,ls=':',zorder=0);ax.text(v,1.35e4,label,ha='center',fontsize=12,color='#64748b',clip_on=False)
fig.suptitle('可視〜近赤外：吸収帯は重なっている',fontsize=21,x=.12,ha='left',y=.98)
fig.legend(*ax.get_legend_handles_labels(),loc='lower left',bbox_to_anchor=(.1,.07),ncol=2,fontsize=12,frameon=False)
fig.text(.12,.025,'Hb：150 g/L換算。水：純水。メラニン：皮膚メラノソーム内の近似値。\n濃度・存在する場所が異なるため、この高さだけで皮膚内の吸収割合は決まりません。',fontsize=11)
finish(fig,'light-basics_吸収曲線_可視近赤外')
fig,ax=plt.subplots(figsize=(11,5.7));fig.subplots_adjust(bottom=.23,top=.79,left=.12,right=.96)
mask=(w[:,0]>=1000)&(w[:,0]<=12000)
ax.loglog(w[mask,0],w[mask,1],color='#1d4f91',lw=2.8)
ax.set(xlim=(1000,12000),ylim=(.05,3e4),xlabel='波長（nm・対数目盛）',ylabel='水の吸収係数（1/cm・対数目盛）')
ax.set_xticks([1000,2000,3000,5000,10000],labels=['1000','2000','3000','5000','10000']);ax.minorticks_off();ax.grid(axis='y',alpha=.2)
for v,y in [(1064,1.8e4),(1450,1.8e4),(1550,4e3),(1940,1.8e4),(2940,1.8e4),(10600,1.8e4)]:
 ax.axvline(v,color='#64748b',lw=.8,ls=':');ax.text(v,y,str(v),ha='center',fontsize=12,bbox={'facecolor':'white','edgecolor':'none','pad':1})
fig.suptitle('赤外域：水への吸収は、波長によって大きく変わる',fontsize=21,x=.12,ha='left',y=.98)
fig.text(.12,.06,'水のみを表示。純水のデータで、縦・横軸とも対数目盛です。\n吸収が強い波長では、光は水を含む組織の浅い範囲で吸収されやすくなります。',fontsize=12)
finish(fig,'light-basics_吸収曲線_水')
# Overview: two linked wavelength ranges, then clinical target rows.
su=np.array([[float(v) for v in line.split()] for line in (BASE/'bloodSuzaki.dat').read_text().splitlines() if re.match(r'^\d+\s+[0-9.eE+\-]+\s+[0-9.eE+\-]+\s*$',line)])
assert su.shape[0]>90
fig=plt.figure(figsize=(14,9))
gs=fig.add_gridspec(2,2,left=.13,right=.97,bottom=.23,top=.76,height_ratios=[3.5,1],width_ratios=[3.4,1],hspace=.25,wspace=.055)
ax=fig.add_subplot(gs[0,0]); ar=fig.add_subplot(gs[0,1],sharey=ax)
bx=fig.add_subplot(gs[1,0],sharex=ax);br=fig.add_subplot(gs[1,1],sharex=ar)
x=np.linspace(400,1100,701)
ax.semilogy(x,1.7e12*x**-3.48,color='#1c1d23',lw=3)
mask=(hb[:,0]>=400)&(hb[:,0]<=1000)
ax.semilogy(hb[mask,0],hb[mask,1]*2.303*150/64500,color='#a34b40',lw=2.6)
ax.semilogy(hb[mask,0],hb[mask,2]*2.303*150/64500,color='#a34b40',lw=2,ls='--')
mask=(su[:,0]>=1000)&(su[:,0]<=1100)
ax.plot(su[mask,0],su[mask,1],color='#a34b40',lw=2.6)
ax.plot(su[mask,0],su[mask,2],color='#a34b40',lw=2,ls='--')
for a in (ax,ar):
 a.plot(w[:,0],w[:,1],color='#1d4f91',lw=3)
 a.set_ylim(1e-4,1e5);a.grid(axis='y',alpha=.15)
ax.set_xlim(400,1100);ax.set_xticks([400,500,600,700,800,900,1000,1100])
ar.set_xscale('log');ar.set_xlim(1100,12000)
ar.set_xticks([2000,5000,10000],labels=['2000','5000','10000']);ar.minorticks_off()
ar.tick_params(axis='y',left=False,labelleft=False);ar.spines['left'].set_visible(False)
ax.set_ylabel('吸収係数（1/cm・対数目盛）',fontsize=13)
ax.text(820,1500,'メラニン',fontsize=17)
ax.text(430,.12,'ヘモグロビン',fontsize=16,color='#a34b40')
ax.annotate('',xy=(570,200),xytext=(520,.6),arrowprops={'arrowstyle':'-','color':'#a34b40'})
ax.text(890,.007,'水',fontsize=17,color='#1d4f91');ar.text(4500,12,'水',fontsize=18,color='#1d4f91')
labels=[(532,'KTP・Nd:YAG\n532',1.30),(595,'色素（ダイ）\n585 / 595',1.08),(694,'ルビー\n694',1.30),(755,'アレキサンドライト\n755',1.08),(810,'ダイオード\n810（例）',1.30),(1064,'Nd:YAG\n1064',1.08)]
for v,label,y in labels:
 ax.axvline(v,color='#84909c',lw=.7,ls=':',zorder=0)
 ax.annotate(label,xy=(v,1),xycoords=('data','axes fraction'),xytext=(v,y),textcoords=('data','axes fraction'),ha='center',va='bottom',fontsize=12,arrowprops={'arrowstyle':'-','color':'#84909c','lw':.7},annotation_clip=False)
for v,label,y in [(2940,'Er:YAG\n2940',1.08),(10600,'CO₂\n10600',1.30)]:
 ar.axvline(v,color='#84909c',lw=.7,ls=':',zorder=0)
 ar.annotate(label,xy=(v,1),xycoords=('data','axes fraction'),xytext=(v,y),textcoords=('data','axes fraction'),ha='center',va='bottom',fontsize=12,arrowprops={'arrowstyle':'-','color':'#84909c','lw':.7},annotation_clip=False)
for a,pos in [(ax,1),(ar,0)]:
 a.plot([pos-.009,pos+.009],[-.018,.018],transform=a.transAxes,color='#555',clip_on=False)
for a in (bx,br):
 a.set_ylim(-.4,2.6);a.spines[['left','bottom']].set_visible(False)
 a.tick_params(axis='both',which='both',bottom=False,labelbottom=False,left=False,labelleft=False)
 for y in (0,1,2):a.axhline(y,color='#d6d9df',lw=.8,zorder=0)
for y,label,color in [(2,'メラニン', '#1c1d23'),(1,'血管', '#a34b40'),(0,'水', '#1d4f91')]:
 bx.text(-.02,y,label,transform=bx.get_yaxis_transform(),ha='right',va='center',fontsize=15,color=color)
for v in [532,694,755,810,1064]:bx.plot(v,2,'o',color='#1c1d23',ms=9)
for v in [532,595,1064]:bx.plot(v,1,'o',color='#a34b40',ms=9)
for v in [2940,10600]:br.plot(v,0,'o',color='#1d4f91',ms=9)
for v in [532,595,694,755,810,1064]:bx.axvline(v,color='#aab2bd',lw=.7,ls=':',zorder=0)
for v in [2940,10600]:br.axvline(v,color='#aab2bd',lw=.7,ls=':',zorder=0)
bx.text(0,1.1,'● 主な治療標的の例（同じ波長で複数を狙える）',transform=bx.transAxes,fontsize=13,ha='left')
fig.suptitle('吸収スペクトルと、各波長で狙う標的',fontsize=23,x=.13,ha='left',y=.98)
fig.text(.13,.175,'1064 nm：色素治療はナノ秒・ピコ秒、血管治療は主にミリ秒のパルスを使います。',fontsize=14)
fig.text(.13,.125,'赤実線：酸素化Hb　赤破線：脱酸素化Hb　横軸：波長（nm）。右側のみ対数目盛で圧縮。',fontsize=12)
fig.text(.13,.075,'Hb：150 g/L換算（1000 nm超はOMLC公開の補正データ）。メラニン：メラノソーム内の近似。水：純水。\n標的の●は代表的な用途で、吸収の強さや治療効果の順位を表しません。',fontsize=11)
finish(fig,'light-basics_クロモフォア吸収スペクトル_標的対応')
