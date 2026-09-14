---
id: hallmarks-of-aging
title: Hallmarks of Aging
subtitle: 老化を構成する仕組み
kind: basic
status: approved
published: 2026-09-14
updated: 2026-09-14
history:
  - {date: 2026-09-14, note: 初公開}
  - {date: 2026-09-13, note: Hallmarksの分類と介入の目的・代表例を整理}
---

> 加齢に伴う皮膚の変化には、細胞の損傷、代謝や分泌の変化、組織を維持する力の低下が関わります。この章では、これまで学んだ仕組みを、加齢の側から整理します。

## この章の一言

> **加齢では、損傷の蓄積と、細胞・組織を維持する仕組みの変化が重なります。** Hallmarks of Agingは、それらの関係を整理する枠組みです。

![老化に関わる12の仕組みを、損傷の蓄積・細胞の応答・組織への波及に分けて整理する。各群は互いに影響する。](figures/hallmarks-of-aging_Hallmarks_of_Aging.png)


## 1　皮膚の加齢を、細胞の変化から捉える

加齢に伴うハリの低下や修復の遅れには、コラーゲンの状態だけでなく、それを作る細胞の代謝、損傷への対応、周囲との情報交換も関わります。

López-Otínらは2023年の総説で、老化に関わる仕組みを **12のHallmarks** に整理しました。本章では、理解しやすいように **損傷の蓄積・細胞の応答・組織への波及** の3群に分けます。これらは互いに影響し合います。[López-Otínら, 2023](https://pubmed.ncbi.nlm.nih.gov/36599349/)

テロメア長の測定やエピジェネティッククロックは、このうち一部の変化を捉えます。クロックはDNAメチル化のパターンなどから年齢を推定するもので、皮膚の修復力や12項目すべてを測る検査ではありません（→ [[epigenome]]）。

## 2　損傷がたまる（損傷系）

| Hallmark | 一言でいうと | どこかで触れた話 |
|---|---|---|
| **ゲノム不安定性**（genomic instability） | DNAの傷や変異がたまる | 核・DNA損傷（[[organelles]]・[[dna-to-protein]]、[[cell-cycle]]のp53） |
| **テロメア短縮**（telomere attrition） | 染色体末端の保護領域が短くなり、損傷応答を起こす | 増殖の限界（[[cell-cycle]]） |
| **エピゲノム変化**（epigenetic alterations） | 「どの遺伝子を読むか」の調節が乱れる | エピゲノム（[[epigenome]]） |
| **プロテオスタシス破綻**（loss of proteostasis） | 折り直す（chaperone/HSP）・タグを付けて壊す・包んで壊すの三手が崩れる | 品質管理の三段構え（[[autophagy]]）、ER・folding（[[organelles]]・[[autophagy]]） |
| **マクロオートファジー低下**（disabled macroautophagy） | 不要物を分解・再利用する掃除が滞る | 量ではなくflux（[[autophagy]]） |

![DNA・エピゲノム・タンパク質の変化と、不要物を分解する仕組みの低下。](figures/hallmarks-of-aging_損傷系Hallmarks.png)

## 3　細胞の対応が乱れる（応答系）

損傷に対して細胞は感知して反応します。この**反応そのものが乱れる**のが第2層です。

| Hallmark | 一言でいうと | どこかで触れた話 |
|---|---|---|
| **栄養感知の異常**（deregulated nutrient sensing） | 栄養・エネルギー状態に応じた成長と維持の調節が変わる | AMPK・mTOR（[[mtorc1]]・[[ampk-mtor]]） |
| **ミトコンドリア機能不全**（mitochondrial dysfunction） | エネルギー変換と代謝調整が崩れる | ミトコンドリア（[[organelles]]・[[electron-transport]]・[[mito-quality-control]]、→[[mito-dysfunction]]） |
| **細胞老化**（cellular senescence） | 細胞が増殖をやめ、性質と分泌物を変える | quiescenceとの違い（[[cell-cycle]]、→[[senescence]]） |

栄養感知には、細胞の成長を促すmTORや、エネルギー不足に応答するAMPKなどが関わります。ここでいう異常には、成長を促す信号の持続も含まれます。**栄養不足だけの話ではありません。**

細胞老化に伴う分泌の変化を **SASP（老化関連分泌形質）** と呼びます。詳しくは[[senescence]]、ミトコンドリアとの関係は[[mito-dysfunction]]で扱います。

![栄養感知、ミトコンドリア、細胞老化の変化。SASPの内容と強さは、細胞種や刺激で異なる。](figures/hallmarks-of-aging_応答系Hallmarks.png)

## 4　組織全体が弱る（波及系）

個々の細胞の乱れが、組織・個体のレベルへ波及します。

| Hallmark | 一言でいうと | どこかで触れた話 |
|---|---|---|
| **幹細胞枯渇**（stem cell exhaustion） | 組織を補う幹細胞の数や働きが低下する | 修復・ターンオーバー（[[wound-healing]]） |
| **細胞間コミュニケーション異常**（altered intercellular communication） | 細胞どうしの連絡（分泌シグナル等）が乱れる | 受容体・シグナル（[[receptors-signaling]]） |
| **慢性炎症**（chronic inflammation） | 低レベルの炎症が持続する | 炎症は本来"始まって終わる"もの（[[wound-healing]]） |
| **dysbiosis**（細菌叢の乱れ） | 腸管などの微生物叢の構成や働きが変わり、宿主の代謝・免疫に影響する | （本教材では概要のみ） |

加齢に伴う持続的で低度の炎症は **inflammaging** と呼ばれます。炎症は細胞の損傷を増やし、組織の維持や修復にも影響します。

![幹細胞、細胞間の情報交換、炎症、微生物叢の変化が、組織の維持・修復に影響する。](figures/hallmarks-of-aging_波及系Hallmarks.png)


## 5　損傷・代謝・炎症が、互いを悪化させる

例えば、次のようなつながりがあります。

- 慢性炎症は、さらにDNA損傷を増やし得る。
- ミトコンドリア機能不全は、ROSを介して損傷を悪化させ得る。
- 細胞老化が出すSASPは、周囲の細胞のコミュニケーションを乱し得る。
- オートファジー低下は品質管理の負荷を上げ、ミトコンドリア機能不全を悪化させ得る。

皮膚では、こうした変化が重なり、細胞の増殖、ECMの合成・分解、炎症の収束に影響します。

![炎症・ROS・SASP・品質管理を通じて、複数の加齢変化が互いを悪化させる。](figures/hallmarks-of-aging_Hallmarksネットワーク.png)


## 6　老化の仕組みへの介入は、何を目指すのか

Hallmarksを学ぶと、老化への介入が、細胞のどの働きを変えようとしているかが分かります。目指すのは、損傷を減らすこと、代謝や品質管理を保つこと、老化細胞の蓄積や炎症性の分泌を抑えることです。一つの介入が、複数の仕組みに関わる場合もあります。

| 何を目指すか | 介入の代表例 | ヒトで確認されていること |
|---|---|---|
| **新たな損傷を減らす** | 日焼け止めなどの紫外線対策 | 日焼け止めを日常的に使う群で、皮膚の光老化の進行を抑えた無作為化試験がある。[Hughesら, 2013](https://pubmed.ncbi.nlm.nih.gov/23732711/) |
| **代謝とミトコンドリアの働きを保つ** | 運動 | 高齢者を含む介入試験で、骨格筋のミトコンドリア呼吸能などの改善が示されている。[Robinsonら, 2017](https://pubmed.ncbi.nlm.nih.gov/28273480/) |
| **NAD⁺代謝に働きかける** | NR・NMNなどのNAD⁺前駆体 | NRの試験では血液中のNAD⁺増加が確認されている。皮膚での合成・修復への効果は別に検証する。[Martensら, 2018](https://pubmed.ncbi.nlm.nih.gov/29599478/) |
| **傷んだミトコンドリアの更新を促す** | urolithin A | 高齢者の筋肉で、ミトコンドリア関連の遺伝子発現や代謝指標の変化が報告されている。[Andreuxら, 2019](https://pubmed.ncbi.nlm.nih.gov/32694802/) |
| **蓄積した老化細胞を減らす** | セノリティクス（dasatinib＋quercetinなど） | 糖尿病性腎疾患患者の小規模試験で、皮膚・脂肪の老化細胞マーカーが低下した。美容効果を確立する試験ではない。[Hicksonら, 2019](https://pubmed.ncbi.nlm.nih.gov/31542391/) |
| **SASPなどの老化形質を抑える** | セノモルフィクス。mTORを抑えるrapamycinなどが研究対象 | 外用rapamycinの探索的試験で、皮膚のp16や外観の変化が報告されている。効果の再現性や長期安全性は検証が必要。[Chungら, 2019](https://pubmed.ncbi.nlm.nih.gov/31761958/) |

運動や紫外線対策から、研究段階の薬剤まで、確かめられている範囲は異なります。栄養も代謝の土台ですが、摂取量を増やすだけで吸収・利用や品質管理まで改善するとは限りません。

NAD⁺前駆体は[[nad-precursors]]、老化細胞やミトファジーへの介入は[[senolytics]]で詳しく扱います。**ここまで学んだ代謝・品質管理・炎症は、こうした介入が何に働きかけるかを理解する基礎になります。**

## この章の到達点

1. Hallmarks of Agingは、老化に関わる複数の仕組みを整理する枠組み。
2. **損傷の蓄積・細胞の応答・組織への波及** をつなげて理解する。
3. 細胞老化はその一つであり、加齢に伴う変化は細胞老化以外にも起こる。
4. テロメア長やエピジェネティッククロックは、加齢変化の一部を捉える指標。
5. 介入は、損傷・代謝・品質管理・老化細胞のどこに働きかけるかと、ヒトで何が確認されたかを合わせて理解する。

![12のHallmarksと、その相互作用を振り返る。](figures/hallmarks-of-aging_まとめ.png)

## 参考文献

- López-Otín C, et al. Hallmarks of aging: An expanding universe. *Cell*. 2023. 総説・枠組みの提案。[PMID: 36599349](https://pubmed.ncbi.nlm.nih.gov/36599349/).

- Hughes MCB, et al. Sunscreen and prevention of skin aging: a randomized trial. *Annals of Internal Medicine*. 2013. [PMID: 23732711](https://pubmed.ncbi.nlm.nih.gov/23732711/).
- Robinson MM, et al. Enhanced Protein Translation Underlies Improved Metabolic and Physical Adaptations to Different Exercise Training Modes in Young and Old Humans. *Cell Metabolism*. 2017. [PMID: 28273480](https://pubmed.ncbi.nlm.nih.gov/28273480/).
- Martens CR, et al. Chronic nicotinamide riboside supplementation is well-tolerated and elevates NAD⁺ in healthy middle-aged and older adults. *Nature Communications*. 2018. [PMID: 29599478](https://pubmed.ncbi.nlm.nih.gov/29599478/).
- Andreux PA, et al. The mitophagy activator urolithin A is safe and induces a molecular signature of improved mitochondrial and cellular health in humans. *Nature Metabolism*. 2019. [PMID: 32694802](https://pubmed.ncbi.nlm.nih.gov/32694802/).
- Hickson LJ, et al. Senolytics decrease senescent cells in humans: Preliminary report from a clinical trial of Dasatinib plus Quercetin in individuals with diabetic kidney disease. *EBioMedicine*. 2019. [PMID: 31542391](https://pubmed.ncbi.nlm.nih.gov/31542391/).
- Chung CL, et al. Topical rapamycin reduces markers of senescence and aging in human skin: an exploratory, prospective, randomized trial. *GeroScience*. 2019. [PMID: 31761958](https://pubmed.ncbi.nlm.nih.gov/31761958/).

> [[senescence]]では、増殖を止めた細胞の働きと、分泌物が皮膚へ与える影響を扱います。
