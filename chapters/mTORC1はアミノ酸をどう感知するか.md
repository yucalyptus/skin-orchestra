---
id: mtorc1
title: mTORC1――タンパク質合成を調節する仕組み
kind: basic
status: approved
published: 2026-08-28
updated: 2026-09-13
history:
  - {date: 2026-09-13, note: 構成を維持して説明の順序・見出し・図の説明を整理}
  - {date: 2026-08-28, note: 初公開}
---

> アミノ酸は、タンパク質の材料であると同時に、**「材料がある」**と細胞へ伝える情報でもあります。この章では、**mTORC1**がアミノ酸・成長刺激・エネルギーの状態を受け取り、タンパク質合成を調節する仕組みを見ます。
>
> **先に読んでおく章**：アミノ酸の働きと輸送体（→ [[amino-acids]]）／ATPとエネルギー代謝（→ [[atp]]）


## この章の一言

> mTORC1 は、**アミノ酸・成長刺激・エネルギー**の状態をまとめて受け取り、タンパク質合成と autophagy の強さを調節します。


## 1　mTORC1は、三つの情報をまとめる

**mTORC1（mechanistic target of rapamycin complex 1）**は、タンパク質合成を調節する酵素複合体です。活性が高まるとタンパク質合成が進み、autophagy は抑えられます。活性が下がると、タンパク質合成は低下し、autophagy が進みやすくなります（→ [[autophagy]]、[[ampk-mtor]]）。

mTORC1は、主に三つの情報を受け取ります。

- **アミノ酸**：mTORC1を、働く場所であるlysosomeの表面へ移動させます。
- **インスリンやIGF-1**：lysosomeの表面で、mTORC1の活性を高めます。
- **細胞内のエネルギー**：不足すると AMPK が働き、mTORC1 を抑えます（→ [[ampk-mtor]]）。


## 2　アミノ酸の量を感知するセンサー

細胞には、特定のアミノ酸や、その代謝物を感知するセンサータンパク質があります。leucineやarginineは、対応するセンサーに直接結合します。**methionineは、そこから作られるSAM（S-adenosylmethionine、S-アデノシルメチオニン）を介して感知されます**（PMID 29123071）。

| 感知するもの | センサー | 測り方 |
|---|---|---|
| **leucine** | Sestrin2 | leucine が直接結合する |
| **arginine** | CASTOR1 | arginine が直接結合する |
| **SAM（methionine から作られる）** | SAMTOR | methionine そのものではなく、そこから作られる SAM が結合する |

センサーがアミノ酸の量を感知すると、その情報がいくつかのタンパク質を介して**Rag**へ伝わります。

## 3　Ragが移し、Rhebが活性を高める

**RagとRhebは、GTPとGDPの結合状態に応じて働きが変わる小型GTPaseです。**いずれもmTORC1を調節しますが、役割が異なります。

### Rag：mTORC1をlysosome表面へ呼ぶ

Ragはlysosomeの表面にあります。アミノ酸センサーから「材料がある」という情報が届くとRagが活性型になり、細胞質にあるmTORC1を**lysosomeの表面へ呼び寄せます**。

### Rheb：呼び寄せられたmTORC1を活性化する

インスリンやIGF-1の刺激は、細胞内の経路を介して**Rhebを活性型にします**。活性型Rhebはlysosomeの表面で、Ragが呼び寄せたmTORC1の活性を高めます。

つまり、**RagはmTORC1を働く場所へ呼び、RhebはそこでmTORC1を活性化します。**二つの情報がlysosomeの表面でそろうと、mTORC1が働きやすくなります。エネルギーが不足しているときは、AMPKがmTORC1を抑えます。

<figure class="book-figure">
<div style="overflow-x:auto">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 650" style="display:block;width:100%;max-width:900px;margin:0 auto;height:auto;background:#fff" role="img" aria-label="アミノ酸センサーから情報を受け取ったRagがmTORC1をlysosome表面へ呼び寄せる。インスリンとIGF-1は細胞内経路を介してRhebを活性型にし、lysosome表面でmTORC1の活性を高める。エネルギー不足ではAMPKがmTORC1を抑える">
<defs>
<marker id="ragMoveArrow" markerUnits="userSpaceOnUse" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="9" markerHeight="9" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="#245B89"/></marker>
<marker id="rhebActArrow" markerUnits="userSpaceOnUse" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="9" markerHeight="9" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="#D6602D"/></marker>
<marker id="outcomeArrow" markerUnits="userSpaceOnUse" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="9" markerHeight="9" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="#3F8A50"/></marker>
</defs>

<text x="450" y="38" font-size="25" font-weight="700" text-anchor="middle" fill="#173B61">二つの情報がlysosome表面で合流する</text>

<!-- amino-acid input -->
<rect x="40" y="62" width="380" height="165" rx="18" fill="#F3F8FD" stroke="#78A3C8" stroke-width="2.5"/>
<text x="230" y="96" font-size="21" font-weight="700" text-anchor="middle" fill="#1E4F7D">① アミノ酸が十分にある</text>
<text x="230" y="130" font-size="17" text-anchor="middle" fill="#405F79">センサーが「材料がある」と感知</text>
<line x1="230" y1="142" x2="230" y2="158" stroke="#245B89" stroke-width="3.5" marker-end="url(#ragMoveArrow)"/>
<rect x="115" y="168" width="230" height="43" rx="20" fill="#DDEBFA" stroke="#3974A8" stroke-width="2"/>
<text x="230" y="196" font-size="18" font-weight="700" text-anchor="middle" fill="#173B61">Ragが活性型になる</text>

<!-- insulin input -->
<rect x="480" y="62" width="380" height="165" rx="18" fill="#FEF6F0" stroke="#D8936D" stroke-width="2.5"/>
<text x="670" y="96" font-size="21" font-weight="700" text-anchor="middle" fill="#A3431E">② インスリン・IGF-1</text>
<text x="670" y="130" font-size="17" text-anchor="middle" fill="#80503B">細胞内の経路を介して伝わる</text>
<line x1="670" y1="142" x2="670" y2="158" stroke="#D6602D" stroke-width="3.5" marker-end="url(#rhebActArrow)"/>
<rect x="555" y="168" width="230" height="43" rx="20" fill="#FBE8DD" stroke="#D6602D" stroke-width="2"/>
<text x="670" y="196" font-size="18" font-weight="700" text-anchor="middle" fill="#A3431E">Rhebが活性型になる</text>

<text x="450" y="263" font-size="19" font-weight="700" text-anchor="middle" fill="#536878">lysosomeの表面で、二つの情報がそろう</text>

<!-- mTORC1 before recruitment -->
<text x="125" y="298" font-size="15" text-anchor="middle" fill="#607487">細胞質</text>
<rect x="55" y="311" width="140" height="54" rx="24" fill="#DDEBFA" fill-opacity="0.65" stroke="#3974A8" stroke-width="2.5" stroke-dasharray="6 5"/>
<text x="125" y="345" font-size="19" font-weight="700" text-anchor="middle" fill="#173B61">mTORC1</text>

<!-- lysosome -->
<path d="M52 478 Q450 402 848 478 L848 535 L52 535 Z" fill="#F7EAD4" stroke="#C99D5A" stroke-width="2.8"/>
<text x="735" y="520" font-size="20" font-weight="700" text-anchor="middle" fill="#754E24">lysosome</text>

<!-- Rag on lysosome -->
<path d="M230 227 C230 292 245 365 285 414" fill="none" stroke="#245B89" stroke-width="4" marker-end="url(#ragMoveArrow)"/>
<ellipse cx="305" cy="435" rx="58" ry="31" fill="#DDEBFA" stroke="#3974A8" stroke-width="2.5"/>
<text x="305" y="431" font-size="18" font-weight="700" text-anchor="middle" fill="#173B61">Rag</text>
<text x="305" y="451" font-size="14" text-anchor="middle" fill="#173B61">lysosome表面</text>

<!-- recruitment of mTORC1 -->
<path d="M195 338 C265 326 334 338 385 372" fill="none" stroke="#245B89" stroke-width="4" stroke-dasharray="8 6" marker-end="url(#ragMoveArrow)"/>
<rect x="227" y="294" width="134" height="29" rx="8" fill="#FFFFFF" fill-opacity="0.94"/>
<text x="294" y="316" font-size="16" font-weight="700" text-anchor="middle" fill="#245B89">Ragが呼び寄せる</text>
<path d="M349 418 C372 401 387 393 401 391" fill="none" stroke="#245B89" stroke-width="4" marker-end="url(#ragMoveArrow)"/>

<!-- mTORC1 at lysosome -->
<rect x="385" y="354" width="150" height="67" rx="28" fill="#DDEFD9" stroke="#3F8A50" stroke-width="3"/>
<text x="460" y="382" font-size="20" font-weight="700" text-anchor="middle" fill="#256436">mTORC1</text>
<text x="460" y="405" font-size="16" font-weight="700" text-anchor="middle" fill="#256436">lysosome表面</text>

<!-- Rheb on lysosome -->
<path d="M670 227 C670 292 655 365 622 414" fill="none" stroke="#D6602D" stroke-width="4" marker-end="url(#rhebActArrow)"/>
<ellipse cx="615" cy="435" rx="58" ry="31" fill="#FBE8DD" stroke="#D6602D" stroke-width="2.5"/>
<text x="615" y="431" font-size="18" font-weight="700" text-anchor="middle" fill="#A3431E">Rheb</text>
<text x="615" y="451" font-size="14" text-anchor="middle" fill="#A3431E">活性型</text>
<path d="M568 418 C545 401 530 393 517 391" fill="none" stroke="#D6602D" stroke-width="4" marker-end="url(#rhebActArrow)"/>
<text x="628" y="342" font-size="16" font-weight="700" text-anchor="middle" fill="#D6602D">活性を高める</text>

<!-- outcome -->
<line x1="460" y1="422" x2="460" y2="552" stroke="#3F8A50" stroke-width="4" marker-end="url(#outcomeArrow)"/>
<rect x="282" y="558" width="356" height="43" rx="20" fill="#E3F2E5" stroke="#5B9B66" stroke-width="2"/>
<text x="460" y="586" font-size="18" font-weight="700" text-anchor="middle" fill="#256436">タンパク質・脂質などの合成へ</text>

<!-- AMPK brake -->
<rect x="125" y="615" width="650" height="29" rx="13" fill="#F2F3F5"/>
<text x="450" y="635" font-size="15" font-weight="700" text-anchor="middle" fill="#6B5555">エネルギー不足 → AMPKが働く → mTORC1を抑える</text>
</svg>
</div>
<figcaption>アミノ酸の情報で活性型になったRagは、mTORC1をlysosome表面へ呼び寄せます。インスリン・IGF-1は細胞内経路を介してRhebを活性型にし、Ragが呼び寄せたmTORC1の活性を高めます。</figcaption>
</figure>

## 4　食後は「作る」、空腹時は「分解して再利用する」

食事をすると、血中のglucoseとアミノ酸が増え、インスリンが分泌されます。細胞にアミノ酸が届き、インスリンの刺激も加わると、mTORC1の活性は高まりやすくなります。mTORC1は、タンパク質や脂質を**作る方向**へ代謝を進めます。これは成長や組織の修復に必要な、正常な反応です。

空腹の時間が続くと、食事から入るアミノ酸とインスリンの刺激が減ります。細胞内のエネルギーが不足すればAMPKも働き、mTORC1の活性は下がります。するとタンパク質合成が抑えられ、autophagyが始まりやすくなります。

autophagyは、細胞内の成分を分解して材料を再利用する仕組みです（→ [[autophagy]]）。食事や運動に応じて、合成と再利用のどちらが優先されるかが変わります。その調節を[[ampk-mtor]]で扱います。

<figure class="book-figure">
<div style="overflow-x:auto">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 390" style="display:block;width:100%;max-width:820px;margin:0 auto;height:auto;background:#fff" role="img" aria-label="食後はアミノ酸とインスリンが増えてmTORC1の活性が高まり、タンパク質や脂質の合成が進む。空腹時はmTORC1の活性が下がり、autophagyによる分解と再利用が進みやすくなる">
<defs>
<marker id="fedArrow" markerUnits="userSpaceOnUse" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="9" markerHeight="9" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="#B26728"/></marker>
<marker id="fastArrow" markerUnits="userSpaceOnUse" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="9" markerHeight="9" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="#356C87"/></marker>
</defs>

<text x="410" y="32" font-size="24" font-weight="700" text-anchor="middle" fill="#173B61">食後と空腹時で、mTORC1の活性が切り替わる</text>

<rect x="25" y="58" width="370" height="270" rx="18" fill="#FFF8EF" stroke="#D4A05C" stroke-width="2.5"/>
<rect x="45" y="76" width="330" height="42" rx="11" fill="#F6E3C8"/>
<text x="210" y="104" font-size="21" font-weight="700" text-anchor="middle" fill="#8A511E">食後</text>
<rect x="64" y="140" width="292" height="44" rx="20" fill="#FFF" stroke="#D4A05C" stroke-width="2"/>
<text x="210" y="168" font-size="17" font-weight="700" text-anchor="middle" fill="#69431E">アミノ酸・インスリンが増える</text>
<line x1="210" y1="185" x2="210" y2="210" stroke="#B26728" stroke-width="4" marker-end="url(#fedArrow)"/>
<rect x="115" y="216" width="190" height="48" rx="22" fill="#F3D8B3" stroke="#B26728" stroke-width="2.5"/>
<text x="210" y="247" font-size="19" font-weight="700" text-anchor="middle" fill="#754111">mTORC1 活性 ↑</text>
<text x="210" y="292" font-size="17" font-weight="700" text-anchor="middle" fill="#754111">タンパク質・脂質の合成 ↑</text>
<text x="210" y="316" font-size="16" text-anchor="middle" fill="#754111">autophagy ↓</text>

<rect x="425" y="58" width="370" height="270" rx="18" fill="#F2F8FB" stroke="#74A2B7" stroke-width="2.5"/>
<rect x="445" y="76" width="330" height="42" rx="11" fill="#DCECF3"/>
<text x="610" y="104" font-size="21" font-weight="700" text-anchor="middle" fill="#285D75">空腹時</text>
<rect x="464" y="132" width="292" height="60" rx="20" fill="#FFF" stroke="#74A2B7" stroke-width="2"/>
<text x="610" y="157" font-size="17" font-weight="700" text-anchor="middle" fill="#285D75">アミノ酸・インスリンが減る</text>
<text x="610" y="180" font-size="15" text-anchor="middle" fill="#285D75">エネルギー不足では AMPK ↑</text>
<line x1="610" y1="193" x2="610" y2="214" stroke="#356C87" stroke-width="4" marker-end="url(#fastArrow)"/>
<rect x="515" y="220" width="190" height="48" rx="22" fill="#D6E8F0" stroke="#356C87" stroke-width="2.5"/>
<text x="610" y="251" font-size="19" font-weight="700" text-anchor="middle" fill="#214F65">mTORC1 活性 ↓</text>
<text x="610" y="293" font-size="17" font-weight="700" text-anchor="middle" fill="#214F65">autophagy ↑</text>
<text x="610" y="317" font-size="16" text-anchor="middle" fill="#214F65">分解して、材料を再利用する</text>

<rect x="95" y="346" width="630" height="34" rx="9" fill="#EEF2F7"/>
<text x="410" y="369" font-size="17" font-weight="700" text-anchor="middle" fill="#173B61">状態に応じて、合成と分解・再利用を切り替える</text>
</svg>
</div>
<figcaption>食後は合成が進み、空腹時には分解と再利用が進みやすくなります。mTORC1は、その切り替えを調節します。</figcaption>
</figure>

### 合成の開始を調節するS6Kと4E-BP1

mTORC1の活性が高まると、**S6K**と**4E-BP1**（細胞内でタンパク質合成の開始を調節するタンパク質）を介して、**翻訳**（mRNAの配列に従ってタンパク質を作る過程）が進みます。

最終的なタンパク質の量は、遺伝子の転写、翻訳、ER内での加工、細胞外への分泌、その後の成熟によって決まります。mTORC1は、そのうち主に翻訳を調節します。collagenも、これらの段階を経て作られます（→ [[fibroblast-collagen]]）。

## 5　この仕組みが関係するもの

インスリンや IGF-1 から mTORC1 へ伝わる経路は、皮膚の代謝や加齢変化にも関係します。

- sebocyte における脂質合成（→ [[sebum]]）
- 加齢に伴う栄養感知の変化と、mTOR・AMPK の調節（→ [[ampk-mtor]]、[[hallmarks-of-aging]]）
- mTOR を標的とする介入の評価（→ [[senolytics]]）

ただし、細胞内でこの経路が変化することと、ヒトの皮膚で美容効果が得られることは別です（→ 巻頭「本教材が守る切り分け」）。

::: column ラパヌイ島の土から、ロンジェビティ研究へ
20世紀半ばは、世界各地の土や植物を採取し、そこにいる微生物が作る物質から薬の候補を探す研究が盛んでした。自然界から薬の種を探す研究者は、**drug hunter（ドラッグハンター）**とも呼ばれます。

1964年、カナダの調査隊がEaster Island（現地名**Rapa Nui、ラパヌイ島**）で土壌を採取しました。そこから分離された放線菌 *Streptomyces hygroscopicus* が作る抗真菌物質は、島の名前にちなんで**rapamycin**と名づけられました。**rapalog**は、rapamycinをもとに作られた類似薬の総称です。

rapamycinには、免疫や細胞増殖を抑える作用も見つかりました。開発が中断されたとき、研究者Suren Sehgalは廃棄予定だったrapamycin産生菌を自宅の冷凍庫に保存しました。その後研究は再開され、1999年にrapamycinは**sirolimus**という一般名で、腎移植後の拒絶反応を防ぐ免疫抑制薬としてFDAに承認されました。

その作用を調べる過程で見つかった標的が**target of rapamycin（TOR）**です。哺乳類のTORを含む複合体の一つがmTORC1です。2009年にrapamycinがマウスの寿命を延ばすことが報告され、ロンジェビティ研究でも注目されるようになりました。ただし、**ヒトの寿命を延ばすことはまだ証明されていません。**現在のrapamycinは免疫抑制薬であり、健康な人への抗老化目的の使用は研究段階です（→ [[senolytics]]）。

この発見の物語は、Donald R. KirschとOgi Ogasの『**新薬の狩人たち――成功率0.1％の探求**』（寺町朋子訳、早川書房、2018年）でも紹介されています。2021年の文庫版は『**新薬という奇跡――成功率0.1％の探求**』に改題されています。

**この本は、私がとても好きな一冊です。**薬の歴史だけでなく、偶然を見逃さず、失敗しても手放さず、何年も研究をつないだ人たちの情熱が伝わってきます。薬は化学物質であると同時に、研究者たちの執念と時間の積み重ねから生まれたものだと感じさせてくれる、おすすめの本です。
:::


## この章の到達点

1. mTORC1 は、**アミノ酸・成長刺激・エネルギー**の状態を受け取り、タンパク質合成と autophagy を調節する。
2. アミノ酸が十分にあると、**Rag** が mTORC1 を lysosome 表面へ移動させる。
3. インスリンやIGF-1などの成長刺激は、mTORC1の活性を高める。エネルギーが不足すると、**AMPK**がmTORC1を抑える。
4. mTORC1は **S6K・4E-BP1**を介して翻訳を促し、autophagyを抑える。最終的なタンパク質量には、転写・加工・分泌・成熟も影響する。

> [[autophagy]]では、細胞内の古い成分を分解し、材料として再利用する仕組みを見ます。mTORC1 の活性が高いと autophagy は抑えられ、mTORC1 の活性が下がると始まりやすくなります。collagen が作られる過程は[[fibroblast-collagen]]で扱います。
