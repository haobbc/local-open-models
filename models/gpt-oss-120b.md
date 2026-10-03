# gpt-oss-120b

官方模型卡：[openai/gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

## 授權

license 欄：apache-2.0。

## 發佈日期

卡上未列。

## 參數與卡上句子

- 卡上文字：117B parameters with 5.1B active parameters。
- 卡上文字：fit into a single 80GB GPU (H100 or MI300X)。MXFP4。
- 卡上沒有基準表，也沒有可轉寫的分數。
- safetensors 索引的參數總數 116829156672（BF16 2167371072、U8 114661785600）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `config.json 頂層`。
- model_type：gpt_oss
- 層數 num_hidden_layers：36
- hidden size：2880
- attention heads：64
- KV heads：8
- head dim：64
- intermediate size：2880
- 本地專家 num_local_experts：128
- 每 token 專家數：4
- 每 token 專家數 experts_per_token：4
- max_position_embeddings：131072
- vocab size：201088
- sliding window：128
- quantization_config：quant_method=mxfp4

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- model 分片：15 個檔，65248893184 bytes，換算 60.77 GiB（bytes ÷ 1024³）。MXFP4。不與 original/、metal/ 加總。
- original/：7 個檔，65248869800 bytes，換算 60.77 GiB（bytes ÷ 1024³）。另一份打包。
- metal/model.bin：1 個檔，65238253568 bytes，換算 60.76 GiB（bytes ÷ 1024³）。另一份打包。

## 基準（販商自報）

卡上沒有可轉寫的數字分數。
