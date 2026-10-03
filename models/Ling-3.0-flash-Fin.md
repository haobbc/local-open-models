# Ling-3.0-flash-Fin

官方模型卡：[inclusionAI/Ling-3.0-flash-Fin](https://huggingface.co/inclusionAI/Ling-3.0-flash-Fin)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

## 授權

license 欄：mit。

## 發佈日期

卡上未列。

## 參數與卡上句子

- 卡上文字：124B total parameters，5.1B activated parameters，256K context window。
- YAML base_model：inclusionAI/Ling-3.0-flash。這一頁是板上的 Fin 檢查點，權重在這個 repo。
- 目前檢查點是 BF16。
- safetensors 索引的參數總數 127486405600（F32 165472、BF16 127486240128）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `config.json 頂層`。
- model_type：bailing_hybrid
- 層數 num_hidden_layers：42
- hidden size：2560
- attention heads：32
- KV heads：32
- head dim：128
- intermediate size：6144
- MoE intermediate：768
- 專家數 num_experts：512
- 共享專家 num_shared_experts：1
- 每 token 專家數：8
- max_position_embeddings：262144
- vocab size：157184
- MTP 層 num_nextn_predict_layers：1

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 主檢查點（不含 model-mtp）：64 個檔，248836487408 bytes，換算 231.75 GiB（bytes ÷ 1024³）。BF16 檔名。MTP 另列，不加進圖。
- MTP：1 個檔，6144582792 bytes，換算 5.72 GiB（bytes ÷ 1024³）。單檔，不與主檢查點加總。

## 基準（販商自報）

卡上沒有可轉寫的數字分數。

卡上點了名、但沒有數字的項目：FinFIRST、FinSearchComp Verified、FinCRAFT、Finance Agent、APEX-Agents、SpreadsheetBench、τ³-Banking。
