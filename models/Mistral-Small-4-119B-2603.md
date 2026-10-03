# Mistral Small 4 119B

官方模型卡：[mistralai/Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

這個檢查點不在 README 的 AA 名次表裡。

## 授權

license 欄：apache-2.0。

## 發佈日期

卡上未列。

## 參數與卡上句子

- 卡上文字：119B parameters，6.5B activated per token。128 experts，4 active。
- 卡上文字：256k context length。config.json 的 max_position_embeddings 是 1048576。兩數都保留。
- 正文數字只有 AA LCR 0.72（並寫輸出約 1.6K characters）。其餘比較在圖裡，文字未列。
- 授權 Apache-2.0。
- safetensors 索引的參數總數 119401317952（BF16 1521452032、F8_E4M3 117879865344）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `text_config`。
- model_type：mistral4
- 層數 num_hidden_layers：36
- hidden size：4096
- attention heads：32
- KV heads：32
- head dim：128
- intermediate size：12288
- MoE intermediate：2048
- 路由專家 n_routed_experts：128
- 共享專家 n_shared_experts：1
- 每 token 專家數：4
- max_position_embeddings：1048576
- vocab size：131072
- quantization_config：quant_method=fp8，activation_scheme=static，weight_block_size=None
- vision_config：num_hidden_layers=24，hidden_size=1024，model_type=pixtral

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- model- 分片：3 個檔，120922973936 bytes，換算 112.62 GiB（bytes ÷ 1024³）。與 consolidated 是兩種包裝，圖只用這一種。
- consolidated 分片：7 個檔，120927211096 bytes，換算 112.62 GiB（bytes ÷ 1024³）。另一種包裝，不加總。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| AA LCR | 0.72 | 卡上正文。 |

其餘基準在圖裡，文字未列。
