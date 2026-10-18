# 痤瘡：毛包と炎症の比較図

- 出力：`figures/acne_毛包と炎症.png`
- 生成方式：built-in image_gen
- 生成日：2026-10-01
- 用途：正常・面皰・炎症性病変の比較。必ずこの順に進むと示す時間軸ではない。

## 最終プロンプト

```text
Use case: scientific-educational
Asset type: Japanese clinical textbook illustration, PNG, one landscape plate.
Primary request: A clear medically accurate educational comparison of THREE pilosebaceous unit cross-sections side by side, headings exactly 「正常」「面皰」「炎症性病変」. These are examples of different lesion states, do not imply an inevitable chronological progression. No arrows between panels.
Scene/backdrop: Pure white background with ample clear margins; three aligned cross sections through the skin surface and dermis.
Style/medium: Soft polished clinical textbook medical illustration, raster painting with precise anatomy and fine clean outlines, soft pale peach dermis, muted yellow sebum and sebaceous glands, warm pink inflammation. Large short Japanese labels in legible clean sans-serif, spacious leader lines.
Anatomy in each panel: Hair follicle is a continuous epithelial-lined tube opening upward at the skin surface; a fine hair shaft inside, a bulb deep below, and a lobulated sebaceous gland lateral to the upper-middle follicle connected by a short duct to the follicle. Keep anatomical positions consistent in all three panels. Skin surface extends horizontally. Sebaceous gland must be distinguishable from the hair bulb.
Normal: Patent upper follicular infundibulum with small amounts of pale yellow sebum, intact wall, a few tiny blue-purple rod-like dots INSIDE the upper follicle representing resident C. acnes, no inflammation.
Comedone: Expanded upper follicular infundibulum with a compact layered tan keratin plug near the opening and accumulated yellow sebum underneath; intact wall. A few resident bacteria dots inside the follicle. Keratin accumulation is clearly within the upper follicle, not the deep bulb.
Inflammatory lesion: Distended upper follicle with keratin and sebum, many purple immune cells accumulating OUTSIDE around follicle; local partial break of upper follicle wall, a small amount of released follicular contents in surrounding dermis, surrounding soft red inflammatory halo. Do not show a catastrophic deep wound. Show a few bacteria dots inside the follicle, and immune cells outside.
Text (verbatim): Panel headings 「正常」「面皰」「炎症性病変」. Sparse explanatory leader labels 「角質の貯留」 pointing to keratin plug in middle panel, 「皮脂腺」 pointing to a lobulated gland in normal panel, 「毛包周囲の炎症」 pointing to peri-follicular immune infiltrate in right panel, 「常在菌 C. acnes」 pointing to sparse bacterial dots in NORMAL follicle. Optional only one label 「皮脂」 to middle yellow contents.
Constraints: Need readable large Japanese typography; exact spelling. Label C. acnes as resident flora and depict in normal follicle as well. No timeline arrows, no pathway boxes, no molecular pathways, no paragraph text, no decorative symbols, no watermark, no extra title. A balanced wide composition with three equal panels taking most of the image.
```

## 検図

view_imageで生成結果を確認。日本語ラベルは「正常」「面皰」「炎症性病変」「角質の貯留」「皮脂」「皮脂腺」「毛包周囲の炎症」「常在菌 C. acnes」で、読みやすく明らかな誤字なし。正常の毛包内にも菌体、面皰の上部毛包内に角質と皮脂、炎症性病変の毛包周囲に免疫細胞と壁の一部破綻が描かれている。比較パネル間の進行矢印なし。

## 模式図の限界

解剖・細胞・菌体は説明のため単純化され、菌体や免疫細胞の大きさと数は実測を表していない。すべての面皰が炎症性病変へ進むことや、炎症に壁破綻が常に必須であることを意味しない。面皰は開放・閉鎖の別を区別しない例示。
