---
id: tca-cycle
title: TCA回路
kind: basic
status: draft
---

> [[glycolysis]]で作られた pyruvate は、ミトコンドリアへ入り、TCA回路へ進みます。

## この章の一言

> **TCA回路は、ミトコンドリアの中で回り続けるサイクルです。**acetyl-CoA が oxaloacetate と結びついて citrate になり、8つの反応を進むあいだに炭素を CO₂ として捨て、最後はまた oxaloacetate に戻り、次の acetyl-CoA を受け取って循環します。
>
> 役割は2つあります。栄養素から取り出した電子を **NAD⁺・FAD** に積み、**NADH・FADH₂** として電子伝達系へ送ること。もう一つは、回路の中間体を**アミノ酸・脂質・核酸・heme の材料**として抜き出すことです。この二役を **amphibolic** といいます。
>
> そしてこのサイクルは、**ビタミンB群・ミネラル・アミノ酸がそろって初めて回ります。**

![ミトコンドリア内の一つの輪から、出力が2方向へ伸びている。出力A（緑）は1周あたり 3 NADH・1 FADH₂・1 GTP・2 CO₂ → 電子伝達系へ。出力B（紫の破線）は中間体をアミノ酸・脂質・heme・nucleotide の材料として抜き出す方向で、破線の補充（anaplerosis）が輪の内側に戻っている。α-ketoglutarate にだけ「コラーゲン水酸化酵素の共基質」と注記があり、赤枠で「TCAを上げればコラーゲンが増える、ではない」と釘が刺されている](figures/tca-cycle_TCA回路.png)

## 1　入口の反応が、5つの補酵素を同時に要求する

ミトコンドリアへ入った pyruvate は、**pyruvate dehydrogenase（PDH）** という酵素複合体で **acetyl-CoA** に変えられます。TCA回路そのものではなく、その手前の一反応です。

> pyruvate ＋ CoA ＋ NAD⁺ ──**PDH**──→ acetyl-CoA ＋ CO₂ ＋ NADH

**この反応には、5つの補酵素が同時に必要です。**その多くはビタミンB群から作られ、さらにマグネシウムも要ります。補酵素と金属イオンをまとめた呼び名が **補因子** です。

| 補酵素 | 由来 | PDH複合体のどこで働くか |
|---|---|---|
| **TPP**（thiamine pyrophosphate） | **thiamine（B1）** | E1：pyruvate の脱炭酸。結合には **Mg²⁺** が要る |
| **lipoate**（lipoamide） | lipoic acid（体内でも合成される） | E2：アセチル基を受け取って転移する |
| **CoA** | **pantothenate（B5）** | E2：アセチル基を acetyl-CoA として持ち出す |
| **FAD** | **riboflavin（B2）** | E3：使い終わった lipoamide を再酸化する |
| **NAD⁺** | **niacin（B3）** | E3：電子を受け取り NADH になる |

**1つでも欠ければ、PDH は働けないため、pyruvate は acetyl-CoA に変換されず、TCA回路へ入れません。**行き場を失った pyruvate は、lactate へ回されます（→ [[glycolysis]]§5）。

**TCA回路に入ったあとも、回路を回すには補酵素と材料（アミノ酸）がそろっている必要があります。**

- **ビタミンB群** … 補酵素の材料（B1 → TPP、B2 → FAD、B3 → NAD⁺、B5 → CoA）。同じ5つは、入口の PDH と回路内の **α-ketoglutarate dehydrogenase**（PDH と同型の複合体）の**2か所**で要る
- **マグネシウム** … TPP を酵素につなぎ止める。PDH を再活性化する phosphatase にも要る（→ §2）
- **鉄と硫黄** … **Fe–S クラスター**として aconitase と Complex II（succinate dehydrogenase）に組み込まれている
- **アミノ酸** … 抜き出された中間体を補充する（→ §3）

アミノ酸が要るのは、**中間体が絶えず抜き出されるから**です。抜けた分を補わなければ、回転は落ちます（→ §3）。

**疲労に対してビタミンB群やマグネシウムを含む点滴・サプリが使われるのは、この依存関係を根拠にしています。**

> **切り分け。**「補因子が欠けていれば回らない」は確立した生化学です。「足せば回転が上がる」は、**欠乏がある場合にしか導けません**。充足している状態で追加したときに代謝回転や臨床所見がどう動くかは、別に検証すべき問いです（→ 巻頭「本教材が守る切り分け」）。

::: note ちなみに ―― 「充足しているか」は測りにくい
切り分けの前提になる「欠乏か、充足か」の判定そのものが、臨床では簡単ではありません。**血清の値が体内のプールを反映しないもの**があるからです。マグネシウムは体内の大半が骨と細胞内にあり、**血中にあるのは1%程度**です。thiamine も、血漿濃度より全血の thiamine pyrophosphate や transketolase 活性のほうが状態を反映するとされます。**基準値内であることは、細胞内で足りていることの保証にはなりません。**
:::

## 2　PDH の活性は、リン酸化で調節される

PDH は、補酵素がそろえば必ず働く酵素ではありません。**PDH kinase にリン酸化されると活性が落ち、PDH phosphatase に脱リン酸化されると戻ります。**TCA回路の入口の通しやすさが、ここで調節されています。

![門として描かれた PDH複合体。右側が開閉の仕組みで、PDH kinase によるリン酸化で活性低下（完全停止ではない）、PDH phosphatase による脱リン酸化で活性回復。下段は閉じる合図（NADH高値・acetyl-CoA高値＝先が足りている）と開く合図（ADP・pyruvate、筋では Ca²⁺）の対比](figures/tca-cycle_PDHゲート.png)

活性が落ちるのは、**エネルギーが足りていて、回路を回す必要がないとき**です。だから、**glucose を取り込んだからといって、その炭素が自動的に TCA回路へ流れるわけではありません。**低酸素で HIF-1α が **PDK1**（PDH kinase の一つ）を増やすのも、この調節を使っています（→ [[glycolysis]]§3）。

## 3　TCA回路で得られるもの

![acetyl-CoA 1分子が一周する間に、2回の脱炭酸で 2 CO₂ が抜け、3 NADH・1 FADH₂・1 GTP が出る。GTP はこの1周で唯一の基質レベルのリン酸化による産物で、PDH段階で出る 1 NADH + 1 CO₂ はこの収支には含めない。右下の赤枠は「TCA回路はATPを直接大量に作る回路ではない」](figures/tca-cycle_TCA回路1周の収支.png)

> acetyl-CoA 1分子 → 2 CO₂ ＋ 3 NADH ＋ 1 FADH₂ ＋ 1 GTP

glucose 1分子からは pyruvate が2つできるので、**回路は2周します**（→ [[glycolysis]]）。

**回路が直接作る高エネルギー化合物は、1周あたり GTP 1個だけ**です。GTP は ATP と同じように使えますが、量はわずかです。**回路の主産物は NADH と FADH₂**で、積んだ電子を[[electron-transport]]へ運びます。ATP の大半は、そこで作られます。

**得られるもう一つが、材料です。**

回路の**中間体**は、次々と**合成の材料として抜き出されます**。抜き出し口は4か所——**citrate・α-ketoglutarate・oxaloacetate・succinyl-CoA**。

![TCA回路からのcataplerosisとanaplerosisを対で示す。citrateは脂肪酸・cholesterol、α-ketoglutarateはglutamate・amino acidおよびcollagenのproline水酸化、oxaloacetateはaspartate・nucleotide、succinyl-CoAはhemeへ抜き出される。pyruvate carboxylaseによるoxaloacetate補充とglutamine由来α-ketoglutarate補充が回路を保ち、NADH・FADH₂は電子伝達系へ渡る。](figures/tca-cycle_材料供給と補充.png)

**抜き出せば、回路内の中間体は減ります。**とくに oxaloacetate が減ると、acetyl-CoA を受け取る相手がいなくなり、入口で滞ります。

だから細胞は、抜いた分を別の経路から**補充**します。これが **anaplerosis** で、代表例は次の二つ。

- **pyruvate carboxylase**：pyruvate ＋ CO₂ → **oxaloacetate**。解糖系から来た炭素を、燃やすためではなく**回路の材料を足すために**使う。この酵素は補因子として **biotin（B7）** を要求します
- **glutaminolysis**：glutamine → glutamate → **α-ketoglutarate**。増殖中の細胞がよく使うルートで、**アミノ酸から回路を支えます**

抜き出す方向が **cataplerosis**、補充する方向が **anaplerosis** です。

> TCA回路は、エネルギーを取り出すためだけの回路ではありません。**同じ回路が、体を作る材料の供給元でもあります。**

::: note ちなみに ―― α-ketoglutarate はコラーゲンの成熟に消費される
コラーゲンは、作られたあとに **prolyl hydroxylase**・**lysyl hydroxylase** による**水酸化**を受けて初めて成熟します（工程の詳細は[[fibroblast-collagen]]）。この酵素は反応のたびに **α-ketoglutarate を共基質として消費します**。TCA回路の中間体が、そのままコラーゲンの加工に使われているということです。

![左のTCA回路から α-ketoglutarate がミトコンドリアの外へ出て、右のER内でプロリル／リシル水酸化酵素の入力の一つになる。入力は Pro/Lys 残基・α-ketoglutarate・O₂・Fe²⁺・ascorbate の5つで、出力は水酸化残基（Hyp/Hyl）と succinate + CO₂。α-ketoglutarate は消費される共基質であって、それ自体が Hyp になるわけではない。下段の3チェックポイント（量があるか／ERで使えるか／酵素と補因子がそろうか）が、「機序上つながる ≠ TCAを高めればコラーゲンが増える」を支えている](figures/tca-cycle_αケトグルタル酸とコラーゲン水酸化.png)

**ただし α-ketoglutarate は、必要な要素の一つにすぎません。**同じ反応には **O₂・Fe²⁺・ascorbate** も要ります。しかも α-ketoglutarate はコラーゲンの一部になるのではなく、消費されて succinate と CO₂ に変わります。

だから「TCA回路を活発にすればコラーゲンが増える」とは言えません。**ここで言えるのは、機序の上でつながっているというところまで**です。この線引きが、のちに栄養や治療を評価するときに効いてきます。
:::

## この章の到達点

1. TCA回路は、acetyl-CoA を受け取って一周し、**oxaloacetate に戻って次の acetyl-CoA を受け取る**サイクル。**入口は TCA回路ではなく、その手前の PDH** で、pyruvate を acetyl-CoA に変える。
2. PDH は **TPP（B1）・lipoate・CoA（B5）・FAD（B2）・NAD⁺（B3）** の5つの補酵素を同時に要求する。**1つでも欠ければ働かず、pyruvate は TCA回路へ入れない**（行き場を失えば lactate へ）。回路を回すには、ほかに **Mg²⁺**、**Fe–S クラスターの鉄と硫黄**、そして**中間体を補充するアミノ酸**が要る。
3. PDH の活性は**リン酸化で下がり、脱リン酸化で戻る**。エネルギーが足りていれば活性は落ちるので、**glucose を取り込んでも、その炭素が自動的に TCA回路へ流れるわけではない**（低酸素では HIF-1α が PDK1 を増やす）。
4. 得られるものは2つ。**1周で 3 NADH・1 FADH₂・1 GTP・2 CO₂**——ATP の大半はこの電子を使って電子伝達系で作られる。同時に**中間体が脂質・アミノ酸・核酸・heme の材料として抜き出され**、抜けた分は **anaplerosis**（pyruvate carboxylase＝biotin依存、glutaminolysis）で補われる。この二役が **amphibolic**。

![TCA回路は代謝の交差点](figures/tca-cycle_まとめ.png)

> [[electron-transport]]では、TCA回路が電子を渡した **NADH・FADH₂** が、**電子伝達系**で酸素へ電子を降ろす場面を見ます。ここが、体内でO₂を大量に消費し続けている唯一の場所です。
