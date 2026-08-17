---
id: atp
title: 代謝とATP
kind: basic
status: draft
---

> 転写も翻訳も、折りたたみも輸送も、細胞の仕事はすべて ATP を使います（→ [[organelles]]）。**では、ATP はどこから来るのか。**

## この章の一言

> 食べたもの、あるいは体に蓄えてあったものを分解すると、**電子**が取り出されます。その電子を **NAD⁺** が受け取って運び、酸素へ渡します。**ATPの大半は、その電子が酸素へ渡るときに、ミトコンドリアの内膜でできます。**
>
> **ATP は、エネルギーの通貨です。** 栄養素や蓄えを分解して得たエネルギーは、そのまま仕事に使われるわけではありません。いったん ATP に移され、細胞はその ATP を分解してエネルギーを受け取り、組み立て・輸送・収縮にあてます。使い終われば ADP に戻り、また作り直されます。

![栄養素から水素＝電子を抜き取り、NAD⁺がNADHとして電子伝達系へ運び、電子が酸素へ渡って水になるときのエネルギーからATPの大半が作られる。NAD⁺とNADHの電子運搬の輪と、ATPとADPのエネルギー運搬の輪は別々で、電子伝達系でのみ噛み合う](figures/atp_電子とATPの流れ.png)

## 1　代謝とは、壊す側と組み立てる側のネットワーク

代謝（metabolism）とは、物質を**分解し・変換し・合成する**化学反応のネットワーク全体を指します。方向が2つあります。

- **異化（catabolism）** ── 大きな分子を壊して、**電子・中間代謝物・使えるエネルギー**を取り出す
- **同化（anabolism）** ── 材料を組み立てて、大きな分子を作る

**異化が壊す相手は、食べた栄養素とはかぎりません。** グリコーゲンも、中性脂肪も、自分のタンパク質も、必要になれば同じように分解されます（→ [[dna-to-protein]]・[[autophagy]]）。壊す相手が何かは、異化かどうかとは別の話です。

壊した先と組み立てる先は、地続きです。異化で出たアミノ酸・脂肪酸・糖は**中間代謝物のプール**に入り、同化はそこから材料を取ります。**壊すことは、捨てることではありません。**

異化と同化をつなぐのが **ATP** です。エネルギーを出す反応と、エネルギーを必要とする反応は、本来つながっていない別の反応です。ATP⇄ADP という共通の輪を挟むことで、初めて連結します。**エネルギーをいったん ATP に移すのは、このためです。**

![異化の対象は食事由来の糖・脂質・タンパク質だけでなく、glycogen・中性脂肪・自分のタンパク質も含む。分解された材料は中間代謝物のプールに入り、同化がそこから取る。異化から得たエネルギーで ADP を ATP に作り直し、ATP は同化・膜輸送・運動へエネルギーを渡して ADP に戻る。ATPは体の材料ではなく、材料を組み立て、運び、動かす側](figures/atp_異化と同化とATPの輪.png)

## 2　ATPは使い切る燃料ではなく、回っている

ATP が仕事にエネルギーを渡すと **ADP** になります。その ADP は、異化から得たエネルギーで再び ATP に戻されます。**ATPとADPは、この往復を絶えず繰り返しています。**

ATP が渡す先は、大きく3つです。

- **同化** ── アミノ酸・脂質・糖といった材料を、タンパク質・膜・グリコーゲン・核酸へ組み立てる
- **膜輸送** ── 濃度勾配に逆らって物質を運ぶ（Na⁺/K⁺ポンプなど）
- **運動** ── 筋収縮、細胞内の輸送、繊毛の運動

**ATPは貯めておく物質ではありません。** 体内にあるATPは常時わずか数十グラムの桁ですが、1日に作られて使われる総量は体重に相当する桁になるとされます。したがって重要なのは、ある瞬間のATP量ではなく、**需要に応じてATPを作り続けられること**です。

**貯蓄はグリコーゲンと脂肪が担い、ATP はその場の受け渡しだけを担当します。** 蓄えから随時ATPを作り、作った分をすぐ使う。だから在庫は少ないのに、流れる量は桁違いに多くなります。

ATPがADPに変わる反応は、材料の合成・膜輸送・運動などと組み合わされ、これらの仕事を進めます。このように、**ATPを使う反応と細胞の仕事を結びつけることをカップリング**といいます。ATP が異化と同化をつなぐというのは、この意味です。

## 3　電子の運び手 ―― NAD⁺／NADH

異化が栄養素から取り出すのは、**電子**です。その電子が酸素へ渡るときに、ATPの大半ができます。

栄養素を分解するというのは、突き詰めれば**そこから水素を抜き取ること**です。水素原子は陽子1個と電子1個でできているので、**水素を抜くことは、電子を抜くこと**でもあります。この教材で「電子を渡す」と書くとき、実体はたいていこの水素の受け渡しです。

> 電子を抜かれた側を**酸化された**、受け取った側を**還元された**といいます。のちに出る「還元当量」「還元力」「酸化ストレス」（→ [[oxidative-stress]]）も、指しているのはこの電子のやりとりです。

電子を抜き取るのは **解糖系（[[glycolysis]]）と TCA回路（[[tca-cycle]]）** です。抜き取られた電子は、最終的に **電子伝達系（[[electron-transport]]）** で酸素へ渡され、水になります。**ATPの大半は、この電子の流れから作られます。**

問題は、**電子を抜き取る場所と、酸素へ渡す場所が離れている**ことです。解糖系は細胞質、電子伝達系はミトコンドリアの内膜。だから**運び手**が要ります。それが **NAD⁺** です。

NAD⁺ は niacin（ビタミンB3）から作られる補酵素です。要点は一つだけです。

> **NAD⁺ と NADH は、別の分子ではありません。同じ分子の、荷を積む前と積んだ後です。**
>
> - **NAD⁺** ＝ 空の荷台。これから電子を受け取る形
> - **NADH** ＝ 電子を積んだ形

流れにすると、こうなります。

1. 解糖系・TCA回路で、栄養素から**電子**が抜き取られる
2. **NAD⁺** がそれを受け取って **NADH** になる（荷を積む）
3. **NADH** が電子伝達系まで運び、そこで電子を降ろす
4. 降ろした NADH は **NAD⁺** に戻り、また次の電子を積む
5. 降ろされた電子は最後に **O₂** へ渡り、**H₂O** になる
6. この電子の流れから、**ATPの大半が作られる**

電子が流れると、ミトコンドリア内膜の外へ **H⁺** が汲み出されます。その H⁺ が戻ってくる流れで **ATP合成酵素**が回り、ATP ができます。仕組みの中身は[[electron-transport]]で扱います。

> NAD⁺ にはもう一つ、往復しない使われ方があります。**酵素に分子ごと切られて消費される**役割で、そちらは実際に減るので作り直しが要ります。「NAD⁺が減る」「NAD⁺を補う」という話は、すべてそちらを指しています（→ [[nad]]）。

![NAD⁺（空の荷台）が解糖系・TCA回路で電子を受け取って NADH（電子を積んだ荷台）になり、電子伝達系で電子を降ろして NAD⁺ に戻る。降ろされた電子は O₂ へ渡って H₂O になり、その流れで得たエネルギーが ATP⇄ADP の輪へ入る。電子を運ぶ輪とエネルギーを渡す輪は別で、ATPは電子を運ばない](figures/atp_NADの二状態.png)

## 4　ATP不足は、AMPの上昇として増幅される

ATP がエネルギーを渡すと ADP になります。ATP・ADP・AMP の違いは、**付いているリン酸の数**だけです（3個・2個・1個）。細胞にある **adenylate kinase** は、**ADP 2個のあいだでリン酸を1個やりとりさせます。** 片方は3個になって ATP、もう片方は1個になって AMP。反応が速いので、次の式は常にほぼ平衡に保たれています。

> 2 ADP（2） ⇄ ATP（3）＋ AMP（1）

この平衡のおかげで、**ATPが少し減って ADP が増えると、AMP はより大きく増えます**。**もともと AMP はごく少量しかありません**から、少し作られるだけで比率が大きく動きます。小さな不足が、大きな変化として表れるわけです。

**その AMP の上昇を読み取るのが AMPK（AMP-activated protein kinase）です。** 異化（ATPを作る側）を促し、同化（ATPを使う側）を抑える——**代謝の向きを切り替える kinase** です（→ [[ampk-mtor]]）。

<div style="margin:22px 0"><svg viewBox="0 0 760 400" width="100%" role="img" aria-label="ATP・ADP・AMPの違いはリン酸の数。adenylate kinaseはADP2個の間でリン酸1個を移し、ATPとAMPにする。ATPがわずかに減るとAMPは何倍にも増え、AMPKがそれを読む"><defs><marker id="a1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#2B4C7E"/></marker></defs><g font-family="system-ui,sans-serif"><text x="16" y="22" font-size="14" font-weight="700" fill="#2B4C7E">① 違いはリン酸の数だけ</text><rect x="30" y="48" width="52" height="30" rx="6" fill="#E8EDF5" stroke="#8894A8" stroke-width="1.2"/><text x="56" y="68" font-size="11.5" text-anchor="middle" fill="#33415C">アデノシン</text><line x1="83" y1="63" x2="87" y2="63" stroke="#8894A8" stroke-width="1.5"/><circle cx="98" cy="63" r="11" fill="#F0A94B" stroke="#C77A2A" stroke-width="1.2"/><text x="98" y="67.5" font-size="11" font-weight="700" text-anchor="middle" fill="#6B4A12">P</text><text x="30" y="40" font-size="13.5" font-weight="700" fill="#33415C">AMP</text><text x="180" y="68" font-size="12" fill="#5A6782">リン酸 1個</text><rect x="30" y="104" width="52" height="30" rx="6" fill="#E8EDF5" stroke="#8894A8" stroke-width="1.2"/><text x="56" y="124" font-size="11.5" text-anchor="middle" fill="#33415C">アデノシン</text><line x1="83" y1="119" x2="87" y2="119" stroke="#8894A8" stroke-width="1.5"/><circle cx="98" cy="119" r="11" fill="#F0A94B" stroke="#C77A2A" stroke-width="1.2"/><text x="98" y="123.5" font-size="11" font-weight="700" text-anchor="middle" fill="#6B4A12">P</text><line x1="113" y1="119" x2="117" y2="119" stroke="#8894A8" stroke-width="1.5"/><circle cx="128" cy="119" r="11" fill="#F0A94B" stroke="#C77A2A" stroke-width="1.2"/><text x="128" y="123.5" font-size="11" font-weight="700" text-anchor="middle" fill="#6B4A12">P</text><text x="30" y="96" font-size="13.5" font-weight="700" fill="#33415C">ADP</text><text x="180" y="124" font-size="12" fill="#5A6782">リン酸 2個</text><rect x="30" y="160" width="52" height="30" rx="6" fill="#E8EDF5" stroke="#8894A8" stroke-width="1.2"/><text x="56" y="180" font-size="11.5" text-anchor="middle" fill="#33415C">アデノシン</text><line x1="83" y1="175" x2="87" y2="175" stroke="#8894A8" stroke-width="1.5"/><circle cx="98" cy="175" r="11" fill="#F0A94B" stroke="#C77A2A" stroke-width="1.2"/><text x="98" y="179.5" font-size="11" font-weight="700" text-anchor="middle" fill="#6B4A12">P</text><line x1="113" y1="175" x2="117" y2="175" stroke="#8894A8" stroke-width="1.5"/><circle cx="128" cy="175" r="11" fill="#F0A94B" stroke="#C77A2A" stroke-width="1.2"/><text x="128" y="179.5" font-size="11" font-weight="700" text-anchor="middle" fill="#6B4A12">P</text><line x1="143" y1="175" x2="147" y2="175" stroke="#8894A8" stroke-width="1.5"/><circle cx="158" cy="175" r="11" fill="#F0A94B" stroke="#C77A2A" stroke-width="1.2"/><text x="158" y="179.5" font-size="11" font-weight="700" text-anchor="middle" fill="#6B4A12">P</text><text x="30" y="152" font-size="13.5" font-weight="700" fill="#33415C">ATP</text><text x="180" y="180" font-size="12" fill="#5A6782">リン酸 3個</text><line x1="16" y1="206" x2="744" y2="206" stroke="#DCE3ED" stroke-width="1"/><text x="16" y="230" font-size="14" font-weight="700" fill="#2B4C7E">② adenylate kinase はリン酸を1個だけ移す</text><rect x="30" y="252" width="52" height="30" rx="6" fill="#E8EDF5" stroke="#8894A8" stroke-width="1.2"/><text x="56" y="272" font-size="11.5" text-anchor="middle" fill="#33415C">アデノシン</text><line x1="83" y1="267" x2="87" y2="267" stroke="#8894A8" stroke-width="1.5"/><circle cx="98" cy="267" r="11" fill="#F0A94B" stroke="#C77A2A" stroke-width="1.2"/><text x="98" y="271.5" font-size="11" font-weight="700" text-anchor="middle" fill="#6B4A12">P</text><line x1="113" y1="267" x2="117" y2="267" stroke="#8894A8" stroke-width="1.5"/><circle cx="128" cy="267" r="11" fill="#F0A94B" stroke="#C77A2A" stroke-width="1.2"/><text x="128" y="271.5" font-size="11" font-weight="700" text-anchor="middle" fill="#6B4A12">P</text><text x="30" y="244" font-size="13.5" font-weight="700" fill="#33415C">ADP</text><text x="180" y="272" font-size="12" fill="#5A6782"></text><rect x="30" y="300" width="52" height="30" rx="6" fill="#E8EDF5" stroke="#8894A8" stroke-width="1.2"/><text x="56" y="320" font-size="11.5" text-anchor="middle" fill="#33415C">アデノシン</text><line x1="83" y1="315" x2="87" y2="315" stroke="#8894A8" stroke-width="1.5"/><circle cx="98" cy="315" r="11" fill="#F0A94B" stroke="#C77A2A" stroke-width="1.2"/><text x="98" y="319.5" font-size="11" font-weight="700" text-anchor="middle" fill="#6B4A12">P</text><line x1="113" y1="315" x2="117" y2="315" stroke="#8894A8" stroke-width="1.5"/><circle cx="128" cy="315" r="11" fill="#F0A94B" stroke="#C77A2A" stroke-width="1.2"/><text x="128" y="319.5" font-size="11" font-weight="700" text-anchor="middle" fill="#6B4A12">P</text><text x="30" y="292" font-size="13.5" font-weight="700" fill="#33415C">ADP</text><text x="180" y="320" font-size="12" fill="#5A6782"></text><path d="M118 268 q34 32 0 62" fill="none" stroke="#C77A2A" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#a1)"/><text x="176" y="302" font-size="11.5" fill="#C77A2A">1個移す</text><text x="272" y="292" font-size="20" fill="#2B4C7E">⇄</text><rect x="320" y="252" width="52" height="30" rx="6" fill="#E8EDF5" stroke="#8894A8" stroke-width="1.2"/><text x="346" y="272" font-size="11.5" text-anchor="middle" fill="#33415C">アデノシン</text><line x1="373" y1="267" x2="377" y2="267" stroke="#8894A8" stroke-width="1.5"/><circle cx="388" cy="267" r="11" fill="#F0A94B" stroke="#C77A2A" stroke-width="1.2"/><text x="388" y="271.5" font-size="11" font-weight="700" text-anchor="middle" fill="#6B4A12">P</text><line x1="403" y1="267" x2="407" y2="267" stroke="#8894A8" stroke-width="1.5"/><circle cx="418" cy="267" r="11" fill="#F0A94B" stroke="#C77A2A" stroke-width="1.2"/><text x="418" y="271.5" font-size="11" font-weight="700" text-anchor="middle" fill="#6B4A12">P</text><line x1="433" y1="267" x2="437" y2="267" stroke="#8894A8" stroke-width="1.5"/><circle cx="448" cy="267" r="11" fill="#F0A94B" stroke="#C77A2A" stroke-width="1.2"/><text x="448" y="271.5" font-size="11" font-weight="700" text-anchor="middle" fill="#6B4A12">P</text><text x="320" y="244" font-size="13.5" font-weight="700" fill="#33415C">ATP</text><text x="470" y="272" font-size="12" fill="#5A6782"></text><rect x="320" y="300" width="52" height="30" rx="6" fill="#E8EDF5" stroke="#8894A8" stroke-width="1.2"/><text x="346" y="320" font-size="11.5" text-anchor="middle" fill="#33415C">アデノシン</text><line x1="373" y1="315" x2="377" y2="315" stroke="#8894A8" stroke-width="1.5"/><circle cx="388" cy="315" r="11" fill="#F0A94B" stroke="#C77A2A" stroke-width="1.2"/><text x="388" y="319.5" font-size="11" font-weight="700" text-anchor="middle" fill="#6B4A12">P</text><text x="320" y="292" font-size="13.5" font-weight="700" fill="#33415C">AMP</text><text x="470" y="320" font-size="12" fill="#5A6782"></text><text x="30" y="352" font-size="12.5" fill="#33415C">左右でリン酸の合計は 4 個。数は変わらず、配り方が変わるだけです。</text><line x1="16" y1="368" x2="744" y2="368" stroke="#DCE3ED" stroke-width="1"/><text x="16" y="390" font-size="13.5" fill="#33415C"><tspan font-weight="700" fill="#2B4C7E">③ </tspan>もともと AMP はごく少量なので、<tspan font-weight="700" fill="#6B4CA3">ATPがわずかに減るだけで AMP は何倍にも増えます</tspan>。その上昇を <tspan font-weight="700">AMPK</tspan> が読みます。</text></g></svg></div>

> **発展：細胞外へ出たATP。** 組織の傷害などで局所的に細胞外へ放出されたATPは、エネルギー源としてではなく、**P2受容体を介した危険信号**として働きます。この役割は DAMPs を扱う[[wound-healing]]で説明します。

## この章の到達点

1. **代謝は、壊す側（異化）と組み立てる側（同化）を含む反応のネットワーク。** ATPはその両者をつなぐエネルギーの通貨で、**常に作られ、常に分解されている。**
2. **NAD⁺ は電子の運び手。** 電子を積んだ姿が NADH で、ミトコンドリアの内膜まで電子を運ぶ（電子伝達系）。
3. **ATP と NAD⁺ は、それぞれ別に循環している。** ATP は**エネルギー**を渡して ADP になり、NADH は**電子**を渡して NAD⁺ に戻る。両者がつながるのは電子伝達系で、**NADH が電子を持ってこなければ、ATPの大半は作れない。**
4. **ATP が減ると AMP が大きく増え、AMPK がそれを読む。** AMPK は異化（作る側）を促し、同化（使う側）を抑える。

> [[glycolysis]]では、電子を抜き取る最初の工程 **解糖系（glycolysis）** を見ます。glucose 1分子から得られる ATP は正味2個——この数字が、細胞の代謝の見方を決めます。
