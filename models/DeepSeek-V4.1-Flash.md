# DeepSeek-V4.1-Flash

官方模型卡：[deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

這個檢查點不在 README 的 AA 名次表裡。

## 授權

license 欄：mit。

## 發佈日期

卡上未列。citation 的 year 是 2026。

## 參數與卡上句子

- 卡上文字：552B backbone parameters，contexts of up to one million tokens。
- 卡上文字：prefill 每 token 啟動 8B，decode 啟動 16B。Engram 196B parameters。1 shared expert，384 routed experts，每 token 6 個路由專家。
- 基座表的啟動參數欄寫 8B / 16B，骨幹 552B。Instruct 表是 reasoning_effort=100。
- HLE 那一格寫 36.8 (39.1†)，† 是卡上說的 text-only subset。不拆成兩根長條。
- safetensors 索引的參數總數 763205315794（BF16 1976441856、F32 42307282、F8_E4M3 204015223296、I8 557171343360）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `text_config`。
- model_type：deepseek_v41_text
- 層數 num_hidden_layers：40
- hidden size：5120
- attention heads：64
- KV heads：1
- head dim：512
- MoE intermediate：2304
- 路由專家 n_routed_experts：384
- 共享專家 n_shared_experts：1
- 每 token 專家數：6
- max_position_embeddings：1048576
- vocab size：129280
- sliding window：128
- MTP 層 num_nextn_predict_layers：3
- quantization_config：quant_method=fp8，activation_scheme=dynamic，weight_block_size=[32, 32]
- vision_config：num_hidden_layers=32，hidden_size=1024，model_type=deepseek_v41_vision

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：48 個檔，510296708312 bytes，換算 475.25 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| AGIEval (EM) | 83.4 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| MMLU-Pro (EM) | 74.1 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| C-Eval (EM) | 92.1 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| MultiLoKo (LLM-Judge) | 45.5 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| SimpleQA-Verified (EM) | 42.3 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| SuperGPQA (EM) | 53.1 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| BBH (EM) | 86.1 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| BBEH (EM) | 27.2 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| DROP (F1) | 87.9 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| HellaSwag (EM) | 87.2 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| BigCodeBench (Pass@1) | 60.6 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| HumanEval (Pass@1) | 79.4 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| GSM8K (EM) | 93.0 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| MATH (EM) | 61.1 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| MGSM (EM) | 80.2 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| LongBench-V2 (EM) | 45.2 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| MMMU-Pro (EM) | 56.5 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| CVBench (EM) | 77.9 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| DocVQA (LLM-Judge) | 95.6 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| RefCOCO-avg (Acc@0.5) | 86.0 | 基座表欄「DeepSeek-V4.1-Flash-Base」。 |
| GPQA Diamond (Pass@1) | 90.9 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| HLE (Pass@1) | 36.8 (39.1†) | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| Codeforces (Rating) | 3471 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| MathArena Apex (Pass@1) | 65.6 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| Terminal-Bench 2.1 (Pass@1) | 90.6 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| Terminal-Bench 3.0 (Pass@1) | 30.0 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| Terminal-Bench 4.0 (Pass@1) | 31.2 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| DeepSWE v1.1 (Resolved) | 74.2 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| ProgramBench (Almost@1) | 20.3 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| NL2Repo-Bench (Score) | 64.0 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| CyberGym (Pass@1) | 88.1 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| SEC-Bench Pro (Pass@1) | 62.8 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| ExploitGym (Pass@1) | 15.3 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| HLE w/ tools (Pass@1) | 63.9 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| AutomationBench (Pass@1) | 54.8 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| Agent's Last Exam (Pass@1) | 31.8 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| Chartography w/ tools (Pass@1) | 78.9 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| BabyVision w/ tools (Pass@1) | 89.6 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
| ZeroBench-main w/ tools (Pass@5) | 49.0 | Instruct 表欄「DS-V4.1-Flash」（reasoning_effort=100）。 |
