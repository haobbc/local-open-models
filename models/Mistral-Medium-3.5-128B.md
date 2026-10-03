# Mistral Medium 3.5 128B

官方模型卡：[mistralai/Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

## 授權

license 欄：other。

## 發佈日期

卡上未列。

## 參數與卡上句子

- 卡上文字：dense 128B model，256k context window。
- 授權是 Modified MIT（license 欄為 other）。
- 正文有兩個數字：τ³-Telecom 91.4%，SWE-Bench Verified 77.6%。其餘分數在圖裡，文字未列。
- safetensors 索引的參數總數 127704210176（BF16 5901622016、F8_E4M3 121802588160）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `text_config`。
- model_type：ministral3
- 層數 num_hidden_layers：88
- hidden size：12288
- attention heads：96
- KV heads：8
- head dim：128
- intermediate size：28672
- max_position_embeddings：262144
- vocab size：131072
- quantization_config：quant_method=fp8，activation_scheme=static，weight_block_size=None
- vision_config：num_hidden_layers=48，hidden_size=1664，model_type=pixtral

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- model- 分片：3 個檔，133606164352 bytes，換算 124.43 GiB（bytes ÷ 1024³）。與 consolidated 是兩種包裝，圖只用這一種。
- consolidated 分片：3 個檔，133606102824 bytes，換算 124.43 GiB（bytes ÷ 1024³）。另一種包裝，不加進 model- 的加總。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| τ³-Telecom | 91.4% | 卡上正文。 |
| SWE-Bench Verified | 77.6% | 卡上正文。 |
