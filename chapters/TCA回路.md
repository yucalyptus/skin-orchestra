---
id: tca-cycle
title: TCA回路
kind: basic
status: approved
published: 2026-08-24
history:
  - {date: 2026-08-24, note: 初公開}
---

> TCA回路へ入るのは **acetyl-CoA** です。糖は[[glycolysis]]で pyruvate になり、さらに **PDH** によって acetyl-CoA に変わります。脂肪酸からは、[[fatty-acid-oxidation]]の**β酸化**によって acetyl-CoA が切り出されます。糖と脂肪酸では acetyl-CoA になるまでの経路が違いますが、**どちらも acetyl-CoA としてTCA回路へ入ります。**

## この章の一言

> **TCA回路は、ミトコンドリアの中で回り続けるサイクルです。**acetyl-CoA が oxaloacetate と結びついて citrate になり、8つの反応を進むあいだに炭素を CO₂ として捨て、最後はまた oxaloacetate に戻り、次の acetyl-CoA を受け取って循環します。
>
> 役割は2つあります。栄養素から取り出した電子を **NAD⁺・FAD** に積み、**NADH・FADH₂** として電子伝達系へ送ること。もう一つは、回路の中間体を**アミノ酸・脂質・核酸・heme の材料**として抜き出すことです。この二役を **amphibolic** といいます。
>
> そしてこのサイクルは、**ビタミンB群・ミネラル・アミノ酸がそろって初めて回ります。**

<!--
<figure class="book-figure"><div style="overflow-x:auto"><svg viewBox="0 0 560 682" style="display:block;width:100%;max-width:560px;margin:0 auto;height:auto;background:#fff" role="img" aria-label="TCA回路。acetyl-CoAがoxaloacetateと結びついてcitrateになり、isocitrate・α-ketoglutarate・succinyl-CoA・succinate・fumarate・malateを経てoxaloacetateに戻る。炭素数は6から4へ減り、2回の脱炭酸でCO₂が抜ける。1周で3 NADH・1 FADH₂・1 GTP・2 CO₂ができる"><defs><marker id="tc" markerUnits="userSpaceOnUse" viewBox="0 0 10 10" refX="0.5" refY="5" markerWidth="10" markerHeight="10" orient="auto"><path d="M0 1 L9 5 L0 9 z" fill="#2F5C87"/></marker><marker id="td" markerUnits="userSpaceOnUse" viewBox="0 0 10 10" refX="0.5" refY="5" markerWidth="11" markerHeight="11" orient="auto"><path d="M0 1 L9 5 L0 9 z" fill="#9A3D28"/></marker><marker id="to_n" markerUnits="userSpaceOnUse" viewBox="0 0 10 10" refX="0.5" refY="5" markerWidth="9" markerHeight="9" orient="auto"><path d="M0 1 L9 5 L0 9 z" fill="#245840"/></marker><marker id="to_a" markerUnits="userSpaceOnUse" viewBox="0 0 10 10" refX="0.5" refY="5" markerWidth="9" markerHeight="9" orient="auto"><path d="M0 1 L9 5 L0 9 z" fill="#6E5316"/></marker></defs><rect x="3" y="3" width="554" height="676" rx="12" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.8"/><g font-family="system-ui,-apple-system,sans-serif"><text x="28" y="46" font-size="20" font-weight="700" fill="#1E3A63">回るあいだに、炭素を捨てて電子を積む</text><text x="28" y="72" font-size="13" fill="#3B4A63">炭素は CO₂ として抜け、電子は NADH・FADH₂ に載って出ていく</text><path d="M292 290 A 116 116 0 0 1 339 309" fill="none" stroke="#2F5C87" stroke-width="2.6" marker-end="url(#tc)"/><path d="M367 337 A 116 116 0 0 1 386 384" fill="none" stroke="#2F5C87" stroke-width="2.6" marker-end="url(#tc)"/><path d="M386 424 A 116 116 0 0 1 367 471" fill="none" stroke="#2F5C87" stroke-width="2.6" marker-end="url(#tc)"/><path d="M339 499 A 116 116 0 0 1 292 518" fill="none" stroke="#2F5C87" stroke-width="2.6" marker-end="url(#tc)"/><path d="M252 518 A 116 116 0 0 1 205 499" fill="none" stroke="#2F5C87" stroke-width="2.6" marker-end="url(#tc)"/><path d="M177 471 A 116 116 0 0 1 158 424" fill="none" stroke="#2F5C87" stroke-width="2.6" marker-end="url(#tc)"/><path d="M158 384 A 116 116 0 0 1 177 337" fill="none" stroke="#2F5C87" stroke-width="2.6" marker-end="url(#tc)"/><path d="M205 309 A 116 116 0 0 1 252 290" fill="none" stroke="#2F5C87" stroke-width="2.6" marker-end="url(#tc)"/><text x="258" y="278" font-size="13.5" font-weight="700" text-anchor="end" fill="#111827">oxaloacetate</text><text x="258" y="293" font-size="11" text-anchor="end" fill="#3B4A63">炭素4個</text><text x="374" y="316" font-size="13.5" font-weight="700" text-anchor="start" fill="#111827">citrate</text><text x="374" y="331" font-size="11" text-anchor="start" fill="#3B4A63">炭素6個</text><text x="412" y="408" font-size="13.5" font-weight="700" text-anchor="start" fill="#111827">isocitrate</text><text x="412" y="423" font-size="11" text-anchor="start" fill="#3B4A63">炭素6個</text><text x="374" y="500" font-size="13.5" font-weight="700" text-anchor="start" fill="#111827">α-ketoglutarate</text><text x="374" y="515" font-size="11" text-anchor="start" fill="#3B4A63">炭素5個</text><text x="272" y="538" font-size="13.5" font-weight="700" text-anchor="middle" fill="#111827">succinyl-CoA</text><text x="272" y="553" font-size="11" text-anchor="middle" fill="#3B4A63">炭素4個</text><text x="170" y="500" font-size="13.5" font-weight="700" text-anchor="end" fill="#111827">succinate</text><text x="170" y="515" font-size="11" text-anchor="end" fill="#3B4A63">炭素4個</text><text x="132" y="408" font-size="13.5" font-weight="700" text-anchor="end" fill="#111827">fumarate</text><text x="132" y="423" font-size="11" text-anchor="end" fill="#3B4A63">炭素4個</text><text x="170" y="316" font-size="13.5" font-weight="700" text-anchor="end" fill="#111827">malate</text><text x="170" y="331" font-size="11" text-anchor="end" fill="#3B4A63">炭素4個</text><line x1="346" y1="434" x2="370" y2="444" stroke="#245840" stroke-width="1.8" marker-end="url(#to_n)"/><text x="331" y="432" font-size="12" font-weight="700" text-anchor="middle" fill="#245840">NADH</text><text x="331" y="447" font-size="12" font-weight="700" text-anchor="middle" fill="#9A3D28">CO₂</text><line x1="306" y1="483" x2="313" y2="502" stroke="#245840" stroke-width="1.8" marker-end="url(#to_n)"/><text x="299" y="472" font-size="12" font-weight="700" text-anchor="middle" fill="#245840">NADH</text><text x="299" y="487" font-size="12" font-weight="700" text-anchor="middle" fill="#9A3D28">CO₂</text><line x1="245" y1="471" x2="232" y2="502" stroke="#6E5316" stroke-width="1.8" marker-end="url(#to_a)"/><text x="251" y="460" font-size="12" font-weight="700" text-anchor="middle" fill="#6E5316">GTP</text><line x1="198" y1="435" x2="174" y2="445" stroke="#245840" stroke-width="1.8" marker-end="url(#to_n)"/><text x="213" y="433" font-size="12" font-weight="700" text-anchor="middle" fill="#245840">FADH₂</text><line x1="241" y1="330" x2="231" y2="306" stroke="#245840" stroke-width="1.8" marker-end="url(#to_n)"/><text x="247" y="349" font-size="12" font-weight="700" text-anchor="middle" fill="#245840">NADH</text><text x="272" y="409" font-size="13" font-weight="700" text-anchor="middle" fill="#8A97AC">TCA回路</text><line x1="395" y1="252" x2="319" y2="292" stroke="#9A3D28" stroke-width="3.2" marker-end="url(#td)"/><rect x="336" y="214" width="168" height="34" rx="8" fill="#FBEDE9" stroke="#9A3D28" stroke-width="1.8"/><text x="420" y="237" font-size="14" font-weight="700" text-anchor="middle" fill="#7A2F1D">acetyl-CoA</text><text x="420" y="202" font-size="11.5" text-anchor="middle" fill="#3B4A63">糖からも脂肪酸からも、ここへ入る</text><rect x="26" y="566" width="508" height="46" rx="10" fill="#EEF2F8"/><text x="280" y="595" font-size="15" font-weight="700" text-anchor="middle" fill="#1E3A63">1周で 3 NADH ・1 FADH₂ ・1 GTP ・2 CO₂</text><text x="44" y="638" font-size="14" fill="#111827"><tspan font-weight="700">直接作る高エネルギー化合物は GTP 1個だけ。</tspan>主産物は</text><text x="44" y="660" font-size="14" fill="#111827"><tspan font-weight="700" fill="#245840">NADH と FADH₂</tspan> で、ATP はこの電子から電子伝達系で作られる。</text></g></svg></div><figcaption>acetyl-CoA が oxaloacetate と結びついて citrate になり、一周して oxaloacetate に戻る。炭素数は6から4へ減り、2回の脱炭酸で CO₂ として抜ける。1周で 3 NADH・1 FADH₂・1 GTP・2 CO₂。直接作る高エネルギー化合物は GTP 1個だけで、主産物は電子を積んだ NADH と FADH₂</figcaption></figure>

-->

<figure class="book-figure">
<div style="overflow-x:auto">
<svg viewBox="0 0 560 736" style="display:block;width:100%;max-width:560px;margin:0 auto;height:auto;background:#fff" role="img" aria-label="TCA回路。8つの中間体を同じ円周上に配置し、同じ半径の円弧矢印で一周を示す。oxaloacetateにacetyl-CoAが加わってcitrateとなり、isocitrate、alpha-ketoglutarate、succinyl-CoA、succinate、fumarate、malateを経てoxaloacetateに戻る。1周で3 NADH、1 FADH2、1 GTP、2 CO2ができる">
<defs>
<marker id="tcaMainArrow" markerUnits="userSpaceOnUse" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="9" markerHeight="9" orient="auto"><path d="M0 1 L9 5 L0 9 z" fill="#2F5C87"/></marker>
<marker id="tcaEntryArrow" markerUnits="userSpaceOnUse" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="10" markerHeight="10" orient="auto"><path d="M0 1 L9 5 L0 9 z" fill="#9A3D28"/></marker>
</defs>
<rect x="3" y="3" width="554" height="730" rx="12" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.8"/>
<g font-family="system-ui,-apple-system,sans-serif">
<text x="28" y="42" font-size="21" font-weight="700" fill="#1E3A63">回るあいだに、炭素を捨てて電子を取り出す</text>
<text x="28" y="69" font-size="14" fill="#3B4A63">炭素は CO₂として抜け、電子は NADH・FADH₂に載って出ていく</text>

<text x="447" y="91" font-size="12.5" text-anchor="middle" fill="#3B4A63">糖からも脂肪酸からも入る</text>
<rect x="365" y="99" width="168" height="42" rx="9" fill="#FBEDE9" stroke="#9A3D28" stroke-width="1.7"/>
<text x="449" y="126" font-size="15.5" font-weight="700" text-anchor="middle" fill="#7A2F1D">acetyl-CoA</text>
<path d="M414 143 Q403 174 380 210" fill="none" stroke="#9A3D28" stroke-width="3" marker-end="url(#tcaEntryArrow)"/>

<!-- 全反応を同じ半径（r=175）の円弧上にそろえる -->
<circle cx="280" cy="365" r="175" fill="none" stroke="#DCE3EC" stroke-width="1.4"/>
<path d="M350 204.6 A175 175 0 0 1 375 218" fill="none" stroke="#2F5C87" stroke-width="2.8" marker-end="url(#tcaMainArrow)"/>
<path d="M423 264 A175 175 0 0 1 453.5 342" fill="none" stroke="#2F5C87" stroke-width="2.8" marker-end="url(#tcaMainArrow)"/>
<path d="M453.5 388 A175 175 0 0 1 423 466" fill="none" stroke="#2F5C87" stroke-width="2.8" marker-end="url(#tcaMainArrow)"/>
<path d="M375 512 A175 175 0 0 1 350 525.4" fill="none" stroke="#2F5C87" stroke-width="2.8" marker-end="url(#tcaMainArrow)"/>
<path d="M210 525.4 A175 175 0 0 1 185 512" fill="none" stroke="#2F5C87" stroke-width="2.8" marker-end="url(#tcaMainArrow)"/>
<path d="M137 466 A175 175 0 0 1 106.5 388" fill="none" stroke="#2F5C87" stroke-width="2.8" marker-end="url(#tcaMainArrow)"/>
<path d="M106.5 342 A175 175 0 0 1 137 264" fill="none" stroke="#2F5C87" stroke-width="2.8" marker-end="url(#tcaMainArrow)"/>
<path d="M185 218 A175 175 0 0 1 210 204.6" fill="none" stroke="#2F5C87" stroke-width="2.8" marker-end="url(#tcaMainArrow)"/>

<!-- 8つの中間体を45度ずつ円周上へ配置 -->
<rect x="210" y="167" width="140" height="46" rx="10" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.5"/>
<text x="280" y="187" font-size="15" font-weight="700" text-anchor="middle" fill="#111827">oxaloacetate</text>
<text x="280" y="206" font-size="12.5" text-anchor="middle" fill="#3B4A63">炭素4個</text>

<rect x="354" y="218" width="100" height="46" rx="10" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.5"/>
<text x="404" y="238" font-size="15" font-weight="700" text-anchor="middle" fill="#111827">citrate</text>
<text x="404" y="257" font-size="12.5" text-anchor="middle" fill="#3B4A63">炭素6個</text>

<rect x="395" y="342" width="120" height="46" rx="10" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.5"/>
<text x="455" y="362" font-size="15" font-weight="700" text-anchor="middle" fill="#111827">isocitrate</text>
<text x="455" y="381" font-size="12.5" text-anchor="middle" fill="#3B4A63">炭素6個</text>

<rect x="324" y="466" width="160" height="46" rx="10" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.5"/>
<text x="404" y="486" font-size="15" font-weight="700" text-anchor="middle" fill="#111827">α-ketoglutarate</text>
<text x="404" y="505" font-size="12.5" text-anchor="middle" fill="#3B4A63">炭素5個</text>

<rect x="210" y="517" width="140" height="46" rx="10" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.5"/>
<text x="280" y="537" font-size="15" font-weight="700" text-anchor="middle" fill="#111827">succinyl-CoA</text>
<text x="280" y="556" font-size="12.5" text-anchor="middle" fill="#3B4A63">炭素4個</text>

<rect x="96" y="466" width="120" height="46" rx="10" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.5"/>
<text x="156" y="486" font-size="15" font-weight="700" text-anchor="middle" fill="#111827">succinate</text>
<text x="156" y="505" font-size="12.5" text-anchor="middle" fill="#3B4A63">炭素4個</text>

<rect x="45" y="342" width="120" height="46" rx="10" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.5"/>
<text x="105" y="362" font-size="15" font-weight="700" text-anchor="middle" fill="#111827">fumarate</text>
<text x="105" y="381" font-size="12.5" text-anchor="middle" fill="#3B4A63">炭素4個</text>

<rect x="106" y="218" width="100" height="46" rx="10" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.5"/>
<text x="156" y="238" font-size="15" font-weight="700" text-anchor="middle" fill="#111827">malate</text>
<text x="156" y="257" font-size="12.5" text-anchor="middle" fill="#3B4A63">炭素4個</text>

<text x="280" y="350" font-size="17" font-weight="700" text-anchor="middle" fill="#8A97AC">TCA回路</text>

<rect x="195" y="274" width="82" height="32" rx="8" fill="#E6F1EA" stroke="#3D6B52"/>
<text x="236" y="295" font-size="13" font-weight="700" text-anchor="middle" fill="#245840">＋ NADH</text>

<rect x="315" y="292" width="106" height="46" rx="8" fill="#F7F9FC" stroke="#3D6B52"/>
<text x="368" y="311" font-size="13" font-weight="700" text-anchor="middle" fill="#245840">＋ NADH</text>
<text x="368" y="329" font-size="13" font-weight="700" text-anchor="middle" fill="#9A3D28">＋ CO₂</text>

<rect x="320" y="407" width="106" height="46" rx="8" fill="#F7F9FC" stroke="#3D6B52"/>
<text x="373" y="426" font-size="13" font-weight="700" text-anchor="middle" fill="#245840">＋ NADH</text>
<text x="373" y="444" font-size="13" font-weight="700" text-anchor="middle" fill="#9A3D28">＋ CO₂</text>

<rect x="222" y="455" width="72" height="32" rx="8" fill="#F5E9D6" stroke="#B4762B"/>
<text x="258" y="476" font-size="13" font-weight="700" text-anchor="middle" fill="#8A5A18">＋ GTP</text>

<rect x="139" y="400" width="92" height="32" rx="8" fill="#E6F1EA" stroke="#3D6B52"/>
<text x="185" y="421" font-size="13" font-weight="700" text-anchor="middle" fill="#245840">＋ FADH₂</text>

<rect x="26" y="603" width="508" height="48" rx="10" fill="#EEF2F8"/>
<text x="280" y="633" font-size="16" font-weight="700" text-anchor="middle" fill="#1E3A63">1周で 3 NADH ・1 FADH₂ ・1 GTP ・2 CO₂</text>

<text x="44" y="681" font-size="14.5" fill="#111827"><tspan font-weight="700">直接作る高エネルギー化合物は GTP 1個だけ。</tspan>主産物は</text>
<text x="44" y="707" font-size="14.5" fill="#111827"><tspan font-weight="700" fill="#245840">NADH と FADH₂</tspan> で、ATP はこの電子から電子伝達系で作られる。</text>
</g>
</svg>
</div>
<figcaption>8つの中間体を同じ円周上に置き、反応矢印を同じ半径の円弧でつないだ。acetyl-CoA が oxaloacetate と結びついて citrate になり、一周して oxaloacetate に戻る。各反応で生じる NADH・FADH₂・GTP・CO₂を回路の内側に示した。1周で 3 NADH・1 FADH₂・1 GTP・2 CO₂ができる</figcaption>
</figure>

## 1　糖から来た炭素は、PDH で acetyl-CoA になる

ミトコンドリアへ入った pyruvate は、**pyruvate dehydrogenase（PDH）** という酵素複合体で **acetyl-CoA** に変えられます。TCA回路そのものではなく、その手前の一反応です。**脂肪酸から来る acetyl-CoA は、この反応を通りません**（→ [[fatty-acid-oxidation]]）。

<figure class="book-figure">
<div style="overflow-x:auto">
<svg viewBox="0 0 560 164" style="display:block;width:100%;max-width:560px;margin:0 auto;height:auto;background:#fff" role="img" aria-label="pyruvate、CoA、NAD⁺が、矢印の途中で働くPDHによってacetyl-CoA、CO₂、NADHに変わる不可逆反応">
<defs><marker id="pdhArrow" markerUnits="userSpaceOnUse" viewBox="0 0 10 10" refX="0.5" refY="5" markerWidth="11" markerHeight="11" orient="auto"><path d="M0 1 L9 5 L0 9 z" fill="#9A3D28"/></marker></defs>
<rect x="3" y="3" width="554" height="158" rx="12" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.8"/>
<g font-family="system-ui,-apple-system,sans-serif">
<text x="28" y="34" font-size="17" font-weight="700" fill="#1E3A63">PDH は、pyruvate を TCA回路へ渡す手前で働く</text>
<rect x="24" y="58" width="202" height="48" rx="9" fill="#E7EEF7" stroke="#2F5C87" stroke-width="1.4"/>
<text x="125" y="87" font-size="13.5" font-weight="700" text-anchor="middle" fill="#1E3A63">pyruvate ＋ CoA ＋ NAD⁺</text>
<line x1="238" y1="82" x2="322" y2="82" stroke="#9A3D28" stroke-width="2.8" marker-end="url(#pdhArrow)"/>
<text x="280" y="70" font-size="13" font-weight="700" text-anchor="middle" fill="#7A2F1D">PDH</text>
<rect x="334" y="58" width="202" height="48" rx="9" fill="#FBEDE9" stroke="#9A3D28" stroke-width="1.4"/>
<text x="435" y="87" font-size="13.5" font-weight="700" text-anchor="middle" fill="#7A2F1D">acetyl-CoA ＋ CO₂ ＋ NADH</text>
<text x="280" y="138" font-size="12" text-anchor="middle" fill="#3B4A63">CO₂が抜け、NAD⁺が電子を受け取ってNADHになる</text>
</g>
</svg>
</div>
<figcaption>PDH は TCA回路の中ではなく、pyruvate を acetyl-CoA に変えて回路へ渡す手前の不可逆反応を進める</figcaption>
</figure>

**この反応には、5つの補酵素が同時に必要です。**その多くはビタミンB群から作られ、さらにマグネシウムも要ります。補酵素と金属イオンをまとめた呼び名が **補因子** です。

| 補酵素 | 由来 | PDH複合体のどこで働くか |
|---|---|---|
| **TPP**（thiamine pyrophosphate） | **thiamine（B1）** | E1：pyruvate の脱炭酸。結合には **Mg²⁺** が要る |
| **lipoate**（lipoamide） | lipoic acid（体内でも合成される） | E2：アセチル基を受け取って転移する |
| **CoA** | **pantothenate（B5）** | E2：アセチル基を acetyl-CoA として持ち出す |
| **FAD** | **riboflavin（B2）** | E3：使い終わった lipoamide を再酸化する |
| **NAD⁺** | **niacin（B3）** | E3：電子を受け取り NADH になる |

**1つでも欠ければ、PDH は働けないため、pyruvate は acetyl-CoA になれません。**行き場を失った pyruvate は、lactate へ回されます（→ [[glycolysis]]§5）。ただし**止まるのは糖から来る炭素だけ**で、β酸化から来る acetyl-CoA はこの門を通らないので、回路へ入り続けます。

**TCA回路に入ったあとも、回路を回すには補酵素と材料（アミノ酸）がそろっている必要があります。**

- **ビタミンB群** … 補酵素の材料（B1 → TPP、B2 → FAD、B3 → NAD⁺、B5 → CoA）。同じ5つは、pyruvateをacetyl-CoAに変える **PDH** と、回路内の **α-ketoglutarate dehydrogenase**（PDH と同型の複合体）の**2か所**で要る
- **マグネシウム** … TPP を酵素につなぎ止める。PDH を再活性化する phosphatase にも要る（→ §2）
- **鉄と硫黄** … **Fe–S クラスター**として aconitase と Complex II（succinate dehydrogenase）に組み込まれている
- **アミノ酸** … 抜き出された中間体を補充する（→ §3）。その炭素骨格を回路へ渡すアミノ基転移には、**pyridoxal phosphate（B6）** が要る（→ §4）

アミノ酸が要るのは、**中間体が絶えず抜き出されるから**です。抜けた分を補わなければ、回転は落ちます（→ §3）。

**疲労に対してビタミンB群やマグネシウムを含む点滴・サプリが使われるのは、この依存関係を根拠にしています。**

> **切り分け。**「補因子が欠けていれば回らない」は確立した生化学です。「足せば回転が上がる」は、**欠乏がある場合にしか導けません**。充足している状態で追加したときに代謝回転や臨床所見がどう動くかは、別に検証すべき問いです（→ 巻頭「本教材が守る切り分け」）。

::: note ちなみに ―― 「充足しているか」は測りにくい
切り分けの前提になる「欠乏か、充足か」の判定そのものが、臨床では簡単ではありません。**血清の値が体内のプールを反映しないもの**があるからです。マグネシウムは体内の大半が骨と細胞内にあり、**血中にあるのは1%程度**です。thiamine も、血漿濃度より全血の thiamine pyrophosphate や transketolase 活性のほうが状態を反映するとされます。**基準値内であることは、細胞内で足りていることの保証にはなりません。**
:::

## 2　pyruvateをTCA回路へ渡すPDHは、活性が調節される

解糖系でできた **pyruvate** の炭素がTCA回路へ進むには、まずPDHによって **acetyl-CoA** に変換される必要があります。**PDHの活性によって、糖由来の炭素がTCA回路へ進む量が変わります。**

PDHは、**リン酸が付いていないときは活性型**です。**PDH kinase**がリン酸を付けると不活性型になり、pyruvateからacetyl-CoAへの変換が減ります。反対に、**PDH phosphatase**がリン酸を外すと活性型に戻り、変換が増えます。PDHが完全に開く・閉じるのではなく、**活性型PDHの割合が変わることで、通過するpyruvateの量が調節されます。**

<figure class="book-figure">
<div style="overflow-x:auto">
<svg viewBox="0 0 560 482" style="display:block;width:100%;max-width:560px;margin:0 auto;height:auto;background:#fff" role="img" aria-label="PDHは脱リン酸化された活性型とリン酸化された不活性型の間を移る。PDH kinaseがリン酸を付けると不活性型になり、PDH phosphataseがリン酸を外すと活性型になる。ATPを作る必要があると活性型PDHが増え、ATP、NADH、acetyl-CoAが多いと不活性型PDHが増える">
<defs>
<marker id="pdhOffArrow" markerUnits="userSpaceOnUse" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 1 L9 5 L0 9 z" fill="#9A3D28"/></marker>
<marker id="pdhOnArrow" markerUnits="userSpaceOnUse" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 1 L9 5 L0 9 z" fill="#3D6B52"/></marker>
</defs>
<rect x="3" y="3" width="554" height="476" rx="12" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.8"/>
<g font-family="system-ui,-apple-system,sans-serif">
<text x="28" y="40" font-size="19" font-weight="700" fill="#1E3A63">PDHの活性は、リン酸化で変わる</text>
<text x="28" y="64" font-size="13.5" fill="#3B4A63">調節するのは、pyruvateをacetyl-CoAに変える反応</text>

<rect x="26" y="84" width="508" height="54" rx="10" fill="#F4F7FA" stroke="#AAB4C4" stroke-width="1.4"/>
<text x="280" y="117" font-size="16" font-weight="700" text-anchor="middle" fill="#1E3A63">pyruvate ── PDH ──→ acetyl-CoA ──→ TCA回路</text>

<rect x="22" y="166" width="220" height="112" rx="11" fill="#E6F1EA" stroke="#3D6B52" stroke-width="1.8"/>
<text x="132" y="194" font-size="15" font-weight="700" text-anchor="middle" fill="#245840">脱リン酸化されたPDH</text>
<text x="132" y="220" font-size="17" font-weight="700" text-anchor="middle" fill="#245840">活性型</text>
<text x="132" y="250" font-size="13" text-anchor="middle" fill="#1F2937">pyruvate → acetyl-CoA が増える</text>

<rect x="318" y="166" width="220" height="112" rx="11" fill="#FBEDE9" stroke="#9A3D28" stroke-width="1.8"/>
<text x="428" y="194" font-size="15" font-weight="700" text-anchor="middle" fill="#7A2F1D">リン酸化されたPDH</text>
<text x="428" y="220" font-size="17" font-weight="700" text-anchor="middle" fill="#7A2F1D">不活性型</text>
<text x="428" y="250" font-size="13" text-anchor="middle" fill="#1F2937">pyruvate → acetyl-CoA が減る</text>

<line x1="242" y1="190" x2="316" y2="190" stroke="#9A3D28" stroke-width="2.4" marker-end="url(#pdhOffArrow)"/>
<text x="280" y="178" font-size="11.5" font-weight="700" text-anchor="middle" fill="#7A2F1D">PDH kinase</text>
<text x="280" y="207" font-size="11" text-anchor="middle" fill="#7A2F1D">リン酸を付ける</text>
<line x1="318" y1="248" x2="244" y2="248" stroke="#3D6B52" stroke-width="2.4" marker-end="url(#pdhOnArrow)"/>
<text x="280" y="295" font-size="11.5" font-weight="700" text-anchor="middle" fill="#245840">PDH phosphatase：リン酸を外す</text>

<rect x="22" y="302" width="246" height="118" rx="11" fill="#F3FAF6" stroke="#86AA94" stroke-width="1.4"/>
<text x="40" y="329" font-size="14.5" font-weight="700" fill="#245840">ATPを作る必要があるとき</text>
<text x="40" y="354" font-size="12.5" fill="#1F2937">ADP↑：PDH kinaseを抑える</text>
<text x="40" y="377" font-size="12.5" fill="#1F2937">pyruvate↑：糖由来の材料が十分にある</text>
<text x="40" y="400" font-size="12.5" fill="#1F2937">筋収縮のCa²⁺：phosphataseを促す</text>

<rect x="292" y="302" width="246" height="118" rx="11" fill="#FFF5F2" stroke="#C68B7C" stroke-width="1.4"/>
<text x="310" y="329" font-size="14" font-weight="700" fill="#7A2F1D">糖をさらに使う必要が低いとき</text>
<text x="310" y="356" font-size="12.5" fill="#1F2937">ATP・NADH・acetyl-CoA↑</text>
<text x="310" y="380" font-size="12.5" fill="#1F2937">→ PDH kinaseが働く</text>
<text x="310" y="404" font-size="12.5" fill="#1F2937">→ PDHがリン酸化され、活性が下がる</text>

<rect x="26" y="438" width="508" height="25" rx="12" fill="#1E3A63"/>
<text x="280" y="455" font-size="12" font-weight="700" text-anchor="middle" fill="#FFFFFF">完全な開閉ではなく、活性型PDHの割合が連続的に変わる</text>
</g>
</svg>
</div>
<figcaption>ATPを作る必要があると活性型PDHが増え、pyruvateからacetyl-CoAへの変換が増える。ATP・NADH・acetyl-CoAが多いとPDH kinaseがPDHをリン酸化し、不活性型を増やす。PDH phosphataseがリン酸を外すと活性型に戻る</figcaption>
</figure>

**PDHの活性が下がると**、pyruvateからacetyl-CoAへの変換が減り、pyruvateはlactateやalanineへ回りやすくなります。**PDHの活性が上がると**、acetyl-CoAへの変換が増え、糖由来の炭素がTCA回路へ進みます。ただし、実際に回路が回るにはoxaloacetateがあり、NADHの電子を電子伝達系へ渡せることも必要です。

基本的には、**ATPを作る必要があるとPDHの活性が上がります。反対に、ミトコンドリア内にATP・NADH・acetyl-CoAが多く、糖をさらに使う必要が低いと、PDHの活性は下がります。**ADPが増えるのはATPが使われている合図です。pyruvateが増えるのは、**acetyl-CoAへ変換できる糖由来の材料が十分にある**という合図です。筋収縮時のCa²⁺は、筋がATPを使って仕事をしていることを伝えます。

反対に、**ミトコンドリア内にATP・NADH・acetyl-CoAが多いとき**は、PDH kinaseが働いてPDHの活性を下げます。これは、**糖由来のpyruvateから、さらにacetyl-CoAとNADHを作る必要が低い**という合図です。

### 特殊な条件：細胞への酸素供給が需要に追いつかないとき

通常は、細胞への酸素供給と消費のバランスが保たれています。**細胞へ届く酸素が、ミトコンドリアで必要な量に追いつかない状態を、低酸素と呼びます。**空気中の酸素が少ない場合だけでなく、血流が途絶える虚血や重い呼吸不全、血流の乏しい創傷や腫瘍などでも、低酸素は局所的・持続的に起こります。

::: note たとえば、手術・救急では
- **気道閉塞・低換気・無呼吸・無気肺**：肺から血液へO₂を取り込めず、動脈血の酸素が下がる
- **大量出血・ショック・重い血圧低下**：酸素を運ぶHbや組織へ送る血流が不足する。SpO₂が保たれていても、組織は低酸素になり得る
- **血管の一時遮断や駆血**：その先の組織だけ血流が止まり、局所的な虚血になる

どれも、最終的には**細胞への酸素供給が需要に追いつかない状態**です。
:::

**細胞への酸素供給が不足すると、まず電子伝達系が滞ります。**電子伝達系の最後では、Complex IVが電子をO₂へ渡します。O₂が少なくなると、この受け渡しが遅くなります。NADHは電子を降ろしてNAD⁺へ戻りにくくなり、NAD⁺を必要とするTCA回路も回りにくくなります。酸素が減った瞬間に完全停止するのではなく、**酸素の低下に応じて電子伝達系とTCA回路の流れが落ちる**と考えると分かりやすいでしょう。

細胞はさらに、糖由来の電子をミトコンドリアへ入れすぎないようにします。低酸素になると **HIF-1α** が増え、**PDK1**（PDH kinase の一つ）を増やします。**PDK1はPDHをリン酸化して、不活性化します。**するとpyruvateからacetyl-CoAへの変換が減り、糖由来の炭素はTCA回路へ入りにくくなります。つまり、糖の経路をTCA回路の手前で抑え、pyruvateの多くをlactateへ回します。

この調節には、電子の渋滞を減らす意味があります。酸素供給が不足していてもO₂が少し残っていると、滞った電子の一部がそのO₂へ漏れ、**ROS（reactive oxygen species）**を生じることがあります。PDHの活性を下げれば、TCA回路が作るNADHが減り、電子伝達系へ入る電子も減ります。その結果、**電子漏れとROSによる細胞傷害を抑えられます**（Kim JW et al., *Cell Metab* 2006;3:177–185. PMID 16517405；→ [[glycolysis]]§3）。

なお、酸素が完全にゼロなら、O₂と反応してROSを作ることもできません。その場合の大きな問題は、電子伝達系とATP産生が止まることです。ROSがとくに問題になりやすいのは、**酸素が少し残る低酸素状態**や、血流が戻って酸素が再び入る**再酸素化**のときです。

**回路の中の酵素も、同じように代謝産物で調節されています。回路は一定の速さで回っているのではなく、使った分だけ回ります。**

## 3　TCA回路で得られるもの

> acetyl-CoA 1分子 → 2 CO₂ ＋ 3 NADH ＋ 1 FADH₂ ＋ 1 GTP

glucose 1分子からは pyruvate が2つできるので、**回路は2周します**（→ [[glycolysis]]）。

**回路が直接作る高エネルギー化合物は、1周あたり GTP 1個だけ**です。GTP は ATP と同じように使えますが、量はわずかです。**回路の主産物は NADH と FADH₂**で、積んだ電子を[[electron-transport]]へ運びます。ATP の大半は、そこで作られます。

つまりTCA回路から得られるものは、**ATPの大半を電子伝達系で作るための NADH・FADH₂**と、**体の成分を合成する材料となる中間体**の二つです。

回路の**中間体**は、次々と**合成の材料として抜き出されます**。抜き出し口は4か所です。

| 抜き出す中間体 | 何になるか |
|---|---|
| **citrate** | 細胞質へ出て、**脂肪酸・コレステロール**の材料になる |
| **α-ketoglutarate** | glutamate を経て**アミノ酸**へ。**コラーゲンの proline の水酸化**にも使われる |
| **oxaloacetate** | aspartate を経て**核酸**の材料になる。細胞質へ出れば**糖新生で glucose** になる |
| **succinyl-CoA** | **heme** の材料になる |

<figure class="book-figure"><div style="overflow-x:auto"><svg viewBox="0 0 560 602" style="display:block;width:100%;max-width:560px;margin:0 auto;height:auto;background:#fff" role="img" aria-label="TCA回路の中間体は合成の材料として抜き出される。citrateは脂肪酸とコレステロール、α-ketoglutarateはアミノ酸とコラーゲンのproline水酸化、oxaloacetateは核酸と糖新生、succinyl-CoAはhemeへ。抜けた分はpyruvate carboxylaseとglutaminolysisで補充される"><defs><marker id="ox" markerUnits="userSpaceOnUse" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="11" markerHeight="11" orient="auto"><path d="M0 1 L9 5 L0 9 z" fill="#B4762B"/></marker></defs><rect x="3" y="3" width="554" height="596" rx="12" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.8"/><g font-family="system-ui,-apple-system,sans-serif"><text x="28" y="46" font-size="20" font-weight="700" fill="#1E3A63">同じ扉が、出口にも入口にもなる</text><text x="28" y="72" font-size="13" fill="#3B4A63">回路は電子を送るだけでなく、体を作る材料の供給元でもある</text><rect x="26" y="98" width="508" height="34" rx="8" fill="#F5E9D6"/><text x="44" y="121" font-size="15" font-weight="700" fill="#8A5A18">抜き出す（cataplerosis）── 中間体は合成の材料になる</text><text x="44" y="162" font-size="13.5" font-weight="700" fill="#111827">citrate</text><line x1="196" y1="157" x2="228" y2="157" stroke="#B4762B" stroke-width="2" marker-end="url(#ox)"/><text x="238" y="162" font-size="13" fill="#1F2937">細胞質へ出て、脂肪酸・コレステロールの材料</text><line x1="44" y1="176" x2="516" y2="176" stroke="#EEF0F4" stroke-width="1"/><text x="44" y="208" font-size="13.5" font-weight="700" fill="#111827">α-ketoglutarate</text><line x1="196" y1="203" x2="228" y2="203" stroke="#B4762B" stroke-width="2" marker-end="url(#ox)"/><text x="238" y="208" font-size="13" fill="#1F2937">アミノ酸へ。コラーゲンの proline 水酸化にも</text><line x1="44" y1="222" x2="516" y2="222" stroke="#EEF0F4" stroke-width="1"/><text x="44" y="254" font-size="13.5" font-weight="700" fill="#111827">oxaloacetate</text><line x1="196" y1="249" x2="228" y2="249" stroke="#B4762B" stroke-width="2" marker-end="url(#ox)"/><text x="238" y="254" font-size="13" fill="#1F2937">核酸の材料。細胞質へ出れば糖新生で glucose</text><line x1="44" y1="268" x2="516" y2="268" stroke="#EEF0F4" stroke-width="1"/><text x="44" y="300" font-size="13.5" font-weight="700" fill="#111827">succinyl-CoA</text><line x1="196" y1="295" x2="228" y2="295" stroke="#B4762B" stroke-width="2" marker-end="url(#ox)"/><text x="238" y="300" font-size="13" fill="#1F2937">heme の材料</text><rect x="26" y="334" width="508" height="34" rx="8" fill="#E7EEF7"/><text x="44" y="357" font-size="15" font-weight="700" fill="#1E3A63">補充する（anaplerosis）── 抜けた分を別の経路から足す</text><text x="44" y="398" font-size="13.5" font-weight="700" fill="#111827">pyruvate carboxylase</text><text x="44" y="416" font-size="13" fill="#1F2937">pyruvate ＋ CO₂ → oxaloacetate（biotin が要る）</text><line x1="44" y1="428" x2="516" y2="428" stroke="#EEF0F4" stroke-width="1"/><text x="44" y="444" font-size="13.5" font-weight="700" fill="#111827">glutaminolysis</text><text x="44" y="462" font-size="13" fill="#1F2937">glutamine → glutamate → α-ketoglutarate</text><rect x="26" y="478" width="508" height="52" rx="10" fill="#1E3A63"/><text x="280" y="510" font-size="15.5" font-weight="700" text-anchor="middle" fill="#FFF">抜いた分を補わなければ、回転は落ちる</text><text x="44" y="556" font-size="13.5" fill="#1F2937">とくに <tspan font-weight="700">oxaloacetate</tspan> が減ると、acetyl-CoA を受け取る相手が</text><text x="44" y="578" font-size="13.5" fill="#1F2937">いなくなり、入口で滞る。</text></g></svg></div><figcaption>TCA回路の中間体は、合成の材料として抜き出される（cataplerosis）。citrate は脂肪酸とコレステロール、α-ketoglutarate はアミノ酸とコラーゲンの proline 水酸化、oxaloacetate は核酸と糖新生、succinyl-CoA は heme へ。抜けた分は pyruvate carboxylase と glutaminolysis が補う（anaplerosis）</figcaption></figure>

**抜き出せば、回路内の中間体は減ります。**とくに oxaloacetate が減ると、acetyl-CoA を受け取る相手がいなくなり、入口で滞ります。絶食時の肝で実際にこれが起こり、行き場を失った acetyl-CoA がケトン体になります（→ [[fatty-acid-oxidation]]）。

だから細胞は、抜いた分を別の経路から**補充**します。これが **anaplerosis** で、代表例は次の二つ。

- **pyruvate carboxylase**：pyruvate ＋ CO₂ → **oxaloacetate**。解糖系から来た炭素を、燃やすためではなく**回路の材料を足すために**使う。この酵素は補因子として **biotin（B7）** を要求します。**同じ反応が糖新生の出発点でもあります**——回路を保つ側にも、glucose を作る側にも使われる反応です
- **glutaminolysis**：glutamine → glutamate → **α-ketoglutarate**。増殖中の細胞がよく使うルートで、**アミノ酸から回路を支えます**

抜き出す方向が **cataplerosis**、補充する方向が **anaplerosis** です。

> TCA回路は、エネルギーを取り出すためだけの回路ではありません。**同じ回路が、体を作る材料の供給元でもあります。**

::: note ちなみに ―― α-ketoglutarate はコラーゲンの成熟に消費される
コラーゲンは、作られたあとに **prolyl hydroxylase**・**lysyl hydroxylase** による**水酸化**を受けて初めて成熟します（工程の詳細は[[fibroblast-collagen]]）。この酵素は反応のたびに **α-ketoglutarate を共基質として消費します**。TCA回路の中間体が、そのままコラーゲンの加工に使われているということです。

**ただし α-ketoglutarate は、必要な要素の一つにすぎません。**同じ反応には **O₂・Fe²⁺・ascorbate** も要ります。しかも α-ketoglutarate はコラーゲンの一部になるのではなく、消費されて succinate と CO₂ に変わります。

だから「TCA回路を活発にすればコラーゲンが増える」とは言えません。**ここで言えるのは、機序の上でつながっているというところまで**です。この線引きが、のちに栄養や治療を評価するときに効いてきます。
:::

## 4　アミノ酸は、窒素を外してから代謝へ入る

> **この節でまず理解したいことは一つです。**アミノ酸を燃料として使うときは、先に**窒素を含む部分**と**炭素骨格**に分けます。窒素は尿素にして捨て、残った炭素骨格を、形に合う場所から代謝へ入れます。

### まず、アミノ酸を二つの部分に分ける

アミノ酸は、**窒素を含むアミノ基**と、**炭素でできた骨格**を持っています。エネルギー産生や糖新生に使えるのは、主に炭素骨格の側です。一方、余った窒素は体内にためておけないため、分けて排泄する必要があります。

多くの場合、最初に **aminotransferase（トランスアミナーゼ）**が、アミノ酸のアミノ基を **α-ketoglutarate** へ移します。この反応が**アミノ基転移**です。aminotransferase が働くには、補酵素の **pyridoxal phosphate（PLP、vitamin B6の誘導体）**が必要です。

アミノ基を渡したアミノ酸は、**炭素骨格（α-ケト酸）**になります。反対に、アミノ基を受け取った α-ketoglutarate は **glutamate** になります。つまりglutamateは、いろいろなアミノ酸から出た窒素を、いったん集める役目です。

### ALT・ASTは、アミノ基を移す酵素

**ALT（alanine aminotransferase、アラニンアミノトランスフェラーゼ）**と**AST（aspartate aminotransferase、アスパラギン酸アミノトランスフェラーゼ）**は、aminotransferaseの代表です。どちらも**アミノ基を別の分子へ移す酵素**です。

> **ALT**：alanine ＋ α-ketoglutarate ⇄ **pyruvate** ＋ glutamate
> **AST**：aspartate ＋ α-ketoglutarate ⇄ **oxaloacetate** ＋ glutamate

血液検査では、肝細胞や筋細胞から血中へ出てきたAST・ALTを測ります。しかし細胞内での本来の仕事は、上のように**アミノ基を移し、残った炭素骨格を代謝へつなぐこと**です。

### glutamateに集めた窒素は、尿素にして排泄する

次に **glutamate dehydrogenase** が、glutamate から窒素を **NH₃** として外します。これが**酸化的脱アミノ**です。NH₃は肝臓で尿素に変えられ、尿中へ排泄されます。窒素を渡したglutamateは α-ketoglutarate に戻り、再びアミノ基の受け手として使われます。

::: note ちなみに ―― BUNは、この窒素処理の下流を見ている
**BUN（blood urea nitrogen、血中尿素窒素）**は、血液中の尿素に含まれる窒素を測った値です。アミノ酸から外された窒素は、**NH₃ → 肝臓で尿素 → 血液 → 腎臓から尿中へ排泄**という順に処理されます。したがってBUNは、この流れの最後にある尿素を見ています。

ただし、BUNはglutamate dehydrogenaseの働きを直接測る検査ではありません。**腎機能の低下や脱水**で上がるほか、**高タンパク食・消化管出血・タンパク質分解の亢進**でも上がります。反対に、**低タンパク摂取・低栄養・過剰な水分・重い肝機能低下**では下がることがあります。BUN単独ではなく、creatinine・eGFR・水分状態・肝機能と合わせて読みます。
:::

<figure class="book-figure">
<div style="overflow-x:auto">
<svg viewBox="0 0 560 700" style="display:block;width:100%;max-width:560px;margin:0 auto;height:auto;background:#fff" role="img" aria-label="アミノ酸のアミノ基をaminotransferaseがalpha-ketoglutarateへ移してglutamateに集める。glutamate dehydrogenaseがglutamateから窒素を外し、alpha-ketoglutarateは再利用され、アンモニアは肝臓で尿素になる。ALTはalanineをpyruvateへ、ASTはaspartateをoxaloacetateへ変える双方向反応を触媒する">
<defs>
<marker id="nitrogenArrow" markerUnits="userSpaceOnUse" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="9" markerHeight="9" orient="auto"><path d="M0 1 L9 5 L0 9 z" fill="#2F5C87"/></marker>
<marker id="nitrogenBack" markerUnits="userSpaceOnUse" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse"><path d="M0 1 L9 5 L0 9 z" fill="#3D6B52"/></marker>
<marker id="nitrogenWaste" markerUnits="userSpaceOnUse" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="9" markerHeight="9" orient="auto"><path d="M0 1 L9 5 L0 9 z" fill="#B4762B"/></marker>
<marker id="nitrogenBlueBack" markerUnits="userSpaceOnUse" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse"><path d="M0 1 L9 5 L0 9 z" fill="#2F5C87"/></marker>
</defs>
<rect x="3" y="3" width="554" height="694" rx="12" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.8"/>
<g font-family="system-ui,-apple-system,sans-serif">
<text x="28" y="44" font-size="20" font-weight="700" fill="#1E3A63">アミノ酸は、窒素と炭素骨格に分けて使う</text>
<text x="28" y="70" font-size="13.5" fill="#3B4A63">窒素は glutamate に集め、残った炭素骨格を代謝へ渡す</text>

<rect x="20" y="88" width="520" height="226" rx="11" fill="#F4F8FC" stroke="#AAB4C4" stroke-width="1.4"/>
<text x="36" y="116" font-size="16" font-weight="700" fill="#1E3A63">① アミノ基を glutamate へ集める</text>

<rect x="30" y="140" width="174" height="54" rx="9" fill="#FFF" stroke="#3D6B52" stroke-width="1.5"/>
<text x="117" y="162" font-size="13.5" font-weight="700" text-anchor="middle" fill="#245840">アミノ酸</text>
<text x="117" y="181" font-size="12" text-anchor="middle" fill="#3B4A63">炭素骨格 ＋ <tspan font-weight="700" fill="#A45A16">NH₂</tspan></text>
<text x="117" y="218" font-size="20" font-weight="700" text-anchor="middle" fill="#64748B">＋</text>
<rect x="30" y="232" width="174" height="50" rx="9" fill="#FFF" stroke="#2F5C87" stroke-width="1.5"/>
<text x="117" y="253" font-size="13.5" font-weight="700" text-anchor="middle" fill="#1E3A63">α-ketoglutarate</text>
<text x="117" y="271" font-size="11.8" text-anchor="middle" fill="#3B4A63">アミノ基の受け手</text>

<line x1="218" y1="211" x2="342" y2="211" stroke="#3D6B52" stroke-width="2.4" marker-start="url(#nitrogenBack)" marker-end="url(#nitrogenBack)"/>
<text x="280" y="178" font-size="13.5" font-weight="700" text-anchor="middle" fill="#245840">aminotransferase</text>
<rect x="241" y="186" width="78" height="20" rx="10" fill="#F5E9D6"/>
<text x="280" y="200" font-size="11.5" font-weight="700" text-anchor="middle" fill="#8A5A18">PLP（B6）</text>
<text x="280" y="234" font-size="11.8" text-anchor="middle" fill="#3B4A63">アミノ基転移</text>

<rect x="356" y="140" width="174" height="54" rx="9" fill="#FFF" stroke="#3D6B52" stroke-width="1.5"/>
<text x="443" y="162" font-size="13.5" font-weight="700" text-anchor="middle" fill="#245840">α-ケト酸</text>
<text x="443" y="181" font-size="12" text-anchor="middle" fill="#3B4A63">残った炭素骨格</text>
<text x="443" y="218" font-size="20" font-weight="700" text-anchor="middle" fill="#64748B">＋</text>
<rect x="356" y="232" width="174" height="50" rx="9" fill="#FFF7E8" stroke="#B4762B" stroke-width="1.5"/>
<text x="443" y="253" font-size="13.5" font-weight="700" text-anchor="middle" fill="#8A5A18">glutamate</text>
<text x="443" y="271" font-size="11.8" text-anchor="middle" fill="#3B4A63"><tspan font-weight="700" fill="#A45A16">NH₂</tspan> を受け取る</text>

<rect x="20" y="328" width="520" height="150" rx="11" fill="#F6FAF7" stroke="#91B19E" stroke-width="1.4"/>
<text x="36" y="356" font-size="16" font-weight="700" fill="#245840">② ALT・AST は、このアミノ基転移を行う</text>

<rect x="32" y="372" width="194" height="40" rx="8" fill="#FFF" stroke="#3D6B52" stroke-width="1.3"/>
<text x="129" y="397" font-size="12.5" font-weight="700" text-anchor="middle" fill="#245840">alanine ＋ α-ketoglutarate</text>
<line x1="241" y1="392" x2="319" y2="392" stroke="#3D6B52" stroke-width="2.2" marker-start="url(#nitrogenBack)" marker-end="url(#nitrogenBack)"/>
<text x="280" y="383" font-size="12" font-weight="700" text-anchor="middle" fill="#245840">ALT</text>
<rect x="334" y="372" width="194" height="40" rx="8" fill="#FFF" stroke="#3D6B52" stroke-width="1.3"/>
<text x="431" y="397" font-size="12.5" font-weight="700" text-anchor="middle" fill="#245840">pyruvate ＋ glutamate</text>

<rect x="32" y="424" width="194" height="40" rx="8" fill="#FFF" stroke="#2F5C87" stroke-width="1.3"/>
<text x="129" y="449" font-size="12.3" font-weight="700" text-anchor="middle" fill="#1E3A63">aspartate ＋ α-ketoglutarate</text>
<line x1="241" y1="444" x2="319" y2="444" stroke="#2F5C87" stroke-width="2.2" marker-start="url(#nitrogenBlueBack)" marker-end="url(#nitrogenBlueBack)"/>
<text x="280" y="435" font-size="12" font-weight="700" text-anchor="middle" fill="#1E3A63">AST</text>
<rect x="334" y="424" width="194" height="40" rx="8" fill="#FFF" stroke="#2F5C87" stroke-width="1.3"/>
<text x="431" y="449" font-size="12.3" font-weight="700" text-anchor="middle" fill="#1E3A63">oxaloacetate ＋ glutamate</text>

<rect x="20" y="492" width="520" height="184" rx="11" fill="#FFF8ED" stroke="#D3A15A" stroke-width="1.4"/>
<text x="36" y="520" font-size="16" font-weight="700" fill="#8A5A18">③ glutamate から窒素を外す</text>
<text x="36" y="542" font-size="12" fill="#3B4A63">肝臓での酸化的脱アミノと尿素への処理</text>

<rect x="30" y="572" width="128" height="50" rx="9" fill="#FFF" stroke="#B4762B" stroke-width="1.5"/>
<text x="94" y="603" font-size="14" font-weight="700" text-anchor="middle" fill="#8A5A18">glutamate</text>
<line x1="170" y1="597" x2="240" y2="597" stroke="#2F5C87" stroke-width="2.4" marker-end="url(#nitrogenArrow)"/>
<text x="205" y="571" font-size="11.5" font-weight="700" text-anchor="middle" fill="#1E3A63">glutamate</text>
<text x="205" y="585" font-size="11.5" font-weight="700" text-anchor="middle" fill="#1E3A63">dehydrogenase</text>

<circle cx="252" cy="597" r="4" fill="#2F5C87"/>
<path d="M252 597 C270 597 270 569 294 569" fill="none" stroke="#2F5C87" stroke-width="2.2" marker-end="url(#nitrogenArrow)"/>
<rect x="306" y="547" width="116" height="44" rx="8" fill="#E7EEF7" stroke="#2F5C87" stroke-width="1.4"/>
<text x="364" y="566" font-size="13" font-weight="700" text-anchor="middle" fill="#1E3A63">α-ketoglutarate</text>
<text x="364" y="582" font-size="11" text-anchor="middle" fill="#3B4A63">受け手として再利用</text>

<path d="M252 597 C270 597 270 631 294 631" fill="none" stroke="#B4762B" stroke-width="2.2" marker-end="url(#nitrogenWaste)"/>
<rect x="306" y="609" width="82" height="44" rx="8" fill="#FBEDE9" stroke="#B05A24" stroke-width="1.4"/>
<text x="347" y="637" font-size="14" font-weight="700" text-anchor="middle" fill="#8A431C">NH₃</text>
<line x1="400" y1="631" x2="432" y2="631" stroke="#B4762B" stroke-width="2.2" marker-end="url(#nitrogenWaste)"/>
<rect x="444" y="609" width="76" height="44" rx="8" fill="#FBEDE9" stroke="#B05A24" stroke-width="1.4"/>
<text x="482" y="627" font-size="13" font-weight="700" text-anchor="middle" fill="#8A431C">尿素</text>
<text x="482" y="644" font-size="10.8" text-anchor="middle" fill="#3B4A63">→ 排泄</text>
</g>
</svg>
</div>
<figcaption>アミノ酸のアミノ基は、aminotransferase によって α-ketoglutarate へ移され、glutamate に集められる。代表がALTとASTで、ALTはalanineとpyruvate、ASTはaspartateとoxaloacetateの間のアミノ基転移を触媒する。どちらも双方向に働き、PLP（vitamin B6）を必要とする。その後、glutamate dehydrogenaseが窒素をNH₃として外し、肝で尿素に変えて排泄する</figcaption>
</figure>

### 残った炭素骨格は、形によって入口が違う

アミノ基を移したあとに残る**炭素骨格**は、元のアミノ酸によって形が違います。alanineの炭素骨格はpyruvateに、aspartateの炭素骨格はoxaloacetateになります。

そのため、すべてのアミノ酸がacetyl-CoAになって同じ入口から入るわけではありません。**pyruvateになるもの、TCA回路の途中へ直接入るもの、acetyl-CoA側へ入るもの**があります。個々のアミノ酸名を暗記するより、まず「入口は一つではない」と理解できれば十分です。次の図は、その入口をまとめた地図です。

<figure class="book-figure">
<div style="overflow-x:auto">
<svg viewBox="0 0 560 760" style="display:block;width:100%;max-width:560px;margin:0 auto;height:auto;background:#fff" role="img" aria-label="アミノ酸から窒素を外した炭素骨格が、①pyruvate、②alpha-ketoglutarate、③succinyl-CoA、④fumarate、⑤oxaloacetateという糖原性の入口と、acetyl-CoAまたはacetoacetateというケト原性の入口へ分かれる。isoleucine、phenylalanine、threonine、tryptophan、tyrosineは両方に現れ、leucineとlysineだけが純粋にケト原性">
<defs>
<marker id="aaCycle" markerUnits="userSpaceOnUse" viewBox="0 0 10 10" refX="0.5" refY="5" markerWidth="9" markerHeight="9" orient="auto"><path d="M0 1 L9 5 L0 9 z" fill="#2F5C87"/></marker>
<marker id="aaIn" markerUnits="userSpaceOnUse" viewBox="0 0 10 10" refX="0.5" refY="5" markerWidth="9" markerHeight="9" orient="auto"><path d="M0 1 L9 5 L0 9 z" fill="#3D6B52"/></marker>
<marker id="aaKet" markerUnits="userSpaceOnUse" viewBox="0 0 10 10" refX="0.5" refY="5" markerWidth="9" markerHeight="9" orient="auto"><path d="M0 1 L9 5 L0 9 z" fill="#B05A24"/></marker>
</defs>
<rect x="3" y="3" width="554" height="754" rx="12" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.8"/>
<g font-family="system-ui,-apple-system,sans-serif">
<text x="28" y="42" font-size="20" font-weight="700" fill="#1E3A63">アミノ酸の炭素骨格は、6か所から入る</text>
<text x="28" y="68" font-size="13" fill="#3B4A63">先に窒素を外し、残った炭素を解糖系の出口またはTCA回路へ渡す</text>
<rect x="28" y="84" width="12" height="12" rx="3" fill="#E6F1EA" stroke="#3D6B52"/>
<text x="48" y="95" font-size="12" font-weight="700" fill="#245840">①〜⑤　糖原性の入口</text>
<rect x="172" y="84" width="12" height="12" rx="3" fill="#FBEDE9" stroke="#B05A24"/>
<text x="192" y="95" font-size="12" font-weight="700" fill="#8A431C">ケト原性の入口</text>

<rect x="24" y="122" width="164" height="102" rx="9" fill="#E6F1EA" stroke="#3D6B52" stroke-width="1.3"/>
<text x="40" y="148" font-size="13.5" font-weight="700" fill="#245840">① → pyruvate</text>
<text x="40" y="173" font-size="11.5" fill="#111827">alanine・cysteine</text>
<text x="40" y="193" font-size="11.2" fill="#111827">glycine・serine・threonine</text>
<text x="40" y="213" font-size="11.5" fill="#111827">tryptophan</text>
<line x1="188" y1="190" x2="200" y2="190" stroke="#3D6B52" stroke-width="2.2" marker-end="url(#aaIn)"/>

<rect x="210" y="174" width="140" height="34" rx="8" fill="#FFFFFF" stroke="#2F5C87" stroke-width="1.4"/>
<text x="280" y="196" font-size="13" font-weight="700" text-anchor="middle" fill="#1E3A63">pyruvate</text>
<line x1="280" y1="210" x2="280" y2="234" stroke="#2F5C87" stroke-width="2.2" marker-end="url(#aaCycle)"/>
<rect x="210" y="244" width="140" height="34" rx="8" fill="#FBEDE9" stroke="#9A3D28" stroke-width="1.4"/>
<text x="280" y="266" font-size="13" font-weight="700" text-anchor="middle" fill="#7A2F1D">acetyl-CoA</text>

<rect x="372" y="116" width="164" height="132" rx="9" fill="#FBEDE9" stroke="#B05A24" stroke-width="1.3"/>
<text x="388" y="141" font-size="12.5" font-weight="700" fill="#8A431C">→ acetyl-CoA／</text>
<text x="388" y="159" font-size="12.5" font-weight="700" fill="#8A431C">　 acetoacetate</text>
<text x="388" y="181" font-size="11.5" font-weight="700" fill="#111827">leucine・lysine</text>
<text x="388" y="200" font-size="10.5" fill="#111827">isoleucine・phenylalanine</text>
<text x="388" y="219" font-size="11" fill="#111827">threonine・tryptophan</text>
<text x="388" y="238" font-size="11.5" fill="#111827">tyrosine</text>
<path d="M390 250 Q376 261 360 261" fill="none" stroke="#B05A24" stroke-width="2.2" marker-end="url(#aaKet)"/>

<rect x="198" y="290" width="164" height="318" rx="12" fill="#F7F9FC" stroke="#AAB4C4" stroke-width="1.5"/>
<text x="280" y="314" font-size="13" font-weight="700" text-anchor="middle" fill="#1E3A63">TCA回路（簡略）</text>
<line x1="280" y1="280" x2="280" y2="318" stroke="#2F5C87" stroke-width="2.2" marker-end="url(#aaCycle)"/>

<rect x="210" y="326" width="140" height="32" rx="8" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.2"/>
<text x="280" y="347" font-size="12.5" font-weight="700" text-anchor="middle" fill="#111827">citrate</text>
<line x1="280" y1="360" x2="280" y2="376" stroke="#2F5C87" stroke-width="2" marker-end="url(#aaCycle)"/>
<rect x="210" y="384" width="140" height="32" rx="8" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.2"/>
<text x="280" y="405" font-size="12.5" font-weight="700" text-anchor="middle" fill="#111827">α-ketoglutarate</text>
<line x1="280" y1="418" x2="280" y2="434" stroke="#2F5C87" stroke-width="2" marker-end="url(#aaCycle)"/>
<rect x="210" y="442" width="140" height="32" rx="8" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.2"/>
<text x="280" y="463" font-size="12.5" font-weight="700" text-anchor="middle" fill="#111827">succinyl-CoA</text>
<line x1="280" y1="476" x2="280" y2="492" stroke="#2F5C87" stroke-width="2" marker-end="url(#aaCycle)"/>
<rect x="210" y="500" width="140" height="32" rx="8" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.2"/>
<text x="280" y="521" font-size="12.5" font-weight="700" text-anchor="middle" fill="#111827">fumarate</text>
<line x1="280" y1="534" x2="280" y2="550" stroke="#2F5C87" stroke-width="2" marker-end="url(#aaCycle)"/>
<rect x="210" y="558" width="140" height="32" rx="8" fill="#FFFFFF" stroke="#8A97AC" stroke-width="1.2"/>
<text x="280" y="579" font-size="12.5" font-weight="700" text-anchor="middle" fill="#111827">oxaloacetate</text>
<path d="M210 574 Q178 455 210 342" fill="none" stroke="#2F5C87" stroke-width="2" marker-end="url(#aaCycle)"/>

<rect x="372" y="344" width="164" height="80" rx="9" fill="#E6F1EA" stroke="#3D6B52" stroke-width="1.2"/>
<text x="388" y="367" font-size="12.5" font-weight="700" fill="#245840">② → α-ketoglutarate</text>
<text x="388" y="388" font-size="11.2" fill="#111827">arginine・glutamate</text>
<text x="388" y="407" font-size="10.8" fill="#111827">glutamine・histidine・proline</text>
<line x1="372" y1="400" x2="360" y2="400" stroke="#3D6B52" stroke-width="2.2" marker-end="url(#aaIn)"/>

<rect x="372" y="434" width="164" height="80" rx="9" fill="#E6F1EA" stroke="#3D6B52" stroke-width="1.2"/>
<text x="388" y="457" font-size="12.5" font-weight="700" fill="#245840">③ → succinyl-CoA</text>
<text x="388" y="478" font-size="11.2" fill="#111827">isoleucine・methionine</text>
<text x="388" y="497" font-size="11.5" fill="#111827">threonine・valine</text>
<path d="M372 477 Q366 458 360 458" fill="none" stroke="#3D6B52" stroke-width="2.2" marker-end="url(#aaIn)"/>

<rect x="24" y="478" width="164" height="70" rx="9" fill="#E6F1EA" stroke="#3D6B52" stroke-width="1.2"/>
<text x="40" y="501" font-size="12.5" font-weight="700" fill="#245840">④ → fumarate</text>
<text x="40" y="523" font-size="11" fill="#111827">aspartate・phenylalanine</text>
<text x="40" y="541" font-size="11.5" fill="#111827">tyrosine</text>
<path d="M188 512 Q194 516 200 516" fill="none" stroke="#3D6B52" stroke-width="2.2" marker-end="url(#aaIn)"/>

<rect x="24" y="556" width="164" height="58" rx="9" fill="#E6F1EA" stroke="#3D6B52" stroke-width="1.2"/>
<text x="40" y="579" font-size="12.5" font-weight="700" fill="#245840">⑤ → oxaloacetate</text>
<text x="40" y="601" font-size="11.5" fill="#111827">asparagine・aspartate</text>
<path d="M188 585 Q194 574 200 574" fill="none" stroke="#3D6B52" stroke-width="2.2" marker-end="url(#aaIn)"/>

<rect x="24" y="630" width="512" height="40" rx="9" fill="#E6F1EA"/>
<text x="280" y="655" font-size="12.5" font-weight="700" text-anchor="middle" fill="#245840">①〜⑤の入口 → oxaloacetate を経て、糖新生で glucose に戻せる</text>
<rect x="24" y="682" width="512" height="50" rx="9" fill="#FBEDE9"/>
<text x="280" y="703" font-size="12.5" font-weight="700" text-anchor="middle" fill="#8A431C">橙の入口 → acetyl-CoA／acetoacetate 側</text>
<text x="280" y="722" font-size="12" text-anchor="middle" fill="#7A2F1D">ここからは、glucoseの材料にできない</text>
</g>
</svg>
</div>
<figcaption>アミノ酸は窒素を外した後、炭素骨格の形に応じて別々の位置から代謝の本流へ入る。① pyruvate、② α-ketoglutarate、③ succinyl-CoA、④ fumarate、⑤ oxaloacetate は糖原性の入口。橙の acetyl-CoA・acetoacetate 側はケト原性の入口。両方に名前があるアミノ酸は、糖原性とケト原性の両方の性質を持つ</figcaption>
</figure>

### 最後に、「糖に戻れるか」で二つに分ける

図の緑色の①〜⑤は、**pyruvateまたはTCA回路の中間体になる入口**です。ここへ入った炭素はoxaloacetateへつながり、肝臓などでは糖新生によってglucoseの材料にできます。このような炭素を持つアミノ酸を、**糖原性（glucogenic）**と呼びます。

一方、橙色の **acetyl-CoA・acetoacetate** 側へ入るものが、**ケト原性（ketogenic）**です。**ケト原性の炭素は、TCA回路でエネルギー産生に使うことはできますが、glucoseの材料にはできません。**

acetyl-CoAは、すでに回路内にあるoxaloacetateと結びついてTCA回路へ入ります。しかしacetyl-CoAとして2個の炭素が入っても、回路から2個の炭素がCO₂として出るため、**TCA回路が一周してもoxaloacetateの量は増えません。**さらにPDHの反応は不可逆なので、acetyl-CoAからpyruvateへ戻ることもできません。したがって、**acetyl-CoA側へ入った炭素はglucoseの材料にできません**（→ [[fatty-acid-oxidation]]）。

なお、ミトコンドリア内のacetyl-CoAは、**citrateにして細胞質へ出し、ATP-citrate lyase（ACLY）で再びacetyl-CoAに戻す**ことができます。これがcitrate shuttleです。ただし、これはacetyl基を脂肪酸やコレステロールの合成場所へ運ぶ仕組みであり、**acetyl-CoAをpyruvateやglucoseへ戻す反応ではありません**（→ [[fatty-acid-oxidation]]§2「余った糖は、脂肪酸として貯蔵される」）。

アミノ酸のなかには、糖原性とケト原性の両方の経路を持つものもあります。純粋にケト原性なのは **leucineとlysine** の2つです。この分類も、まずは名前を暗記するより、**「pyruvate・TCA中間体側なら糖の材料になれる／acetyl-CoA側からは糖へ戻れない」**という境界が分かれば十分です。

§3では、TCA回路の中間体を脂質・アミノ酸・核酸などの材料として**回路から取り出しました**。この節では反対に、アミノ酸の炭素骨格をpyruvateやTCA回路の中間体として**代謝へ入れました**。同じ中間体の名前が何度も出てくるのは、そこが出口にも入口にもなるからです。

> **この節のまとめ：**アミノ酸を使うときは、まず窒素と炭素骨格に分ける。窒素は尿素として捨て、炭素骨格は形に合う入口から代謝へ入る。その入口によって、糖の材料に戻れるかどうかが決まる。

## この章の到達点

1. TCA回路は、**acetyl-CoAの炭素をCO₂まで酸化し、その途中で電子をNADHとFADH₂へ渡す回路**です。一周するとoxaloacetateへ戻り、次のacetyl-CoAを受け取ります。acetyl-CoAは、糖・脂肪酸・一部のアミノ酸から作られます。
2. 糖からできたpyruvateがTCA回路へ進むには、まず**PDHによってacetyl-CoAへ変換される**必要があります。PDHの反応には、**TPP（B1）・lipoate・CoA（B5）・FAD（B2）・NAD⁺（B3）**とMg²⁺が必要です。一方、脂肪酸からできたacetyl-CoAはPDHを通りません。
3. PDHは、**脱リン酸化されると活性が上がり、リン酸化されると活性が下がります。**ATPが使われてADPが増えたとき、pyruvateが十分にあるとき、筋収縮でCa²⁺が増えたときは、PDHの活性が上がる方向へ調節されます。反対に、ミトコンドリア内にATP・NADH・acetyl-CoAが多いと、PDH kinaseがPDHをリン酸化して活性を下げます。こうして、**糖由来の炭素をTCA回路へ入れる量が、ATPを作る必要性に合わせて調節されます。**
4. acetyl-CoA 1分子が一周すると、**3 NADH・1 FADH₂・1 GTP・2 CO₂**が生じます。TCA回路で直接できるATP相当量はGTP 1分子です。ATPの大半は、NADHとFADH₂が運ぶ電子を使って、電子伝達系で作られます。
5. TCA回路の中間体は、**脂質・アミノ酸・核酸・hemeなどを合成する材料**にもなります。材料として抜けた中間体は、pyruvate carboxylaseやglutaminolysisなどの**anaplerosis（補充反応）**で補われます。エネルギー産生と合成材料の供給を担うため、TCA回路は**amphibolic**な回路です。
6. アミノ酸を使うときは、窒素を含む部分と炭素骨格に分けます。窒素はglutamateに集め、最終的に尿素として排泄します。炭素骨格は、その形に応じてpyruvate、TCA回路の中間体、acetyl-CoAなどになります。**pyruvate・TCA回路の中間体になればglucoseの材料にできますが、acetyl-CoA側からはglucoseへ戻れません。**ALT・ASTは、この最初のアミノ基転移を行う酵素です。

> **低酸素時の補足：**細胞への酸素供給が需要に追いつかないときは、HIF-1αがPDK1を増やしてPDHの活性を下げます。これは、通常のエネルギー需要による調節とは別に働く、低酸素への適応です。

> [[electron-transport]]では、TCA回路で生じた **NADH・FADH₂** が、電子を**電子伝達系**へ渡す過程を見ます。電子は最後にO₂へ渡されます。
