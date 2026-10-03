# LongCat-Flash-Lite

官方模型卡：[meituan-longcat/LongCat-Flash-Lite](https://huggingface.co/meituan-longcat/LongCat-Flash-Lite)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

這個檢查點不在 README 的 AA 名次表裡。

## 授權

license 欄：mit。

## 發佈日期

卡上未列。

## 參數與卡上句子

- 卡上文字：non-thinking 68.5B parameter MoE，approximately 3B activated；表上 # Total Params 68.5B，# Activated Params 2.9B~4.5B。
- 卡上文字：256k context length through the YaRN method。config.json 的 max_position_embeddings 是 327680。
- config.json：num_layers 14，n_routed_experts 256，moe_topk 12，hidden_size 3072。
- safetensors 索引的參數總數 69073335552（F32 16520448、BF16 69056815104）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `config.json 頂層`。
- 層數 num_layers：14
- hidden size：3072
- attention heads：32
- expert FFN hidden：1024
- FFN hidden：6144
- 路由專家 n_routed_experts：256
- moe_topk：12
- max_position_embeddings：327680
- vocab size：131072

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：26 個檔，138181101448 bytes，換算 128.69 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| Tau2-Airline(avg@8) | 58.00 | 欄「LongCat-Flash-Lite」。 |
| Tau2-Retail(avg@8) | 73.10 | 欄「LongCat-Flash-Lite」。 |
| Tau2-Telecom(avg@8) | 72.80 | 欄「LongCat-Flash-Lite」。 |
| SWE-Bench(acc) | 54.40 | 欄「LongCat-Flash-Lite」。 |
| TerminalBench(acc) | 33.75 | 欄「LongCat-Flash-Lite」。 |
| SWE-Bench Multiligual | 38.10 | 欄「LongCat-Flash-Lite」。 |
| PRDBench | 39.63 | 欄「LongCat-Flash-Lite」。 |
| GPQA-Diamond(avg@16) | 66.78 | 欄「LongCat-Flash-Lite」。 |
| MMLU(acc) | 85.52 | 欄「LongCat-Flash-Lite」。 |
| MMLU-Pro(acc) | 78.29 | 欄「LongCat-Flash-Lite」。 |
| CEval(acc) | 86.55 | 欄「LongCat-Flash-Lite」。 |
| CMMLU(acc) | 82.48 | 欄「LongCat-Flash-Lite」。 |
| MATH500(acc) | 96.80 | 欄「LongCat-Flash-Lite」。 |
| AIME24(avg@32) | 72.19 | 欄「LongCat-Flash-Lite」。 |
| AIME25(avg@32) | 63.23 | 欄「LongCat-Flash-Lite」。 |
