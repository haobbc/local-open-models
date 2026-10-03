# Qwen3.6-35B-A3B

官方模型卡：[Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

## 授權

license 欄：apache-2.0。license_link：https://huggingface.co/Qwen/Qwen3.6-35B-A3B/blob/main/LICENSE。

## 發佈日期

卡上未列。「February release」那句講的是 Qwen3.5，不是這個檢查點的日期。

## 參數與卡上句子

- 卡上文字：Number of Parameters: 35B in total and 3B activated。
- 卡上文字：Number of Experts: 256；Activated Experts: 8 Routed + 1 Shared；Expert Intermediate Dimension: 512。
- 卡上文字：Context Length: 262,144 natively and extensible up to 1,010,000 tokens。
- 比較表有兩張。表 1 的欄名是 Qwen3.6-35BA3B，表 2 是 Qwen3.6-35B-A3B。不採用旁邊的 Qwen3.5-35B 欄。
- safetensors 索引的參數總數 35951822704（BF16 35951822704）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `text_config`。
- model_type：qwen3_5_moe_text
- 層數 num_hidden_layers：40
- hidden size：2048
- attention heads：16
- KV heads：2
- head dim：256
- MoE intermediate：512
- shared expert intermediate：512
- 專家數 num_experts：256
- 每 token 專家數：8
- max_position_embeddings：262144
- vocab size：248320
- vision_config：hidden_size=1152，model_type=qwen3_5_moe

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：26 個檔，71903776776 bytes，換算 66.97 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| SWE-bench Verified | 73.4 | 表 1 欄「Qwen3.6-35BA3B」。 |
| SWE-bench Multilingual | 67.2 | 表 1 欄「Qwen3.6-35BA3B」。 |
| SWE-bench Pro | 49.5 | 表 1 欄「Qwen3.6-35BA3B」。 |
| Terminal-Bench 2.0 | 51.5 | 表 1 欄「Qwen3.6-35BA3B」。 |
| Claw-Eval Avg | 68.7 | 表 1 欄「Qwen3.6-35BA3B」。 |
| Claw-Eval Pass^3 | 50.0 | 表 1 欄「Qwen3.6-35BA3B」。 |
| SkillsBench Avg5 | 28.7 | 表 1 欄「Qwen3.6-35BA3B」。 |
| QwenClawBench | 52.6 | 表 1 欄「Qwen3.6-35BA3B」。 |
| NL2Repo | 29.4 | 表 1 欄「Qwen3.6-35BA3B」。 |
| QwenWebBench | 1397 | 表 1 欄「Qwen3.6-35BA3B」。 |
| TAU3-Bench | 67.2 | 表 1 欄「Qwen3.6-35BA3B」。 |
| VITA-Bench | 35.6 | 表 1 欄「Qwen3.6-35BA3B」。 |
| DeepPlanning | 25.9 | 表 1 欄「Qwen3.6-35BA3B」。 |
| Tool Decathlon | 26.9 | 表 1 欄「Qwen3.6-35BA3B」。 |
| MCPMark | 37.0 | 表 1 欄「Qwen3.6-35BA3B」。 |
| MCP-Atlas | 62.8 | 表 1 欄「Qwen3.6-35BA3B」。 |
| WideSearch | 60.1 | 表 1 欄「Qwen3.6-35BA3B」。 |
| MMLU-Pro | 85.2 | 表 1 欄「Qwen3.6-35BA3B」。 |
| MMLU-Redux | 93.3 | 表 1 欄「Qwen3.6-35BA3B」。 |
| SuperGPQA | 64.7 | 表 1 欄「Qwen3.6-35BA3B」。 |
| C-Eval | 90.0 | 表 1 欄「Qwen3.6-35BA3B」。 |
| GPQA | 86.0 | 表 1 欄「Qwen3.6-35BA3B」。 |
| HLE | 21.4 | 表 1 欄「Qwen3.6-35BA3B」。 |
| LiveCodeBench v6 | 80.4 | 表 1 欄「Qwen3.6-35BA3B」。 |
| HMMT Feb 25 | 90.7 | 表 1 欄「Qwen3.6-35BA3B」。 |
| HMMT Nov 25 | 89.1 | 表 1 欄「Qwen3.6-35BA3B」。 |
| HMMT Feb 26 | 83.6 | 表 1 欄「Qwen3.6-35BA3B」。 |
| IMOAnswerBench | 78.9 | 表 1 欄「Qwen3.6-35BA3B」。 |
| AIME26 | 92.7 | 表 1 欄「Qwen3.6-35BA3B」。 |
| MMMU | 81.7 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| MMMU-Pro | 75.3 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| Mathvista(mini) | 86.4 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| ZEROBench_sub | 34.4 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| RealWorldQA | 85.3 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| MMBench EN-DEV-v1.1 | 92.8 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| SimpleVQA | 58.9 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| HallusionBench | 69.8 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| OmniDocBench1.5 | 89.9 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| CharXiv(RQ) | 78.0 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| CC-OCR | 81.9 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| AI2D_TEST | 92.7 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| RefCOCO(avg) | 92.0 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| ODInW13 | 50.8 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| EmbSpatialBench | 84.3 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| RefSpatialBench | 64.3 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| VideoMME (w sub.) | 86.6 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| VideoMME (w/o sub.) | 82.5 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| VideoMMMU | 83.7 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| MLVU | 86.2 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| MVBench | 74.6 | 表 2 欄「Qwen3.6-35B-A3B」。 |
| LVBench | 71.4 | 表 2 欄「Qwen3.6-35B-A3B」。 |
