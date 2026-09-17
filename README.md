# tech-notes

> Plain-language IT notes for non-engineers, built around clickable diagrams.

給看不懂術語的人的 IT 白話筆記。每一頁只處理一個「看不懂」的具體場面，例如架構圖、錯誤訊息、專案資料夾，圖上的方塊點下去就有說明。網站在 https://hsuiris.github.io/tech-notes/ 。

[![網站](https://img.shields.io/badge/demo-hsuiris.github.io%2Ftech--notes-E8447D)](https://hsuiris.github.io/tech-notes/)
![HTML](https://img.shields.io/badge/HTML-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-1572B6?logo=css&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-vanilla-F7DF1E?logo=javascript&logoColor=black)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-222222?logo=githubpages&logoColor=white)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey)

![tech-notes 首頁，八個主題以卡片列出](docs/screenshots/home.png)

## 頁面

| 頁面 | 解決什麼 |
|---|---|
| [看懂架構圖](https://hsuiris.github.io/tech-notes/architecture.html) | 看到方塊跟箭頭的圖就腦袋一片空白 |
| [看懂錯誤訊息](https://hsuiris.github.io/tech-notes/errors.html) | 跳出一大串紅字，不知道要看哪一行 |
| [看懂專案資料夾](https://hsuiris.github.io/tech-notes/project.html) | 打開別人的 repo，滿滿的檔案不敢碰 |
| [自己做一個 Claude 技能](https://hsuiris.github.io/tech-notes/skills.html) | 每次都要跟 AI 重複交代同一件事 |
| [幾個 AI 一起做事，有幾種組法](https://hsuiris.github.io/tech-notes/agents.html) | 大家都說要派很多 AI，但到底怎麼派 |
| [系統設計的基本元件與取捨](https://hsuiris.github.io/tech-notes/sysdesign.html) | 大家都說要加快取加佇列，但什麼時候該加 |
| [一個 AI 產品，從資料到上線](https://hsuiris.github.io/tech-notes/mlsystem.html) | 聽得懂每個字，但不知道它們怎麼串起來 |
| [ML System Design 的 45 分鐘](https://hsuiris.github.io/tech-notes/mldesign.html) | 知道要答什麼，但不知道怎麼開場 |

## 可以點的圖解

### 架構圖：點方塊看說明

架構圖上的每個方塊都可以點。點「後端 API」之後，下方會列出它是什麼、為什麼要有它、沒有它會怎樣，縮寫也會補上英文全名跟中文意思。

![架構圖頁，點開後端 API 方塊後的說明](docs/screenshots/architecture-api.png)

### AI 大軍：八種組法對照

左邊選一種組法，右邊會換成那種組法的示意圖，再寫出適合什麼題目、什麼情況不要用、成本怎麼算，以及這個想法從哪裡來。

![AI 大軍頁，選了主管派工之後的說明卡](docs/screenshots/agents-boss.png)

### 專案資料夾：點檔案看能不能改

檔案樹裡每個檔案都標了類型（你寫的、產生的、設定、別人的）。點 `.env` 會說明它放的是密碼跟金鑰，可以改，但不能上傳。

![專案資料夾頁，點開 .env 之後的說明](docs/screenshots/project-env.png)

錯誤訊息頁可以用關鍵字搜尋常見錯誤，架構圖頁跟 ML 系統頁的名詞解碼器也可以搜尋。系統設計頁跟面試頁用分頁切換不同題目，Claude 技能頁的指令旁邊有複製按鈕。

## 寫作規則

1. 術語第一次出現，後面用括號解釋一句。縮寫一律補上英文全名跟中文意思。
2. 不貼整段錯誤訊息，只留關鍵那一行並翻成中文。
3. 能點就不要只用讀的，圖上每個方塊、每一層、每一站都可以點開看說明。
4. 繁體中文，國中生看得懂的程度。不確定就直說「我不確定」。
5. 只用台灣慣用語，不用大陸用語、不從英文硬翻。專業術語直接寫英文原文，後面括號註明白話。
6. 不用破折號。標題底下不放引言，語氣客觀不下斷言。

## 技術架構

沒有用任何框架，每一頁就是一個 HTML 檔，改完重新整理瀏覽器就看得到。

| 部分 | 做法 |
|---|---|
| 頁面 | 每個主題一個 HTML 檔，頁面專屬的樣式跟程式寫在同一個檔案裡 |
| 互動 | vanilla JavaScript（瀏覽器內建的 JavaScript，不裝套件）處理點擊、搜尋、分頁切換 |
| 圖解 | inline SVG（直接寫在 HTML 裡的向量圖），方塊可以用滑鼠點，也可以用鍵盤選 |
| 樣式 | `assets/base.css` 全站共用，淺色、深色主題跟著系統設定切換 |
| 捲動效果 | `assets/reveal.js` 讓區塊捲到畫面裡才浮出來，系統開了「減少動態效果」就不做 |
| 字體 | 資源圓體，用 `build.py` 砍成只留站上用到的字 |
| 部署 | GitHub Pages（GitHub 免費的靜態網站空間），直接發布 `main` 分支的根目錄 |

## 本機預覽

開一個小伺服器就好：

```bash
git clone https://github.com/hsuiris/tech-notes.git
cd tech-notes
python3 -m http.server 8000
```

然後打開 http://localhost:8000 。

直接用瀏覽器開 `index.html` 也行，只是字體檔可能載不到。

## 專案結構

```
tech-notes/
├── index.html          首頁
├── architecture.html   看懂架構圖
├── errors.html         看懂錯誤訊息
├── project.html        看懂專案資料夾
├── skills.html         自己做一個 Claude 技能
├── agents.html         幾個 AI 一起做事
├── sysdesign.html      系統設計
├── mlsystem.html       一個 AI 產品，從資料到上線
├── mldesign.html       ML System Design 的 45 分鐘
├── assets/
│   ├── base.css        全站共用樣式
│   ├── reveal.js       捲動浮出效果
│   └── rhr-*.woff2     瘦身後的字體檔
├── build.py            字體瘦身程式
└── docs/screenshots/   README 用的截圖
```

## 加一頁新的

1. 複製 `errors.html` 當範本，改掉 `<title>`、`<header>`、內容。
2. 在**所有頁面**的 `<nav>` 加一個連結，並在自己那頁的連結加上 `aria-current="page"`。
3. 在 `index.html` 的 `.cards` 加一張卡片。
4. 跑一次 `python3 build.py`（見下一節）。新頁面如果用了舊字體檔沒有的字，不跑的話那些字會顯示成系統預設字體。

## 字體

用 [資源圓體 Resource Han Rounded TW](https://github.com/CyanoHao/Resource-Han-Rounded)（思源黑體的圓角繁中版，開源）。

原始字體檔一個 9MB，太重。`build.py` 會掃過所有 HTML 跟 CSS，把字體砍成只留站上真的用到的字，瘦身後一個檔案約 220KB。

```bash
pip install fonttools brotli

# 下載原始字體，解壓後把 ttf 放進 fonts/
# https://github.com/CyanoHao/Resource-Han-Rounded/releases → RHR-TW-*.7z

python3 build.py
```

`fonts/*.ttf` 太大，沒有放進 git。`assets/*.woff2`（瘦身後的網頁字體檔）有放進 git，所以**不跑 build.py 網站也能正常顯示**，只有新增了現有字體檔沒涵蓋的字才需要重跑。

字體檔缺字的話，畫面不會壞掉，缺的字會改用系統內建的蘋方（PingFang TC）。

## 授權

內容 CC BY 4.0。字體依 [SIL Open Font License 1.1](https://github.com/CyanoHao/Resource-Han-Rounded/blob/master/LICENSE.txt)。
