# Qwen3.8-Flash-Next

官方模型卡：[Qwen/Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

## 授權

license 欄：other。license_name：qwen-community-1.0。license_link：LICENSE。

## 發佈日期

卡上未列。

## 參數與卡上句子

- 卡上文字：125B with 6B activated, plus 51B n-gram embedding and 4B MTP。
- 卡上文字：512 experts，10 Routed + 1 Shared，expert intermediate 640。
- 卡上文字：Context Length: 262,144 natively and extensible up to 1,000,000 tokens。
- 授權 license 欄是 other，license_name 是 qwen-community-1.0。
- safetensors 索引的參數總數 179999981459（BF16 179999981424、I64 35）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `text_config`。
- model_type：qwen4_exp_text
- 層數 num_hidden_layers：48
- hidden size：2560
- attention heads：24
- KV heads：2
- head dim：256
- MoE intermediate：640
- shared expert intermediate：640
- 專家數 num_experts：512
- 每 token 專家數：10
- max_position_embeddings：262144
- vocab size：248320
- vision_config：hidden_size=1152，model_type=qwen4_exp

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：131 個檔，360000192888 bytes，換算 335.28 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| Agentic coding DeepSWE 1.1 | 58.7 | 表 1 欄「Qwen3.8-Flash-Next」。 |
| Agentic coding SWE-bench Pro | 62.5 | 表 1 欄「Qwen3.8-Flash-Next」。 |
| Multilingual software engineering SWE-bench Multilingual | 81.0 | 表 1 欄「Qwen3.8-Flash-Next」。 |
| Repo-level code generation NL2Repo-Bench | 48.1 | 表 1 欄「Qwen3.8-Flash-Next」。 |
| Long-horizon office work CoWorkBench | 73.9 | 表 1 欄「Qwen3.8-Flash-Next」。 |
| Professional job tasks JobBench | 55.7 | 表 1 欄「Qwen3.8-Flash-Next」。 |
| Frontier agentic tasks Agents' Last Exam | Pass@1 24.3 Score 51.2 | 表 1 欄「Qwen3.8-Flash-Next」。 |
| Real-world tool use Toolathlon Verified (Pass@1) | 73.5 | 表 1 欄「Qwen3.8-Flash-Next」。 |
| Instruction following IFBench | 81.3 | 表 1 欄「Qwen3.8-Flash-Next」。 |
| Scientific reasoning GPQA Diamond | 91.7 | 表 1 欄「Qwen3.8-Flash-Next」。 |
| Multidisciplinary reasoning HLE | 35.9 | 表 1 欄「Qwen3.8-Flash-Next」。 |
| Competitive coding LiveCodeBench v6 | 91.9 | 表 1 欄「Qwen3.8-Flash-Next」。 |
| Multimodal tool use ClawEval-MM | Pass@3 64.4 Average 60.4 | 表 2 欄「Qwen3.8-Flash-Next」。 |
| Application recreation RecreationBench | 49.9 | 表 2 欄「Qwen3.8-Flash-Next」。 |
| Mobile use AndroidWorld | 84.5 | 表 2 欄「Qwen3.8-Flash-Next」。 |
| Computer use OSWorld 2.0 | Binary 19.4 Partial 52.3 | 表 2 欄「Qwen3.8-Flash-Next」。 |
| Visual web development Vision2Web | 64.0 | 表 2 欄「Qwen3.8-Flash-Next」。 |
| Embodied intelligence ERQA | 72.3 | 表 2 欄「Qwen3.8-Flash-Next」。 |
| Long video understanding LVBench | 76.6 | 表 2 欄「Qwen3.8-Flash-Next」。 |
| Real-world perception RealWorldQA | 88.5 | 表 2 欄「Qwen3.8-Flash-Next」。 |
| Visual math problem solving MathVision | Without CI 90.6 With CI 95.7 | 表 2 欄「Qwen3.8-Flash-Next」。 |
| Scientific chart analysis CharXiv (RQ) | Without CI 84.6 With CI 90.6 | 表 2 欄「Qwen3.8-Flash-Next」。 |
