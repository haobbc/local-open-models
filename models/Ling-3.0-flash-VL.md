# Ling-3.0-flash-VL

官方模型卡：[inclusionAI/Ling-3.0-flash-VL](https://huggingface.co/inclusionAI/Ling-3.0-flash-VL)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

## 授權

license 欄：mit。

## 發佈日期

卡上未列。

## 參數與卡上句子

- 卡上文字：124B total，5.5B activated per token，context window of up to 256K tokens。
- 卡上文字：42-layer hybrid backbone。
- config.json 的 max_position_embeddings 是 131072。卡上 256K 與這個欄位不同，兩數都保留。
- 正文分數 42 是 Artificial Analysis Intelligence Index v4.1.1。不是本榜 v4.3.2 的 25。其餘多模態分數在圖裡，文字未列。
- safetensors 索引的參數總數 124848460496（F32 164960、BF16 124848295536）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `text_config`。
- 層數 num_hidden_layers：42
- hidden size：2560
- attention heads：32
- KV heads：32
- head dim：128
- intermediate size：6144
- MoE intermediate：768
- 專家數 num_experts：512
- 每 token 專家數：8
- max_position_embeddings：131072
- vocab size：157184
- vision_config：hidden_size=1152，model_type=qwen3_moe_vit

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 主檢查點 safetensors：64 個檔，249705022256 bytes，換算 232.56 GiB（bytes ÷ 1024³）。不含 pure_common.pt。
- pure_common.pt：1 個檔，26757 bytes，換算 0.00 GiB（bytes ÷ 1024³）。位元組很小，不進權重圖。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| Artificial Analysis Intelligence Index v4.1.1 | 42 | 卡上正文。 |

卡上點了名、但沒有數字的項目：Terminal-Bench 2.1（只寫了 AA protocol，沒有分數）。
