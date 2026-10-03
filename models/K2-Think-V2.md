# K2 Think V2

官方模型卡：[IFM/K2-Think-V2](https://huggingface.co/IFM/K2-Think-V2)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

這個檢查點不在 README 的 AA 名次表裡。

## 授權

license 欄：apache-2.0。

## 發佈日期

卡上未列。citation 的 year 是 2026，沒有檢查點日期。

## 參數與卡上句子

- 卡上文字：70 billion parameter open-weights general reasoning model。
- YAML base_model：LLM360/K2-V2-Instruct。這一頁是 IFM/K2-Think-V2。卡上 transformers 範例寫的 model id 是 LLM360/K2-Think-V2。
- 服務表：Context Length 131072，Context Length Extension 2x using YaRN。config.json 的 max_position_embeddings 是 262144。
- 索引參數是 F32，不是 BF16。不把 AA 筆記裡的 70B 拿來改這兩個來源。
- safetensors 索引的參數總數 72550195200（F32 72550195200）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `config.json 頂層`。
- model_type：llama
- 層數 num_hidden_layers：80
- hidden size：8192
- attention heads：64
- KV heads：8
- head dim：128
- intermediate size：28672
- max_position_embeddings：262144
- vocab size：250112

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：62 個檔，290200865568 bytes，換算 270.27 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| AIME 2025 | 90.42 | 欄「K2 Think V2」（pass@1，16 次平均）。 |
| HMMT 2025 | 84.79 | 欄「K2 Think V2」（pass@1，16 次平均）。 |
| SciCode | 33.00 | 欄「K2 Think V2」（pass@1，16 次平均）。 |
| GPQA-Diamond | 72.98 | 欄「K2 Think V2」（pass@1，16 次平均）。 |
| Humanity's Last Exam | 9.5 | 欄「K2 Think V2」（pass@1，16 次平均）。 |
| Content & Public Safety | 98.20 | 安全表 Safety-4（Macro-Avg）。 |
| Truthfulness & Reliability | 97.98 | 安全表 Safety-4（Macro-Avg）。 |
| Societal Alignment | 97.25 | 安全表 Safety-4（Macro-Avg）。 |
| Data & Infrastructure | 83.00 | 安全表 Safety-4（Macro-Avg）。 |
