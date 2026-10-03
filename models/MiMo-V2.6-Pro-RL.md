# MiMo-V2.6-Pro-RL

官方模型卡：[XiaomiMiMo/MiMo-V2.6-Pro-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

這個檢查點不在 README 的 AA 名次表裡。

## 授權

license 欄：mit。

## 發佈日期

卡上未列。citation 的 year 是 2026。

## 參數與卡上句子

- 卡上文字：Sparse MoE，1.02T total / 42B activated parameters。Context Length 1M tokens。
- Vision Encoder 681M（28 layers: 24 SWA + 4 Full）。Audio Encoder 308M AudioTokenizer + 127M audio patch encoder。MTP：5-layer speculative decoder。
- 架構表：Layers 70 / 60 / 10，Hidden 6144，Routed Experts 384 / 8，sliding window 128。沒有 shared experts（卡上寫 without shared experts）。
- 比較表欄名是 MiMo-V2.6 Pro。
- safetensors 索引的參數總數 1024216603392（BF16 10647286656、F32 26496、F8_E4M3 13378781184、U8 1000190509056）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `config.json 頂層`。
- model_type：mimo_v2
- 層數 num_hidden_layers：70
- hidden size：6144
- attention heads：128
- KV heads：8
- head dim：192
- intermediate size：16384
- MoE intermediate：2048
- 路由專家 n_routed_experts：384
- 每 token 專家數：8
- max_position_embeddings：1048576
- vocab size：152576
- sliding window：128
- quantization_config：quant_method=fp8，fmt=e4m3，activation_scheme=dynamic，weight_block_size=[128, 128]
- vision_config：hidden_size=1280

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- model_pp0_ep* 分片：129 個檔，563584462616 bytes，換算 524.88 GiB（bytes ÷ 1024³）。檔名是同一份主檢查點的 expert 分片（只有 pp0）。dflash、MTP、audio tokenizer 不加進來。
- dflash：5 個檔，5536673549 bytes，換算 5.16 GiB（bytes ÷ 1024³）。草稿頭，不進主權重圖。
- model_mtp：1 個檔，2463641280 bytes，換算 2.29 GiB（bytes ÷ 1024³）。MTP，不進主權重圖。
- audio_tokenizer：5 個檔，1872631395 bytes，換算 1.74 GiB（bytes ÷ 1024³）。音訊 tokenizer，不進主權重圖。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| DeepSWE v1.1 | 71.9 | 欄「MiMo-V2.6 Pro」。 |
| ProgramBench | 26.5 | 欄「MiMo-V2.6 Pro」。 |
| MiMo Code Bench | 63.2 | 欄「MiMo-V2.6 Pro」。 |
| AutomationBench v1.0.6 | 53.1 | 欄「MiMo-V2.6 Pro」。 |
| Toolathlon-Verified | 76.9 | 欄「MiMo-V2.6 Pro」。 |
| GDPval-AA 2.1 | 1673 | 欄「MiMo-V2.6 Pro」。 |
| Agents’ Last Exam | 31.6 | 欄「MiMo-V2.6 Pro」。 |
| Terminal Bench 4.0 | 34.9 | 欄「MiMo-V2.6 Pro」。 |
| Terminal Bench 2.1 | 89.9 | 欄「MiMo-V2.6 Pro」。 |
| OSWorld-Verified | 82.0 | 欄「MiMo-V2.6 Pro」。 |
| JobBench | 62.0 | 欄「MiMo-V2.6 Pro」。 |
| CyberGym | 94.0 | 欄「MiMo-V2.6 Pro」。 |
| MiMo Cyber Bench | 80.2 | 欄「MiMo-V2.6 Pro」。 |
| ExploitGym | 17.8 | 欄「MiMo-V2.6 Pro」。 |
| ExploitBench | 47.9 | 欄「MiMo-V2.6 Pro」。 |
| SEC Bench Pro | 66.3 | 欄「MiMo-V2.6 Pro」。 |
| MiMo VisualCoding | 72.3 | 欄「MiMo-V2.6 Pro」。 |
