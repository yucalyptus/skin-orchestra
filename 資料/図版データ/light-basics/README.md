# 吸収曲線のデータと再生成

2026-10-27取得。再生成：`.venv/bin/python 資料/図版データ/light-basics/plot_absorption.py`（matplotlib・numpy）。SVGをfiguresへ、目視確認用PNGを/tmpへ出力。

- hemoglobin.html： https://omlc.org/spectra/hemoglobin/summary.html 。Scott Prahl編、Gratzer/Kolliasデータ。モル吸光係数から `2.303 × 150 / 64500` を掛けて吸収係数cm^-1へ換算。酸素化・脱酸素化ともHb150 g/Lの条件。CSVは抽出値。
- hale73.txt： https://omlc.org/spectra/water/data/hale73.txt 。Hale GM, Querry MR. Appl Opt. 1973;12:555–563. DOI:10.1364/AO.12.000555。配布表の波長nm・吸収係数cm^-1を使用。
- メラノソーム： https://omlc.org/spectra/melanin/mua.html 。皮膚用の近似 `1.70e12 × wavelength_nm**(-3.48)`。実測点ではなく近似線。旧図では400–1000 nmに使用し、現行の標的対応図では1100 nmまで表示（下記参照）。Jacques SL, McAuliffe DJ. Photochem Photobiol. 1991;53:769–775を参照するOMLC解説。

異なる濃度・存在状態の吸収係数を並べた図。各物質の皮膚内寄与や皮膚全体の吸収係数を示さない。曲線外への外挿なし。波長マーカーは代表的治療波長の位置であり、測定点・推奨設定ではない。

総覧図の改訂：400–1100 nmは線形軸で広く、1100–12000 nmは対数軸で圧縮。旧SVGを保持。代表的な脱毛レーザーの755 / 810 / 1064 nmは比較試験（https://pubmed.ncbi.nlm.nih.gov/16336886/）でも確認。ダイオードの810 nmは代表例であり全機種共通ではない。

### 図2：標的対応の改訂
- 主図 `light-basics_クロモフォア吸収スペクトル_標的対応.svg`。旧版保持。
- Hb 400–1000 nmは従来のPrahl公開表、1000–1100 nmは https://omlc.org/news/feb15/generic_optics/bloodSuzaki.dat を使用。OMLCがSuzaki 2006のデータを1000 nmでGratzer/Kolliasに合わせた補正済みデータ。生の実測値だけの連続曲線とは呼ばない。単位cm^-1で追加の150g/L換算は不要。
- 出典説明：https://omlc.org/news/feb15/generic_optics/index.html 。メラニンは同近似式を1100 nmまで表示し、それを超えて外挿しない。
- 1064 nmはHbピークではない。この公開表では酸素化Hbの広い山は約925–935 nm。1064 nmでは吸収が残ることと深達性を区別する。
- 臨床標的の点は吸収強度・適応一覧・優劣を示すものではない。532/1064は複数標的を示す。1064色素作用はAnderson1989 PMID2746004、血管はSadick2001 https://jamanetwork.com/journals/jamadermatology/fullarticle/478337 を参照。

### 本文幅での再構成
現行図の生成は `.venv/bin/python 資料/図版データ/light-basics/plot_readable.py`。
- `light-basics_吸収曲線_可視近赤外_本文幅.svg`：400–1100 nm、Hb直接ラベル、可視帯、波長と標的。
- `light-basics_吸収曲線_赤外水_本文幅.svg`：水の赤外吸収のみ。両軸対数。
- `light-basics_熱緩和_時間軸.svg`：同じ時間軸にTRT、パルス、照射終了時の熱の広がりを配置。二つのパルスの面積は同じ（0.8×0.95＝3.8×0.2）で同じ吸収エネルギーを示す模式図。
データ源・換算は前述と同じ。旧生成スクリプトと旧図は保存。7 inch幅、最小11.5 ptの文字を使用。700 pxレンダリングでは約16 px。図中のタイトルと技術注は本文・キャプション・折りたたみへ移動した。

### v3（2026-10-27、Claude）
`.venv/bin/python 資料/図版データ/light-basics/plot_spectrum_v3.py`。データと換算は本文幅版と同じ。文字の重なりとはみ出しを除き、ヘモグロビンの実線・破線を凡例で示し、治療波長の段を曲線の直下に寄せた。本文幅版のSVGは保持。
