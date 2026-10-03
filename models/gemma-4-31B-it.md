# Gemma 4 31B

官方模型卡：[google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

## 授權

license 欄：apache-2.0。license_link：https://ai.google.dev/gemma/docs/gemma_4_license。

## 發佈日期

卡上未列。

## 參數與卡上句子

- 屬性表「31B Dense」：Total Parameters 30.7B，Layers 60，sliding window 1024，context 256K，vocab 262K，文字加影像，vision ~550M，No Audio。
- 基準欄是 Gemma 4 31B。索引參數總數另列，不改卡上的 30.7B。
- safetensors 索引的參數總數 31273088876（BF16 31273088876）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `text_config`。
- model_type：gemma4_text
- 層數 num_hidden_layers：60
- hidden size：5376
- attention heads：32
- KV heads：16
- head dim：256
- intermediate size：21504
- max_position_embeddings：262144
- vocab size：262144
- sliding window：1024
- vision_config：num_hidden_layers=27，hidden_size=1152，model_type=gemma4_vision

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：2 個檔，62546338248 bytes，換算 58.25 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| MMLU Pro | 85.2% | 欄「Gemma 4 31B」。 |
| AIME 2026 no tools | 89.2% | 欄「Gemma 4 31B」。 |
| LiveCodeBench v6 | 80.0% | 欄「Gemma 4 31B」。 |
| Codeforces ELO | 2150 | 欄「Gemma 4 31B」。 |
| GPQA Diamond | 84.3% | 欄「Gemma 4 31B」。 |
| Tau2 (average over 3) | 76.9% | 欄「Gemma 4 31B」。 |
| HLE no tools | 19.5% | 欄「Gemma 4 31B」。 |
| HLE with search | 26.5% | 欄「Gemma 4 31B」。 |
| BigBench Extra Hard | 74.4% | 欄「Gemma 4 31B」。 |
| MMMLU | 88.4% | 欄「Gemma 4 31B」。 |
| MMMU Pro | 76.9% | 欄「Gemma 4 31B」。 |
| OmniDocBench 1.5 (average edit distance, lower is better) | 0.131 | 欄「Gemma 4 31B」。低分較好。 |
| MATH-Vision | 85.6% | 欄「Gemma 4 31B」。 |
| MedXPertQA MM | 61.3% | 欄「Gemma 4 31B」。 |
| MRCR v2 8 needle 128k (average) | 66.4% | 欄「Gemma 4 31B」。 |
