---
id: pbm
title: PBM・LEDの生化学
subtitle: photobiomodulation
kind: applied
status: draft
---

> **ここまでのデバイス各章はすべて「制御された損傷」で創傷治癒を起動するデバイスでした。PBM（photobiomodulation、旧称LLLT＝low-level laser therapy、実装としてのLED光線療法）だけは、その系譜から外れます。**
> LED機器の設定項目は、赤色・近赤外・青色といった波長と、照射時間です。照射量（irradiance＝mW/cm²、fluence＝J/cm²）の表示は機種によってばらつきます。
> 前提を一つ。**PBMは、機序が分子まで詰められている一方で、臨床効果の確からしさが適応ごとに大きく違う分野です。** 主要な吸収体（chromophore）と一次反応はよく研究されていますが、正確な作用波長・至適用量、opsin/TRPなど"第二の受容体"は仮説段階にあります。この章はそのずれをそのまま見せます。


## この章の一言

> **PBMだけは組織を壊しません。だから「多く当てるほど効く」が成り立ちません。**
>
> 入口が損傷ではなく、ミトコンドリアの **cytochrome c oxidase（CcO＝complex IV）への光吸収**だからです。傷ベースのデバイスは出力を上げるほど深く広く壊れる——用量と結果が単調に対応しました。PBMでは低用量で促進、過剰で無効〜抑制に転じる（**biphasic dose response**）。**用量の意味が他デバイスと逆向きになる**——これがこの章の中心です。


![左＝PBM：赤色・近赤外の光子が細胞に届くだけで、ミトコンドリアの構造（外膜・内膜・クリステ・mtDNA）は保たれたまま、電子伝達系やATP産生、転写因子の活性が"調節"される。右＝熱損傷型デバイス：高出力の熱で凝固ゾーンができ、タンパク変性・膜破壊・mtDNA損傷が起き、そこから創傷治癒応答が始まる。中央の矢印が示すとおり**入口が違う**。図の注意書きは「非熱的作用と"温度が絶対に上がらない"は同義ではない」](figures/pbm_PBMと熱損傷の違い.png)


## 1　入口が「傷」ではないから、用量の意味が逆になる

ここまでのデバイス各章で使ってきた道具立て——「どれだけ壊すか」「procollagen I:III 比」「profibrosisリスク」——は、PBMには**そのままでは効きません**。壊していないので、評価の軸が「どれだけ壊して、どんな質の線維で埋めたか」から、**「細胞のエネルギー状態と適応応答を、どちらに、どれだけ動かせたか」**に変わります。

用量の扱いも、この入口の違いからそのまま出てきます。

| | 傷ベースのデバイス | PBM |
|---|---|---|
| 入口 | 熱・機械力による組織の損傷 | 酵素（CcO）への光吸収 |
| 用量を上げると | 損傷が深く広くなる（単調） | 促進 → 頭打ち → 無効〜抑制（二相性） |
| 押さえどころ | 強さと瘢痕リスクのトレードオフ | 効くのは限られた"窓"の中だけ。外れれば同じ機器でも動かない |

**酵素に吸わせる系は、飽和し、過剰では逆に振れます。** 壊す系のように「積めば積むほど」にはなりません。§2〜§3でその入口の分子を、§4でこの二相性そのものを扱い、§5で適応ごとの臨床エビデンスに落とします。

## 2　光を吸うのは cytochrome c oxidase（CcO＝complex IV）

![上段＝内膜の電子伝達系（複合体I→III→cyt c→IV→V）に、赤色・近赤外光が複合体IVに差し込む図。下段＝主流仮説の5段：①光の照射→②CcOに結合したNOの解離→③電子伝達／プロトン勾配の調節→④ATP合成酵素（複合体V）→⑤ATP変化。⑤には「?」が添えられ、増加・減少のいずれもあり得ると明示。最下段の「エビデンスの限界」欄は、直接効果が検出されない実験があること、変化が微小・一過性で検出困難なこと、代替の光受容体・経路も報告されていることを挙げる](figures/pbm_PBM_CcOとATP.png)

光が細胞に何かをさせるには、**光を吸う分子（chromophore／photoacceptor）**が要ります。吸われなかった光は素通りするだけです。PBMで最も有力視されているのが **cytochrome c oxidase（CcO）＝電子伝達系の complex IV**（[[electron-transport]]）。

[[electron-transport]]で complex IV は、電子を最後に **O₂ に渡して H₂O にする**電子伝達系の出口でした。CcOは内部に **銅中心（CuA・CuB）と heme a/a3** という金属中心を持ち、これらが **red（~630–660nm）と near-infrared（~810–850nm）**の吸収帯を持ちます。PBMの作用波長がこの2帯に集中しているのは、**CcOが吸う色だから**という理屈です。

主流の仮説は次の3段です。

1. ふだん **NO（一酸化窒素）**が CcO に結合し、O₂ と競合して電子伝達を**部分的に抑制**していることがある（とくに低酸素・炎症・ストレス下）。
2. red/NIR光が CcO に吸われると、その**結合NOが光で解離（photodissociation）**する。
3. 抑制が解除されて **complex IV の電子伝達が回復**し、**プロトン勾配が高まり、ATP synthase（complex V）が回って ATP産生が上がる**。

[[electron-transport]]の図（電子の落差→H⁺の坂→ATP）に、**左端から光が差し込んで complex IV の律速を外す**と重ねて読んでください。[[electron-transport]]で学んだ「**酸素消費 ≠ ATP産生**」の逆向きにあたります——PBMは complex IV の律速を外して、同じ呼吸鎖からより効率よくATPを引き出そうとする。

## 3　その先で動くもの：軽度ROSと retrograde signaling

![ミトコンドリアから核へ向かう候補シグナルを4本並べる：①ATP/ADP比の変化 ②軽度ROS ③NO ④細胞質Ca²⁺の変動。核側の出口はredox応答（Nrf2など）・遺伝子発現・修復/増殖の調節。下段の帯は**ROSの用量依存的な二面性**——低レベル＝シグナル領域、中間＝細胞種と状況で有益にも有害にも、高レベル＝酸化ストレス領域。図の結語は「分子変化が臨床美容効果を保証するわけではない」](figures/pbm_ミトコンドリアから核へのシグナル.png)

ATPが上がるだけなら話は単純ですが、二相性の理由は**二次シグナル**の側にあります。

| 二次シグナル | 何が起きるか | 押さえどころ |
|---|---|---|
| **軽度ROS** | 電子伝達が動くと副産物として一過性・低量のROSが出る | **"損傷を起こすROS"と"シグナルとして働くROS"は量が違う**。低量は適応応答のスイッチになりうる（→ [[oxidative-stress]]） |
| **retrograde signaling** | ミトコンドリアの状態変化（ATP・ROS・膜電位・Ca²⁺）が核へ「代謝が動いた」と返す | **Nrf2**（抗酸化・解毒遺伝子のマスター転写因子）などが動きうる |
| **その他** | cAMP、細胞内Ca²⁺、解離して局所で働くNO | 変化しうるという報告があるが、寄与の大きさは不明 |

ROSがシグナルの域から酸化ストレスの域へ移る境目があること——これが§4の二相性の分子的な理由になります。

> **"第二の受容体"問題**：CcO以外の光受容体として、**opsin（OPN2/OPN3/OPN5）や温度感受性のCaチャネル**がヒト皮膚で同定されています。ただし一次データはほぼ**青色光（415〜453 nm）と980 nm**のもので、**本章が扱う red/NIR（630〜850 nm）への寄与を直接示したデータはありません**。しかも皮膚で最も確からしい opsin の作用は「青色光→OPN3→melanogenesis」——**PBMの効能側ではなく色素沈着側**の経路です。この章では「CcO＝主流」「opsin/TRP＝別の波長域で実在するが、red/NIR PBM への寄与は未確定」と切り分けます。

**「軽度ROS→Nrf2→臨床改善」という鎖には、未検証の矢印が複数あります**（※ → 巻頭「本教材が守る切り分け」）。

## 4　【核心】biphasic dose response（Arndt-Schulz）

![横軸＝光の用量、縦軸＝生物学的応答。曲線は「不足＝反応が小さい」→「適正域＝促進が観察されうる（最適ウィンドウ）」→「過剰＝無効〜抑制／ストレス」でベースラインを割り込む。下段は、波長・照射強度・照射時間・照射距離・細胞と組織の状態が変わると**ウィンドウの位置と幅そのものが動く**ことを示す。結語は「強く長く当てるほど効く、ではない」「曲線は条件ごとに変わる」](figures/pbm_biphasic.png)

> **PBMは biphasic dose response（二相性用量反応、Arndt-Schulz曲線）に従います。** 低用量では促進、用量を上げると効果が頭打ちになり、さらに上げると無効化・むしろ抑制に転じる。**「たくさん当てれば効く」は、PBMでははっきり誤りです。**

低用量では §2〜§3 の「CcO活性化→ATP↑→適応的な軽度ROS」が働きます。用量を上げすぎると、**ROSがシグナルの域を超えて酸化ストレス（損傷）の域に入り**、さらに過剰な光は光化学的・（強度によっては）熱的な負荷になって、正味の効果が消える・逆転する——これが説明の骨格です（Huang 2009／Hamblin 2017）。

効くのは **「波長・出力（irradiance）・総照射量（fluence）・照射時間・距離」が噛み合った"窓（window）"の中だけ**です。窓を外せば、同じ機器でも動かない。だから **"効かなかった"の多くはパラメータ外し**であり、**"当てるほど良い"は生化学的に否定されます**。

ここで冒頭の事実が効いてきます。**機器の設定項目が波長と照射時間だけで、irradiance と fluence の表示がない場合、自分がこの曲線のどこにいるかを外から確認する手立てがありません。** 窓の位置と幅は波長・照射距離・組織の状態でも動くので、他機種の照射条件をそのまま持ち込む根拠にもなりません。

## 5　適応ごとに、機序の確からしさと臨床効果の確からしさがずれる

![左＝赤色/近赤外（約620–1100nm）：光子がヒト皮膚細胞のミトコンドリアに届き、内膜のCcOに吸収されて電子伝達・redox・ATPを調節するという主流仮説。右＝青色光（約405–470nm）：光は毛穴の皮脂内にいる*Cutibacterium acnes*の**内因性porphyrin**に吸収され、酸素依存的に¹O₂・ROSを発生させて菌の脂質・タンパク・DNAを酸化損傷する。両者は標的分子も標的細胞も違う。図の結語は「LED＝すべて同じ機序、ではない」](figures/pbm_赤色光と青色光の作用点.png)

| 適応 | 臨床エビデンスの現状 |
|---|---|
| **創傷治癒・組織修復** | ATP↑・線維芽細胞の増殖/遊走促進という機序と整合し、慢性創傷などで比較的支持されている（機種・条件のばらつき大） |
| **口腔粘膜炎（oral mucositis）** | がん治療関連の口腔粘膜炎ではガイドラインで推奨されるレベルまで来ている。抗炎症・鎮痛の一部は機序とも整合 |
| **育毛（androgenetic alopecia）** | LLLT/LEDデバイスで一定の報告はあるが、機器・波長・照射計画で結果のばらつきが大きく、効果量・持続は未確立の部分が多い |
| **美容的なしわ・肌質改善** | red/NIRでコラーゲン産生の促進を示す報告はあるが、パラメータ依存・小規模・短期が多い。**最も控えめに語るべき領域** |
| **ニキビ（acne）** | 赤色光の抗炎症はPBM的だが、青色光（~415nm）は**別機序**（下記） |

青色光のニキビ治療は、**Cutibacterium acnes の内因性porphyrin（coproporphyrin III など）に吸われて、光線力学的に ROS を発生させ菌を傷害する**反応です。標的分子も標的細胞もCcOではありません。**「LED＝全部PBM」と一括りにしないこと。**

> **この章に固有の切り分けは「機序の確からしさと臨床効果の確からしさが、適応ごとにずれている」ことです。** 創傷治癒・口腔粘膜炎はやや堅く、育毛・しわは機器とパラメータ依存で未確立が多い。適応ごとのこの差を保ったまま扱います。

PBMは**出口で他デバイスと合流しうる**——ATP↑・炎症収束の後押しは、他デバイス後の修復支援という文脈で語られます。ただし併用プロトコルの臨床的優位はまだ確立していません。


## この章の到達点

1. **PBMだけは組織を壊さない。** 他デバイスが「制御された損傷で創傷治癒を起動する」のに対し、PBMの入口は**非侵襲・非加熱の光吸収**。だから「量より質」「procollagen I:III 比」という傷の道具立てが効かない。
2. **入口の分子は cytochrome c oxidase（CcO＝complex IV）**（[[electron-transport]]）。**CuA/CuB・heme a/a3** が red(~630–660nm)/NIR(~810–850nm)を吸収する。主流の仮説は、CcO結合NOの光解離→電子伝達↑→プロトン勾配↑→**ATP産生↑**、加えて**軽度ROS→retrograde signaling→Nrf2**。opsin/TRPなど"第二の受容体"は**有望だが未確定**。
3. **【核心】だから用量の意味が他デバイスと逆向きになる。** biphasic dose response（Arndt-Schulz）：低用量で促進、高用量で無効〜抑制。**「たくさん当てれば効く」は誤り**。効くのは波長・出力・照射量が噛み合った"窓"の中だけで、**irradiance・fluenceの表示がなければ窓のどこにいるかを確認できない**。
4. **臨床効果は適応でエビデンスの質が大きく違う**。創傷治癒・口腔粘膜炎はやや堅く、育毛・しわは機器/パラメータ依存で未確立が多い。ニキビの青色光は**porphyrin経由の別機序**でPBMと混同しない。

![6枚の要点カード：①入口（低い光負荷で細胞応答を調節）②主流仮説（CcO／NO／呼吸鎖）③二次信号（ATP・ROS・NO・Ca²⁺の変化）④二相性（不足・適正域・過剰）⑤別機序（青色光が細菌のポルフィリンに吸収され酸素依存的にROSを生成）⑥評価（機序の確かさと臨床効果は別）。最下段は「波長・用量・細胞状態で反応が変わる」と、比喩の行き過ぎを戒める一行「光は栄養素としての燃料ではない」](figures/pbm_まとめ.png)

### Evidence meter

- red/NIR光の主要chromophoreが cytochrome c oxidase（complex IV）である：**確立した生化学（吸収スペクトル・分光学）／皮膚での寄与比率は一部推定**
- 光でCcO結合NOを解離→電子伝達↑→ATP産生↑（NO photodissociation仮説）：**確立しつつある細胞生物学（主流仮説）／in vivoヒト皮膚での定量は限定的**
- 一過性の軽度ROS→retrograde signaling→Nrf2 などの適応応答：**確立した細胞生物学の枠組み／PBM特異的な因果の鎖には未検証の矢印あり**
- opsin/TRP など"第二の受容体"が皮膚に存在すること：**ヒト皮膚細胞・ex vivo ヒト皮膚で確認済み**
- それらの red/NIR PBM 効果への寄与：**未確立（一次データは青色光と980 nmに限られる）**
- **biphasic dose response（Arndt-Schulz）＝多すぎると無効/抑制**：**確立した細胞生物学（PBMの基本原則）**
- 「強く長く当てるほど効く」：**否定的（生化学的に誤り）**
- 慢性創傷・組織修復での臨床効果：**製剤・条件ごとに検証が必要（比較的支持あり）**
- がん治療関連の口腔粘膜炎（oral mucositis）でのPBM：**臨床エビデンスやや堅い（ガイドライン推奨レベルの領域）／機序と整合**
- 育毛（AGA）への効果：**製剤・パラメータごとに検証が必要（ばらつき大・未確立多い）**
- 美容的しわ改善（red/NIR）：**未確立寄り（小規模・短期・パラメータ依存）**
- 青色光ニキビ治療：**porphyrin経由の光線力学的機序＝CcO経由PBMとは別物**
- 他デバイス後の修復支援としての併用：**未確立（生化学的にはありうる）**

### 中核参考文献

- Hamblin MR. Mechanisms and applications of the anti-inflammatory effects of photobiomodulation. *AIMS Biophys.* 2017;4(3):337-361. PMID: 28748217. DOI: 10.3934/biophy.2017.3.337.（NO/CcO・biphasicを含む機序総説）
- Karu TI, Afanas'eva NI. Cytochrome c oxidase as the primary photoacceptor upon laser exposure of cultured cells to visible and near IR-range light [ロシア語原著]. *Dokl Akad Nauk.* 1995;342(5):693-695. PMID: 7670387.（CcO＝primary photoacceptor仮説の原典。英語原著ではない点に注意）
- de Freitas LF, Hamblin MR. Proposed mechanisms of photobiomodulation or low-level light therapy. *IEEE J Sel Top Quantum Electron.* 2016;22(3):7000417. PMID: 28070154. DOI: 10.1109/JSTQE.2016.2561201.（機序の整理）
- Huang YY, Chen AC, Carroll JD, Hamblin MR. Biphasic dose response in low level light therapy. *Dose Response.* 2009;7(4):358-383. PMID: 20011653.（Arndt-Schulz曲線）
- 口腔粘膜炎（PBM）：Zadik Y, Arany PR, Fregnani ER, et al. Systematic review of photobiomodulation for the management of oral mucositis in cancer patients and clinical practice guidelines. *Support Care Cancer.* 2019;27(10):3969-3983. PMID: 31286228.／全体ガイドライン: Elad S, Cheng KKF, Lalla RV, et al. MASCC/ISOO clinical practice guidelines for the management of mucositis secondary to cancer therapy. *Cancer.* 2020;126(19):4423-4431. PMID: 32786044.
- 青色光/ニキビ（porphyrin機序）：Ashkenazi H, Malik Z, Harth Y, Nitzan Y. Eradication of Propionibacterium acnes by its endogenic porphyrins after illumination with high intensity blue light. *FEMS Immunol Med Microbiol.* 2003;35(1):17-24. PMID: 12589953.／Patwardhan SV, et al. Measuring acne using Coproporphyrin III, Protoporphyrin IX, and lesion-specific inflammation. *Arch Dermatol Res.* 2017;309(3):159-167. PMID: 28180934.（coproporphyrin III優位を支持。ただし"主要"の定義で強調点が変わり、単一数値で断定はできない）

> 本章§4の biphasic dose response は、用量が単調でない介入を読むときの土台になります（cold plasmaのRONS用量 → [[plasma]]）。
> [[plasma]]では、同じ「壊さない」側にもう一つの装置が出てきます。「プラズマ」と呼ばれるものは2系統で、窒素プラズマは制御された熱損傷の仲間ですが、cold atmospheric plasma は電離ガスが作る **RONS（reactive oxygen and nitrogen species）** で細胞に信号を送ります。PBMが光で cytochrome c oxidase に届くのに対し、そちらは化学種そのものを届ける——**損傷を入口にしない治療**の、もう一つの形です。
> なお、エネルギーではなく**分子そのものを組織に置く**注入系（肌育 → [[skin-boosters]]／神経筋接合部でSNAP-25を切るボツリヌストキシン → [[botulinum]]）は、デバイス各論を終えてから扱います。
