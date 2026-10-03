# Qwen3.8-2.4T-A95B

官方模型卡：[Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

這個檢查點不在 README 的 AA 名次表裡。

## 授權

license 欄：other。license_name：qwen3.8-max。license_link：LICENSE。

## 發佈日期

卡上未列。

## 參數與卡上句子

- 卡上文字：2.4T in total and 95B activated。
- 512 experts，10 Routed + 1 Shared，expert intermediate 2048。
- Context Length: 262,144 natively and extensible up to 1,010,000 tokens。
- 授權 license 欄為 other，license_name 為 qwen3.8-max。
- 比較表高亮欄的名稱是 Qwen3.8-Max。卡上寫 Qwen3.8-Max 是以這個檢查點為基礎、另外帶視覺與預設 1M 的官方版本。分數記在欄名 Qwen3.8-Max 下面，不改寫成 repo 名稱，也不進 AA 名次。
- safetensors 索引的參數總數 2446182725504（BF16 2446182725504）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `config.json 頂層`。
- model_type：qwen3_5_moe_text
- 層數 num_hidden_layers：92
- hidden size：8192
- attention heads：64
- KV heads：4
- head dim：256
- MoE intermediate：2048
- shared expert intermediate：2048
- 專家數 num_experts：512
- 每 token 專家數：10
- max_position_embeddings：262144
- vocab size：248320

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：213 個檔，4892365649336 bytes，換算 4556.37 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| Terminal Bench 2.1 | 86.6 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| SWE-bench Pro | 67.7 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| DeepSWE 1.1 | 56.6 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| NL2Repo-Bench | 55.9 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| FrontierSWE | 73.5 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| MLS-Bench-Lite | 41.0 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| PaperBench | 93.0 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| AndroidBench | 75.1 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| QwenSWEBench | 80.7 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| QwenQoderBench | 58.4 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| QwenReactBench | 1724 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| QwenSVGBench | 1713 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| CoWorkBench | 74.8 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| WorkSpaceBench | 67.7 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| JobBench | 53.4 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| SkillsBench | 70.2 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| Agents' Last Exam (Pass / Score) | 27.0 / 52.4 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| Automation-Bench (Pass@1) | 27.3 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| Toolathlon Verified (Pass@1) | 72.5 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| WideSearch | 81.9 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| HLE w/ tools | 56.2 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| GPQA Diamond | 92.6 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| HLE | 43.6 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| IFBench | 82.8 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| $OneMillion-Bench (expert score) | 52.5 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| HealthBench | 60.2 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| PLawBench | 73.2 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| PRBench-Legal | 57.6 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| PRBench-Finance | 58.3 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| MRCR v2 256K (8-needle) | 92.9 | 欄「Qwen3.8-Max」（卡上欄名）。 |
| LongBench v2 | 66.3 | 欄「Qwen3.8-Max」（卡上欄名）。 |
