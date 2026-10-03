# HyperNova 60B 2605

官方模型卡：[MultiverseComputingCAI/Hypernova-60B-2605](https://huggingface.co/MultiverseComputingCAI/Hypernova-60B-2605)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

這個檢查點不在 README 的 AA 名次表裡。

## 授權

license 欄：apache-2.0。

## 發佈日期

卡上寫 Release date 26/02/2026。

## 參數與卡上句子

- 卡上文字：60B total parameters。架構表：60B, 4.8B active MoE。
- 比較表可見欄是 GPT-OSS-120B、HyperNova 60B 2602、HyperNova 60B 2605。分數取最後一欄。表頭裡被藏起來的對照名稱不採用。
- 量化是 MXFP4。
- safetensors 索引的參數總數 58659018048（BF16 2035914048、U8 56623104000）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `config.json 頂層`。
- model_type：gpt_oss
- 層數 num_hidden_layers：32
- hidden size：2880
- attention heads：64
- KV heads：8
- head dim：64
- intermediate size：2560
- 本地專家 num_local_experts：80
- 每 token 專家數：4
- 每 token 專家數 experts_per_token：4
- max_position_embeddings：131072
- vocab size：201088
- sliding window：128
- quantization_config：quant_method=mxfp4

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：7 個檔，34152921664 bytes，換算 31.81 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| HLE | 15.0 | 欄「HyperNova 60B 2605」。 |
| MMLU-Pro | 76.8 | 欄「HyperNova 60B 2605」。 |
| AIME25 | 90.0 | 欄「HyperNova 60B 2605」。 |
| GPQA:d | 71.9 | 欄「HyperNova 60B 2605」。 |
| IFBench | 66.6 | 欄「HyperNova 60B 2605」。 |
| AA-LCR | 40.3 | 欄「HyperNova 60B 2605」。 |
| Tau2-bench Telecom | 61.7 | 欄「HyperNova 60B 2605」。 |
| SciCode | 36.0 | 欄「HyperNova 60B 2605」。 |
| LiveCodeBench | 68.7 | 欄「HyperNova 60B 2605」。 |
| Terminal Bench | 15.9 | 欄「HyperNova 60B 2605」。 |
| AIDER | 34.2 | 欄「HyperNova 60B 2605」。 |
| StereoSet stereotype score | 56.0 | 安全表「HyperNova 60B 2605」。 |
| StereoSet language model score | 97.3 | 安全表「HyperNova 60B 2605」。 |
| StereoSet ICAT | 85.6 | 安全表「HyperNova 60B 2605」。 |
| StrongREJECT jailbreak rate | 0 | 安全表「HyperNova 60B 2605」。 |
| StrongREJECT metric | 0 | 安全表「HyperNova 60B 2605」。 |
| XSTest safe refusal | 30.4 | 安全表「HyperNova 60B 2605」。 |
| XSTest unsafe refusal | 99.0 | 安全表「HyperNova 60B 2605」。 |
| BBQ | 96.4 | 安全表「HyperNova 60B 2605」。 |
