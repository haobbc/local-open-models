# Nemotron 3 Super 120B A12B BF16

官方模型卡：[nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

## 授權

license 欄：other。license_name：nvidia-nemotron-open-model-license。license_link：https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license/。

## 發佈日期

卡上寫 Release Date: March 11, 2026。同頁另有 Hugging Face 03/11/2026。Model Dates: December 2025–March 2026。

## 參數與卡上句子

- 卡上文字：120B (12B active)；另一處寫 120B Total / 12B Active。
- 卡上文字：Context Length up to 1M tokens。同頁寫預設 Hugging Face 設定是 256k，要用到 1M 需另開長上下文。config.json 的 max_position_embeddings 是 262144。
- 授權 license 欄為 other，license_name 為 nvidia-nemotron-open-model-license。
- safetensors 索引的參數總數 123611012096（F32 20992、BF16 123611012096）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `config.json 頂層`。
- model_type：nemotron_h
- 層數 num_hidden_layers：88
- hidden size：4096
- attention heads：32
- KV heads：2
- head dim：128
- intermediate size：2688
- MoE intermediate：2688
- 路由專家 n_routed_experts：512
- 共享專家 n_shared_experts：1
- 每 token 專家數：22
- max_position_embeddings：262144
- vocab size：131072
- MTP 層 num_nextn_predict_layers：1

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：50 個檔，247227650480 bytes，換算 230.25 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| MMLU-Pro | 83.73 | 欄「Nemotron 3 Super」。 |
| AIME25 (no tools) | 90.21 | 欄「Nemotron 3 Super」。 |
| HMMT Feb25 (no tools) | 93.67 | 欄「Nemotron 3 Super」。 |
| HMMT Feb25 (with tools) | 94.73 | 欄「Nemotron 3 Super」。 |
| GPQA (no tools) | 79.23 | 欄「Nemotron 3 Super」。 |
| GPQA (with tools) | 82.70 | 欄「Nemotron 3 Super」。 |
| LiveCodeBench (v5 2024-07↔2024-12) | 81.19 | 欄「Nemotron 3 Super」。 |
| SciCode (subtask) | 42.05 | 欄「Nemotron 3 Super」。 |
| HLE (no tools) | 18.26 | 欄「Nemotron 3 Super」。 |
| HLE (with tools) | 22.82 | 欄「Nemotron 3 Super」。 |
| Terminal Bench (hard subset) | 25.78 | 欄「Nemotron 3 Super」。 |
| Terminal Bench Core 2.0 | 31.00 | 欄「Nemotron 3 Super」。 |
| SWE-Bench (OpenHands) | 60.47 | 欄「Nemotron 3 Super」。 |
| SWE-Bench (OpenCode) | 59.20 | 欄「Nemotron 3 Super」。 |
| SWE-Bench (Codex) | 53.73 | 欄「Nemotron 3 Super」。 |
| SWE-Bench Multilingual (OpenHands) | 45.78 | 欄「Nemotron 3 Super」。 |
| TauBench V2 Airline | 56.25 | 欄「Nemotron 3 Super」。 |
| TauBench V2 Retail | 62.83 | 欄「Nemotron 3 Super」。 |
| TauBench V2 Telecom | 64.36 | 欄「Nemotron 3 Super」。 |
| TauBench V2 Average | 61.15 | 欄「Nemotron 3 Super」。 |
| BrowseComp with Search | 31.28 | 欄「Nemotron 3 Super」。 |
| BIRD Bench | 41.80 | 欄「Nemotron 3 Super」。 |
| IFBench (prompt) | 72.56 | 欄「Nemotron 3 Super」。 |
| Scale AI Multi-Challenge | 55.23 | 欄「Nemotron 3 Super」。 |
| Arena-Hard-V2 | 73.88 | 欄「Nemotron 3 Super」。 |
| AA-LCR | 58.31 | 欄「Nemotron 3 Super」。 |
| RULER @ 256k | 96.30 | 欄「Nemotron 3 Super」。 |
| RULER @ 512k | 95.67 | 欄「Nemotron 3 Super」。 |
| RULER @ 1M | 91.75 | 欄「Nemotron 3 Super」。 |
| MMLU-ProX (avg over langs) | 79.36 | 欄「Nemotron 3 Super」。 |
| WMT24++ (en→xx) | 86.67 | 欄「Nemotron 3 Super」。 |
