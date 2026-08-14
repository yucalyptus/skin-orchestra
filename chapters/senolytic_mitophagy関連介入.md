---
id: senolytics
title: senolytic・mitophagy関連介入
kind: applied
status: draft
---

> dasatinib + quercetin、fisetin、外用rapamycin、urolithin A、spermidine。これらは「老化細胞を除く」「ミトファジーを促す」という説明で研究され、一部はサプリメントとして販売されています。この章では、それぞれが**どこまで示されていて、どこから先が空欄なのか**を並べます。

**この章の前提**：細胞老化とSASP（→ [[senescence]]）／ミトコンドリア品質管理とmitophagy（→ [[mito-quality-control]]）／両者の関係（→ [[mito-dysfunction]]）／mTORC1（→ [[mtorc1]]）／オートファジー（→ [[autophagy]]）

## この章の一言

> 老化細胞やmitophagyを狙う介入は、**動物と初期臨床の段階にあります。**
>
> だから成分ごとの効能ではなく、**各介入が証拠の階段のどこまで登っているか**で並べます。段を飛ばして語らないことが、この章の原則です。

![証拠の階段（①分子機序 ②培養細胞 ③動物モデル ④ヒトで標的が動くtarget engagement ⑤ヒト臨床アウトカム ⑥長期安全性・疾患予防・美容効果）に、各介入が今どこまで登っているかを旗で示した図。senolytic D+Qは4段目（小規模ヒト試験で老化細胞マーカー低下まで）、rapamycin/rapalogは4段目（一部ヒト皮膚での探索試験あり）、urolithin Aは4段目（ヒト筋で分子指標と一部持久力）、spermidineは3段目（動物では強いがヒト臨床は限定的）。vitamin Dだけは別枠で、欠乏是正は5段目・不確実性は低いが、longevity上乗せは3〜4段目・不確実性は高い](figures/senolytics_senolytic_mitophagy関連介入.png)

> 各介入がどの段にあるかが、この章の見取り図です。**どれも4段目前後で止まっていて、5段目（ヒトの臨床アウトカム）と6段目（美容領域での効果）が空欄**。空欄があること自体は珍しくありません。問題は、空欄を埋まっているかのように語ることです。

## 1　なぜ「どこまで来ているか」で並べるのか

[[mito-dysfunction]]で、細胞老化とミトコンドリア機能不全は別の現象で、臨床の線維芽細胞をどちらの型かに分ける手段もまだない、というところまで来ました。その続きがこの章です。**型で患者を分けられない以上、「この人にはsenolytic、この人にはmitophagy促進」という選び方は、いまの知見では成り立ちません。** 残るのは、介入ごとに何がどこまで示されたかを見ることだけです。

その前に、混同される二つの語を分けておきます。

![左のsenolyticは老化細胞が依存するSCAP（BCL-2/BCL-xL・XIAP・MCL-1などの抗アポトーシス生存経路）を一時的に弱めて選択的アポトーシスを誘導し、細胞数そのものを減らす（例：D+Q）。右のsenomorphicは殺さずにmTORC1・NF-κBを調節してSASP転写と分泌を抑え、老化細胞の数は残る（例：rapamycin/rapalog）。中央に「目標は同じ（SASPを介した慢性炎症の低減）が方法＝作用点は異なる」。下段は結果をp16/p21陽性細胞数・SASP因子・組織機能・臨床症状・長期安全性の5指標に分けて評価し、単一マーカーの減少だけで「除去できた」と断定しないこと](figures/senolytics_senolyticとsenomorphic.png)

| 語 | 何をするか | 押さえどころ |
|---|---|---|
| **senolytic** | 老化細胞そのものをアポトーシスへ誘導し、数を減らす | 老化細胞は SCAP（senescent cell anti-apoptotic pathway：BCL-2 family、PI3K/AKT、チロシンキナーゼ系など）に依存して生き延びる。そこを一時的に外すと死ぬ。例：D+Q、fisetin |
| **senomorphic** | 殺さずに SASP（有害な分泌）を抑える | 細胞数は変わらない。mTORC1・NF-κB を介して分泌側を鎮める。例：rapamycin、metformin。より広く老化進行を遅らせる薬は geroprotector とも呼ばれる |

> ★よくある混同：「mTORC1を抑えるsenolyticの代表＝ラパマイシン」という言い方がありますが、**不正確**です。ラパマイシンは老化細胞を殺しません。mTORC1を抑えてSASPを鎮め、オートファジーを促す senomorphic / geroprotector です。数を減らすのか、分泌を抑えるのかで、期待できる効果も安全性の論点も変わります。

## 2　senolytic：D+Q と fisetin

dasatinib + quercetin（D+Q）が二剤の組み合わせなのは、**単剤ですべての老化細胞に効く薬がないから**です。dasatinibは老化した preadipocyte を、quercetinは老化した血管内皮細胞をよく殺す、というように効く細胞種が薬ごとに違うため、標的の異なる二剤を併用します。「老化細胞」がひとつの均質な集団ではないことの裏返しでもあります（→ [[senescence]]）。

投与設計も他の薬と違います。老化細胞が再び蓄積するには時間がかかるので、血中濃度を維持し続ける必要がなく、**短期間だけ投与して休む（intermittent dosing）**という考え方が取られます。

どこまで来ているかを段ごとに分けます。

- **動物（3段目）**：24〜27か月齢のマウスへの間欠投与で、投与後の生存期間が約36%延長し、身体機能も改善しました。強いデータですが、マウスの話です。
- **ヒトの target engagement（4段目）**：糖尿病性腎症患者9例のオープンラベル試験で、3日間の投与後に皮下脂肪組織のp16/p21陽性細胞とSA-β-gal活性が低下し、**表皮のp16/p21陽性細胞も減少**しました。経口senolyticがヒトの皮膚で老化細胞マーカーを動かした報告は、いまのところここまでです。ただし対照群がなく、9例、評価は投与11日後の一点のみです。
- **ヒトの臨床アウトカム（5段目）**：特発性肺線維症14例のオープンラベル試験で6分間歩行距離・歩行速度などが改善しましたが、非盲検・対照なしで、肺機能は不変でした。
- **皮膚・美容（6段目）**：空欄です。老化細胞マーカーが動いた先に、しわ・ハリ・色調といった外見の改善が続いたというヒトのデータはありません。

安全性も切り分けが要ります。dasatinibは日本では慢性骨髄性白血病とPh⁺ALLにのみ承認されたチロシンキナーゼ阻害薬で、骨髄抑制・胸水などの副作用があります。BCL-2/BCL-xL阻害薬 navitoclax は senolytic 活性を持つ一方で血小板減少を起こします。**「老化細胞だけを狙う」ことと「他の細胞に影響しない」ことは同じではありません。** fisetin は食品にも含まれるフラボノイドで、毒性の低さから臨床試験が進んでいますが、有効性の結論は出ていません。

## 3　senomorphic：rapamycin と mTORC1

![上段はrapamycinがFKBP12と複合体を作ってmTORC1を阻害し、S6K/4E-BP1の翻訳促進シグナルが下がることでタンパク質合成・細胞増殖が減り、autophagyが促進側へ、SASP産生が低下側へ傾く対比（活性化時と抑制時の2枚）。中段は皮膚での仮説的な経路（SASP低下→p16などの老化関連指標の低下→表皮分化の恒常性→基底膜・ECMの維持）で、点線＝仮説であることが明示されている。下段はヒト皮膚の探索的試験を読むポイント（小規模、左右またはプラセボ比較、組織・分子指標が主評価、外観は二次的、再現性と長期安全性）と想定リスク（免疫抑制・創傷治癒の遅延・代謝・感染）](figures/senolytics_rapamycin_mTORC1.png)

**rapamycin（sirolimus）** とラパログ（everolimus など）は、FKBP12 と複合体を作って mTORC1 を阻害します（→ [[mtorc1]]）。mTORC1が下がるとオートファジーが誘導され（→ [[autophagy]]）、SASPの産生が抑えられる方向に傾く——これが「殺さずに分泌を抑える」作用の分子的な経路です。

- **動物（3段目）は、この分野で最も強い部類のデータ**です。遺伝的背景が均一でないマウスに、しかも**600日齢という中高年後期から**投与しても、残存寿命の中央値がメスで14%・オスで9%延びました。3施設で同時に実施された試験です。酵母・線虫・ショウジョウバエでも一貫しており、老化研究のなかで再現性の高い介入です。
- **ヒト皮膚（4段目）**：**外用**ラパマイシンの探索的な split-body 試験で、6〜8か月の塗布後に手背皮膚の **p16 低下（P=0.008）と collagen VII 増加（P=0.0077）**が報告されました。血中濃度は検出限界未満で、全身曝露はありません。ただし36例が登録され完遂は17例、組織を解析できたのは8例です。**主要評価項目を事前に定めていない探索的デザイン**であり、外見の評価は付随的です。
- **全身投与は話の重さが違う**：rapamycin/ラパログは臓器移植や一部の腫瘍で使われる**免疫抑制薬**です。感染・創傷治癒遅延・代謝への影響があり、前臨床の魅力だけで美容目的の全身投与を正当化することはできません。日本で承認されている外用sirolimusゲルも、適応は結節性硬化症に伴う血管線維腫に限られます。

**同じ軸を食事から動かす**のがカロリー制限・糖質制限です。カロリー・糖質の過剰は mTOR 亢進側、制限は AMPK↑・mTOR↓ の向きに整理でき（→ [[ampk-mtor]]）、慢性的なmTOR亢進とオートファジー低下は Hallmarks of Aging の「deregulated nutrient sensing」の中核をなします（→ [[hallmarks-of-aging]]）。ただし**「mTORC1が栄養で動く」（確立した細胞生物学）と「糖質を控えればヒトの肌が若返る・collagenが増える」（未確立）は別**です。

## 4　urolithin A：mitophagyを促すと言われる代謝物

![上段は二つの入り方——食事由来（ellagitannin→ellagic acid→特定の腸内細菌がurolithin Aを産生。産生できるかどうかのmetabotypeに個人差が大きい）と、サプリ由来（腸内細菌に依存せず小腸から吸収されて血中へ）。中段はmitophagy仮説（損傷ミトコンドリア→PINK1蓄積→Parkinのリクルート→オートファゴソーム形成→リソソーム融合と分解）で、urolithin Aがこの流れを促すのは前臨床データとして点線で描かれ、新生と分解のバランスを最適化するという位置づけ。下段はヒトRCTでアウトカムを分けて測る例（血漿UA代謝物・筋生検の分子signature・筋持久力・6分間歩行・最大ATP産生）と、高齢者RCTで筋持久力やバイオマーカーは改善した一方6分間歩行や最大ATP産生では群間差が出なかったという食い違い、そして皮膚美容への外挿は未確立という注記](figures/senolytics_urolithinA_mitophagy.png)

**urolithin A** は食品そのものではありません。ザクロやベリーに含まれる **ellagitannin** が消化管で ellagic acid になり、**それを代謝できる腸内細菌がいる人でだけ**生じる代謝物です。産生能には個人差が大きく、同じものを食べても全員が同じ血中濃度になるわけではない——サプリメントとして分子そのものを投与する製品があるのは、この個人差を回避するためです。

- **前臨床（2〜3段目）**：損傷ミトコンドリアの PINK1/Parkin を介した選択的除去（mitophagy、→ [[mito-quality-control]]）を促し、線虫の寿命延長・老齢げっ歯類の筋機能改善が報告されています。
- **ヒトの target engagement（4段目）**：高齢者への first-in-human 試験は**主要評価項目が安全性**で、そこは良好でした。副次的に血漿acylcarnitineと骨格筋のミトコンドリア関連遺伝子発現が変化しています。ただしこの試験は筋力・持久力を評価していません。
- **ヒトの臨床アウトカム（5段目）は、主要評価項目で達成されていません。** 65〜90歳を対象とした4か月のRCT（66例）では、**主要評価項目である6分間歩行距離と筋の最大ATP産生の両方に群間差が出ませんでした**。有意だったのは副次の筋持久力（疲労までの収縮回数）と血漿バイオマーカーです。中年・非運動習慣者を対象とした別のRCT（88例）でも、主要評価項目である peak power output は約4%増にとどまり有意差なし、有意だったのは副次の筋力です。**「筋力が改善した」という紹介は、いずれも副次項目の話です。** どちらの試験もメーカーが関与しています。
- **皮膚（6段目）**：空欄です。筋のデータを皮膚線維芽細胞へ外挿する根拠はありません。

## 5　spermidine：オートファジーを促すと言われるポリアミン

![左はspermidine——食事・内因性合成（アルギニン→オルニチン→プトレスシン）・腸内細菌由来がpolyamine poolを作り、EP300のアセチル化抑制を介してオートファジー関連遺伝子（ATG群）の発現を促し、オートファゴソーム形成からリソソーム分解へ進むという前臨床仮説。ヒトでは動物モデルの寿命延長報告が強い一方、RCTは小規模・短期・アウトカム限定で再現性は未十分、観察研究の血中高値は因果ではないと明記される。右はvitamin D——皮膚でのUVB合成と食事由来から肝で25(OH)D、腎で1,25(OH)₂Dになり、VDR（核内受容体）を介して骨・筋・免疫などに多面的に働く。欠乏是正は骨・筋・免疫のアウトカムで確立、充足者への追加投与で寿命・美容・施術との相乗を支持する十分なエビデンスはない。下段の比較表は両者を分子機序・target engagement・臨床アウトカム・欠乏・安全性の5行で並べ、共通原則は「欠乏の是正を優先し、過剰に注意する」](figures/senolytics_spermidineとvitaminD.png)

**spermidine** はポリアミンの一種で、アセチル基転移酵素 **EP300** を抑えることでautophagy関連遺伝子の発現を促すとされます（→ [[autophagy]]）。酵母では寿命延長がATG依存であることまで示され、マウスでは経口投与で寿命延長・心肥大の抑制・心筋のmitophagy亢進が報告されています。**動物データ（3段目）は強い**ほうです。

一方で**ヒト（5段目）は陰性**です。主観的認知機能低下のある高齢者100例に12か月投与した二重盲検RCTでは、**主要評価項目である記憶課題の成績に群間差がありませんでした**（群間差 −0.03、95%CI −0.11〜0.05）。副次項目でも有意差はありません。食事由来spermidine摂取量が多い人ほど心血管イベントが少ない、という観察研究の関連はありますが、**関連は因果ではありません**。

ここで[[autophagy]]の注意を思い出してください——**「マーカーが上がったこと ≠ flux（実際の分解と再利用の流量）が増えたこと」**。LC3-IIやp62は、オートファジーが回っていても、リソソームで詰まっていても増えうる指標です。「autophagyが誘導された」という報告が、どちらを測ったものかを確認する必要があります。

> **図の右半分のビタミンDについて。** 「アンチエイジングに効く」と語られる代表なので同じ図に並べていますが、これは senolytic/mitophagy 系ではありません。名前は"ビタミン"でも実体は **VDR（vitamin D receptor）に結合して遺伝子発現を動かすホルモン様物質（secosteroid）**で（→ [[receptors-signaling]]）、角化細胞の分化・バリア脂質・抗菌ペプチド（cathelicidin/LL-37）の誘導という**皮膚での機序は確立**しています。ただし**真皮コラーゲンを増やして「しわ・ハリ」を改善する上乗せ効果のヒトエビデンスは弱く一貫しません**（外用ビタミンD類似体は主に乾癬の治療薬で、美容用途の製剤ではありません）。血中低値と疾患・死亡率の関連を報告する疫学は多いものの、一般集団25,871人を5年余り追跡した大規模RCT（VITAL）では、主要評価項目である浸潤癌（HR 0.96）と主要心血管イベント（HR 0.97）のいずれにも差が出ませんでした。**「欠乏の是正」と「足りている人への上乗せ」を分ける物差しは[[nad-precursors]]が正典**です（→ [[nad-precursors]]）。

## 6　境界はどこにあり、施術との併用はどう扱うか

ここまでの介入に共通するのは、**3段目（動物）と4段目（ヒトで標的が動く）は埋まっているのに、5段目から先が空いている**という形です。前臨床は濃度・投与法・遺伝的背景を実験者が最適化でき、測るのも中間指標（老化細胞が減った、mitophagyが増えた）です。ヒトでは何も最適化できず、測るべきアウトカムのほうが測りにくい。**「前臨床 ≠ ヒト臨床」を含む6本の未検証の矢印は、巻頭「本教材が守る切り分け」が正典**です（→ 巻頭、および最終章 §5）。

**施術との併用**——施術で刺激しつつ掃除系の介入を足せば相乗するのでは、という発想は機序上は筋が通りますが、**現時点では点線（未確立の仮説）**です。理由は三つ。施術後の一過性の炎症・senescence-like な細胞は修復に必要な側面を持つこと（→ [[wound-healing]]・[[senescence]]）、組み合わせを検証したヒト試験がないこと、そしていつ・どれだけ・どの細胞を残すかという設計自体が決まっていないこと。**患者に上乗せ効果を約束できる段階ではありません。**

> ただし**「ヒトで未確立だから読む価値がない」ではありません**。前臨床と初期臨床は、いま手元にある唯一の手がかりです。どの段まで来ているかにラベルを付けたまま持っておくことが、**次に何が示されたら考えを変えるべきかを知っている状態**でもあります。

## この章の到達点

![[[senolytics]]のまとめ。①用語（senolytic＝老化細胞を減らす／senomorphic＝SASPを抑え細胞は残す）②rapamycin（mTORC1抑制でautophagy促進・SASP調節、ヒト皮膚は探索データのみ）③urolithin A（mitophagy仮説、ヒト筋の分子指標と一部持久力、主要アウトカムは一貫せず）④spermidine（autophagy仮説は前臨床中心、ヒト臨床は限定的）⑤vitamin D（欠乏是正は確立、充足者の上乗せは別証拠）⑥証拠の階段（分子→細胞→動物→ヒトtarget engagement→臨床アウトカム→長期安全性）。結語は「機序がもっともらしい ≠ ヒトで若返る ≠ 美容施術と相乗」](figures/senolytics_まとめ.png)

1. **senolytic（数を減らす：D+Q・fisetin）と senomorphic（SASPを抑え細胞は残す：rapamycin・metformin）は別戦略。★ラパマイシンはsenolyticではありません**——この分野で最も多い混同。
2. **単剤ですべての老化細胞に効く薬はない**（効く細胞種が薬ごとに違うためD+Qは併用）。ヒトでは9例のオープンラベル試験で**脂肪組織と表皮のp16/p21陽性細胞が減った**ところまで。**外見のアウトカムは空欄**。dasatinibは抗腫瘍薬であり、選択性と安全性は同じではない。
3. **ラパマイシンは動物データが最も強い部類**（中高年後期から投与しても寿命延長）。だが**ヒト皮膚は外用の探索的試験（組織解析は8例、p16↓・collagen VII↑）どまりで、全身投与は免疫抑制薬**。カロリー制限も同じmTOR軸だが、美容アウトカムは未確立。
4. **中間指標とヒトのアウトカムは別**。urolithin A は腸内細菌代謝物で産生に個人差があり、**ヒトRCTは2本とも主要評価項目が未達**（有意なのは副次の筋持久力・筋力）。spermidine は動物で強い一方、**12か月RCTの主要評価項目は陰性**。加えて**マーカー上昇 ≠ flux増加**。
5. **美容施術との相乗効果は未確立**。老化細胞の一時的な有益性・組み合わせ試験の不在・タイミングと用量と選択性の未解決、の三つが理由。

### Evidence meter

- 老化細胞が SCAP に依存し、それを外すとアポトーシスへ向かう：**確立した細胞生物学（主に前臨床）**
- senolyticでヒトの**脂肪組織・表皮**の老化細胞マーカーが減る：**少人数・対照なしの初期臨床で示唆**／症状・機能の改善：**探索段階**／**外見のアウトカム：未確立**
- rapamycin が mTORC1 を阻害し、autophagy誘導・SASP抑制へ傾ける：**確立した細胞生物学**／モデル生物・マウスの寿命延長：**前臨床で再現性が高い**
- **外用**ラパマイシンがヒト皮膚の老化指標（p16↓等）を下げる：**小規模・探索段階（限定的）**／美容目的の全身投与：**未確立（免疫抑制リスクあり）**
- urolithin A が mitophagy を、spermidine が autophagy を促す：**前臨床で確立**／urolithin A のヒト筋 target engagement：**示されている**／urolithin A・spermidine のヒトRCTの主要評価項目：**達成されていない**（有意なのは副次項目）
- mTORC1 が栄養（糖質・カロリー）で動く：**確立**／「糖質・カロリー制限でヒトの肌が若返る・collagenが増える」：**未確立**
- ビタミンD（VDR）が角化細胞分化・バリア脂質・抗菌ペプチド誘導に関与：**確立した細胞生物学**／充足者への補充が longevity・美容アウトカムを上乗せ改善：**限定的・多くは未確立**
- これら介入がヒトで**皮膚の美容アウトカム**を改善する／**美容施術との相乗効果**：**いずれも未確立**

### 中核参考文献

**senolytic**

- Zhu Y, Tchkonia T, Pirtskhalava T, et al. The Achilles' heel of senescent cells: from transcriptome to senolytic drugs. *Aging Cell.* 2015;14(4):644-658. PMID: 25754370. DOI: 10.1111/acel.12344.（**SCAPとD+Qの原典**。in vitro＋マウス。老化細胞の抗アポトーシス経路を同定し、dasatinibとquercetinが細胞種依存的に効くことを示した）
- Xu M, Pirtskhalava T, Farr JN, et al. Senolytics improve physical function and increase lifespan in old age. *Nat Med.* 2018;24(8):1246-1256. PMID: 29988130. DOI: 10.1038/s41591-018-0092-9.（マウス。24〜27か月齢へのD+Q間欠投与で投与後生存期間が36%延長）
- Hickson LJ, Langhi Prata LGP, Bobart SA, et al. Senolytics decrease senescent cells in humans: Preliminary report from a clinical trial of Dasatinib plus Quercetin in individuals with diabetic kidney disease. *EBioMedicine.* 2019;47:446-456. PMID: 31542391. DOI: 10.1016/j.ebiom.2019.08.069.（**ヒトでの target engagement**。オープンラベル第1相、n=9、3日間投与・11日後評価。脂肪組織と**表皮**のp16/p21陽性細胞が減少。対照群なし）
- Justice JN, Nambiar AM, Tchkonia T, et al. Senolytics in idiopathic pulmonary fibrosis: Results from a first-in-human, open-label, pilot study. *EBioMedicine.* 2019;40:554-563. PMID: 30616998. DOI: 10.1016/j.ebiom.2018.12.052.（n=14、非盲検・対照なし。6分間歩行距離・歩行速度は改善、肺機能は不変）
- Kirkland JL, Tchkonia T. Senolytic drugs: from discovery to translation. *J Intern Med.* 2020;288(5):518-536. PMID: 32686219. DOI: 10.1111/joim.13141.（**総説**。分野全体の見取り図として）

**mTORC1／rapamycin**

- Harrison DE, Strong R, Sharp ZD, et al. Rapamycin fed late in life extends lifespan in genetically heterogeneous mice. *Nature.* 2009;460(7253):392-395. PMID: 19587680. DOI: 10.1038/nature08221.（NIA Interventions Testing Program、3施設。600日齢から投与し残存寿命中央値がメス14%・オス9%延長）
- Chung CL, Lawrence I, Hoffman M, et al. Topical rapamycin reduces markers of senescence and aging in human skin: an exploratory, prospective, randomized trial. *GeroScience.* 2019;41(6):861-869. PMID: 31761958. DOI: 10.1007/s11357-019-00113-y.（**外用ラパマイシンのヒト皮膚**。split-body、36例登録・17例完遂・組織解析8例、6〜8か月。p16低下 P=0.008、collagen VII増加 P=0.0077。血中濃度は検出限界未満。主要評価項目の事前規定なし）

**urolithin A**

- Ryu D, Mouchiroud L, Andreux PA, et al. Urolithin A induces mitophagy and prolongs lifespan in C. elegans and increases muscle function in rodents. *Nat Med.* 2016;22(8):879-888. PMID: 27400265. DOI: 10.1038/nm.4132.（前臨床の原典。ヒトデータなし）
- Andreux PA, Blanco-Bose W, Ryu D, et al. The mitophagy activator urolithin A is safe and induces a molecular signature of improved mitochondrial and cellular health in humans. *Nat Metab.* 2019;1(6):595-603. PMID: 32694802. DOI: 10.1038/s42255-019-0073-4.（first-in-human、二重盲検プラセボ対照。**主要評価項目は安全性**。筋力・持久力は評価していない）
- Liu S, D'Amico D, Shankland E, et al. Effect of Urolithin A Supplementation on Muscle Endurance and Mitochondrial Health in Older Adults: A Randomized Clinical Trial. *JAMA Netw Open.* 2022;5(1):e2144279. PMID: 35050355. DOI: 10.1001/jamanetworkopen.2021.44279.（n=66、65〜90歳、4か月。**主要評価項目（6分間歩行距離・最大ATP産生）はいずれも群間差なし**。副次の筋持久力と血漿バイオマーカーが改善。メーカーのCOIあり）
- Singh A, D'Amico D, Andreux PA, et al. Urolithin A improves muscle strength, exercise performance, and biomarkers of mitochondrial health in a randomized trial in middle-aged adults. *Cell Rep Med.* 2022;3(5):100633. PMID: 35584623. DOI: 10.1016/j.xcrm.2022.100633.（n=88、4か月。**主要エンドポイント peak power output は未達**（約4%増、有意差なし）。筋力改善は副次。メーカー主導）

**spermidine**

- Eisenberg T, Knauer H, Schauer A, et al. Induction of autophagy by spermidine promotes longevity. *Nat Cell Biol.* 2009;11(11):1305-1314. PMID: 19801973. DOI: 10.1038/ncb1975.（酵母・線虫・ハエ・ヒト免疫細胞。寿命延長はATG依存。哺乳類の寿命データは含まない）
- Eisenberg T, Abdellatif M, Schroeder S, et al. Cardioprotection and lifespan extension by the natural polyamine spermidine. *Nat Med.* 2016;22(12):1428-1438. PMID: 27841876. DOI: 10.1038/nm.4222.（マウス・ラットで寿命延長と心保護。ヒト部分は摂取量と血圧・心血管イベントの**観察研究**）
- Schwarz C, Horn N, Benson G, et al. Effects of Spermidine Supplementation on Cognition and Biomarkers in Older Adults With Subjective Cognitive Decline: A Randomized Clinical Trial. *JAMA Netw Open.* 2022;5(5):e2213875. PMID: 35616942. DOI: 10.1001/jamanetworkopen.2022.13875.（SmartAge試験。二重盲検プラセボ対照 phase 2b、n=100、12か月。**主要評価項目の記憶課題は陰性**：群間差 −0.03、95%CI −0.11〜0.05、P=.47）

**vitamin D**

- Manson JE, Cook NR, Lee IM, et al. Vitamin D Supplements and Prevention of Cancer and Cardiovascular Disease. *N Engl J Med.* 2019;380(1):33-44. PMID: 30415629. DOI: 10.1056/NEJMoa1809944.（VITAL試験、n=25,871、追跡中央値5.3年。浸潤癌 HR 0.96、主要心血管イベント HR 0.97、いずれも有意差なし）

> [[antioxidant-supplements]]では、美容皮膚科でいちばん多く出されている介入群——**抗酸化サプリメントと点滴**を、同じ物差しで読みます。そのあと最終章で、[[cell]]からここまで積み上げた「細胞の構造 → 代謝 → 品質管理 → 加齢 → 施術への応答 → 栄養・介入の評価」を一枚の流れに束ね、美容医療を細胞から考えるとはどういうことかを締めくくります。
