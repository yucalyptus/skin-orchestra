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

異化と同化は、つながっています。異化で出たアミノ酸・脂肪酸・糖は**中間代謝物のプール**に入り、同化はそこから材料を取ります。

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

栄養素を分解するというのは、突き詰めれば**そこから水素を抜き取ること**です。水素原子は陽子1個と電子1個でできているので、**水素を抜くことは、電子を抜くこと**でもあります。この教材で「電子を渡す」と書くとき、実体はたいていこの水素の受け渡しです。

> 電子を抜かれた側を**酸化された**、受け取った側を**還元された**といいます。のちに出る「還元当量」「還元力」「酸化ストレス」（→ [[oxidative-stress]]）も、指しているのはこの電子のやりとりです。

電子を抜き取るのは **解糖系（[[glycolysis]]）と TCA回路（[[tca-cycle]]）** です。抜き取られた電子は、最終的に **電子伝達系（[[electron-transport]]）** で酸素へ渡され、水になります。

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

> **NAD⁺ が減るのには、二通りあります。**
>
> - **NADH に偏る。** 電子を積む・降ろすという循環では、NAD⁺ と NADH を合わせた総量は増減しません。しかし低酸素や、ミトコンドリアそのものの機能低下で電子伝達系が渋滞すると、電子を降ろせない NADH が溜まり、**NAD⁺ が減ります。**
> - **NAD⁺ が消費される。** NAD⁺ は電子の運び手であると同時に、**PARP や sirtuin が分子ごと切って使う基質**でもあります。この消費は循環と並行して絶えず起きていて、切られた分は戻らないので作り直しが要ります。
>
> 加齢では、**この二つが両方とも起こり、互いを悪化させます**（→ [[nad]]・[[mito-dysfunction]]）。

![NAD⁺（空の荷台）が解糖系・TCA回路で電子を受け取って NADH（電子を積んだ荷台）になり、電子伝達系で電子を降ろして NAD⁺ に戻る。降ろされた電子は O₂ へ渡って H₂O になり、その流れで得たエネルギーが ATP⇄ADP の輪へ入る。電子を運ぶ輪とエネルギーを渡す輪は別で、ATPは電子を運ばない](figures/atp_NADの二状態.png)

## 4　ATP不足は、AMPの上昇として増幅される

ATP がエネルギーを渡すと ADP になります。ATP・ADP・AMP の違いは、**付いているリン酸の数**だけです（3個・2個・1個）。細胞にある **adenylate kinase** は、**ADP 2個のあいだでリン酸を1個やりとりさせます。** 片方は3個になって ATP、もう片方は1個になって AMP。反応が速いので、次の式は常にほぼ平衡に保たれています。

> 2 ADP（2） ⇄ ATP（3）＋ AMP（1）

この平衡のおかげで、**ATPが少し減って ADP が増えると、AMP はより大きく増えます**。**もともと AMP はごく少量しかありません**から、少し作られるだけで比率が大きく動きます。小さな不足が、大きな変化として表れるわけです。

**AMP の上昇は、エネルギー不足の合図です。** それを感知するのが **AMPK（AMP-activated protein kinase）** です。 異化（ATPを作る側）を促し、同化（ATPを使う側）を抑える——**代謝の向きを切り替える kinase** です（→ [[ampk-mtor]]）。

<figure class="book-figure"><div style="overflow-x:auto"><svg viewBox="0 0 760 424" style="display:block;width:100%;max-width:100%;height:auto;background:#fff" role="img" aria-label="ATP・ADP・AMPの違いはリン酸の数。ADP2個のうち片方のリン酸1個がもう片方へ移り、受け取った側がATP、渡した側がAMPになる。もともとAMPは少ないので、ATPがわずかに減るだけでAMPは何倍にも増え、それがエネルギー不足の合図としてAMPKに感知される"><defs><marker id="mk1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 1 L9 5 L0 9 z" fill="#B04A33"/></marker></defs><rect x="3" y="3" width="754" height="418" rx="12" fill="#FFFFFF" stroke="#9FB0C8" stroke-width="1.8"/><g font-family="system-ui,-apple-system,sans-serif"><rect x="14" y="14" width="732" height="132" rx="8" fill="#F6F8FC"/><text x="30" y="42" font-size="15" font-weight="700" fill="#2B4C7E">① 違いは、付いているリン酸の数だけ</text><rect x="36" y="72" width="108" height="50" rx="9" fill="#FFFFFF" stroke="#B9C4D6" stroke-width="1.3"/><text x="36" y="64" font-size="15" font-weight="700" fill="#2B4C7E">AMP</text><rect x="44" y="81" width="66" height="32" rx="7" fill="#EDF1F8" stroke="#93A1B8" stroke-width="1.2"/><text x="77.0" y="102" font-size="12" text-anchor="middle" fill="#3B4A63">アデノシン</text><line x1="110" y1="97" x2="114" y2="97" stroke="#93A1B8" stroke-width="1.5"/><circle cx="125" cy="97" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="125" y="101.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><text x="36" y="140" font-size="13" fill="#5A6782">リン酸 1個</text><rect x="286" y="72" width="138" height="50" rx="9" fill="#FFFFFF" stroke="#B9C4D6" stroke-width="1.3"/><text x="286" y="64" font-size="15" font-weight="700" fill="#2B4C7E">ADP</text><rect x="294" y="81" width="66" height="32" rx="7" fill="#EDF1F8" stroke="#93A1B8" stroke-width="1.2"/><text x="327.0" y="102" font-size="12" text-anchor="middle" fill="#3B4A63">アデノシン</text><line x1="360" y1="97" x2="364" y2="97" stroke="#93A1B8" stroke-width="1.5"/><circle cx="375" cy="97" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="375" y="101.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><line x1="389" y1="97" x2="393" y2="97" stroke="#93A1B8" stroke-width="1.5"/><circle cx="404" cy="97" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="404" y="101.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><text x="286" y="140" font-size="13" fill="#5A6782">リン酸 2個</text><rect x="546" y="72" width="166" height="50" rx="9" fill="#FFFFFF" stroke="#B9C4D6" stroke-width="1.3"/><text x="546" y="64" font-size="15" font-weight="700" fill="#2B4C7E">ATP</text><rect x="554" y="81" width="66" height="32" rx="7" fill="#EDF1F8" stroke="#93A1B8" stroke-width="1.2"/><text x="587.0" y="102" font-size="12" text-anchor="middle" fill="#3B4A63">アデノシン</text><line x1="620" y1="97" x2="624" y2="97" stroke="#93A1B8" stroke-width="1.5"/><circle cx="635" cy="97" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="635" y="101.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><line x1="649" y1="97" x2="653" y2="97" stroke="#93A1B8" stroke-width="1.5"/><circle cx="664" cy="97" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="664" y="101.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><line x1="678" y1="97" x2="682" y2="97" stroke="#93A1B8" stroke-width="1.5"/><circle cx="693" cy="97" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="693" y="101.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><text x="546" y="140" font-size="13" fill="#5A6782">リン酸 3個</text><rect x="14" y="158" width="732" height="186" rx="8" fill="#FFFFFF" stroke="#E4E9F2" stroke-width="1"/><text x="30" y="186" font-size="15" font-weight="700" fill="#2B4C7E">② adenylate kinase が、ADP 2個を ATP と AMP に変える</text><rect x="30" y="216" width="138" height="50" rx="9" fill="#FFFFFF" stroke="#B9C4D6" stroke-width="1.3"/><text x="30" y="208" font-size="15" font-weight="700" fill="#2B4C7E">ADP</text><rect x="38" y="225" width="66" height="32" rx="7" fill="#EDF1F8" stroke="#93A1B8" stroke-width="1.2"/><text x="71.0" y="246" font-size="12" text-anchor="middle" fill="#3B4A63">アデノシン</text><line x1="104" y1="241" x2="108" y2="241" stroke="#93A1B8" stroke-width="1.5"/><circle cx="119" cy="241" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="119" y="245.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><line x1="133" y1="241" x2="137" y2="241" stroke="#93A1B8" stroke-width="1.5"/><circle cx="148" cy="241" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="148" y="245.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><text x="177" y="248" font-size="18" fill="#5A6782">＋</text><rect x="197" y="216" width="138" height="50" rx="9" fill="#FFFFFF" stroke="#B9C4D6" stroke-width="1.3"/><text x="197" y="208" font-size="15" font-weight="700" fill="#2B4C7E">ADP</text><rect x="205" y="225" width="66" height="32" rx="7" fill="#EDF1F8" stroke="#93A1B8" stroke-width="1.2"/><text x="238.0" y="246" font-size="12" text-anchor="middle" fill="#3B4A63">アデノシン</text><line x1="271" y1="241" x2="275" y2="241" stroke="#93A1B8" stroke-width="1.5"/><circle cx="286" cy="241" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="286" y="245.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><line x1="300" y1="241" x2="304" y2="241" stroke="#93A1B8" stroke-width="1.5"/><circle cx="315" cy="241" r="11.5" fill="#E2725B" stroke="#B04A33" stroke-width="1.3"/><text x="315" y="245.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><text x="364" y="250" font-size="24" text-anchor="middle" fill="#2B4C7E">⇄</text><rect x="394" y="216" width="166" height="50" rx="9" fill="#FFFFFF" stroke="#B9C4D6" stroke-width="1.3"/><text x="394" y="208" font-size="15" font-weight="700" fill="#2B4C7E">ATP</text><rect x="402" y="225" width="66" height="32" rx="7" fill="#EDF1F8" stroke="#93A1B8" stroke-width="1.2"/><text x="435.0" y="246" font-size="12" text-anchor="middle" fill="#3B4A63">アデノシン</text><line x1="468" y1="241" x2="472" y2="241" stroke="#93A1B8" stroke-width="1.5"/><circle cx="483" cy="241" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="483" y="245.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><line x1="497" y1="241" x2="501" y2="241" stroke="#93A1B8" stroke-width="1.5"/><circle cx="512" cy="241" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="512" y="245.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><line x1="526" y1="241" x2="530" y2="241" stroke="#93A1B8" stroke-width="1.5"/><circle cx="541" cy="241" r="11.5" fill="#E2725B" stroke="#B04A33" stroke-width="1.3"/><text x="541" y="245.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><text x="570" y="248" font-size="18" fill="#5A6782">＋</text><rect x="590" y="216" width="108" height="50" rx="9" fill="#FFFFFF" stroke="#B9C4D6" stroke-width="1.3"/><text x="590" y="208" font-size="15" font-weight="700" fill="#2B4C7E">AMP</text><rect x="598" y="225" width="66" height="32" rx="7" fill="#EDF1F8" stroke="#93A1B8" stroke-width="1.2"/><text x="631.0" y="246" font-size="12" text-anchor="middle" fill="#3B4A63">アデノシン</text><line x1="664" y1="241" x2="668" y2="241" stroke="#93A1B8" stroke-width="1.5"/><circle cx="679" cy="241" r="11.5" fill="#86B39A" stroke="#4F8468" stroke-width="1.3"/><text x="679" y="245.5" font-size="12" font-weight="700" text-anchor="middle" fill="#123A28">P</text><path d="M315 274 C 360 314 500 314 537 278" fill="none" stroke="#B04A33" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#mk1)"/><text x="426" y="332" font-size="12.5" text-anchor="middle" fill="#B04A33">この1個が移る</text><rect x="14" y="356" width="732" height="54" rx="8" fill="#F6F8FC"/><text x="30" y="380" font-size="13.5" fill="#3B4A63">受け取った側はリン酸3個で <tspan font-weight="700">ATP</tspan>、渡した側は1個だけ残って <tspan font-weight="700">AMP</tspan>。<tspan font-weight="700" fill="#6B4CA3">AMPの上昇＝エネルギー不足の合図</tspan>です。</text><text x="30" y="400" font-size="13" fill="#5A6782">もともと AMP はごく少量なので、ATPがわずかに減るだけで AMP は何倍にも増え、それを AMPK が感知します。</text></g></svg></div><figcaption>ATP・ADP・AMPの違いは、付いているリン酸の数（3個・2個・1個）だけ。adenylate kinase は ADP 2個のあいだでリン酸を1個だけ移し、受け取った側を ATP、渡した側を AMP にする。もともと AMP は少ないので、ATPのわずかな低下が AMP の大きな上昇として現れ、それがエネルギー不足の合図として AMPK に感知される</figcaption></figure>

> **発展：細胞外へ出たATP。** 組織の傷害などで局所的に細胞外へ放出されたATPは、エネルギー源としてではなく、**P2受容体を介した危険信号**として働きます。この役割は DAMPs を扱う[[wound-healing]]で説明します。

## この章の到達点

1. **代謝は、壊す側（異化）と組み立てる側（同化）を含む反応のネットワーク。** ATPはその両者をつなぐエネルギーの通貨で、**常に作られ、常に分解されている。**
2. **NAD⁺ は電子の運び手。** 電子を積んだ姿が NADH で、ミトコンドリアの内膜まで電子を運ぶ（電子伝達系）。
3. **ATP と NAD⁺ は、それぞれ別に循環している。** ATP は**エネルギー**を渡して ADP になり、NADH は**電子**を渡して NAD⁺ に戻る。両者がつながるのは電子伝達系で、**NADH が電子を持ってこなければ、ATPの大半は作れない。**
4. **ATP が減ると AMP が大きく増え、AMPK がそれを感知する。** AMPK は異化（作る側）を促し、同化（使う側）を抑える。

> [[glycolysis]]では、電子を抜き取る最初の工程 **解糖系（glycolysis）** を見ます。glucose 1分子から得られる ATP は正味2個——この数字が、細胞の代謝の見方を決めます。
