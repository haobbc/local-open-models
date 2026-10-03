# GLM-5.3

官方模型卡：[zai-org/GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

這個檢查點不在 README 的 AA 名次表裡。

## 授權

license 欄：other。license_name：glm-5.3。

## 發佈日期

卡上未列。FrontierSWE 腳註的 2026/08/14 是該項評測的 as-of 日期，不是發佈日。

## 參數與卡上句子

- 總參數量與啟動參數量：卡上未列。下面的索引總數不改寫成卡上句子。
- 授權 license 欄為 other，license_name 為 glm-5.3。不是 MIT。
- 比較表欄名是 GLM-5.3。ExploitGym 那一格是 2h / 6h 兩個數，不畫成一根長條。
- safetensors 索引的參數總數 753329940480（BF16 2103729152、F8_E4M3 751226191872、F32 19456）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `config.json 頂層`。
- model_type：glm_moe_dsa
- 層數 num_hidden_layers：78
- hidden size：6144
- attention heads：64
- KV heads：64
- head dim：192
- intermediate size：12288
- MoE intermediate：2048
- 路由專家 n_routed_experts：256
- 共享專家 n_shared_experts：1
- 每 token 專家數：8
- max_position_embeddings：1048576
- vocab size：154880
- MTP 層 num_nextn_predict_layers：1
- quantization_config：quant_method=fp8，fmt=e4m3，activation_scheme=dynamic，weight_block_size=[128, 128]

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：141 個檔，755632050320 bytes，換算 703.74 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| Terminal Bench 2.1 | 88.2 | 欄「GLM-5.3」。 |
| Terminal Bench 3.0 | 28.3 | 欄「GLM-5.3」。 |
| DeepSWE (v1.1) | 66.9 | 欄「GLM-5.3」。 |
| NL2Repo | 58.0 | 欄「GLM-5.3」。 |
| ProgramBench (Almost Solved) | 19.0 | 欄「GLM-5.3」。 |
| FrontierSWE | 78.1 | 欄「GLM-5.3」。 |
| SWE-Marathon (v1.1) | 42.5 | 欄「GLM-5.3」。 |
| PostTrainBench | 39.8 | 欄「GLM-5.3」。 |
| CyberGym | 84.5 | 欄「GLM-5.3」。 |
| ExploitGym (2h / 6h) | 105 / 130 | 欄「GLM-5.3」。 |
| ExploitBench | 54.4 | 欄「GLM-5.3」。 |
| Toolathlon Verified | 73.0 | 欄「GLM-5.3」。 |
| AutomationBench (v1.0.6) | 48.2 | 欄「GLM-5.3」。 |
| Agents' Last Exam (ALE-CLI) | 28.5 | 欄「GLM-5.3」。 |
| HLE w/ Tools | 62.5 | 欄「GLM-5.3」。 |
| GDPval-AA v2 | 1769 | 欄「GLM-5.3」。 |
