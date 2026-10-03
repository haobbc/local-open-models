# Gemma 4 26B A4B

官方模型卡：[google/gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

## 授權

license 欄：apache-2.0。license_link：https://ai.google.dev/gemma/docs/gemma_4_license。

## 發佈日期

卡上未列。

## 參數與卡上句子

- 屬性表「26B A4B MoE」：Total 25.2B，Active 3.8B，Layers 30，sliding window 1024，context 256K，vocab 262K，experts 8 active / 128 total and 1 shared，vision encoder ~550M，文字加影像。
- 這份 repo 是板上的 instruction-tuned 檢查點。基準欄是 Gemma 4 26B A4B。
- safetensors 索引的參數總數 25805936206（BF16 25805936206）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `text_config`。
- model_type：gemma4_text
- 層數 num_hidden_layers：30
- hidden size：2816
- attention heads：16
- KV heads：8
- head dim：256
- intermediate size：2112
- MoE intermediate：704
- 專家數 num_experts：128
- top_k_experts：8
- max_position_embeddings：262144
- vocab size：262144
- sliding window：1024
- vision_config：num_hidden_layers=27，hidden_size=1152，model_type=gemma4_vision

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：2 個檔，51612009916 bytes，換算 48.07 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| MMLU Pro | 82.6% | 欄「Gemma 4 26B A4B」。 |
| AIME 2026 no tools | 88.3% | 欄「Gemma 4 26B A4B」。 |
| LiveCodeBench v6 | 77.1% | 欄「Gemma 4 26B A4B」。 |
| Codeforces ELO | 1718 | 欄「Gemma 4 26B A4B」。 |
| GPQA Diamond | 82.3% | 欄「Gemma 4 26B A4B」。 |
| Tau2 (average over 3) | 68.2% | 欄「Gemma 4 26B A4B」。 |
| HLE no tools | 8.7% | 欄「Gemma 4 26B A4B」。 |
| HLE with search | 17.2% | 欄「Gemma 4 26B A4B」。 |
| BigBench Extra Hard | 64.8% | 欄「Gemma 4 26B A4B」。 |
| MMMLU | 86.3% | 欄「Gemma 4 26B A4B」。 |
| MMMU Pro | 73.8% | 欄「Gemma 4 26B A4B」。 |
| OmniDocBench 1.5 (average edit distance, lower is better) | 0.149 | 欄「Gemma 4 26B A4B」。低分較好。 |
| MATH-Vision | 82.4% | 欄「Gemma 4 26B A4B」。 |
| MedXPertQA MM | 58.1% | 欄「Gemma 4 26B A4B」。 |
| MRCR v2 8 needle 128k (average) | 44.1% | 欄「Gemma 4 26B A4B」。 |
