# K2-Horizon-MoVA-36B-A4B

官方模型卡：[IFM/K2-Horizon-MoVA-36B-A4B](https://huggingface.co/IFM/K2-Horizon-MoVA-36B-A4B)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

## 授權

license 欄：apache-2.0。

## 發佈日期

卡上未列。Artifact 表 Last updated: 2026-09-28 是表的更新日期，不是發佈日。

## 參數與卡上句子

- 卡上文字：stores 36B parameters and runs 4B per token。
- 比較表同一列寫 # Params 36B、# Activated params 4B。
- 上下文：卡上未另寫一個總字數；config.json 的 max_position_embeddings 是 524288。
- safetensors 索引的參數總數 37444792020（BF16 37444792020）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `config.json 頂層`。
- model_type：k2_horizon
- 層數 num_hidden_layers：48
- hidden size：2560
- attention heads：32
- KV heads：8
- head dim：128
- intermediate size：6144
- MoE intermediate：768
- 專家數 num_experts：100
- 共享專家 num_shared_experts：1
- 每 token 專家數：8
- max_position_embeddings：524288
- vocab size：250624
- MoVA 專家數：64
- MoVA 每 token 專家數：4
- mlp_only_layers：[0, 1, 2]

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：48 個檔，74891674376 bytes，換算 69.75 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| tau3-Banking Agentic tool use | 26.8 | 欄「K2-Horizon-MoVA-36B-A4B」。 |
| Terminal-Bench 2.1 Agentic terminal use | 58.6 | 欄「K2-Horizon-MoVA-36B-A4B」。 |
| SciCode Scientific coding | 38.9 | 欄「K2-Horizon-MoVA-36B-A4B」。 |
| Humanity's Last Exam (without tools) Expert-level reasoning | 25.2 | 欄「K2-Horizon-MoVA-36B-A4B」。 |
| GPQA Diamond Graduate-level science QA | 80.8 | 欄「K2-Horizon-MoVA-36B-A4B」。 |
| CritPt Frontier physics reasoning | 2.1 | 欄「K2-Horizon-MoVA-36B-A4B」。 |
| AA-LCR Long-context reasoning | 66.3 | 欄「K2-Horizon-MoVA-36B-A4B」。 |
| AA-Omniscience Accuracy Factual accuracy | 18.8 | 欄「K2-Horizon-MoVA-36B-A4B」。 |
| AA-Omniscience Non-Hallucination Non-hallucination rate | 69.2 | 欄「K2-Horizon-MoVA-36B-A4B」。 |
