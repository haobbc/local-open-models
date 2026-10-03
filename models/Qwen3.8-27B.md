# Qwen3.8-27B

官方模型卡：[Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

## 授權

license 欄：apache-2.0。

## 發佈日期

卡上未列。citation 的 month 不是檢查點發佈日。

## 參數與卡上句子

- 卡上文字：Number of Parameters: 27B。
- 卡上文字：Context Length: 262,144 natively and extensible up to 1,000,000 tokens。
- 卡上架構句：Hidden Layout 為 16 × (3 × (Gated DeltaNet → FFN) → 1 × (Gated Attention → FFN))。MTP trained with multiple steps。
- 稠密模型，卡上沒有專家數。
- safetensors 索引的參數總數 27781427952（BF16 27781427952）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `text_config`。
- model_type：qwen3_5_text
- 層數 num_hidden_layers：64
- hidden size：5120
- attention heads：24
- KV heads：4
- head dim：256
- intermediate size：17408
- max_position_embeddings：262144
- vocab size：248320
- vision_config：hidden_size=1152，model_type=qwen3_5

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 根目錄 safetensors：18 個檔，55563006776 bytes，換算 51.75 GiB（bytes ÷ 1024³）。只有一種包裝。

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| Agentic terminal coding Terminal Bench 2.1 (Terminus) | 73.0 | 表 1 欄「Qwen3.8-27B」。 |
| Agentic coding SWE-bench Pro | 61.7 | 表 1 欄「Qwen3.8-27B」。 |
| Repo-level code generation NL2Repo-Bench | 42.3 | 表 1 欄「Qwen3.8-27B」。 |
| Agentic coding DeepSWE 1.1 | 42.2 | 表 1 欄「Qwen3.8-27B」。 |
| Software engineering QwenSWEBench | 79.0 | 表 1 欄「Qwen3.8-27B」。 |
| Long-horizon office work CoWorkBench | 70.7 | 表 1 欄「Qwen3.8-27B」。 |
| Professional job tasks JobBench | 33.4 | 表 1 欄「Qwen3.8-27B」。 |
| Frontier agentic tasks Agents' Last Exam | Pass@1 20.4 Score 42.9 | 表 1 欄「Qwen3.8-27B」。 |
| Instruction following IFBench | 79.5 | 表 1 欄「Qwen3.8-27B」。 |
| Scientific reasoning GPQA Diamond | 89.2 | 表 1 欄「Qwen3.8-27B」。 |
| Multidisciplinary reasoning HLE | 30.8 | 表 1 欄「Qwen3.8-27B」。 |
| Competitive coding LiveCodeBench v6 | 90.3 | 表 1 欄「Qwen3.8-27B」。 |
| Computer use OSWorld-Verified | 84.3 | 表 2 欄「Qwen3.8-27B」。 |
| Browser use WebArena-Verified | 64.8 | 表 2 欄「Qwen3.8-27B」。 |
| Mobile use AndroidWorld | 81.9 | 表 2 欄「Qwen3.8-27B」。 |
| Application recreation RecreationBench | 47.1 | 表 2 欄「Qwen3.8-27B」。 |
| Multimodal tool use ClawEval-MM | Pass@3 57.4 Average 56.9 | 表 2 欄「Qwen3.8-27B」。 |
| Multimodal software engineering SWE-MM | 38.6 | 表 2 欄「Qwen3.8-27B」。 |
| Visual web development Vision2Web | 62.9 | 表 2 欄「Qwen3.8-27B」。 |
| Visual math problem solving MathVision | Without CI 90.0 With CI 94.6 | 表 2 欄「Qwen3.8-27B」。 |
| General visual reasoning BabyVision | Without CI 65.7 With CI 85.6 | 表 2 欄「Qwen3.8-27B」。 |
| Scientific chart analysis CharXiv (RQ) | Without CI 83.7 With CI 90.2 | 表 2 欄「Qwen3.8-27B」。 |
| Document intelligence OmniDocBench 1.5 | 91.1 | 表 2 欄「Qwen3.8-27B」。 |
| Real-world perception RealWorldQA | 85.9 | 表 2 欄「Qwen3.8-27B」。 |
| Embodied intelligence ERQA | 65.5 | 表 2 欄「Qwen3.8-27B」。 |
