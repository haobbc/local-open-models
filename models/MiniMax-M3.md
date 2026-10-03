# MiniMax-M3

官方模型卡：[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

這個檢查點不在 README 的 AA 名次表裡。

## 授權

license 欄：other。license_name：minimax-community。license_link：LICENSE。

## 發佈日期

卡上未列。

## 參數與卡上句子

- 卡上文字：native multimodal model with 1M context。~428B parameters and ~23B activated parameters。
- 卡上速度句（相對 M2，販商自報，不是具名基準分數）：9× prefill、15× decode speedups at 1M context，per-token compute to 1/20。
- 沒有可轉寫的基準數字。分數若在圖裡，文字未列。
- 授權 license 欄為 other，license_name 為 minimax-community。
- safetensors 索引的參數總數 427040140160（BF16 426993800960、F32 46339200）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `text_config`。
- 層數 num_hidden_layers：60
- hidden size：6144
- attention heads：64
- KV heads：4
- head dim：128
- intermediate size：3072
- 本地專家 num_local_experts：128
- 共享專家 n_shared_experts：1
- 每 token 專家數：4
- max_position_embeddings：1048576
- vocab size：200064
- MTP 層 num_nextn_predict_layers：1
- vision_config：num_hidden_layers=32，hidden_size=1280，model_type=clip_vision_model

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：59 個檔，854176398808 bytes，換算 795.51 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

卡上沒有可轉寫的數字分數。

卡上沒有可轉寫的基準數字。
