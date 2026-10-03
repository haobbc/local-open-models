# K2-Horizon-7B

官方模型卡：[IFM/K2-Horizon-7B](https://huggingface.co/IFM/K2-Horizon-7B)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

## 授權

license 欄：apache-2.0。

## 發佈日期

卡上未列。Artifact 表 Last updated: 2026-10-01 是表的更新日期，不是發佈日。

## 參數與卡上句子

- 卡上文字：7B-core decoder-only model with a 512K context window。
- config.json 的 max_position_embeddings 是 524288，與 512K 同一量級。
- 主比較表註腳：BrowseComp 用 Discard-all@95k；對照模型的 harness 可能不同。
- 另一張表的「7B after」是對照 7B before 的消融，不取代主比較表。主表的 HMMT Feb 2026 是 73.3，與 7B before 相同，不是 7B after 的 77.8。
- safetensors 索引的參數總數 8999178240（BF16 8999178240）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `config.json 頂層`。
- model_type：k2_horizon
- 層數 num_hidden_layers：36
- hidden size：4096
- attention heads：32
- KV heads：8
- head dim：128
- intermediate size：12288
- MoE intermediate：0
- 專家數 num_experts：0
- 共享專家 num_shared_experts：0
- 每 token 專家數：0
- max_position_embeddings：524288
- vocab size：250624
- MoVA 專家數：0
- MoVA 每 token 專家數：0
- mlp_only_layers：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：36 個檔，17998399920 bytes，換算 16.76 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| HMMT Feb 2026 Competition mathematics | 73.3 | 欄「K2-Horizon-7B」。 |
| SWE-bench Verified Software engineering | 70.6 | 欄「K2-Horizon-7B」。 |
| HLE Expert-level reasoning | 18.6 | 欄「K2-Horizon-7B」。 |
| SciCode Scientific coding | 31.6 | 欄「K2-Horizon-7B」。 |
| LCR Long-context reasoning | 68.0 | 欄「K2-Horizon-7B」。 |
| Terminal-Bench 2.1 Agentic terminal use | 39.1 | 欄「K2-Horizon-7B」。 |
| tau3-Banking Agentic tool use | 25.8 | 欄「K2-Horizon-7B」。 |
| BrowseComp Web browsing | 59.0 | 欄「K2-Horizon-7B」。 |
| AIME 2025 | 90.3 (-1.6) | 另一張表的「7B after」欄（括號是相對 7B before 的差）。 |
| AIME 2026 | 90.2 (+0.1) | 另一張表的「7B after」欄（括號是相對 7B before 的差）。 |
| HMMT Feb 2025 | 87.7 (+3.5) | 另一張表的「7B after」欄（括號是相對 7B before 的差）。 |
| HMMT Feb 2026 | 77.8 (+4.5) | 另一張表的「7B after」欄（括號是相對 7B before 的差）。 |
| GPQA Diamond | 75.6 (-1.5) | 另一張表的「7B after」欄（括號是相對 7B before 的差）。 |
| HLE (text) | 19.5 (+0.8) | 另一張表的「7B after」欄（括號是相對 7B before 的差）。 |
| IFEval (loose) | 86.9 (-1.8) | 另一張表的「7B after」欄（括號是相對 7B before 的差）。 |
| IFBench (loose) | 50.7 (-1.3) | 另一張表的「7B after」欄（括號是相對 7B before 的差）。 |
| LiveCodeBench v6 | 72.7 (+1.2) | 另一張表的「7B after」欄（括號是相對 7B before 的差）。 |
| OJBench | 29.4 (+0.4) | 另一張表的「7B after」欄（括號是相對 7B before 的差）。 |
| SciCode | 33.6 (+2.0) | 另一張表的「7B after」欄（括號是相對 7B before 的差）。 |
| SWE-bench Verified | 72.4 (+3.2) | 另一張表的「7B after」欄（括號是相對 7B before 的差）。 |
| Terminal-Bench 2.1 | 44.6 (+4.9) | 另一張表的「7B after」欄（括號是相對 7B before 的差）。 |
| BFCL v4 | 67.0 (+4.6) | 另一張表的「7B after」欄（括號是相對 7B before 的差）。 |
