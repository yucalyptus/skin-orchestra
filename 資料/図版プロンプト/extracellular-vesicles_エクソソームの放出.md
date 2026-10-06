# エクソソームの放出

- 作成日：2026-10-06
- 図版：`figures/extracellular-vesicles_エクソソームの放出.png`
- 作成方法：組み込み image_gen（PNG、1536×1024）
- 目的：エンドソーム内への出芽、多胞体と細胞膜の融合、内腔小胞の放出を連続して示す。下段では細胞膜からの直接出芽を比較する。
- 点検：生成後の画像を view_image で確認。内向き出芽、多胞体外膜と細胞膜の融合、膜に包まれた小胞の放出、直接出芽の向き、日本語ラベルを確認。内容物を RNA などに固定せず、サイズや治療評価は含めない。

## 生成プロンプト

Use case: scientific-educational
Asset type: Japanese medical textbook illustration, raster PNG.
Primary request: An accurate, exceptionally clear medical illustration showing how exosomes form and are released, with a small comparison of direct plasma membrane budding. Landscape 3:2 composition on a clean white background. Detailed gentle 3D scientific illustration of lipid membranes, soft translucent blue cytoplasm, teal endosomal membranes, muted coral plasma membrane. Readable large Japanese text, dark navy rounded sans-serif. No decorative borders, no text-box flow chart.

Main illustration (upper 75% of image): one cropped portion of a cell occupies the left and middle, with extracellular space on the right. A clearly continuous roughly vertical coral plasma membrane at x about 75% separates pale-blue intracellular space (left) from white extracellular space (right). Within the cell, show three spaced successive stages from left to right, connected by two simple directional arrows:
1 at left: a cross-sectioned endosome, circular teal enclosing membrane, with a small bud growing inward into the endosomal lumen and one completed small membrane-bound intraluminal vesicle. The inward bud is visibly connected at its neck to the enclosing endosomal membrane, originating from the cytoplasmic side and projecting INTO THE LUMEN. Large label above: 「エンドソーム」. Small label below only: 「膜が内側へくぼむ」.
2 middle: a cross-sectioned multivesicular body as a closed enclosing teal membrane containing 5–6 distinctly separate small membrane-bound vesicles. Large label above: 「多胞体」. Small label below: 「内部に小さな小胞ができる」.
3 at plasma membrane: the outer enclosing membrane of the multivesicular body has fused seamlessly with the plasma membrane, creating a U-shaped open pocket connected to the extracellular space. The intraluminal vesicles remain individually membrane-enclosed as they exit THROUGH THE OPEN FUSION PORE INTO THE RIGHT-HAND EXTRACELLULAR SPACE, drawn as 4 small closed teal membrane vesicles outside, with one or two still within the open fusion pocket. A clear short outward arrow points right through this pore. The outer MVB membrane is merged with plasma membrane and never leaves as a giant extracellular vesicle. Large label near the released small vesicles: 「エクソソーム」. Label 「細胞膜」 points to the continuous coral cell boundary outside the fusion region. Small label beneath fusion region: 「細胞膜と融合して放出」.
At top left of entire main diagram, small location label 「細胞内」; at top right 「細胞外」. A simple clean content title at very top, not chapter number: 「エクソソームができるまで」.
The vesicles are hollow membrane-bound spheres with gently tinted contents; do not draw RNA helices, DNA, obligatory cargo, secreted proteins, molecular structures, a recipient cell, or nucleus.

Small clearly separate comparison strip (lower 25% with lots of white space, separated by a thin light-gray horizontal rule):
At lower left/middle show a small coral plasma membrane horizontal segment, cytoplasm beneath it, extracellular space above it. Draw an outward bud still attached by a narrow neck and beside it one detached coral membrane-bound vesicle ABOVE the membrane. The bud bulges out from the cell directly; no inner vesicles. A single short arrow shows detachment. Large label above the strip: 「細胞膜から直接出芽する小胞」. Smaller text to the right: 「エクソソームとは別の経路」.
Bottom one-line modest note centered: 「どちらも細胞外小胞（EV）の一種」.
Constraints: Scientific membrane topology is essential; show inward budding into endosomal lumen, multivesicular body outer membrane fusing with continuous cell membrane, and intact individual intraluminal vesicles becoming extracellular exosomes. Small lower diagram is direct OUTWARD plasma membrane budding, clearly distinct. Use few labels and generous whitespace; large text at typical webpage width. No English except EV; no MVB abbreviation, no quantitative size cutoff, no products/treatment claims, no chapter number, no watermark.
