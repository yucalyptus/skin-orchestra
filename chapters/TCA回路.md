---
id: tca-cycle
title: TCA回路
kind: basic
status: draft
---

> [[glycolysis]]で作られた pyruvate は、ここでミトコンドリアへ入ります。解糖系・TCA回路・電子伝達系という3つの工程の、**2段目**がこの章です。

## この章の一言

> TCA回路は、**ビタミンB群・ミネラル・アミノ酸がそろって初めて回ります。**
>
> **TCA回路が出すものは2つ**です。栄養素から取り出した電子を **NADH・FADH₂** に渡して電子伝達系へ送る。同時に、回路の中間体を**アミノ酸・脂質・heme の材料**として抜き出す。この二役を **amphibolic** といいます。

![ミトコンドリア内の一つの輪から、出力が2方向へ伸びている。出力A（緑）は1周あたり 3 NADH・1 FADH₂・1 GTP・2 CO₂ → 電子伝達系へ。出力B（紫の破線）は中間体をアミノ酸・脂質・heme・nucleotide の材料として抜き出す方向で、破線の補充（anaplerosis）が輪の内側に戻っている。α-ketoglutarate にだけ「コラーゲン水酸化酵素の共基質」と注記があり、赤枠で「TCAを上げればコラーゲンが増える、ではない」と釘が刺されている](figures/tca-cycle_TCA回路.png)

## 1　入口の反応が、5つの補因子を同時に要求する

ミトコンドリアへ入った pyruvate は、**pyruvate dehydrogenase（PDH）** という酵素複合体で **acetyl-CoA** に変えられます。TCA回路そのものではなく、その手前の一反応です。

> pyruvate ＋ CoA ＋ NAD⁺ → acetyl-CoA ＋ CO₂ ＋ NADH

この一つの反応に、**5つの補因子が同時に要ります。** ビタミンB群やマグネシウムを含む点滴が代謝のどこで働いているかというと、その中心がここです。

| 補因子 | 由来 | PDH複合体のどこで働くか |
|---|---|---|
| **TPP**（thiamine pyrophosphate） | **thiamine（B1）** | E1：pyruvate の脱炭酸。結合には **Mg²⁺** が要る |
| **lipoate**（lipoamide） | lipoic acid（体内でも合成される） | E2：アセチル基を受け取って転移する |
| **CoA** | **pantothenate（B5）** | E2：アセチル基を acetyl-CoA として持ち出す |
| **FAD** | **riboflavin（B2）** | E3：使い終わった lipoamide を再酸化する |
| **NAD⁺** | **niacin（B3）** | E3：電子を受け取り NADH になる |

**1つでも欠ければ、PDHは動きません。** thiamine が欠乏すると PDH が止まり、pyruvate と lactate が上昇するのはこのためです。

しかも同じ5つの組み合わせが、**回路の中でもう一度**要求されます。**α-ketoglutarate dehydrogenase** は PDH と同型の複合体で、TPP・lipoate・CoA・FAD・NAD⁺ を同じように使います。回路の他の酵素も、それぞれ補因子を持っています。**aconitase と Complex II（succinate dehydrogenase）は Fe–S クラスター**を、**isocitrate dehydrogenase と malate dehydrogenase は NAD⁺** を必要とします。**Mg²⁺** は TPP の結合に要るほか、PDH を再活性化する PDH phosphatase にも要ります（この phosphatase は Ca²⁺ で活性が上がります）。

そしてTCA回路は、閉じた輪ではありません。中間体はアミノ酸・脂質・heme の材料として絶えず抜き出され、抜けた分は補充されています。**回路を回すには、補因子だけでなくアミノ酸の供給も要る**ということです（→ §4）。

> **切り分け。**「補因子が欠けていれば回らない」は確立した生化学です。「足せば回転が上がる」は、**欠乏がある場合にしか導けません**。充足している状態で追加したときに代謝回転や臨床所見がどう動くかは、別に検証すべき問いです（→ 巻頭「本教材が守る切り分け」）。

## 2　PDHは「開閉するゲート」でもある

PDH は補因子を要求するだけでなく、リン酸化で活性が落ち、脱リン酸化で戻ります。

![門として描かれた PDH複合体。右側が開閉の仕組みで、PDH kinase によるリン酸化で活性低下（完全停止ではない）、PDH phosphatase による脱リン酸化で活性回復。下段は閉じる合図（NADH高値・acetyl-CoA高値＝先が足りている）と開く合図（ADP・pyruvate、筋では Ca²⁺）の対比](figures/tca-cycle_PDHゲート.png)

**glucose が細胞に入ったからといって、その炭素が自動的に全部 TCA回路へ流れるわけではありません。** HIF-1α が **PDK1** を介してこのゲートを閉じる、というのがまさにこの調節です（→ [[glycolysis]]§3）。

## 3　1周でできるもの

![acetyl-CoA 1分子が一周する間に、2回の脱炭酸で 2 CO₂ が抜け、3 NADH・1 FADH₂・1 GTP が出る。GTP はこの1周で唯一の基質レベルのリン酸化による産物で、PDH段階で出る 1 NADH + 1 CO₂ はこの収支には含めない。右下の赤枠は「TCA回路はATPを直接大量に作る回路ではない」](figures/tca-cycle_TCA回路1周の収支.png)

NADH と FADH₂ が電子を運び、[[electron-transport]]でATPになります。**TCA回路そのものが直接作るATP（GTP）は1周1個だけ**です。

## 4　抜き出しと補充が同時に走っている

回路の**中間体**は、次々と**合成の材料として抜き出されます**。抜き出し口は4か所——**citrate・α-ketoglutarate・oxaloacetate・succinyl-CoA**。

四つとも、美容の関心に直結します。citrate から出る**脂質合成**は皮脂と脂肪細胞の話につながり、α-ketoglutarate から glutamate を経て作られる **proline** は collagen の主要アミノ酸、oxaloacetate 由来の **nucleotide** は細胞が分裂・修復するときの必需品、succinyl-CoA から作られる **heme** はヘモグロビンとミトコンドリアの電子伝達体の部品です。

TCA回路は、中間体が消費されずに一周して戻る回路として説明されます。ところが途中で抜き出せば、**中間体の総量が減って回転が落ちます**。とくに oxaloacetate が減ると、acetyl-CoA を受け取る相手がいなくなり、入口で滞ります。

だから細胞は、抜いた分を別の経路から**補充**します。これが **anaplerosis** で、代表例は次の二つ。

- **pyruvate carboxylase**：pyruvate ＋ CO₂ → **oxaloacetate**。解糖系から来た炭素を、燃やすためではなく**回路の材料を足すために**使う。この酵素は補因子として **biotin（B7）** を要求します
- **glutaminolysis**：glutamine → glutamate → **α-ketoglutarate**。増殖中の細胞がよく使うルートで、**アミノ酸から回路を支えます**

抜き出す方向が **cataplerosis**、補充する方向が **anaplerosis** です。

![TCA回路からのcataplerosisとanaplerosisを対で示す。citrateは脂肪酸・cholesterol、α-ketoglutarateはglutamate・amino acidおよびcollagenのproline水酸化、oxaloacetateはaspartate・nucleotide、succinyl-CoAはhemeへ抜き出される。pyruvate carboxylaseによるoxaloacetate補充とglutamine由来α-ketoglutarate補充が回路を保ち、NADH・FADH₂は電子伝達系へ渡る。](figures/tca-cycle_材料供給と補充.png)

> TCA回路を ATP 産生経路とだけ捉えると、なぜ細胞が材料を作れるのかを見失います。**抜き出しと補充が同時に走っている交差点**として捉える。

## 5　α-ketoglutarate とコラーゲンの接点 ―― 慎重に

コラーゲンが正しく成熟するには、**prolyl hydroxylase** や **lysyl hydroxylase** による**水酸化**が必要です（工程の詳細は[[fibroblast-collagen]]§3）。これらの酵素は **α-ketoglutarate依存性dioxygenase** と呼ばれる一群に属し、反応のたびに **α-ketoglutarate（TCA回路の中間体）を共基質として消費します**。

**TCA回路の中間体が、コラーゲンの加工にそのまま使われている。**ここが接点です。

では、TCA回路を活発にすればコラーゲンの成熟が進むのか。**そうは言えません。**

- この酵素が働くには α-ketoglutarate **以外の条件**もそろっている必要がある（O₂・Fe²⁺・ascorbate。補因子の全体像は → [[fibroblast-collagen]]）
- 「TCA中間体の量」「代謝の流れ（フラックス）」「ER内で実際に材料が使える状態か」「酵素が働けるか」は、**それぞれ別の話**として検討しなければならない

![左のTCA回路から α-ketoglutarate がミトコンドリアの外へ出て、右のER内でプロリル／リシル水酸化酵素の入力の一つになる。入力は Pro/Lys 残基・α-ketoglutarate・O₂・Fe²⁺・ascorbate の5つで、出力は水酸化残基（Hyp/Hyl）と succinate + CO₂。α-ketoglutarate は消費される共基質であって、それ自体が Hyp になるわけではない。下段の3チェックポイント（量があるか／ERで使えるか／酵素と補因子がそろうか）が、「機序上つながる ≠ TCAを高めればコラーゲンが増える」を支えている](figures/tca-cycle_αケトグルタル酸とコラーゲン水酸化.png)

ここで言えるのは、**機序の上でつながっている**というところまでです。この線引きが、のちに栄養や治療を評価するときに効いてきます。

## この章の到達点

1. 入口の **PDH** は **TPP（B1）・lipoate・CoA（B5）・FAD（B2）・NAD⁺（B3）** の5つを同時に要求し、TPPの結合には **Mg²⁺** が要る。**1つでも欠ければPDHは動かない。** 同じ5つは回路内の **α-ketoglutarate dehydrogenase** でもう一度要求され、aconitase と Complex II は **Fe–S** を要求する。
2. 「補因子が欠けていれば回らない」と「足せば回転が上がる」は別の主張。後者は**欠乏がある場合にしか導けない**。
3. PDH はゲートでもあり、リン酸化で閉じる。**glucose の炭素が自動的に全部 TCA へ流れるわけではない。**
4. TCA回路は1周で **3 NADH・1 FADH₂・1 GTP・2 CO₂** を生む。同時に中間体が**citrate→脂質、α-ketoglutarate→glutamate/proline、oxaloacetate→aspartate/核酸、succinyl-CoA→heme** として抜き出され、**anaplerosis**（pyruvate carboxylase＝biotin依存、glutaminolysis）で補充される。この二役が **amphibolic**。
5. **α-ketoglutarate はコラーゲン水酸化酵素が消費する共基質**という接点があるが、「TCAを上げれば成熟が進む」とは結論できない。

![TCA回路は代謝の交差点](figures/tca-cycle_まとめ.png)

> [[electron-transport]]では、TCA回路が電子を渡した **NADH・FADH₂** が、**電子伝達系**で酸素へ電子を降ろす場面を見ます。ここが、体内でO₂を大量に消費し続けている唯一の場所です。
