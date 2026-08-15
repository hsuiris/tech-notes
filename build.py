#!/usr/bin/env python3
"""字體瘦身：掃過站上所有頁面，只保留真的用到的字。

原始字體一個 9MB，全部塞進網站太重。這支程式把它砍成只剩用到的幾百個字，
一個檔案剩約 130KB。

用法：
    python3 build.py

需要（只要裝一次）：
    pip install fonttools brotli

字體原始檔放在 fonts/（沒有的話從這裡下載）：
    https://github.com/CyanoHao/Resource-Han-Rounded/releases → RHR-TW-*.7z
"""
import base64, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).parent
FONTS = [("fonts/ResourceHanRoundedTW-Regular.ttf", "assets/rhr-regular.woff2"),
         ("fonts/ResourceHanRoundedTW-Bold.ttf",    "assets/rhr-bold.woff2")]

# 掃描所有網頁 + 樣式表，收集用到的字元
sources = sorted(ROOT.glob("*.html")) + sorted(ROOT.glob("assets/*.css"))
chars = set()
for f in sources:
    chars |= set(f.read_text(encoding="utf-8"))

chars |= set(chr(c) for c in range(0x20, 0x7f))            # 完整 ASCII
chars |= set("，。、；：？！「」『』（）〈〉《》—…·～　"        # 常見中文標點
             "％＋－×÷＝→←↑↓★☆●○■□▲▼◆")
text = "".join(sorted(c for c in chars if c.isprintable() and c != "﻿"))
(ROOT / "subset.txt").write_text(text, encoding="utf-8")

for src, dst in FONTS:
    src_p, dst_p = ROOT / src, ROOT / dst
    if not src_p.exists():
        sys.exit(f"找不到字體原始檔：{src}\n請看這支程式最上面的說明去下載。")
    subprocess.run([sys.executable, "-m", "fontTools.subset", str(src_p),
                    f"--text-file={ROOT / 'subset.txt'}", "--flavor=woff2",
                    f"--output-file={dst_p}", "--layout-features=", "--no-hinting",
                    "--desubroutinize", "--drop-tables+=DSIG", "--name-IDs=",
                    "--notdef-outline"], check=True)
    print(f"{dst}  {dst_p.stat().st_size / 1024:.0f} KB")

(ROOT / "subset.txt").unlink()
print(f"掃了 {len(sources)} 個檔案，保留 {len(text)} 個字元。")
