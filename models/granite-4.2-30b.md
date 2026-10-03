# Granite 4.2 30B

官方模型卡：[ibm-granite/granite-4.2-30b](https://huggingface.co/ibm-granite/granite-4.2-30b)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

## 授權

license 欄：apache-2.0。

## 發佈日期

卡上寫 Release Date: August 25, 2026。

## 參數與卡上句子

- 架構表「30B Dense」：# Parameters 30B，embedding 4096，layers 64，head size 128，heads 32，KV heads 8，MLP 32768，sequence length 131072。
- 卡上另寫 Context Length：Natively Supports 128K（Long-context extension to 512K）。
- 索引參數總數與卡上的 30B 分開記，不互相改寫。
- safetensors 索引的參數總數 29276770304（BF16 29276770304）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `config.json 頂層`。
- model_type：granite
- 層數 num_hidden_layers：64
- hidden size：4096
- attention heads：32
- KV heads：8
- intermediate size：32768
- max_position_embeddings：131072
- vocab size：100352

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：11 個檔，58553607904 bytes，換算 54.53 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| SWE Bench Multilingual | 41.89 | 欄「30B Dense」。 |
| SWE Bench Pro | 33.29 | 欄「30B Dense」。 |
| SWE Bench Verified | 57 | 欄「30B Dense」。 |
| Terminal-Bench 2.1 | 29.24 | 欄「30B Dense」。 |
| τ³-bench (AVG) | 62.00 | 欄「30B Dense」。 |
| BFCL (v4) | 61.39 | 欄「30B Dense」。 |
| ProfBench | 42.90 | 欄「30B Dense」。 |
| BirdBench | 41.85 | 欄「30B Dense」。 |
| GDPval | 1225 | 欄「30B Dense」。 |
| AIME25 | 89.17 | 欄「30B Dense」。 |
| HMMT Feb25 | 89.17 | 欄「30B Dense」。 |
| GPQA | 66.41 | 欄「30B Dense」。 |
| LiveCodeBench v6 | 75.77 | 欄「30B Dense」。 |
| SciCode | 38.76 | 欄「30B Dense」。 |
| MMLU-Pro | 77.60 | 欄「30B Dense」。 |
| MMLU-ProX lite (IBM) | 66.64 | 欄「30B Dense」。 |
| Arena-Hard-V2 | 67.93 | 欄「30B Dense」。 |
| IFBench (prompt) | 77.17 | 欄「30B Dense」。 |
| RULER 64K | 89.96 | 欄「30B Dense」。 |
| RULER 128K | 81.38 | 欄「30B Dense」。 |
