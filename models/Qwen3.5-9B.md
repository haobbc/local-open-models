# Qwen3.5-9B

官方模型卡：[Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

## 授權

license 欄：apache-2.0。license_link：https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/LICENSE。

## 發佈日期

卡上未列。

## 參數與卡上句子

- 卡上文字：Number of Parameters: 9B。
- 卡上文字：Context Length: 262,144 natively and extensible up to 1,010,000 tokens。
- YAML 的 base_model 是 Qwen/Qwen3.5-9B-Base。這一頁整理的是板上的 Qwen/Qwen3.5-9B，權重在這個 repo。
- 稠密。Hidden Layout: 8 × (3 × (Gated DeltaNet → FFN) → 1 × (Gated Attention → FFN))。
- safetensors 索引的參數總數 9653104368（BF16 9653100528、F32 3840）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `text_config`。
- model_type：qwen3_5_text
- 層數 num_hidden_layers：32
- hidden size：4096
- attention heads：16
- KV heads：4
- head dim：256
- intermediate size：12288
- max_position_embeddings：262144
- vocab size：248320
- vision_config：hidden_size=1152，model_type=qwen3_5

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：4 個檔，19306310880 bytes，換算 17.98 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| MMLU-Pro | 82.5 | 表 1 欄「Qwen3.5-9B」。 |
| MMLU-Redux | 91.1 | 表 1 欄「Qwen3.5-9B」。 |
| C-Eval | 88.2 | 表 1 欄「Qwen3.5-9B」。 |
| SuperGPQA | 58.2 | 表 1 欄「Qwen3.5-9B」。 |
| GPQA Diamond | 81.7 | 表 1 欄「Qwen3.5-9B」。 |
| IFEval | 91.5 | 表 1 欄「Qwen3.5-9B」。 |
| IFBench | 64.5 | 表 1 欄「Qwen3.5-9B」。 |
| MultiChallenge | 54.5 | 表 1 欄「Qwen3.5-9B」。 |
| AA-LCR | 63.0 | 表 1 欄「Qwen3.5-9B」。 |
| LongBench v2 | 55.2 | 表 1 欄「Qwen3.5-9B」。 |
| HMMT Feb 25 | 83.2 | 表 1 欄「Qwen3.5-9B」。 |
| HMMT Nov 25 | 82.9 | 表 1 欄「Qwen3.5-9B」。 |
| LiveCodeBench v6 | 65.6 | 表 1 欄「Qwen3.5-9B」。 |
| OJBench | 29.2 | 表 1 欄「Qwen3.5-9B」。 |
| BFCL-V4 | 66.1 | 表 1 欄「Qwen3.5-9B」。 |
| TAU2-Bench | 79.1 | 表 1 欄「Qwen3.5-9B」。 |
| VITA-Bench | 29.8 | 表 1 欄「Qwen3.5-9B」。 |
| DeepPlanning | 18.0 | 表 1 欄「Qwen3.5-9B」。 |
| MMMLU | 81.2 | 表 1 欄「Qwen3.5-9B」。 |
| MMLU-ProX | 76.3 | 表 1 欄「Qwen3.5-9B」。 |
| NOVA-63 | 55.9 | 表 1 欄「Qwen3.5-9B」。 |
| INCLUDE | 75.6 | 表 1 欄「Qwen3.5-9B」。 |
| Global PIQA | 83.2 | 表 1 欄「Qwen3.5-9B」。 |
| PolyMATH | 57.3 | 表 1 欄「Qwen3.5-9B」。 |
| WMT24++ | 72.6 | 表 1 欄「Qwen3.5-9B」。 |
| MAXIFE | 83.4 | 表 1 欄「Qwen3.5-9B」。 |
| MMMU | 78.4 | 表 2 欄「Qwen3.5-9B」。 |
| MMMU-Pro | 70.1 | 表 2 欄「Qwen3.5-9B」。 |
| MathVision | 78.9 | 表 2 欄「Qwen3.5-9B」。 |
| Mathvista(mini) | 85.7 | 表 2 欄「Qwen3.5-9B」。 |
| We-Math | 75.2 | 表 2 欄「Qwen3.5-9B」。 |
| DynaMath | 83.6 | 表 2 欄「Qwen3.5-9B」。 |
| ZEROBench | 3.0 | 表 2 欄「Qwen3.5-9B」。 |
| ZEROBench_sub | 31.1 | 表 2 欄「Qwen3.5-9B」。 |
| VlmsAreBlind | 93.7 | 表 2 欄「Qwen3.5-9B」。 |
| BabyVision | 28.6/25.8 | 表 2 欄「Qwen3.5-9B」。 |
| RealWorldQA | 80.3 | 表 2 欄「Qwen3.5-9B」。 |
| MMStar | 79.7 | 表 2 欄「Qwen3.5-9B」。 |
| MMBench EN-DEV-v1.1 | 90.1 | 表 2 欄「Qwen3.5-9B」。 |
| SimpleVQA | 51.2 | 表 2 欄「Qwen3.5-9B」。 |
| HallusionBench | 69.3 | 表 2 欄「Qwen3.5-9B」。 |
| OmniDocBench1.5 | 87.7 | 表 2 欄「Qwen3.5-9B」。 |
| CharXiv(RQ) | 73.0 | 表 2 欄「Qwen3.5-9B」。 |
| MMLongBench-Doc | 57.7 | 表 2 欄「Qwen3.5-9B」。 |
| CC-OCR | 79.3 | 表 2 欄「Qwen3.5-9B」。 |
| AI2D_TEST | 90.2 | 表 2 欄「Qwen3.5-9B」。 |
| OCRBench | 89.2 | 表 2 欄「Qwen3.5-9B」。 |
| ERQA | 55.5 | 表 2 欄「Qwen3.5-9B」。 |
| CountBench | 97.2 | 表 2 欄「Qwen3.5-9B」。 |
| RefCOCO(avg) | 89.7 | 表 2 欄「Qwen3.5-9B」。 |
| EmbSpatialBench | 83.0 | 表 2 欄「Qwen3.5-9B」。 |
| RefSpatialBench | 58.5 | 表 2 欄「Qwen3.5-9B」。 |
| LingoQA | 80.4 | 表 2 欄「Qwen3.5-9B」。 |
| Hypersim | 13.5 | 表 2 欄「Qwen3.5-9B」。 |
| Nuscene | 11.8 | 表 2 欄「Qwen3.5-9B」。 |
| VideoMME (w sub.) | 84.5 | 表 2 欄「Qwen3.5-9B」。 |
| VideoMME (w/o sub.) | 78.4 | 表 2 欄「Qwen3.5-9B」。 |
| VideoMMMU | 78.9 | 表 2 欄「Qwen3.5-9B」。 |
| MLVU | 84.4 | 表 2 欄「Qwen3.5-9B」。 |
| MVBench | 74.4 | 表 2 欄「Qwen3.5-9B」。 |
| LVBench | 70.0 | 表 2 欄「Qwen3.5-9B」。 |
| MMVU | 67.8 | 表 2 欄「Qwen3.5-9B」。 |
| ScreenSpot Pro | 65.2 | 表 2 欄「Qwen3.5-9B」。 |
| OSWorld-Verified | 41.8 | 表 2 欄「Qwen3.5-9B」。 |
| AndroidWorld | 57.8 | 表 2 欄「Qwen3.5-9B」。 |
| TIR-Bench | 45.6/31.9 | 表 2 欄「Qwen3.5-9B」。 |
| V* | 90.1/88.5 | 表 2 欄「Qwen3.5-9B」。 |
| SLAKE | 79.0 | 表 2 欄「Qwen3.5-9B」。 |
| PMC-VQA | 57.9 | 表 2 欄「Qwen3.5-9B」。 |
| MedXpertQA-MM | 49.9 | 表 2 欄「Qwen3.5-9B」。 |
