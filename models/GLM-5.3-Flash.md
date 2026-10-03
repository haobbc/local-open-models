# GLM-5.3-Flash

官方模型卡：[zai-org/GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

## 授權

license 欄：mit。

## 發佈日期

卡上未列。

## 參數與卡上句子

- 卡上文字：320B total parameters and just 18B active parameters。
- 分數卡上未列。下面這些名字出現在評估腳註，沒有數字：DeepSWE、Terminal-Bench 2.1、Agent’s Last Exam、Toolathlon Verified、AutomationBench v1.0.6、GDPval-AA v2、BabyVision。
- safetensors 索引的參數總數 321323031390（BF16 6926096640、F8_E4M3 314396639232、F32 295518）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `text_config`。
- model_type：glm5_next_text
- 層數 num_hidden_layers：45
- hidden size：4096
- attention heads：64
- KV heads：64
- head dim：config.json 這一欄是 0，卡上未另列。
- intermediate size：12288
- MoE intermediate：2048
- 路由專家 n_routed_experts：288
- 共享專家 n_shared_experts：1
- 每 token 專家數：8
- max_position_embeddings：1048576
- vocab size：154880
- MTP 層 num_nextn_predict_layers：1
- quantization_config：quant_method=fp8，fmt=e4m3，activation_scheme=dynamic，weight_block_size=[128, 128]
- vision_config：hidden_size=1024，model_type=glm5_next_vision

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：62 個檔，328337455672 bytes，換算 305.79 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

卡上沒有可轉寫的數字分數。

卡上點了名、但沒有數字的項目：DeepSWE、Terminal-Bench 2.1、Agent’s Last Exam、Toolathlon Verified、AutomationBench、GDPval-AA v2、BabyVision。
