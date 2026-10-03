# Muse Glimmer 30B

官方模型卡：[meta-models/Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

## 授權

license 欄：apache-2.0。

## 發佈日期

卡上寫 Model Release Date: August 2026。

## 參數與卡上句子

- 卡上正文：30-billion-parameter causal language model。
- 總表：Total Parameters ~29.6B。Language Model 那列寫 29.6B (including vision encoder)。Perception encoder ~1.8B param ViT-G/14。
- Context length 131,072+。Knowledge cutoff January 4, 2026。
- 量化衰減表（販商自報，不進基準圖）：K-Quant-Dynamic 0.2%，K-Quant-17GB 1.0%。
- 速率表是販商自報，不進 README 的輸出速率：RTX 5090 無投機 74.9 tok/s、含 DFlash 233.4；M4 Max 23.7 / 37.8；M5 Max 26.6 / 50.2。
- safetensors 索引的參數總數 29776626688（BF16 29776626688）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `text_config`。
- model_type：muse_glimmer_text
- 層數 num_hidden_layers：52
- hidden size：6656
- attention heads：32
- KV heads：2
- head dim：128
- intermediate size：19968
- max_position_embeddings：131072
- vocab size：202048
- sliding window：2048
- vision_config：num_hidden_layers=50，hidden_size=1536，model_type=muse_glimmer_vision

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：2 個檔，59553435272 bytes，換算 55.46 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| MCP Atlas (Public) | 75.5 | 欄「Muse Glimmer-30B High Reasoning」。 |
| DeepSearch QA | 74.6 | 欄「Muse Glimmer-30B High Reasoning」。 |
| 𝛕3-Banking | 23.5 | 欄「Muse Glimmer-30B High Reasoning」。 |
| WildClawBench | 47.6 | 欄「Muse Glimmer-30B High Reasoning」。 |
| GDPVal-AA v2 | 953 | 欄「Muse Glimmer-30B High Reasoning」。 |
| Gaia2 | 43.3 | 欄「Muse Glimmer-30B High Reasoning」。 |
| SkillsBench (with skills) | 44.3 | 欄「Muse Glimmer-30B High Reasoning」。 |
| OSWorld-Verified | 65.9 | 欄「Muse Glimmer-30B High Reasoning」。 |
| SWE-Bench Pro | 51.2 | 欄「Muse Glimmer-30B High Reasoning」。 |
| SWE-Bench Verified | 76.0 | 欄「Muse Glimmer-30B High Reasoning」。 |
| TerminalBench 2.1 (with terminus2) | 51.7 | 欄「Muse Glimmer-30B High Reasoning」。 |
| SciCode | 43.6 | 欄「Muse Glimmer-30B High Reasoning」。 |
| Charxiv Reasoning | 78.8 | 欄「Muse Glimmer-30B High Reasoning」。 |
| ScreenSpot Pro | 75.4 | 欄「Muse Glimmer-30B High Reasoning」。 |
| OmniDocBench v1.5 | 75.8 | 欄「Muse Glimmer-30B High Reasoning」。 |
| MMMU Pro | 74 | 欄「Muse Glimmer-30B High Reasoning」。 |
| CI Memories Violation (↓) | 26.4 | 欄「Muse Glimmer-30B High Reasoning」。低分較好。 |
| CI Memories Coverage | 64.8 | 欄「Muse Glimmer-30B High Reasoning」。 |
| Siren AgentDojo Attack Success Rate (↓) | 28.4 | 欄「Muse Glimmer-30B High Reasoning」。低分較好。 |
| Siren AgentDojo Utility | 94.2 | 欄「Muse Glimmer-30B High Reasoning」。 |
| IFBench | 77.0 | 欄「Muse Glimmer-30B High Reasoning」。 |
| AIME 2026 | 94.7 | 欄「Muse Glimmer-30B High Reasoning」。 |
| GPQA Diamond (AA) | 83.5 | 欄「Muse Glimmer-30B High Reasoning」。 |
| HLE Text (AA) | 22.0 | 欄「Muse Glimmer-30B High Reasoning」。 |
| AA-LCR | 80.0 | 欄「Muse Glimmer-30B High Reasoning」。 |
| Beam128K | 65.1 | 欄「Muse Glimmer-30B High Reasoning」。 |
| MBCT | 41.5% | 欄「Muse Glimmer-30B」（preparedness）。 |
| HPCT | 52.3% | 欄「Muse Glimmer-30B」（preparedness）。 |
| VCT | 37.0% | 欄「Muse Glimmer-30B」（preparedness）。 |
| WMDP (Bio) | 86.5% | 欄「Muse Glimmer-30B」（preparedness）。 |
| WMDP (Chem) | 75.2% | 欄「Muse Glimmer-30B」（preparedness）。 |
| Lab Bench (ProtocolQA) | 80.2% | 欄「Muse Glimmer-30B」（preparedness）。 |
