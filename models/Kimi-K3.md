# Kimi K3

官方模型卡：[moonshotai/Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

這個檢查點不在 README 的 AA 名次表裡。

## 授權

license 欄：other。license_name：kimi-k3。

## 發佈日期

卡上未列。

## 參數與卡上句子

- 架構表：Total 2.8T，Activated 104B，layers 93，dense layers 1，experts 896，selected per token 16。
- config.json 另有 num_shared_experts 2、num_experts_per_token 16、hidden 7168、moe intermediate 3072。
- 授權 license 欄為 other，license_name 為 kimi-k3。
- 比較表欄名是 Kimi K3 (max)。檔案是 U8 為主的打包，卡上未另給一份 BF16 檔案大小。
- safetensors 索引的參數總數 2779931837184（F32 11122432、BF16 57179884544、U8 2722740830208）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `text_config`。
- model_type：kimi_linear
- 層數 num_hidden_layers：93
- hidden size：7168
- attention heads：96
- KV heads：96
- intermediate size：33792
- MoE intermediate：3072
- 專家數 num_experts：896
- 共享專家 num_shared_experts：2
- 每 token 專家數：16
- max_position_embeddings：1048576
- vocab size：163840
- MTP 層 num_nextn_predict_layers：0

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：96 個檔，1560936091448 bytes，換算 1453.74 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| GPQA Diamond | 93.5 | 欄「Kimi K3 (max)」。 |
| CritPt | 23.4 | 欄「Kimi K3 (max)」。 |
| AA-LCR | 74.7 | 欄「Kimi K3 (max)」。 |
| HLE-Full | 43.5 / 56.0 | 欄「Kimi K3 (max)」。 |
| DeepSWE | 67.5 | 欄「Kimi K3 (max)」。 |
| ProgramBench | 77.8 | 欄「Kimi K3 (max)」。 |
| Terminal-Bench 2.1 | 88.3 | 欄「Kimi K3 (max)」。 |
| FrontierSWE | 81.2 | 欄「Kimi K3 (max)」。 |
| SWE-Marathon | 42.0 | 欄「Kimi K3 (max)」。 |
| PostTrainBench | 36.6 | 欄「Kimi K3 (max)」。 |
| MLS-Bench-Lite | 48.3 | 欄「Kimi K3 (max)」。 |
| SciCode | 58.7 | 欄「Kimi K3 (max)」。 |
| Kimi Code Bench 2.0 | 72.9 | 欄「Kimi K3 (max)」。 |
| BrowseComp | 91.2 | 欄「Kimi K3 (max)」。 |
| DeepSearchQA (F1) | 95.0 | 欄「Kimi K3 (max)」。 |
| ResearchRubrics | 76.2 | 欄「Kimi K3 (max)」。 |
| GDPval-AA v2 (Elo) | 1686 | 欄「Kimi K3 (max)」。 |
| Toolathlon-Verified | 76.5 | 欄「Kimi K3 (max)」。 |
| MCPMark-Verified | 94.5 | 欄「Kimi K3 (max)」。 |
| MCP-Atlas | 84.2 | 欄「Kimi K3 (max)」。 |
| AutomationBench | 30.8 | 欄「Kimi K3 (max)」。 |
| JobBench | 54.3 | 欄「Kimi K3 (max)」。 |
| AA-Briefcase (Elo) | 1548 | 欄「Kimi K3 (max)」。 |
| Agents' Last Exam | 28.3 | 欄「Kimi K3 (max)」。 |
| APEX-Agents | 41.0 | 欄「Kimi K3 (max)」。 |
| OfficeQA Pro | 63.3 | 欄「Kimi K3 (max)」。 |
| SpreadsheetBench 2 | 34.8 | 欄「Kimi K3 (max)」。 |
| OSWorld-Verified | 84.8 | 欄「Kimi K3 (max)」。 |
| OSWorld 2.0 | 58.3 | 欄「Kimi K3 (max)」。 |
| SaaS-Bench | 60.1 | 欄「Kimi K3 (max)」。 |
| τ³-Banking | 33.4 | 欄「Kimi K3 (max)」。 |
| Harvey Lab-AA | 94.6 | 欄「Kimi K3 (max)」。 |
| CorpFin v2 | 71.6 | 欄「Kimi K3 (max)」。 |
| Finance Agent v2 | 54.4 | 欄「Kimi K3 (max)」。 |
| Legal Research Bench | 44.2 | 欄「Kimi K3 (max)」。 |
| WorldVQA ForceAnswer | 51.0 | 欄「Kimi K3 (max)」。 |
| OmniDocBench | 91.1 | 欄「Kimi K3 (max)」。 |
| PerceptionBench | 58.5 | 欄「Kimi K3 (max)」。 |
| Video-MME (w. sub) | 90.0 | 欄「Kimi K3 (max)」。 |
| MMVU | 82.1 | 欄「Kimi K3 (max)」。 |
| BabyVision w/ python | 85.7 | 欄「Kimi K3 (max)」。 |
| MMMU-Pro | 81.6 / 83.4 | 欄「Kimi K3 (max)」。 |
| CharXiv (RQ) | 84.8 / 91.3 | 欄「Kimi K3 (max)」。 |
| MathVision | 94.3 / 97.8 | 欄「Kimi K3 (max)」。 |
| ZeroBench (pass@5) | 23.0 / 41.0 | 欄「Kimi K3 (max)」。 |
