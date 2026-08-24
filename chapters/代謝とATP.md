---
id: atp
title: 代謝とATP
kind: basic
status: approved
published: 2026-08-24
updated: 2026-08-24
history:
  - {date: 2026-08-24, note: 初公開}
---

> 転写も翻訳も、折りたたみも輸送も、細胞の仕事はすべて ATP を使います（→ [[organelles]]）。**では、ATP はどこから来るのか。**

## この章の一言

> **ATP は、異化から生じるエネルギーの通貨です。**栄養素や、体に蓄えた glycogen・中性脂肪を壊すとエネルギーが出ますが、それはそのまま仕事に使われるわけではありません。いったん ATP に移され、細胞はその ATP を分解してエネルギーを受け取り、組み立て・輸送・収縮にあてます。
>
> **そして ATP は貯まりません。**使えば ADP に戻り、また作り直される。**同じ分子が、1日のうちに何度も作られては使われています。**だいじなのは、ある瞬間の ATP 量ではなく、**需要に応じて作り続けられること**です。

## 1　代謝とは、壊す側と組み立てる側のネットワーク

代謝（metabolism）とは、物質を**分解し・変換し・合成する**化学反応のネットワーク全体を指します。方向が2つあります。

- **異化（catabolism）** ── 大きな分子を壊して、**中間代謝物と使えるエネルギー**を取り出す
- **同化（anabolism）** ── 材料を組み立てて、大きな分子を作る

**異化が壊す相手は、食べた栄養素とはかぎりません。**体に貯蔵してあるエネルギー——**glycogen（糖の貯蔵形）と中性脂肪（脂質の貯蔵形）**——も、必要になれば同じように分解されます。自分のタンパク質も同じです（→ [[dna-to-protein]]・[[autophagy]]）。

異化と同化は、つながっています。異化で出たアミノ酸・脂肪酸・糖は**中間代謝物のプール**に入り、同化はそこから材料を取ります。

エネルギーのほうは、**ATP がすべて引き受けます。**食べたものや体の貯蔵物を分解して ATP を作り（[[glycolysis]]・[[tca-cycle]]・[[electron-transport]]）、**その ATP が分解されるときに出るエネルギーで、細胞は仕事をします。**

![食事や体の蓄えを分解して中間代謝物へつなぎ、そこから新しい物質を組み立てる流れ。下段はATPとADP＋Piの循環](figures/atp_異化と同化.png)

## 2　エネルギー源は3つあり、入る場所が違う

糖質・脂質・タンパク質は、どれもエネルギー源になります。**最後は acetyl-CoA か TCA回路の中間体に合流しますが、そこへ至る道筋と、入る場所が違います。**

![三大栄養素が別々の入口から一つの合流点へ向かう地図。糖質は単糖になり細胞質の解糖系を通ってpyruvateへ、そこからミトコンドリアでacetyl-CoAになる。脂質は脂肪酸とglycerolに分かれ、脂肪酸はミトコンドリアに入ってから炭素2個ずつacetyl-CoAとして切り出される一方、glycerolだけは解糖系の途中に合流する。タンパク質はアミノ酸になり、アミノ基を外した炭素骨格がpyruvate・acetyl-CoA・TCA回路の中間体という複数の場所から入る。合流したあとは区別されず、TCA回路と電子伝達系を経てATPになる](figures/atp_三大栄養素の合流.png)

| 栄養素 | 分解されて | どこから入るか |
|---|---|---|
| **糖質** | glucose などの単糖 | 細胞質の解糖系を通って **pyruvate** になり、ミトコンドリアで acetyl-CoA へ（→ [[glycolysis]]） |
| **脂質** | 脂肪酸と glycerol | 脂肪酸はミトコンドリアに入ってから、**炭素2個ずつ acetyl-CoA** として切り出される。glycerol だけは解糖系の途中に合流する（→ [[fatty-acid-oxidation]]） |
| **タンパク質** | アミノ酸 | アミノ基を外した**炭素骨格**が、pyruvate・acetyl-CoA・TCA回路の中間体という**複数の場所**から入る（→ [[tca-cycle]]） |

## 3　ATP は貯金ではない ―― 在庫は少なく、流れは多い

**ATP は、分解されるときにエネルギーを放します。**ATP が **ADP と無機リン酸（Pi）** に分かれるとき、そこでエネルギーが出て、細胞はそれを使って仕事をします。残った ADP は、異化から得たエネルギーで再び ATP に戻されます。**この往復が絶えず繰り返されています。**

ATP を使う仕事は、大きく3つです。

- **同化** ── アミノ酸・脂質・糖といった材料を、タンパク質・膜・glycogen・核酸へ組み立てる
- **膜輸送** ── 濃度勾配に逆らって物質を運ぶ（Na⁺/K⁺ポンプなど）
- **運動** ── 筋収縮、細胞内の輸送、繊毛の運動

**ATPは貯めておく物質ではありません。** 体内にあるATPは常時わずか数十グラムの桁ですが、1日に作られて使われる総量は体重に相当する桁になるとされます。したがって重要なのは、ある瞬間のATP量ではなく、**需要に応じてATPを作り続けられること**です。

**貯蓄は glycogen と中性脂肪が担い、ATP はその場の受け渡しだけを担当します。** 蓄えから随時ATPを作り、作った分をすぐ使う。だから在庫は少ないのに、流れる量は桁違いに多くなります。

## 4　ATP不足は、AMPの上昇として増幅される

**ATP・ADP・AMP は、同じ分子です。違うのは、付いているリン酸の数だけ**——ATP が **3個**、ADP が **2個**、AMP が **1個**です。

細胞にある **adenylate kinase** は、**ADP 2個のあいだでリン酸を1個やりとりさせます。**渡された側は3個になって ATP に、渡した側は1個になって AMP になります。反応が速いので、次の式は常にほぼ平衡に保たれています。

> **2 ADP ⇄ ATP ＋ AMP**
> リン酸の数：2 ＋ 2 ＝ 3 ＋ 1

**リン酸が付け替わるだけなので、3つを合わせた総量は変わりません。動くのは内訳だけ**です。

ここで効いてくるのが、**もともとの量の差**です。平常時の比は、おおよそ **ATP : ADP : AMP ＝ 100 : 10 : 1**。**AMP だけ桁違いに少ない。**

だから内訳が動いたとき、**それぞれにとっての「増え方」がまるで違います。**ATP を1割ぶん使ったときの計算がこれです。

| | 平常時 | ATP を1割使ったあと | 変化 |
|---|---|---|---|
| **ATP** | 100 | 91.9 | **8% 減っただけ** |
| **ADP** | 10 | 16.3 | 1.6倍 |
| **AMP** | 1 | 2.9 | **約3倍** |
| 合計 | 111 | 111 | **変わらない** |

**ATP の側では誤差にしか見えない変化が、AMP の側では3倍になって現れます。**もとの量が少ないほど、同じだけ増えても倍率が大きくなるからです。**エネルギー不足を測る目盛りとしては、ATP より AMP のほうがずっと感度が高い**ということです。

**AMP の上昇は、エネルギー不足の合図です。** それを感知するのが **AMPK（AMP-activated protein kinase）** です。 異化（ATPを作る側）を促し、同化（ATPを使う側）を抑える——**代謝の向きを切り替える kinase** です（→ [[ampk-mtor]]）。

<figure class="book-figure"><div style="overflow-x:auto"><svg viewBox="0 0 760 754" style="display:block;width:100%;max-width:100%;height:auto;background:#fff" role="img" aria-label="ATP・ADP・AMPの違いは付いているリン酸の数。adenylate kinase はADP2個のあいだでリン酸を1個だけ移し、受け取った側をATP、渡した側をAMPにする。ATP対ADP対AMPを100対10対1とし、ATPを10消費してadenylate kinaseの平衡（K＝1）まで戻すと、ATP91.9・ADP16.3・AMP2.9になる。合計111は変わらない。平常時を100とするとATP92・ADP163・AMP287で、ATPが8%減るだけでAMPは約2.9倍になる。この増幅がエネルギー不足の合図としてAMPKに感知される"><defs><marker id="mk1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 1 L9 5 L0 9 z" fill="#B04A33"/></marker></defs><rect x="3" y="3" width="754" height="748" rx="12" fill="#FFFFFF" stroke="#9FB0C8" stroke-width="1.8"/><g font-family="system-ui,-apple-system,sans-serif"><rect x="14" y="14" width="732" height="132" rx="8" fill="#F6F8FC"/><text x="30" y="42" font-size="15" font-weight="700" fill="#2B4C7E">① 違いは、付いているリン酸の数だけ</text><rect x="36" y="72" width="108" height="50" rx="9" fill="#FFFFFF" stroke="#B9C4D6" stroke-width="1.3"/><text x="36" y="64" font-size="15" font-weight="700" fill="#2B4C7E">AMP</text><rect x="44" y="81" width="66" height="32" rx="7" fill="#EDF1F8" stroke="#93A1B8" stroke-width="1.2"/><text x="77.0" y="102" font-size="12" text-anchor="middle" fill="#3B4A63">アデノシン</text><line x1="110" y1="97" x2="114" y2="97" stroke="#93A1B8" stroke-width="1.5"/><circle cx="125" cy="97" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="125" y="101.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><text x="36" y="140" font-size="13" fill="#5A6782">リン酸 1個</text><rect x="286" y="72" width="138" height="50" rx="9" fill="#FFFFFF" stroke="#B9C4D6" stroke-width="1.3"/><text x="286" y="64" font-size="15" font-weight="700" fill="#2B4C7E">ADP</text><rect x="294" y="81" width="66" height="32" rx="7" fill="#EDF1F8" stroke="#93A1B8" stroke-width="1.2"/><text x="327.0" y="102" font-size="12" text-anchor="middle" fill="#3B4A63">アデノシン</text><line x1="360" y1="97" x2="364" y2="97" stroke="#93A1B8" stroke-width="1.5"/><circle cx="375" cy="97" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="375" y="101.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><line x1="389" y1="97" x2="393" y2="97" stroke="#93A1B8" stroke-width="1.5"/><circle cx="404" cy="97" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="404" y="101.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><text x="286" y="140" font-size="13" fill="#5A6782">リン酸 2個</text><rect x="546" y="72" width="166" height="50" rx="9" fill="#FFFFFF" stroke="#B9C4D6" stroke-width="1.3"/><text x="546" y="64" font-size="15" font-weight="700" fill="#2B4C7E">ATP</text><rect x="554" y="81" width="66" height="32" rx="7" fill="#EDF1F8" stroke="#93A1B8" stroke-width="1.2"/><text x="587.0" y="102" font-size="12" text-anchor="middle" fill="#3B4A63">アデノシン</text><line x1="620" y1="97" x2="624" y2="97" stroke="#93A1B8" stroke-width="1.5"/><circle cx="635" cy="97" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="635" y="101.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><line x1="649" y1="97" x2="653" y2="97" stroke="#93A1B8" stroke-width="1.5"/><circle cx="664" cy="97" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="664" y="101.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><line x1="678" y1="97" x2="682" y2="97" stroke="#93A1B8" stroke-width="1.5"/><circle cx="693" cy="97" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="693" y="101.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><text x="546" y="140" font-size="13" fill="#5A6782">リン酸 3個</text><rect x="14" y="158" width="732" height="186" rx="8" fill="#FFFFFF" stroke="#E4E9F2" stroke-width="1"/><text x="30" y="186" font-size="15" font-weight="700" fill="#2B4C7E">② adenylate kinase が、ADP 2個を ATP と AMP に変える</text><rect x="30" y="216" width="138" height="50" rx="9" fill="#FFFFFF" stroke="#B9C4D6" stroke-width="1.3"/><text x="30" y="208" font-size="15" font-weight="700" fill="#2B4C7E">ADP</text><rect x="38" y="225" width="66" height="32" rx="7" fill="#EDF1F8" stroke="#93A1B8" stroke-width="1.2"/><text x="71.0" y="246" font-size="12" text-anchor="middle" fill="#3B4A63">アデノシン</text><line x1="104" y1="241" x2="108" y2="241" stroke="#93A1B8" stroke-width="1.5"/><circle cx="119" cy="241" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="119" y="245.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><line x1="133" y1="241" x2="137" y2="241" stroke="#93A1B8" stroke-width="1.5"/><circle cx="148" cy="241" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="148" y="245.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><text x="177" y="248" font-size="18" fill="#5A6782">＋</text><rect x="197" y="216" width="138" height="50" rx="9" fill="#FFFFFF" stroke="#B9C4D6" stroke-width="1.3"/><text x="197" y="208" font-size="15" font-weight="700" fill="#2B4C7E">ADP</text><rect x="205" y="225" width="66" height="32" rx="7" fill="#EDF1F8" stroke="#93A1B8" stroke-width="1.2"/><text x="238.0" y="246" font-size="12" text-anchor="middle" fill="#3B4A63">アデノシン</text><line x1="271" y1="241" x2="275" y2="241" stroke="#93A1B8" stroke-width="1.5"/><circle cx="286" cy="241" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="286" y="245.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><line x1="300" y1="241" x2="304" y2="241" stroke="#93A1B8" stroke-width="1.5"/><circle cx="315" cy="241" r="11.5" fill="#E2725B" stroke="#B04A33" stroke-width="1.3"/><text x="315" y="245.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><text x="364" y="250" font-size="24" text-anchor="middle" fill="#2B4C7E">⇄</text><rect x="394" y="216" width="166" height="50" rx="9" fill="#FFFFFF" stroke="#B9C4D6" stroke-width="1.3"/><text x="394" y="208" font-size="15" font-weight="700" fill="#2B4C7E">ATP</text><rect x="402" y="225" width="66" height="32" rx="7" fill="#EDF1F8" stroke="#93A1B8" stroke-width="1.2"/><text x="435.0" y="246" font-size="12" text-anchor="middle" fill="#3B4A63">アデノシン</text><line x1="468" y1="241" x2="472" y2="241" stroke="#93A1B8" stroke-width="1.5"/><circle cx="483" cy="241" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="483" y="245.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><line x1="497" y1="241" x2="501" y2="241" stroke="#93A1B8" stroke-width="1.5"/><circle cx="512" cy="241" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="512" y="245.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><line x1="526" y1="241" x2="530" y2="241" stroke="#93A1B8" stroke-width="1.5"/><circle cx="541" cy="241" r="11.5" fill="#E2725B" stroke="#B04A33" stroke-width="1.3"/><text x="541" y="245.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><text x="570" y="248" font-size="18" fill="#5A6782">＋</text><rect x="590" y="216" width="108" height="50" rx="9" fill="#FFFFFF" stroke="#B9C4D6" stroke-width="1.3"/><text x="590" y="208" font-size="15" font-weight="700" fill="#2B4C7E">AMP</text><rect x="598" y="225" width="66" height="32" rx="7" fill="#EDF1F8" stroke="#93A1B8" stroke-width="1.2"/><text x="631.0" y="246" font-size="12" text-anchor="middle" fill="#3B4A63">アデノシン</text><line x1="664" y1="241" x2="668" y2="241" stroke="#93A1B8" stroke-width="1.5"/><circle cx="679" cy="241" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="679" y="245.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><path d="M315 274 C 360 314 500 314 537 278" fill="none" stroke="#B04A33" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#mk1)"/><text x="426" y="332" font-size="12.5" text-anchor="middle" fill="#B04A33">この1個が移る</text><rect x="14" y="356" width="732" height="292" rx="8" fill="#F6F8FC"/><text x="30" y="384" font-size="15" font-weight="700" fill="#2B4C7E">③ 総量は変わらない。それでも AMP だけが数倍になる</text>

<rect x="28" y="396" width="344" height="236" rx="8" fill="#FFFFFF" stroke="#E4E9F2" stroke-width="1"/>
<text x="46" y="420" font-size="13" font-weight="700" fill="#5A6782">実際の量（同じ目盛り）</text>
<line x1="44" y1="578" x2="356" y2="578" stroke="#B9C4D6" stroke-width="1.4"/>
<rect x="56" y="448" width="30" height="130" fill="#86B39A" stroke="#4F8468" stroke-width="1.2"/>
<rect x="96" y="565" width="30" height="13" fill="#7FA7CE" stroke="#3F6F9F" stroke-width="1.2"/>
<rect x="136" y="576" width="30" height="2" fill="#E2725B" stroke="#B04A33" stroke-width="1.2"/>
<rect x="216" y="459" width="30" height="119" fill="#86B39A" stroke="#4F8468" stroke-width="1.2"/>
<rect x="256" y="557" width="30" height="21" fill="#7FA7CE" stroke="#3F6F9F" stroke-width="1.2"/>
<rect x="296" y="574" width="30" height="4" fill="#E2725B" stroke="#B04A33" stroke-width="1.2"/>
<text x="71" y="592" font-size="10.5" text-anchor="middle" fill="#3B4A63">ATP</text><text x="111" y="592" font-size="10.5" text-anchor="middle" fill="#3B4A63">ADP</text><text x="151" y="592" font-size="10.5" text-anchor="middle" fill="#3B4A63">AMP</text>
<text x="231" y="592" font-size="10.5" text-anchor="middle" fill="#3B4A63">ATP</text><text x="271" y="592" font-size="10.5" text-anchor="middle" fill="#3B4A63">ADP</text><text x="311" y="592" font-size="10.5" text-anchor="middle" fill="#3B4A63">AMP</text>
<text x="111" y="612" font-size="12" font-weight="700" text-anchor="middle" fill="#5A6782">平常時</text>
<text x="271" y="612" font-size="12" font-weight="700" text-anchor="middle" fill="#5A6782">ATP を1割使ったあと</text>
<text x="200" y="440" font-size="11" text-anchor="middle" fill="#8A93A6">この目盛りでは、AMP はどちらも棒が見えない</text>

<rect x="388" y="396" width="344" height="236" rx="8" fill="#FFFFFF" stroke="#E4E9F2" stroke-width="1"/>
<text x="406" y="420" font-size="13" font-weight="700" fill="#5A6782">平常時を 100 としたときの変化</text>
<line x1="404" y1="578" x2="716" y2="578" stroke="#B9C4D6" stroke-width="1.4"/>
<line x1="404" y1="528" x2="716" y2="528" stroke="#E4E9F2" stroke-width="1.2" stroke-dasharray="4 4"/>
<rect x="440" y="532" width="56" height="46" fill="#86B39A" stroke="#4F8468" stroke-width="1.2"/>
<rect x="540" y="496" width="56" height="82" fill="#7FA7CE" stroke="#3F6F9F" stroke-width="1.2"/>
<rect x="640" y="434" width="56" height="144" fill="#E2725B" stroke="#B04A33" stroke-width="1.2"/>
<text x="468" y="524" font-size="13" font-weight="700" text-anchor="middle" fill="#4F8468">92</text>
<text x="568" y="488" font-size="13" font-weight="700" text-anchor="middle" fill="#3F6F9F">163</text>
<text x="668" y="426" font-size="13" font-weight="700" text-anchor="middle" fill="#B04A33">287</text>
<text x="468" y="592" font-size="11" text-anchor="middle" fill="#3B4A63">ATP</text><text x="568" y="592" font-size="11" text-anchor="middle" fill="#3B4A63">ADP</text><text x="668" y="592" font-size="11" text-anchor="middle" fill="#3B4A63">AMP</text>
<text x="406" y="546" font-size="10" fill="#C6CFDD">100</text>
<text x="560" y="612" font-size="12" font-weight="700" text-anchor="middle" fill="#B04A33">ATP は 8% 減っただけ。AMP は約2.9倍</text>

<rect x="14" y="660" width="732" height="78" rx="8" fill="#FFFFFF" stroke="#E4E9F2" stroke-width="1"/><text x="30" y="683" font-size="12.5" fill="#3B4A63">ATP : ADP : AMP ＝ 100 : 10 : 1 から ATP を1割消費し、adenylate kinase の平衡まで戻したとき——</text><text x="30" y="705" font-size="12.5" fill="#3B4A63"><tspan font-weight="700">ATP 91.9 ／ ADP 16.3 ／ AMP 2.9。合計は 111 のまま変わらない。</tspan></text><text x="30" y="727" font-size="12.5" fill="#3B4A63">リン酸が移るだけで分子の数は増減しない。この増幅を <tspan font-weight="700" fill="#6B4CA3">AMPK</tspan> が感知する。</text></g></svg></div><figcaption>ATP・ADP・AMPの違いは、付いているリン酸の数（3個・2個・1個）だけ。adenylate kinase は ADP 2個のあいだでリン酸を1個だけ移し、受け取った側を ATP、渡した側を AMP にする。ATP:ADP:AMP＝100:10:1 から ATP を1割使い、adenylate kinase の平衡まで戻すと ATP 91.9／ADP 16.3／AMP 2.9——合計は 111 のまま変わらない。同じ目盛りでは AMP の棒は見えないが、平常時を100として比べると、ATP が8%減っただけで AMP は約2.9倍になる。この増幅された合図を AMPK が感知する</figcaption></figure>

> **発展：細胞外へ出たATP。** 組織の傷害などで局所的に細胞外へ放出されたATPは、エネルギー源としてではなく、**P2受容体を介した危険信号**として働きます。この役割は DAMPs を扱う[[wound-healing]]で説明します。

## この章の到達点

1. **代謝は、壊す側（異化）と組み立てる側（同化）を含む反応のネットワーク。** エネルギーの受け渡しは ATP がすべて引き受ける——**分解して ATP を作り、その ATP を分解して仕事をする。**
2. **エネルギー源は糖質・脂質・タンパク質の3つ。**最後は acetyl-CoA か TCA回路の中間体に合流するが、**そこへ入る場所が違う**。
3. **ATP は貯める分子ではない。**在庫は数十グラムの桁でも、1日に作られて使われる総量は体重に相当する桁になる。貯蔵は glycogen と中性脂肪が担う。
4. **ATP が減ると AMP が大きく増え、AMPK がそれを感知する。**

> [[glycolysis]]では、電子を抜き取る最初の工程 **解糖系（glycolysis）** を見ます。glucose 1分子から得られる ATP は正味2個——この数字が、細胞の代謝の見方を決めます。
