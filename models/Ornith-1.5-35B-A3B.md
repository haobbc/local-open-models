# Ornith-1.5-35B-A3B

官方模型卡：[ornith-ai/Ornith-1.5-35B-A3B](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)

這一頁只整理該 repo 的 README、`config.json`，以及同一 repo 檔案列表上的位元組。沒有寫出來的數字記「卡上未列」。表內分數都是販商自報，不跟 README 排行用的 Artificial Analysis Intelligence Index v4.3.2 放在同一欄。

這個檢查點不在 README 的 AA 名次表裡。

## 授權

license 欄：mit。license_link：https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B/blob/main/LICENSE。

## 發佈日期

卡上未列。

## 參數與卡上句子

- 卡上文字：~35B mixture-of-experts model with ~3B activated parameters per token (≈70 GB in bf16)。
- 服務說明寫 256K context，並以 2× 80GB GPU 當範例。
- 比較表是販商自報。不寫進 README 的 Artificial Analysis 名次。
- 官方 GGUF repo：https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B-GGUF 。各檔分開列，不加總。
- safetensors 索引的參數總數 35951822704（BF16 35951822704）。這是檔案索引，不是模型卡正文的句子。

## 架構

架構數字取自 `text_config`。
- model_type：qwen3_5_moe_text
- 層數 num_hidden_layers：40
- hidden size：2048
- attention heads：16
- KV heads：2
- head dim：256
- MoE intermediate：512
- shared expert intermediate：512
- 專家數 num_experts：256
- 每 token 專家數：8
- max_position_embeddings：262144
- vocab size：248320
- vision_config：hidden_size=1152，model_type=qwen3_5_moe_vision

## 權重檔

GiB 一律是檔案列表的 bytes ÷ 1024³，不是卡上另寫的一句話。不同量化、不同目錄的重複打包不加在一起。

- 基座 safetensors：16 個檔，71903871064 bytes，換算 66.97 GiB（bytes ÷ 1024³）。官方基座卡自己有權重，所以 GGUF 不另開一張卡，也不把各量化加總成一根長條。

官方 GGUF（各檔分開，不加總）：

- `Ornith-1.5-35B-BF16.gguf`：71066994400 bytes，66.19 GiB
- `Ornith-1.5-35B-Q4_K_M.gguf`：21713463040 bytes，20.22 GiB
- `Ornith-1.5-35B-Q5_K_M.gguf`：25347532544 bytes，23.61 GiB
- `Ornith-1.5-35B-Q6_K.gguf`：29208731392 bytes，27.20 GiB
- `Ornith-1.5-35B-Q8_0.gguf`：37802149280 bytes，35.21 GiB
- `mmproj-Ornith-1.5-35B-BF16.gguf`：902822240 bytes，0.84 GiB

## 基準（販商自報）

| 基準 | 分數 | 出處 |
| --- | --- | --- |
| Terminal-Bench 2.1 (Terminus-2) | 67.8 | 欄「Ornith-1.5-35B-A3B」。 |
| Terminal-Bench 2.1 (Claude Code) | 68.5 | 欄「Ornith-1.5-35B-A3B」。 |
| SWE-bench Verified | 79 | 欄「Ornith-1.5-35B-A3B」。 |
| SWE-bench Pro | 59.6 | 欄「Ornith-1.5-35B-A3B」。 |
| SWE-bench Multilingual | 71.4 | 欄「Ornith-1.5-35B-A3B」。 |
| DeepSWE | 22 | 欄「Ornith-1.5-35B-A3B」。 |
| Frontier-Bench v0.1 | 5.1 | 欄「Ornith-1.5-35B-A3B」。 |
| NL2Repo | 46.2 | 欄「Ornith-1.5-35B-A3B」。 |
| SWE Atlas - QnA | 39.8 | 欄「Ornith-1.5-35B-A3B」。 |
| HLE (no tools) | 25.6 | 欄「Ornith-1.5-35B-A3B」。 |
| HLE (with tools) | 33.4 | 欄「Ornith-1.5-35B-A3B」。 |
| GPQA Diamond | 89.2 | 欄「Ornith-1.5-35B-A3B」。 |
| MCP-Atlas | 70.2 | 欄「Ornith-1.5-35B-A3B」。 |
| Toolathlon-Verified | 48.7 | 欄「Ornith-1.5-35B-A3B」。 |
| WideSearch | 67.8 | 欄「Ornith-1.5-35B-A3B」。 |
| BrowseComp | 67.6 | 欄「Ornith-1.5-35B-A3B」。 |
| ClawEval | 72.5 | 欄「Ornith-1.5-35B-A3B」。 |
