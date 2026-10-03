# Qwen3.5-122B-A10B

官方模型卡：[Qwen/Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

## 授權

license 欄：apache-2.0。license_link：https://huggingface.co/Qwen/Qwen3.5-122B-A10B/blob/main/LICENSE。

## 發佈日期

卡上未列。表頭的 GPT-5-mini 2025-08-07 是對照欄名稱，不是這個檢查點的發佈日。

## 參數與卡上句子

- 卡上文字：122B in total and 10B activated。
- 256 experts，8 Routed + 1 Shared，expert intermediate 1024。
- Context Length: 262,144 natively and extensible up to 1,010,000 tokens。
- safetensors 索引的參數總數 125086497008（BF16 125086490096、F32 6912）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `text_config`。
- model_type：qwen3_5_moe_text
- 層數 num_hidden_layers：48
- hidden size：3072
- attention heads：32
- KV heads：2
- head dim：256
- MoE intermediate：1024
- shared expert intermediate：1024
- 專家數 num_experts：256
- 每 token 專家數：8
- max_position_embeddings：262144
- vocab size：248320
- vision_config：hidden_size=1152，model_type=qwen3_5_moe

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：39 個檔，250173250864 bytes，換算 232.99 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| MMLU-Pro | 86.7 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| MMLU-Redux | 94.0 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| C-Eval | 91.9 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| SuperGPQA | 67.1 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| IFEval | 93.4 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| IFBench | 76.1 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| MultiChallenge | 61.5 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| AA-LCR | 66.9 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| LongBench v2 | 60.2 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| HLE w/ CoT | 25.3 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| GPQA Diamond | 86.6 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| HMMT Feb 25 | 91.4 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| HMMT Nov 25 | 90.3 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| SWE-bench Verified | 72.0 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| Terminal Bench 2 | 49.4 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| LiveCodeBench v6 | 78.9 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| CodeForces | 2100 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| OJBench | 39.5 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| FullStackBench en | 62.6 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| FullStackBench zh | 58.7 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| BFCL-V4 | 72.2 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| TAU2-Bench | 79.5 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| VITA-Bench | 33.6 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| DeepPlanning | 24.1 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| HLE w/ tool | 47.5 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| Browsecomp | 63.8 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| Browsecomp-zh | 69.9 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| WideSearch | 60.5 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| Seal-0 | 44.1 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| MMMLU | 86.7 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| MMLU-ProX | 82.2 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| NOVA-63 | 58.6 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| INCLUDE | 82.8 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| Global PIQA | 88.4 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| PolyMATH | 68.9 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| WMT24++ | 78.3 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| MAXIFE | 87.9 | 表 1 欄「Qwen3.5-122B-A10B」。 |
| MMMU | 83.9 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| MMMU-Pro | 76.9 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| MathVision | 86.2 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| Mathvista(mini) | 87.4 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| DynaMath | 85.9 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| ZEROBench | 9 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| ZEROBench_sub | 36.2 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| VlmsAreBlind | 96.7 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| BabyVision | 40.2 / 34.5 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| RealWorldQA | 85.1 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| MMStar | 82.9 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| MMBench EN-DEV-v1.1 | 92.8 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| SimpleVQA | 61.7 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| HallusionBench | 67.6 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| OmniDocBench1.5 | 89.8 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| CharXiv(RQ) | 77.2 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| MMLongBench-Doc | 59.0 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| CC-OCR | 81.8 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| AI2D_TEST | 93.3 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| OCRBench | 92.1 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| ERQA | 62.0 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| CountBench | 97.0 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| RefCOCO(avg) | 91.3 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| ODInW13 | 44.5 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| EmbSpatialBench | 83.9 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| RefSpatialBench | 69.3 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| LingoQA | 80.8 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| Hypersim | 12.7 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| SUNRGBD | 36.2 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| Nuscene | 15.4 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| VideoMME (w sub.) | 87.3 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| VideoMME (w/o sub.) | 83.9 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| VideoMMMU | 82.0 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| MLVU | 87.3 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| MVBench | 76.6 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| LVBench | 74.4 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| MMVU | 74.7 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| ScreenSpot Pro | 70.4 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| OSWorld-Verified | 58.0 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| AndroidWorld | 66.4 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| TIR-Bench | 53.2 / 42.5 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| V* | 93.2 / 90.1 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| SLAKE | 81.6 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| PMC-VQA | 63.3 | 表 2 欄「Qwen3.5-122B-A10B」。 |
| MedXpertQA-MM | 67.3 | 表 2 欄「Qwen3.5-122B-A10B」。 |
