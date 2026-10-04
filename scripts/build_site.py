#!/usr/bin/env python3
"""Rebuild the GitHub Pages homepage, terminology, and scatter data from repo numbers."""

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COPY = "本站由 Cursor／Grok Bot 自主完成的本地模型研究。"
COLORS = {
    "b32": "#b7e4c7",
    "b96": "#a9c7f5",
    "b128": "#ffe08a",
    "b192": "#f6c48a",
    "bover": "#f4b4b4",
}

PARAMS = {
    "Qwen3.8-27B": "27B",
    "K2-Horizon-MoVA-36B-A4B": "36B／啟動 4B",
    "G9v3-39A5B": "約 39B／啟動約 5B",
    "K2-Horizon-7B": "7B",
    "Qwen3.6-35B-A3B": "35B／啟動 3B",
    "Muse-Glimmer-30B": "約 29.6B",
    "gemma-4-26B-A4B-it": "25.2B／啟動 3.8B",
    "granite-4.2-30b": "30B",
    "gemma-4-31B-it": "30.7B",
    "Qwen3.5-9B": "9B",
    "Qwen3.8-Flash-Next": "125B／啟動 6B；n-gram 51B",
    "Ling-3.0-flash-VL": "124B／啟動 5.5B",
    "Ling-3.0-flash-Fin": "124B／啟動 5.1B",
    "Qwen3.5-122B-A10B": "122B／啟動 10B",
    "Mistral-Medium-3.5-128B": "128B 稠密",
    "NVIDIA-Nemotron-3-Super-120B-A12B-BF16": "120B／啟動 12B",
    "gpt-oss-120b": "117B／啟動 5.1B",
    "gpt-oss-20b": "21B／啟動 3.6B",
    "GLM-5.3-Flash": "320B／啟動 18B",
    "Ornith-1.5-35B-A3B": "約 35B／啟動約 3B",
    "K2-Think-V2": "70B",
    "LongCat-Flash-Lite": "68.5B／啟動 2.9–4.5B",
    "Mistral-Small-4-119B-2603": "119B／啟動 6.5B",
    "Hypernova-60B-2605": "60B／啟動 4.8B",
    "MiMo-V2.6-Pro-RL": "1.02T／啟動 42B",
    "GLM-5.3": "",
    "Kimi-K3": "2.8T／啟動 104B",
    "Qwen3.8-2.4T-A95B": "2.4T／啟動 95B",
    "DeepSeek-V4.1-Flash": "骨幹 552B；prefill 8B，decode 16B",
    "MiniMax-M3": "約 428B／啟動約 23B",
}
DATES = {
    "NVIDIA-Nemotron-3-Super-120B-A12B-BF16": "2026-03-11",
    "Muse-Glimmer-30B": "2026-08",
    "granite-4.2-30b": "2026-08-25",
    "Hypernova-60B-2605": "26/02/2026",
}
# slug, pack, display, number, unit. Only figures already written in the repo.
EXTRAS = [
    ("Qwen3.8-27B", "q4_k_m 實測", "17.77 GB", 17.77, "GB"),
    ("Qwen3.8-27B", "q8_0 實測", "29.12 GB", 29.12, "GB"),
    ("Qwen3.8-27B", "BF16 實測", "54.66 GB", 54.66, "GB"),
    ("Qwen3.8-Flash-Next", "UD-IQ4_XS 載入", "87.24 GiB", 87.24, "GiB"),
    ("Qwen3.8-Flash-Next", "UD-IQ4_XS 磁碟", "93.68 GB", 93.68, "GB"),
    ("Qwen3.8-Flash-Next", "unsloth 4-bit 所列", "112 GB", 112.0, "GB"),
    ("K2-Horizon-MoVA-36B-A4B", "Q4 粗算", "約 16.8 GiB", 16.8, "GiB"),
    ("G9v3-39A5B", "Q4 粗算", "約 18.2 GiB", 18.2, "GiB"),
    ("K2-Horizon-7B", "Q4 粗算", "約 3.3 GiB", 3.3, "GiB"),
    ("Qwen3.6-35B-A3B", "Q4 粗算", "約 16.3 GiB", 16.3, "GiB"),
    ("Muse-Glimmer-30B", "Q4 粗算", "約 14.0 GiB", 14.0, "GiB"),
    ("gemma-4-26B-A4B-it", "Q4 粗算", "約 11.7 GiB", 11.7, "GiB"),
    ("granite-4.2-30b", "Q4 粗算", "約 14.0 GiB", 14.0, "GiB"),
    ("gemma-4-31B-it", "Q4 粗算", "約 14.3 GiB", 14.3, "GiB"),
    ("gemma-4-31B-it", "Q8 粗算", "約 28.6 GiB", 28.6, "GiB"),
    ("Qwen3.5-9B", "Q4 粗算", "約 4.5 GiB", 4.5, "GiB"),
    ("Ling-3.0-flash-VL", "Q4 粗算", "約 57.7 GiB", 57.7, "GiB"),
    ("Ling-3.0-flash-Fin", "Q4 粗算", "約 57.7 GiB", 57.7, "GiB"),
    ("Qwen3.5-122B-A10B", "Q4 粗算", "約 56.8 GiB", 56.8, "GiB"),
    ("Mistral-Medium-3.5-128B", "Q4 粗算", "約 59.6 GiB", 59.6, "GiB"),
    ("NVIDIA-Nemotron-3-Super-120B-A12B-BF16", "Q4 粗算", "約 56.2 GiB", 56.2, "GiB"),
    ("gpt-oss-120b", "4-bit 粗算", "約 54.5 GiB", 54.5, "GiB"),
    ("GLM-5.3-Flash", "Q4 粗算", "約 149 GiB", 149.0, "GiB"),
    ("MiniMax-M3", "Q4 粗算", "約 199 GiB", 199.0, "GiB"),
    ("DeepSeek-V4.1-Flash", "骨幹 Q4 粗算", "約 257 GiB", 257.0, "GiB"),
    ("GLM-5.3", "Q4 粗算", "約 351 GiB", 351.0, "GiB"),
    ("MiMo-V2.6-Pro-RL", "Q4 粗算", "約 475 GiB", 475.0, "GiB"),
    ("Qwen3.8-2.4T-A95B", "Q4 粗算", "約 1118 GiB", 1118.0, "GiB"),
    ("Kimi-K3", "原生 MXFP4 粗算", "約 1304 GiB", 1304.0, "GiB"),
]
# name, slug or None, score text, sort value
AA = [
    ("Claude Opus 5.5（max）", None, "58", 58),
    ("GPT-6 Astra（max）", None, "53", 53),
    ("Gemini 4 Argon（high）", None, "53", 53),
    ("Grok 4.7（xhigh）", None, "46", 46),
    ("MiMo-V2.6-Pro-RL", "MiMo-V2.6-Pro-RL", "46", 46),
    ("GLM-5.3-Flash", "GLM-5.3-Flash", "42", 42),
    ("Qwen3.8-Flash-Next", "Qwen3.8-Flash-Next", "40", 40),
    ("Qwen3.8-27B", "Qwen3.8-27B", "34", 34),
    ("K2-Horizon-MoVA-36B-A4B", "K2-Horizon-MoVA-36B-A4B", "25", 25),
    ("Ling-3.0-flash-VL", "Ling-3.0-flash-VL", "25", 25),
    ("Ling-3.0-flash-Fin", "Ling-3.0-flash-Fin", "23", 23),
    ("G9v3-39A5B", "G9v3-39A5B", "22", 22),
    ("K2-Horizon-7B", "K2-Horizon-7B", "21", 21),
    ("Ling 3.0 Flash", None, "20", 20),
    ("Qwen3.6-35B-A3B", "Qwen3.6-35B-A3B", "18", 18),
    ("Qwen3.5-122B-A10B", "Qwen3.5-122B-A10B", "18", 18),
    ("Muse-Glimmer-30B", "Muse-Glimmer-30B", "17", 17),
    ("gemma-4-26B-A4B-it", "gemma-4-26B-A4B-it", "17", 17),
    ("granite-4.2-30b", "granite-4.2-30b", "15", 15),
    ("gemma-4-31B-it", "gemma-4-31B-it", "15", 15),
    ("Mistral-Medium-3.5-128B", "Mistral-Medium-3.5-128B", "14", 14),
    ("Gemma 4 12B", None, "14（估計）", 14),
    ("NVIDIA-Nemotron-3-Super-120B-A12B-BF16", "NVIDIA-Nemotron-3-Super-120B-A12B-BF16", "13", 13),
    ("gpt-oss-120b", "gpt-oss-120b", "12", 12),
    ("Qwen3.5-9B", "Qwen3.5-9B", "11", 11),
    ("gpt-oss-20b", "gpt-oss-20b", "9", 9),
]

# Exact explanation text -> (category, plain sentence). Only texts that match a name on the site.
PLAIN = {
    "長任務或專家評分。高分較好。": ("other", "很長的任務，或專家給的分數。高分比較好。"),
    "長上下文（AA-LCR、LongBench、RULER、MRCR）。高分代表長文裡仍答得準。長度標記（64K、128K、256K、1M）要分開。": ("long", "長文裡還答不答得準。64K、128K、256K、1M 要分開看。高分比較好。"),
    "代理人或辦公室長任務。高分代表完成較多。Pass@1 與另一個 Score 若寫在同一格，圖上不拆。": ("tool", "做一串辦公室或代理人任務。高分代表做完的比較多。同一格有兩個數就整格看。"),
    "AA-Omniscience：事實是否答對，以及不亂答的比例。Accuracy 與 Non-Hallucination 是兩列。高分較好。": ("know", "事實有沒有答對，以及會不會亂答。兩項分開。高分比較好。"),
    "AGIEval：考試風格的選擇與生成題。高分較好。": ("know", "考試形式的選擇與作答。高分比較好。"),
    "圖文理解、文件、圖表或視覺數學。高分通常較好。OmniDocBench 若寫的是 edit distance，低分較好，那一列的名字裡會標出來。": ("vision", "看圖、文件、圖表，或圖裡的數學。高分通常比較好。名字若寫 edit distance 或低分較好，則低分比較好。"),
    "程式題（LiveCodeBench、Codeforces、HumanEval、SciCode、AIDER 等）。分數或 rating 愈高，代表解題較多或對手段位較高。": ("code", "寫程式解題。分數或等級越高，解掉的題越多，或對手段位越高。"),
    "數學競賽或數學應用題（AIME、HMMT、MATH、GSM8K 等）。高分代表解對較多。不同年份是不同卷。": ("math", "數學競賽或應用題。高分代表算對比較多。不同年份是不同考卷。"),
    "軟體工程：在真實或仿真的程式庫裡改程式（SWE-bench、DeepSWE、NL2Repo、FrontierSWE 等）。高分代表解掉較多任務。Verified、Pro、Multilingual 是不同題集。": ("code", "在真實或模擬的程式庫裡改程式。高分代表完成的題比較多。Verified、Pro、多語是不同題組。"),
    "Terminal-Bench：在終端裡完成任務。2.0、2.1、3.0、4.0 與 Terminus、Claude Code 等 harness 要分開看。高分較好。": ("pc", "在終端機裡完成任務。版本和操作方式不同，要分開看。高分比較好。"),
    "Android 介面或程式任務。高分較好。": ("pc", "Android 畫面或程式任務。高分比較好。"),
    "操作電腦、手機或瀏覽器的介面任務。高分代表任務完成較多。": ("pc", "操作電腦、手機或瀏覽器畫面。高分代表完成的任務比較多。"),
    "Arena-Hard：模型對戰的勝率風格分數。不是 LMArena 文字榜的 Elo。高分較好。": ("know", "模型對打的勝率分數。不是 LMArena 文字榜。高分比較好。"),
    "這是模型卡自己引用的 Artificial Analysis 指數。Ling-VL 這格是 v4.1.1 的 42，不是本榜快照 v4.3.2 的 25。": ("score", "模型卡自己引的 Artificial Analysis 總分。Ling-VL 這格是 v4.1.1 的 42，不是首頁那張 v4.3.2。"),
    "BigBench / BBEH：多樣任務的推理集合。高分較好。": ("know", "很多種推理題放在一起。高分比較好。"),
    "BBH：難度較高的語言推理題組。高分較好。": ("know", "比較難的語言推理題。高分比較好。"),
    "安全或偏見。卡上寫 lower is better 或帶 ↓ 的項目，低分較好；拒絕有害請求的比例則是高分較好。": ("safe", "安全或偏見。標了低分較好或 ↓ 的，低分比較好。拒絕有害請求的比例則是高分比較好。"),
    "工具呼叫與 MCP 任務（BFCL、Toolathlon、MCP-Atlas、MCPMark）。高分代表叫對工具或完成任務。": ("tool", "會不會正確呼叫工具或 MCP。高分代表叫對或做完。"),
    "BIRD / BirdBench：自然語言轉 SQL。高分較好。": ("code", "把人話轉成 SQL。高分比較好。"),
    "網頁瀏覽或搜尋（BrowseComp、WideSearch、DeepSearch）。高分代表找到的答案較準。各卡的上下文協議可能不同。": ("tool", "上網找答案。高分代表找得比較準。各卡的上下文設定可能不同。"),
    "C-Eval：中文多科考試題。高分較好。": ("know", "中文多科考試。高分比較好。"),
    "CI Memories：情境隱私。Violation 低分較好；Coverage 高分較好。": ("safe", "情境裡的隱私。Violation 低分比較好。Coverage 高分比較好。"),
    "MMLU：多科選擇題。高分代表答對較多。": ("know", "多科選擇題。高分代表答對比較多。"),
    "CVBench：視覺理解。高分較好。": ("vision", "看懂畫面。高分比較好。"),
    "K2 Think 的 Safety-4 巨觀分數。高分代表該安全面向較好；卡上把 Data & Infrastructure 標成 Critical。": ("safe", "安全面向的總分。高分代表該面向比較好。Data & Infrastructure 在卡上被標成 Critical。"),
    "醫療、法律或金融專業題。高分較好。": ("other", "醫療、法律或金融的專業題。高分比較好。"),
    "CritPt：物理前沿推理。高分較好。": ("know", "前沿物理推理。高分比較好。"),
    "資安任務（CyberGym、ExploitGym、ExploitBench、SEC Bench）。高分代表通過較多題。時間預算不同的格子要分開。": ("safe", "資安題。高分代表通過比較多。時間限制不同的分數要分開。"),
    "DROP：需要離散推理的閱讀理解，卡上指標是 F1。高分較好。": ("know", "要一步步算的閱讀理解，分數是 F1。高分比較好。"),
    "長程規劃、產品文件或工作區任務。高分較好。": ("other", "長程規劃、產品文件或工作區任務。高分比較好。"),
    "空間、駕駛或具身視覺題。高分較好，除非該列另寫低分較好。": ("vision", "空間、開車或身體感知的視覺題。高分比較好，除非該列另寫低分較好。"),
    "Frontier-Bench：Ornith 卡上的這個名稱。卡上沒有寫題目內容。圖上只跟同一名稱比，高分較好。": ("other", "Ornith 卡上的名稱。卡上沒寫題目內容。高分比較好。"),
    "GDPval：辦公產出的評分，卡上有的記 Elo、有的記分數。只跟同一欄的寫法比。高分較好。": ("tool", "辦公產出的分數。有的記 Elo、有的記分數，只跟同一種寫法比。高分比較好。"),
    "GPQA：研究生程度的科學問答，Diamond 是較難子集。高分較好。": ("know", "研究所程度的科學題。Diamond 是比較難的那一組。高分比較好。"),
    "GAIA：多步問答。高分較好。": ("tool", "要分好多步的問答。高分比較好。"),
    "Global PIQA：多語言的物理常識選擇。高分較好。": ("know", "多種語言的物理常識選擇。高分比較好。"),
    "HLE（Humanity's Last Exam）：跨領域難題。有的卡分「無工具／有工具」或「只要文字子集」，不能跟總分混成一根。高分較好。": ("know", "跨很多領域的難題。有沒有開工具、是不是只考文字，都是不同分數。高分比較好。"),
    "化學與生物預備性評測。高分代表該知識題答對較多；卡上把它們放在風險討論裡，不是本榜的能力名次。": ("safe", "化學與生物的知識題。高分代表答對比較多。卡上放在風險討論，不是能力名次。"),
    "HellaSwag：句子接龍常識。高分較好。": ("know", "句子接下去怎麼寫才合理。高分比較好。"),
    "指令遵循（IFEval、IFBench、MultiChallenge）。高分代表較常照格式與限制做。": ("know", "照指示的格式與限制做。高分代表比較常做到。"),
    "INCLUDE：多語言知識題。高分較好。": ("know", "多語知識題。高分比較好。"),
    "廠商自建的程式、資安或視覺題。高分較好。": ("code", "廠商自己出的程式、資安或視覺題。高分比較好。"),
    "影片理解。高分較好。有字幕與無字幕是不同設定。": ("vision", "看影片作答。高分比較好。有字幕和沒字幕是不同考法。"),
    "MMLU-Pro：比 MMLU 更難的多科選擇題。高分代表答對較多。": ("know", "比一般 MMLU 更難的多科選擇題。高分代表答對比較多。"),
    "MMLU-Redux：MMLU 的訂正版多科題。高分較好。": ("know", "訂正過的 MMLU 多科題。高分比較好。"),
    "MedXpertQA：醫學多模態題。高分較好。": ("know", "醫學圖文題。高分比較好。"),
    "MultiLoKo：多語言長知識。高分較好。": ("know", "多語的長知識。高分比較好。"),
    "NOVA-63：多語言題組。高分較好。": ("know", "多語題。高分比較好。"),
    "醫學圖文問答。高分較好。": ("vision", "醫學圖片問答。高分比較好。"),
    "視覺問答或感知題。高分較好。": ("vision", "看圖回答或知覺題。高分比較好。"),
    "PostTrainBench：後訓練相關任務。高分較好。": ("other", "後訓練相關任務。高分比較好。"),
    "ProfBench：專業任務。高分較好。": ("other", "專業任務。高分比較好。"),
    "廠商自己的網頁、SVG 或代理人題。高分較好。只在該卡的欄位裡比較。": ("other", "廠商自己的網頁、SVG 或代理人題。高分比較好。只跟同一欄比。"),
    "ResearchRubrics：研究任務的量表。高分較好。": ("other", "研究任務的評分表。高分比較好。"),
    "SEC Bench：資安修補或利用題。高分較好。": ("safe", "資安修補或利用題。高分比較好。"),
    "SaaS 操作任務。高分較好。": ("pc", "操作 SaaS。高分比較好。"),
    "多輪挑戰題。高分較好。": ("know", "多輪對話的挑戰題。高分比較好。"),
    "SimpleQA：短事實問答，看會不會亂編。高分較好。": ("know", "短事實問題，看會不會亂編。高分比較好。"),
    "SuperGPQA：研究生程度的多科問答。高分較好。": ("know", "研究所程度的多科問答。高分比較好。"),
    "τ³ / Tau / TAU2：多輪工具呼叫（航空、零售、銀行、電信等）。高分代表任務完成較多。": ("tool", "多輪叫工具。場景有航空、零售、銀行、電信。高分代表做完的比較多。"),
    "視覺推理或指向題。卡上若有兩種條件，整格保留，不拆成名次。": ("vision", "視覺推理，或指出圖裡的位置。一格若有兩種條件，整格一起看。"),
    "WMT：機器翻譯。高分較好。": ("know", "翻譯。高分比較好。"),
}
CATS = [
    ("score", "總分"),
    ("know", "知識與考試"),
    ("math", "數學"),
    ("code", "程式"),
    ("pc", "操作電腦"),
    ("tool", "工具與代理人"),
    ("long", "長文"),
    ("vision", "看圖與文件"),
    ("safe", "安全"),
    ("other", "其他"),
]


def esc(s):
    return html.escape(s if s is not None else "", quote=True)


def band_of(n):
    if n <= 32:
        return "b32", "≤32"
    if n <= 96:
        return "b96", "≤96"
    if n <= 128:
        return "b128", "≤128"
    if n <= 192:
        return "b192", "≤192"
    return "bover", ">192"


def td_style(band):
    if not band:
        return ""
    return f' style="background:{COLORS[band]};color:#1c1915"'


def row(cells, band=None):
    st = td_style(band)
    return "<tr>" + "".join(f"<td{st}>{c}</td>" for c in cells) + "</tr>"


def link_model(slug, title, prefix=""):
    if not slug:
        return esc(title)
    return f'<a href="{prefix}models/{esc(slug)}.md">{esc(title)}</a>'


def legend():
    labels = [
        ("b32", "≤32　顯卡"),
        ("b96", "≤96　顯卡"),
        ("b128", "≤128　系統記憶體"),
        ("b192", "≤192　系統記憶體"),
        ("bover", ">192　放不下"),
    ]
    bits = [
        f'<span class="swatch" style="background:{COLORS[k]};color:#1c1915">{esc(lab)}</span>'
        for k, lab in labels
    ]
    return "<p>" + "".join(bits) + "</p>"


def table(headers, rows_html):
    th = "".join(f"<th>{esc(h)}</th>" for h in headers)
    return f'<div class="wrap"><table><thead><tr>{th}</tr></thead><tbody>{"".join(rows_html)}</tbody></table></div>'


def load_card():
    raw = (ROOT / "charts" / "data.js").read_text(encoding="utf-8")
    raw = raw.split("=", 1)[1].strip()
    if raw.endswith(";"):
        raw = raw[:-1]
    return json.loads(raw)


def license_of(text):
    if "Modified MIT" in text:
        return "Modified MIT"
    m = re.search(r"license_name(?:：| 是 | 為 )([^。\s]+)", text)
    if m:
        return m.group(1)
    m = re.search(r"license 欄：([^。\s]+)", text)
    return m.group(1) if m else ""


def shell(title, body, depth=""):
    css = f"{depth}assets/site.css"
    nav = (
        f'<nav><a href="{depth}">權重</a>'
        f'<a href="{depth}terminology.html">名詞</a>'
        f'<a href="{depth}scatter/">散點圖</a>'
        f'<a href="{depth}charts/">模型卡圖</a></nav>'
    )
    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
<main>
{nav}
{body}
<footer>{esc(COPY)}</footer>
</main>
</body>
</html>
"""


def main():
    old = (ROOT / "README.md").read_text(encoding="utf-8")
    for token in [
        "17.77", "29.12", "54.66", "87.24", "93.68", "112 GB", "16.8", "18.2",
        "3.3", "16.3", "14.0", "11.7", "14.3", "28.6", "4.5", "57.7", "56.8",
        "59.6", "56.2", "54.5", "149", "199", "257", "351", "475", "1118", "1304",
        "4.66", "7.93", "7.92", "11.77", "28.02", "27.92", "23.26", "95.3", "95.7",
        "1525", "v4.3.2",
    ]:
        if token not in old:
            raise SystemExit(f"old README missing {token}")

    data = load_card()
    titles = {w["slug"]: w["title"] for w in data["weights"]}
    files = {w["slug"]: w for w in data["weights"]}
    lics = {}
    for slug in titles:
        lics[slug] = license_of((ROOT / "models" / f"{slug}.md").read_text(encoding="utf-8"))

    weight_rows = []
    for w in data["weights"]:
        weight_rows.append({
            "slug": w["slug"],
            "title": w["title"],
            "date": DATES.get(w["slug"], ""),
            "params": PARAMS[w["slug"]],
            "lic": lics[w["slug"]],
            "pack": w["label"],
            "size": f"{w['gib']:.2f} GiB",
            "n": w["gib"],
            "unit": "GiB",
        })
    for slug, pack, display, num, unit in EXTRAS:
        weight_rows.append({
            "slug": slug,
            "title": titles[slug],
            "date": DATES.get(slug, ""),
            "params": PARAMS[slug],
            "lic": lics[slug],
            "pack": pack,
            "size": display,
            "n": num,
            "unit": unit,
        })
    for g in data["gguf"]:
        if g["name"].startswith("mmproj"):
            continue
        slug = "Ornith-1.5-35B-A3B"
        weight_rows.append({
            "slug": slug,
            "title": titles[slug],
            "date": "",
            "params": PARAMS[slug],
            "lic": lics[slug],
            "pack": g["name"],
            "size": f"{g['gib']:.2f} GiB",
            "n": g["gib"],
            "unit": "GiB",
        })
    weight_rows.sort(key=lambda r: (r["n"], r["title"].lower(), r["pack"]))

    whtml = []
    for r in weight_rows:
        b, lab = band_of(r["n"])
        whtml.append(row([
            link_model(r["slug"], r["title"]),
            esc(r["date"]),
            esc(r["params"]),
            esc(r["lic"]),
            esc(r["pack"]),
            esc(r["size"]),
            esc(lab),
        ], b))

    aa_sorted = sorted(AA, key=lambda r: (-r[3], r[0]))
    aa_html = []
    for name, slug, score, _sort in aa_sorted:
        title = titles.get(slug, name) if slug else name
        if slug and slug in files:
            b, lab = band_of(files[slug]["gib"])
            size = f'{files[slug]["gib"]:.2f} GiB'
        else:
            b, lab, size = None, "", ""
        aa_html.append(row([
            link_model(slug, title),
            esc(score),
            esc(size),
            esc(lab),
        ], b))

    arena_html = [row([
        "Gemini 4 Argon（high）",
        "1525",
        "2026-10-02",
        "Preliminary，文字榜榜首",
    ])]

    # vendor tables: same name, at least two models, single numeric only
    groups = {}
    for p in data["plotted"]:
        key = p["name"]
        groups.setdefault(key, []).append(p)
    vendor_blocks = []
    series = []
    for name in sorted(groups, key=lambda s: s.lower()):
        rows = groups[name]
        lower = any(r.get("lower") for r in rows)
        rows_sorted = sorted(rows, key=lambda r: (r["value"] if lower else -r["value"], r["title"]))
        bucket = rows[0]["bucket"]
        heading = name
        if bucket == "unit":
            heading += "（0–1）"
        if lower:
            heading += "（低分較好）"
        sid = "v" + str(len(series))
        series.append({
            "id": sid,
            "group": "廠商自報",
            "name": heading,
            "lower": lower,
            "rows": [{
                "slug": r["model"],
                "title": r["title"],
                "y": r["value"],
                "raw": r["raw"],
            } for r in rows],
        })
        if len({r["model"] for r in rows}) < 2:
            continue
        body = []
        for r in rows_sorted:
            gib = files[r["model"]]["gib"]
            b, lab = band_of(gib)
            body.append(row([
                link_model(r["model"], r["title"]),
                esc(str(r["raw"])),
                esc(lab),
            ], b))
        vendor_blocks.append(f"<h3>{esc(heading)}</h3>" + table(["模型", "分數", "區間"], body))

    speed = [
        ("Qwen3.8-27B", "BF16", "54.66 GB", 54.66, "4.66 t/s"),
        ("Qwen3.8-27B", "q8_0", "29.12 GB", 29.12, "7.93 t/s；同機 vLLM FP8 7.92 t/s"),
        ("Qwen3.8-27B", "q4_k_m", "17.77 GB", 17.77, "11.77 t/s"),
        ("Qwen3.8-Flash-Next", "UD-IQ4_XS", "載入 87.24 GiB", 87.24, "28.02 t/s"),
    ]
    speed_html = []
    for slug, pack, size, num, rate in speed:
        b, lab = band_of(num)
        speed_html.append(row([
            link_model(slug, titles[slug]) + " " + esc(pack),
            esc(size),
            esc(lab),
            esc(rate),
            "未測",
            "未測",
        ], b))

    body = f"""
<h1>開源模型權重</h1>
<p class="note">快照 2026-10-03。空格是倉庫裡沒有的數字。</p>
{legend()}
<p class="note">底色用該列數字直接比 32、96、128、192，不換算 GB／GiB，不扣 KV。32 與 96 是顯卡記憶體；128 與 192 是系統／統一記憶體。權重放進顯卡，就不必溢到系統記憶體。</p>
<h2 id="weights">權重與發行日</h2>
<p class="note">一列一種包裝。粗算與實測只列倉庫裡已經寫下的數字。</p>
{table(["模型", "發行日", "參數", "授權", "包裝", "大小", "區間"], whtml)}
<h2 id="aa">Artificial Analysis</h2>
<p class="note">Intelligence Index v4.3.2。底色是主權重檔。沒有權重檔的列不上色。這張表沒有 LMArena，也沒有廠商自報。</p>
{table(["模型", "指數", "主權重檔", "區間"], aa_html)}
<h2 id="arena">LMArena</h2>
<p class="note">文字榜，2026-10-02。跟上一張表不是同一個分數。</p>
{table(["模型", "文字榜", "日期", "註"], arena_html)}
<h2 id="vendor">廠商自報</h2>
<p class="note">只收同一名稱、至少兩個模型、而且是單一數字的分數。底色仍是主權重檔。Ornith 只出現在這裡。</p>
{''.join(vendor_blocks)}
<h2 id="speed">實測速率（參考）</h2>
<p class="note">不是能力排名。iThome Day 14，機器 DGX Spark GB10，llama.cpp，未開投機解碼。獨立顯卡與混合到系統記憶體都未測。n-gram 表釘到 CPU 後 27.92 → 23.26 t/s，峰值 95.3 → 95.7 GiB，仍是同一塊統一記憶體。</p>
{table(["模型與量化", "大小", "區間", "統一記憶體", "獨立顯卡", "混合到系統記憶體"], speed_html)}
<h2>出處</h2>
<ul>
<li>權重檔：<a href="models/Qwen3.8-27B.md">models/</a>、<a href="charts/">charts/</a></li>
<li>Artificial Analysis v4.3.2，2026-10-03：<a href="https://artificialanalysis.ai/leaderboards/models">artificialanalysis.ai</a></li>
<li>LMArena 文字榜，2026-10-02：<a href="https://arena.ai/leaderboard/text/">arena.ai</a></li>
<li>速率：<a href="https://ithelp.ithome.com.tw/articles/10405431">iThome Day 14</a></li>
<li>粗算是本庫已經寫下的估計，這次沒有重算。</li>
</ul>
"""

    # terminology
    appear = {p["name"] for p in data["plotted"] + data["unplotted"]}
    by_text = {}
    for e in data["explanations"]:
        if e["name"] not in appear:
            continue
        by_text.setdefault(e["text"], set()).add(e["name"])
    missing = [t for t in by_text if t not in PLAIN]
    unused = [t for t in PLAIN if t not in by_text]
    if missing or unused:
        raise SystemExit(f"plain map mismatch missing={len(missing)} unused={len(unused)} {missing[:2]} {unused[:2]}")
    buckets = {k: [] for k, _ in CATS}
    for text, names in by_text.items():
        cat, sentence = PLAIN[text]
        buckets[cat].append((sentence, sorted(names, key=lambda s: s.lower())))
    buckets["score"].insert(0, (
        "很多題收成一個總分。數字大表示整體比較強。跟 LMArena 分開。",
        ["Artificial Analysis Intelligence Index v4.3.2"],
    ))
    buckets["score"].insert(1, (
        "真人對打後的文字榜分數。跟 Arena-Hard、跟 Artificial Analysis 都不是同一件事。",
        ["LMArena 文字榜"],
    ))
    parts = [
        "<h1>基準在量什麼</h1>",
        '<p class="note">只寫這個網站上有出現的指標。</p>',
        '<label for="q">篩名字</label><input id="q" type="search">',
    ]
    for key, label in CATS:
        items = buckets[key]
        if not items:
            continue
        chunks = [f'<h2>{esc(label)}</h2>']
        for sentence, names in items:
            blob = "、".join(names)
            chunks.append(
                f'<div class="item"><p>{esc(sentence)}</p>'
                f'<p class="names">{esc(blob)}</p></div>'
            )
        parts.append("".join(chunks))
    parts.append("""
<script>
const q = document.getElementById("q");
q.addEventListener("input", () => {
  const f = q.value.trim().toLowerCase();
  document.querySelectorAll(".item").forEach(el => {
    el.style.display = !f || el.textContent.toLowerCase().includes(f) ? "" : "none";
  });
  document.querySelectorAll("h2").forEach(h => {
    let n = h.nextElementSibling;
    let any = false;
    while (n && n.tagName !== "H2") {
      if (n.classList.contains("item") && n.style.display !== "none") any = true;
      n = n.nextElementSibling;
    }
    h.style.display = any ? "" : "none";
  });
});
</script>
""")
    term = shell("基準在量什麼", "\n".join(parts))

    index = shell("開源模型權重", body)
    readme = body + f"\n<footer>{esc(COPY)}</footer>\n"

    aa_series = []
    for name, slug, score, sort in AA:
        if not slug or slug not in files:
            continue
        aa_series.append({
            "slug": slug,
            "title": titles[slug],
            "y": sort,
            "raw": score,
        })
    plot = {
        "files": [{
            "slug": w["slug"],
            "title": w["title"],
            "gib": w["gib"],
            "pack": w["label"],
            "unit": "GiB",
        } for w in data["weights"]],
        "extras": [{
            "slug": r["slug"],
            "title": r["title"],
            "gib": r["n"],
            "pack": r["pack"],
            "unit": r["unit"],
        } for r in weight_rows if r["pack"] not in {w["label"] for w in data["weights"] if w["slug"] == r["slug"]} or r["slug"] == "___"],
        "series": [
            {"id": "aa", "group": "Artificial Analysis", "name": "Intelligence Index v4.3.2", "lower": False, "rows": aa_series},
            {"id": "arena", "group": "LMArena", "name": "文字榜", "lower": False, "rows": []},
        ] + series,
    }
    # extras: measured/estimate/gguf rows only, not the primary file row
    primary = {(w["slug"], w["label"]) for w in data["weights"]}
    plot["extras"] = [{
        "slug": r["slug"],
        "title": r["title"],
        "gib": r["n"],
        "pack": r["pack"],
        "unit": r["unit"],
    } for r in weight_rows if (r["slug"], r["pack"]) not in primary]

    (ROOT / "index.html").write_text(index, encoding="utf-8")
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    (ROOT / "terminology.html").write_text(term, encoding="utf-8")
    (ROOT / "scatter" / "data.js").write_text(
        "window.PLOT = " + json.dumps(plot, ensure_ascii=False) + ";\n",
        encoding="utf-8",
    )
    (ROOT / "_config.yml").write_text(
        "title: 開源模型權重\ndescription: 權重、發行日與基準\ntheme: jekyll-theme-cayman\n",
        encoding="utf-8",
    )
    patch_charts()
    verify(index, term)


def patch_charts():
    p = ROOT / "charts" / "index.html"
    t = p.read_text(encoding="utf-8")
    t = t.replace(
        "販商自報的分數不進 README 的 Artificial Analysis 名次。",
        "販商自報的分數不進首頁的 Artificial Analysis 表。指標說明在 <a href=\"../terminology.html\">名詞</a>。",
    )
    block = """  <h2>名稱在測什麼</h2>
  <p class="note">說明也寫在 README。這裡可以對到圖上的名稱。</p>
  <div id="explain"></div>
"""
    t = t.replace(block, "")
    start = t.find('const ex = document.getElementById("explain");')
    if start >= 0:
        end = t.find("</script>", start)
        t = t[:start] + t[end:]
    if "<nav>" not in t:
        t = t.replace(
            "<main>\n  <h1>",
            '<main>\n  <nav><a href="../">權重</a><a href="../terminology.html">名詞</a><a href="../scatter/">散點圖</a><a href="./">模型卡圖</a></nav>\n  <h1>',
            1,
        )
    t = t.replace(
        "排行榜上的 Q4 粗算與 Day 14 的 GGUF 實測不在這張圖。",
        "Q4 粗算與 Day 14 的實測不在這張圖。",
    )
    if "本站由 Cursor" not in t:
        t = t.replace("</main>", f"<footer>{COPY}</footer>\n</main>")
    if "footer { margin-top" not in t:
        t = t.replace(
            "a { color:#6e2e24; }",
            "a { color:#6e2e24; }\n  footer { margin-top:48px; color:var(--muted); font-size:.9rem; }\n  nav a { margin-right:12px; }",
        )
    p.write_text(t, encoding="utf-8")


def verify(index, term):
    aa = index.split('id="aa"')[1].split('id="arena"')[0]
    arena = index.split('id="arena"')[1].split('id="vendor"')[0]
    vendor = index.split('id="vendor"')[1].split('id="speed"')[0]
    if "Ornith" in aa:
        raise SystemExit("Ornith leaked into AA")
    if "1525" in aa or "v4.3.2" in arena:
        raise SystemExit("AA and LMArena mixed")
    if "4.66" in aa or "28.02" in vendor:
        raise SystemExit("speed mixed into capability tables")
    for bad in ["5090", "RTX", "PRO 6000", "Mac"]:
        if bad in index or bad in term:
            raise SystemExit("hardware name in page: " + bad)
    if "約 12.6" in index or "12.6 GiB" in index:
        raise SystemExit("rejected 12.6 estimate resurfaced")
    if "FinCRAFT" in term or "FinFIRST" in term:
        raise SystemExit("absent metric in terminology")
    if COPY not in index or COPY not in term:
        raise SystemExit("copyright missing")
    if "2026-03-11" not in index or "2026-08-25" not in index or "26/02/2026" not in index:
        raise SystemExit("release date missing")
    if "17.77 GB" not in index or "約 475 GiB" not in index:
        raise SystemExit("weight figure missing")
    print("ok", "weights rows", index.count("<tr>") )


if __name__ == "__main__":
    main()
