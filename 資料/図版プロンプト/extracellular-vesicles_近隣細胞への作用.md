# EVが近隣の細胞に作用する仕組み

- 作成日：2026-10-06
- 図版：`figures/extracellular-vesicles_近隣細胞への作用.png`
- 方法：組み込み image_gen、新規 PNG（1536×1024）。
- 対応箇所：『細胞外小胞とエクソソーム』第 3 節。
- 目的：表面の分子が受容体に作用する経路と、取り込み後に内容物が細胞質へ届く経路を区別する。
- 確認：view_image で実画像を点検。上の EV は細胞外に保たれ、受容体の細胞内側からシグナルが続く。下は内向きの膜陥入による取り込み、閉じたエンドソーム内の膜小胞を描き、内容物の移動を二つの膜を越える破線として示した。『条件によって異なる』『働く場所へ届くことが必要』の条件付き表現あり。全小胞に RNA を描いておらず、核への到達や美容効果を示さない。細胞・小胞の大きさは模式的。

## 生成プロンプト

Use case: scientific-educational.
Create ONE original Japanese medical-textbook raster illustration, landscape 3:2, clean white background, polished soft 3D membrane drawing, consistent with a textbook illustration of teal vesicles, coral lipid-bilayer cell membranes, pale blue transparent cytoplasm and dark navy Japanese sans-serif labels. The visual should explain actual cell structures and membrane topology, not boxes containing paragraphs. Keep labels large, few and correctly written. All text Japanese except EV and RNA.

Title at top: 「EVが近隣の細胞に作用する仕組み」.

Layout: left 30% a rounded pale-blue donor cell in cross-section, cropped at left margin, coral plasma membrane boundary, labelled above 「EVを放出する細胞」. Show 3 small closed teal membrane vesicles emerging near its right boundary into the white extracellular gap in the center. No detailed biogenesis mechanism here, no MVB necessary. Short restrained blue arrows guide individual teal EVs across the intercellular space towards the receiver at right. Label one moving vesicle 「EV」. Small teal membrane vesicles are filled with soft pale-blue lumen; occasional tiny gold protein dots or one purple short RNA curve can show different contents, not EVERY vesicle with RNA. EVs have a few gold surface molecules.

Right 60% one LARGE neighboring receiving cell in section, pale blue cytoplasm and continuous coral plasma membrane with gently curved nearly vertical LEFT EDGE at about 55% of total image width. Entire receiver interior extends to the right of this membrane. Above receiver label 「近隣の細胞」. Its left facing membrane accommodates TWO clearly separated pathways, top and bottom. One readable simple receptor and EV contact on upper part; one invagination plus endosome on lower part. No obligatory nucleus, no RNA entering nucleus, no collagen, no beauty/treatment outcome.

UPPER PATH (at about 35% height): a teal EV remains OUTSIDE the receiving cell, left of the receptor. A GOLD ligand protruding from EV surface touches the receptor extracellular domain. A PURPLE receptor visibly spans the coral cell membrane exactly once: extracellular domain to left, transmembrane segment within bilayer, cytoplasmic tail to right in pale-blue cytoplasm. To the RIGHT of the receptor intracellular tail, a short arrow points to 3 small purple signal dots deeper inside the recipient, label 「細胞内シグナル」. Text above this pathway 「表面の分子が受容体に作用」. Fine leader label 「受容体」 points only to the purple membrane-spanning protein. EV STAYS OUTSIDE, not merging into receptor or entering cell, no arrow conveying EV inside at upper pathway.

LOWER PATH (at about 65% height): receiving cell plasma membrane is invaginated toward the RIGHT (INTO receiving cell interior) to wrap ONE closed teal EV. Show a narrow-neck inward plasma membrane pocket containing the teal EV, followed to the RIGHT by a fully separate CLOSED coral membrane ENDOSOME entirely inside cytoplasm. Short navy arrow from inward invagination toward endosome indicates uptake. Small text near invagination 「エンドサイトーシス」. Large clear label above the detached intracellular organelle 「エンドソーム」.
This endosome is a cross-section circle at x about 78%, with its own clearly continuous enclosing coral bilayer membrane. It contains ONE smaller separately closed teal EV, so the content is surrounded by BOTH its own EV membrane AND the endosome membrane. The smaller EV within endosome may show a couple gold dots and a purple short RNA curve. Pale lumen inside endosome visibly differs from outside pale-blue cytoplasm. Both closed membranes must be obvious; EV is not floating freely in cytoplasm.
From inside the small EV through its enclosing teal membrane and then through the enclosing coral endosome membrane, draw a THIN DASHED teal arrow to a few tiny gold dots and one purple RNA curve in the CYTOPLASM to the lower right of the endosome. Make the dashed arrow direction outward from endosome into cytoplasm, and use dashed style only for this conditional cargo-delivery process. Do not erase or open the membranes: arrow crosses the two membranes schematically to show barriers must be overcome. Label the few released cytoplasmic illustrative objects 「タンパク質・RNAなど」 and directly beneath in smaller navy text 「条件によって異なる」.
A single clearly readable note below the lower pathway, inside clear whitespace, states 「内容物が出て、働く場所へ届くことが必要」. This is a conditional requirement, not a guarantee of escape.
No endosome-to-nucleus arrow. Avoid graphic implying all uptake gives an effect. No list of beneficial effects. Do not label receptor binding as content delivery.

Scientific constraints: receptor orientation extracellular left / intracellular right; endocytosis into right-side cytoplasm; intact EV held inside separate intact endosome membrane; dashed cargo delivery as conditional; receiving plasma membrane separate from endosome membrane; extracellular vesicles never drawn as cells with nuclei. Cell boundaries continuous except a physically clear uptake invagination, no extra disconnected membrane fragments. Use only minimal labels listed, no long legends, no numbered boxes or paragraph flowchart. Large generous white space and readable labels. Main structures may be magnified and schematic.
