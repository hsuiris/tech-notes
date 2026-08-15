# tech-notes

給看不懂術語的人的 IT 白話筆記。

**網站：https://hsuiris.github.io/tech-notes/**

每一頁只解決一個「我看不懂」的具體場面，不做百科全書。

| 頁面 | 解決什麼 |
|---|---|
| [看懂架構圖](https://hsuiris.github.io/tech-notes/architecture.html) | 看到方塊跟箭頭的圖就腦袋一片空白 |
| [看懂錯誤訊息](https://hsuiris.github.io/tech-notes/errors.html) | 跳出一大串紅字，不知道要看哪一行 |
| [按鈕之旅](https://hsuiris.github.io/tech-notes/request.html) | 知道有前端後端，但中間到底發生什麼 |
| [看懂專案資料夾](https://hsuiris.github.io/tech-notes/project.html) | 打開別人的 repo，滿滿的檔案不敢碰 |
| [自己做一個 Claude 技能](https://hsuiris.github.io/tech-notes/skills.html) | 別人的外掛很好用，但那到底是怎麼做出來的 |

## 寫作規則

1. 術語第一次出現，後面用括號解釋一句。縮寫一律補上英文全名跟中文意思。
2. 不貼整段錯誤訊息，只留關鍵那一行並翻成中文。
3. 能點就不要只用讀的——圖上每個方塊、每一層、每一站都可以點開看說明。
4. 繁體中文，國中生看得懂的程度。不確定就直說「我不確定」。

## 本機預覽

沒有建置步驟，就是靜態 HTML。直接開一個小伺服器就好：

```bash
python3 -m http.server 8000
# 然後打開 http://localhost:8000
```

（直接用瀏覽器開 `index.html` 也行，只是字體檔可能載不到。）

## 加一頁新的

1. 複製 `errors.html` 當範本，改掉 `<title>`、`<header>`、內容。
2. 在**所有頁面**的 `<nav>` 加一個連結，並在自己那頁的連結加上 `aria-current="page"`。
3. 在 `index.html` 的 `.cards` 加一張卡片。
4. 跑一次 `python3 build.py`（見下）——新頁面如果用了舊字體檔沒有的字，不跑會顯示成系統預設字體。

## 字體

用 [資源圓體 Resource Han Rounded TW](https://github.com/CyanoHao/Resource-Han-Rounded)（思源黑體的圓角繁中版，開源）。

原始字體檔一個 9MB，太重，所以用 `build.py` 砍成只留站上真的用到的字，剩下約 150KB。

```bash
pip install fonttools brotli

# 下載原始字體，解壓後把 ttf 放進 fonts/
# https://github.com/CyanoHao/Resource-Han-Rounded/releases → RHR-TW-*.7z

python3 build.py
```

`fonts/*.ttf` 沒有進版控（太大）。`assets/*.woff2` 有進版控，所以**不跑 build.py 網站也能正常顯示**——只有在你新增了現有字體檔沒涵蓋的字時才需要重跑。

漏字也不會爆掉，只會 fallback 到系統的蘋方（PingFang TC）。

## 授權

內容 CC BY 4.0。字體依 [SIL Open Font License 1.1](https://github.com/CyanoHao/Resource-Han-Rounded/blob/master/LICENSE.txt)。
