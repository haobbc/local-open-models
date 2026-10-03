# 開源模型以及本地部署深入研究：以實作為導向的榜單

快照日：**2026-10-03**。這份文件只做一件事：哪一檔硬體放得進哪些開源權重，以及那一檔拿來做什麼工作。

排序用 [Artificial Analysis Intelligence Index v4.3.2](https://artificialanalysis.ai/leaderboards/models)。閉源只當天花板，不進硬體榜：Claude Opus 5.5（max）**58**，GPT-6 Astra（max）與 Gemini 4 Argon（high）**53**，Grok 4.7（xhigh）**46**。開源最高的 MiMo-V2.6-Pro 也是 46，Q4 粗算約 475 GiB，單機榜排不進去。[LMArena](https://arena.ai/leaderboard/text/)（2026-10-02）文字榜第一是 Gemini 4 Argon（high）1525，Preliminary。兩榜不混成同一名次。

開源指權重可下載。授權以模型卡為準，不一定是 OSI 的 open source。

## 怎麼讀

**放得下 = 權重 ≤ 裝置記憶體。** 不為 KV cache 預留顯示記憶體。上下文不夠就縮，llama.cpp 與 vLLM 都做得到。

- MoE 要載入全部專家。啟動參數影響速度，不影響權重檔大小。
- 沒有實測檔的列是粗算：`GiB ≈ 參數量 × 0.5 ÷ 2^30`，不含 GGUF scale。
- Qwen3.8-27B 與 Qwen3.8-Flash-Next 的檔案大小用實測，不用上面的粗算。出處在文末「實測參考」。27B 的純 Q4 粗算約 12.6 GiB，實測 `q4_k_m` 是 17.77 GB。
- 小模型頁與中型頁當天只展開前 12 列。5090 前七名在已展開的列裡；第 8 名以後若還有分數約 12–16 的檢查點，名次可能往後移。
- Qwen3.8-27B 的 AA 是 **34**，Ling-3.0-flash-VL 是 **25**。記憶體變大也不把分數低的模型排到前面。

| 硬體 | 官方記憶體 | 權重上界 |
| --- | --- | --- |
| GeForce RTX 5090 | [32 GB GDDR7](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/) | ≤ 32 GiB |
| RTX PRO 6000 Blackwell | [96 GB GDDR7 ECC](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-family/) | ≤ 96 GiB |
| DGX Spark（GB10）或 128 GB Mac | [128 GB LPDDR5x](https://docs.nvidia.com/dgx/dgx-spark/hardware.html) | ≤ 128 GiB |
| 192 GB Mac | 192 GB 統一記憶體 | ≤ 192 GiB |

三張 32GB 卡加總不是單張 96GB。5090 前十的權重都低於 32 GiB，所以 **64 GB Mac 跑得了那前十**，跑不了下面五、六十 GiB 以上的權重。

## RTX 5090 32GB，前十

**這檔硬體拿來做什麼：** 繁體中文寫作、摘要、客服、公文，一次留一顆主力。`q4_k_m` 與 `q8_0` 都進得了 32GB。Qwen3.8-Flash-Next 進不去，英文 agent 不是這張卡的工作。

| # | 模型 | 參數 | AA | 權重 | 授權 | 這檔硬體拿來做什麼 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | 27B 稠密 | **34** | `q4_k_m` **17.77 GB**；`q8_0` **29.12 GB**。BF16 54.66 GB 要 96GB | Apache-2.0 | 繁中寫作。`q8_0` 約 8 t/s，品質接近全精度。這張卡一次留這一顆 |
| 2 | [K2-Horizon-MoVA-36B-A4B](https://huggingface.co/IFM/K2-Horizon-MoVA-36B-A4B) | 36B／4B | **25** | Q4 估算約 16.8 GiB | Apache-2.0 | 長上下文 MoE。官方雙卡 BF16 是速度配方，不是 32GB 的部署條件 |
| 3 | [G9v3-39A5B](https://huggingface.co/ai9stars/G9v3-39A5B) | 約 39B／5B | **22** | Q4 估算約 18.2 GiB | Apache-2.0 | 預覽版 MoE，上下文 131,072 |
| 4 | [K2-Horizon-7B](https://huggingface.co/IFM/K2-Horizon-7B) | 7B | **21** | Q4 估算約 3.3 GiB | Apache-2.0 | 同一系列的小模型，把記憶體留給上下文 |
| 5 | [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) | 35B／3B | **18** | Q4 估算約 16.3 GiB | Apache-2.0 | 圖文 MoE。同一份權重的 non-reasoning 只有 15，不另排 |
| 6 | [Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) | 30B | **17** | Q4 估算約 14.0 GiB | Apache-2.0 | 模型卡定位是本機 agent。感知編碼器另計 |
| 7 | [Gemma 4 26B A4B](https://huggingface.co/google/gemma-4-26B-A4B-it) | 25.2B／3.8B | **17** | Q4 估算約 11.7 GiB | Apache-2.0 | 圖文，與第 6 名同分 |
| 8 | [Granite 4.2 30B](https://huggingface.co/ibm-granite/granite-4.2-30b) | 30B | **15** | Q4 估算約 14.0 GiB | Apache-2.0 | 一般文字。參數用 AA 的 30B |
| 9 | [Gemma 4 31B-it](https://huggingface.co/google/gemma-4-31B-it) | 30.7B | **15** | Q4 估算約 14.3 GiB；Q8 估算約 28.6 GiB，也低於 32 GiB | Apache-2.0 | 圖文，與第 8 名同分 |
| 10 | [Qwen3.5 9B](https://huggingface.co/Qwen/Qwen3.5-9B) | 9.7B | **11** | Q4 估算約 4.5 GiB | Apache-2.0 | 小尺寸圖文 |

不進前十：Gemma 4 12B 是 14 分帶星號（估計），不拿來壓過已實測的 11。[gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) 是 9 分，MXFP4、16GB 以內，進得了這張卡，低於第 10 名。同一份 27B 權重的 medium／low／non-reasoning（28／26／20）不另排。

## RTX PRO 6000 96GB

**這檔硬體拿來做什麼：** 英文 agent 改由 Qwen3.8-Flash-Next 承擔，繁中與多模型常駐仍用 27B。Flash-Next 載入 87.24 GiB，權重進得了 96GB；在 128GB 機器上量到的執行峰值是 95.3 GiB，所以 96GB 上要把上下文縮短。unsloth 所列 4-bit 要 112 GB，96GB 與 128GB 都放不下。小模型留在表裡，只按 AA 排，Ling-3.0-flash-VL（25）因此在 27B（34）後面。

| # | 模型 | 參數 | AA | 權重 | 授權 | 這檔硬體拿來做什麼 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | 125B＋n-gram 51B；啟動 6B。AA 記 180B／6B | **40** | UD-IQ4_XS 磁碟 **93.68 GB**，載入 **87.24 GiB**。峰值 **95.3 GiB**（128GB 上量到） | Qwen Community License 1.0 | 英文 agent、程式、長輸入。decode 約 28 t/s，英文 PPL 比 27B BF16 好約 32%。繁中 PPL 差約 13%。一顆佔滿這張卡，不拿來當多模型的一員。商用先讀授權，與 27B 的 Apache-2.0 不同 |
| 2 | Qwen3.8-27B | 27B | **34** | BF16 **54.66 GB**、`q8_0` **29.12 GB**、`q4_k_m` **17.77 GB** | Apache-2.0 | 繁中寫作、摘要、客服、公文，並可與其他模型一起常駐。`q8_0` 約 8 t/s。BF16 在這張卡放得下 |
| 3 | K2-Horizon-MoVA-36B-A4B | 36B／4B | **25** | Q4 估算約 16.8 GiB | Apache-2.0 | 32GB 已能跑。這裡把餘裕留給上下文，或跟 27B 一起常駐 |
| 4 | [Ling-3.0-flash-VL](https://huggingface.co/inclusionAI/Ling-3.0-flash-VL) | 124B／5.5B | **25** | Q4 估算約 57.7 GiB | MIT | 視覺 MoE。與第 3 名同分，權重大很多。模型卡自引的 42 分是 v4.1.1，不跟本榜的 25 比 |
| 5 | [Ling-3.0-flash-Fin](https://huggingface.co/inclusionAI/Ling-3.0-flash-Fin) | 124B／5.1B | **23** | Q4 估算約 57.7 GiB | MIT | 金融向續訓 |
| 6 | G9v3-39A5B | 約 39B／5B | **22** | Q4 估算約 18.2 GiB | Apache-2.0 | 32GB 已能跑 |
| 7 | K2-Horizon-7B | 7B | **21** | Q4 估算約 3.3 GiB | Apache-2.0 | 32GB 已能跑。多模型時當小的那一顆 |
| 8 | Qwen3.6-35B-A3B | 35B／3B | **18** | Q4 估算約 16.3 GiB | Apache-2.0 | 32GB 已能跑的圖文 MoE |
| 9 | [Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) | 122B／10B | **18** | Q4 估算約 56.8 GiB | Apache-2.0 | 較大的 Qwen MoE。同一份權重取較高的 non-reasoning 列（reasoning 為 16） |
| 10 | Muse Glimmer 30B | 30B | **17** | Q4 估算約 14.0 GiB | Apache-2.0 | 32GB 已能跑的本機 agent |
| 11 | Gemma 4 26B A4B | 25.2B／3.8B | **17** | Q4 估算約 11.7 GiB | Apache-2.0 | 32GB 已能跑的圖文 |
| 12 | Granite 4.2 30B | 30B | **15** | Q4 估算約 14.0 GiB | Apache-2.0 | 32GB 已能跑 |
| 13 | Gemma 4 31B-it | 30.7B | **15** | Q4 估算約 14.3 GiB | Apache-2.0 | 32GB 已能跑的圖文 |
| 14 | [Mistral Medium 3.5](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B) | 128B 稠密 | **14** | Q4 估算約 59.6 GiB | 模型卡 `other` | 稠密大模型。32GB 放不下 |
| 15 | [Nemotron 3 Super 120B A12B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16) | 120.6B／12.7B | **13** | Q4 估算約 56.2 GiB | NVIDIA Nemotron Open Model License | MoE。授權先讀模型卡 |
| 16 | [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) | 117B／5.1B，MXFP4 | **12** | 4-bit 粗算約 54.5 GiB。模型卡寫單張 80GB，那是部署說法 | Apache-2.0 | 較舊的 MoE。官方說單張 80GB 放得下，96GB 夠用。與閉源 GPT-6 是不同模型 |
| 17 | Qwen3.5 9B | 9.7B | **11** | Q4 估算約 4.5 GiB | Apache-2.0 | 32GB 已能跑的小尺寸圖文 |
| 18 | [gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) | 21B／3.6B（AA） | **9** | 模型卡：MXFP4、16GB 以內 | Apache-2.0 | 低於 5090 前十。96GB 榜保留較小的模型 |

中型頁當天沒有展開的 K2 Think V2、LongCat-Flash-Lite、Mistral Small 4、HyperNova 60B 2605 不插進這張 AA 名次，模型卡在下文。Ling 3.0 Flash（指數 20）的權重欄是 Not available，仍然不放。Ornith-1.5-35B-A3B 與更大的前段開源權重也只做模型卡，販商自報分數不進上表。

統一記憶體上，把 Flash-Next 的 n-gram 表卸到 CPU 不會騰出記憶體。那一列是給獨立顯卡的。

## GB10 與 128GB Mac

**這檔硬體拿來做什麼：** 與 96GB 同一份 18 個名字、同一個名次。這次沒有「大於 96 GiB、小於等於 128 GiB」的新模型。128GB 讓 Flash-Next 的 95.3 GiB 峰值有餘裕，它仍吃掉約四分之三，要同時常駐多個模型就留 27B，把 Flash-Next 當成英文 agent 時再單獨載入。unsloth 的 4-bit（112 GB）不進這檔。

## 192GB Mac

**這檔硬體拿來做什麼：** 多跑一顆分數更高的 GLM-5.3-Flash。96GB 榜全體往後一名。

| 名次 | 模型 | AA | 權重 | 授權 | 這檔硬體拿來做什麼 |
| --- | --- | --- | --- | --- | --- |
| **1** | [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) | **42** | Q4 粗算約 **149 GiB** | MIT | 這張榜上單機放得下、分數最高的開源權重。320B 總／18B 啟動。149 GiB 大於 96，也大於 128。此列仍是粗算 |
| 2 | Qwen3.8-Flash-Next | 40 | 載入 87.24 GiB | Qwen Community License 1.0 | 英文 agent。餘裕比 128GB 大，仍不適合跟 GLM 同時常駐 |
| 3 | Qwen3.8-27B | 34 | BF16 54.66 GB 起 | Apache-2.0 | 繁中寫作，以及跟較小模型一起常駐 |

其餘沿用 96GB 榜，名次各加 1。

192GB 仍放不下的 Q4 粗算：MiniMax-M3 約 199 GiB、DeepSeek-V4.1-Flash 骨幹約 257 GiB、GLM-5.3 約 351 GiB、MiMo-V2.6-Pro 約 475 GiB、Qwen3.8-2.4T 約 1118 GiB、Kimi K3 原生 MXFP4 約 1304 GiB。

## 輸出速率

同一顆模型的 decode，要分開看資料放在哪。三欄的路徑不同：獨立顯示卡的權重在 GDDR；混合是權重放不進 VRAM 的部分留在系統記憶體，每個 token 跨 PCIe；統一記憶體是 CPU 與 GPU 共用同一塊 DRAM。有實測才填數字。沒有出處的格子寫「未測」，不用頻寬比例去補。

上文用途欄的「約 8 t/s」「約 28 t/s」是下面統一記憶體這一欄的四捨五入，機器是 DGX Spark GB10，不是 RTX 5090，也不是 RTX PRO 6000。

出處只有 [Day 14](https://ithelp.ithome.com.tw/articles/10405431)。機器是 DGX Spark GB10，128GB 統一記憶體，頻寬 273 GB/s。下列都未開投機解碼。

| 模型與量化 | 獨立顯示卡 VRAM（5090、RTX PRO 6000） | GPU/CPU 混合（權重溢出到系統記憶體） | 統一記憶體（GB10） |
| --- | --- | --- | --- |
| Qwen3.8-27B BF16 | 未測 | 未測 | **4.66 t/s**。llama.cpp |
| Qwen3.8-27B `q8_0` | 未測 | 未測 | **7.93 t/s**。llama.cpp。同文 vLLM 的 FP8 是 7.92 t/s，同一台機器 |
| Qwen3.8-27B `q4_k_m` | 未測 | 未測 | **11.77 t/s**。llama.cpp |
| Qwen3.8-Flash-Next UD-IQ4_XS | 未測 | 未測 | **28.02 t/s**。llama.cpp |

Day 14 另有一則說明，不填進混合欄：把 Flash-Next 的 n-gram 表釘到 CPU 之後，decode 從 27.92 t/s 到 23.26 t/s，大約慢 16.7%，系統記憶體峰值從 95.3 GiB 到 95.7 GiB。那仍是 GB10 的同一塊 DRAM，卸載沒有釋出 RAM，也不是獨立顯卡上權重溢出到系統記憶體的速率。獨立顯卡那條路，文中沒有給出 tok/s。

## 模型卡

排行表裡每個開源權重都有一頁，路徑是 `models/<repo 名稱>.md`。另外幾顆沒有插進上面 AA 名次的前段檢查點也有頁。圖在 [權重檔大小與模型卡基準](charts/index.html)。一根長條只代表一種權重包裝。一個基準名稱只跟同一個名稱比，沒有寫的模型不補 0。

### 在 AA 名次裡的模型卡

[Qwen3.8-27B](models/Qwen3.8-27B.md)、[K2-Horizon-MoVA-36B-A4B](models/K2-Horizon-MoVA-36B-A4B.md)、[G9v3-39A5B](models/G9v3-39A5B.md)、[K2-Horizon-7B](models/K2-Horizon-7B.md)、[Qwen3.6-35B-A3B](models/Qwen3.6-35B-A3B.md)、[Muse Glimmer 30B](models/Muse-Glimmer-30B.md)、[Gemma 4 26B A4B](models/gemma-4-26B-A4B-it.md)、[Granite 4.2 30B](models/granite-4.2-30b.md)、[Gemma 4 31B](models/gemma-4-31B-it.md)、[Qwen3.5-9B](models/Qwen3.5-9B.md)、[Qwen3.8-Flash-Next](models/Qwen3.8-Flash-Next.md)、[Ling-3.0-flash-VL](models/Ling-3.0-flash-VL.md)、[Ling-3.0-flash-Fin](models/Ling-3.0-flash-Fin.md)、[Qwen3.5-122B-A10B](models/Qwen3.5-122B-A10B.md)、[Mistral Medium 3.5](models/Mistral-Medium-3.5-128B.md)、[Nemotron 3 Super](models/NVIDIA-Nemotron-3-Super-120B-A12B-BF16.md)、[gpt-oss-120b](models/gpt-oss-120b.md)、[gpt-oss-20b](models/gpt-oss-20b.md)、[GLM-5.3-Flash](models/GLM-5.3-Flash.md)。

### 有卡，但不進 AA 名次

這些檢查點的分數如果出現在模型卡上，都是販商自報，不寫進上面的 Artificial Analysis 表。

[Ornith-1.5-35B-A3B](models/Ornith-1.5-35B-A3B.md)、[K2 Think V2](models/K2-Think-V2.md)、[LongCat-Flash-Lite](models/LongCat-Flash-Lite.md)、[Mistral Small 4](models/Mistral-Small-4-119B-2603.md)、[HyperNova 60B 2605](models/Hypernova-60B-2605.md)、[MiMo-V2.6-Pro-RL](models/MiMo-V2.6-Pro-RL.md)、[GLM-5.3](models/GLM-5.3.md)、[Kimi K3](models/Kimi-K3.md)、[Qwen3.8-2.4T-A95B](models/Qwen3.8-2.4T-A95B.md)、[DeepSeek-V4.1-Flash](models/DeepSeek-V4.1-Flash.md)、[MiniMax-M3](models/MiniMax-M3.md)。

K2 Think V2、LongCat-Flash-Lite、Mistral Small 4、HyperNova 60B 2605 是快照當天中型頁沒有展開的名字，所以不插進名次。MiMo-V2.6-Pro、GLM-5.3、Kimi K3、Qwen3.8-2.4T、DeepSeek-V4.1-Flash、MiniMax-M3 的權重檔大於 192 GiB 這張榜的上界。Ornith-1.5-35B-A3B 的基座 safetensors 約 66.97 GiB，官方 GGUF 各檔分開列在同一頁，販商自報分數不進 AA 表。

## 基準名稱

下面只解釋模型卡上實際出現的名稱：它在測什麼、高分通常代表什麼。同一個英文名在不同卡上的題集、工具和 harness 可能不同。卡上標 lower is better 或 ↓ 的，低分較好。這些數字都不是本榜的 AA v4.3.2。Ling-3.0-flash-VL 卡上的 42 是 v4.1.1，排行表用的是 v4.3.2 的 25。

### 知識與指令

- AGIEval (EM)：AGIEval：考試風格的選擇與生成題。高分較好。
- Arena-Hard-V2：Arena-Hard：模型對戰的勝率風格分數。不是 LMArena 文字榜的 Elo。高分較好。
- BBEH (EM)：BigBench / BBEH：多樣任務的推理集合。高分較好。
- BBH (EM)：BBH：難度較高的語言推理題組。高分較好。
- C-Eval、C-Eval (EM)、CEval(acc)：C-Eval：中文多科考試題。高分較好。
- CMMLU(acc)、MMLU(acc)、MMMLU：MMLU：多科選擇題。高分代表答對較多。
- DROP (F1)：DROP：需要離散推理的閱讀理解，卡上指標是 F1。高分較好。
- GPQA、GPQA Diamond、GPQA Diamond (AA)、GPQA Diamond (Pass@1)、GPQA Diamond Graduate-level science QA、GPQA-Diamond、GPQA-Diamond(avg@16)、GPQA:d、Scientific reasoning GPQA Diamond：GPQA：研究生程度的科學問答，Diamond 是較難子集。高分較好。
- Global PIQA：Global PIQA：多語言的物理常識選擇。高分較好。
- HLE、HLE (Pass@1)、HLE (text)、HLE Expert-level reasoning、HLE Text (AA)、HLE w/ CoT、HLE with search、HLE-Full、Humanity's Last Exam、Multidisciplinary reasoning HLE：HLE（Humanity's Last Exam）：跨領域難題。有的卡分「無工具／有工具」或「只要文字子集」，不能跟總分混成一根。高分較好。
- HellaSwag (EM)：HellaSwag：句子接龍常識。高分較好。
- IFBench、IFBench (loose)、IFBench (prompt)、IFEval、IFEval (loose)、Instruction following IFBench、MultiChallenge：指令遵循（IFEval、IFBench、MultiChallenge）。高分代表較常照格式與限制做。
- INCLUDE：INCLUDE：多語言知識題。高分較好。
- MMLU Pro、MMLU-Pro、MMLU-Pro (EM)、MMLU-Pro(acc)、MMLU-ProX、MMLU-ProX (avg over langs)、MMLU-ProX lite (IBM)：MMLU-Pro：比 MMLU 更難的多科選擇題。高分代表答對較多。
- MMLU-Redux：MMLU-Redux：MMLU 的訂正版多科題。高分較好。
- NOVA-63：NOVA-63：多語言題組。高分較好。
- SimpleQA-Verified (EM)：SimpleQA：短事實問答，看會不會亂編。高分較好。
- SuperGPQA、SuperGPQA (EM)：SuperGPQA：研究生程度的多科問答。高分較好。
- WMT24++、WMT24++ (en→xx)：WMT：機器翻譯。高分較好。

### 數學

- AIME 2025、AIME 2026、AIME 2026 no tools、AIME24(avg@32)、AIME25、AIME25 (no tools)、AIME25(avg@32)、AIME26、GSM8K (EM)、HMMT 2025、HMMT Feb 2025、HMMT Feb 2026、HMMT Feb 2026 Competition mathematics、HMMT Feb 25、HMMT Feb 26、HMMT Feb25、HMMT Feb25 (no tools)、HMMT Feb25 (with tools)、HMMT Nov 25、IMOAnswerBench、MATH (EM)、MATH500(acc)、MGSM (EM)、MathArena Apex (Pass@1)、PolyMATH：數學競賽或數學應用題（AIME、HMMT、MATH、GSM8K 等）。高分代表解對較多。不同年份是不同卷。
- DynaMath、MATH-Vision、MathVision、Mathvista(mini)、Visual math problem solving MathVision、We-Math：圖文理解、文件、圖表或視覺數學。高分通常較好。OmniDocBench 若寫的是 edit distance，低分較好，那一列的名字裡會標出來。
- Multimodal software engineering SWE-MM：軟體工程：在真實或仿真的程式庫裡改程式（SWE-bench、DeepSWE、NL2Repo、FrontierSWE 等）。高分代表解掉較多任務。Verified、Pro、Multilingual 是不同題集。
- Multimodal tool use ClawEval-MM：代理人或辦公室長任務。高分代表完成較多。Pass@1 與另一個 Score 若寫在同一格，圖上不拆。

### 程式與軟體工程

- AIDER、BigCodeBench (Pass@1)、CodeForces、Codeforces (Rating)、Codeforces ELO、Competitive coding LiveCodeBench v6、FullStackBench en、FullStackBench zh、HumanEval (Pass@1)、LiveCodeBench、LiveCodeBench (v5 2024-07↔2024-12)、LiveCodeBench v6、OJBench、SciCode、SciCode (subtask)、SciCode Scientific coding：程式題（LiveCodeBench、Codeforces、HumanEval、SciCode、AIDER 等）。分數或 rating 愈高，代表解題較多或對手段位較高。
- Agentic coding DeepSWE 1.1、Agentic coding SWE-bench Pro、DeepSWE、DeepSWE (v1.1)、DeepSWE 1.1、DeepSWE v1.1、DeepSWE v1.1 (Resolved)、FrontierSWE、Multilingual software engineering SWE-bench Multilingual、NL2Repo、NL2Repo-Bench、NL2Repo-Bench (Score)、PaperBench、ProgramBench、ProgramBench (Almost Solved)、ProgramBench (Almost@1)、QwenQoderBench、QwenReactBench、QwenSWEBench、Repo-level code generation NL2Repo-Bench、SWE Atlas - QnA、SWE Bench Multilingual、SWE Bench Pro、SWE Bench Verified、SWE-Bench (Codex)、SWE-Bench (OpenCode)、SWE-Bench (OpenHands)、SWE-Bench Multiligual、SWE-Bench Multilingual (OpenHands)、SWE-Bench Pro、SWE-Bench Verified、SWE-Bench(acc)、SWE-Marathon、SWE-Marathon (v1.1)、SWE-bench Multilingual、SWE-bench Pro、SWE-bench Verified、SWE-bench Verified Software engineering、Software engineering QwenSWEBench：軟體工程：在真實或仿真的程式庫裡改程式（SWE-bench、DeepSWE、NL2Repo、FrontierSWE 等）。高分代表解掉較多任務。Verified、Pro、Multilingual 是不同題集。
- CritPt Frontier physics reasoning：CritPt：物理前沿推理。高分較好。
- Frontier agentic tasks Agents' Last Exam：代理人或辦公室長任務。高分代表完成較多。Pass@1 與另一個 Score 若寫在同一格，圖上不拆。
- Frontier-Bench v0.1：Frontier-Bench：Ornith 卡上的這個名稱。卡上沒有寫題目內容。圖上只跟同一名稱比，高分較好。
- WorldVQA ForceAnswer：視覺問答或感知題。高分較好。

### 終端與電腦操作

- Agentic terminal coding Terminal Bench 2.1 (Terminus)、Terminal Bench、Terminal Bench (hard subset)、Terminal Bench 2、Terminal Bench 2.1、Terminal Bench 3.0、Terminal Bench 4.0、Terminal Bench Core 2.0、Terminal-Bench 2.0、Terminal-Bench 2.1、Terminal-Bench 2.1 (Claude Code)、Terminal-Bench 2.1 (Pass@1)、Terminal-Bench 2.1 (Terminus-2)、Terminal-Bench 2.1 Agentic terminal use、Terminal-Bench 2.1（只寫了 AA protocol，沒有分數）、Terminal-Bench 3.0 (Pass@1)、Terminal-Bench 4.0 (Pass@1)、TerminalBench 2.1 (with terminus2)、TerminalBench(acc)：Terminal-Bench：在終端裡完成任務。2.0、2.1、3.0、4.0 與 Terminus、Claude Code 等 harness 要分開看。高分較好。
- AndroidBench：Android 介面或程式任務。高分較好。
- AndroidWorld、Application recreation RecreationBench、Browser use WebArena-Verified、Computer use OSWorld 2.0、Computer use OSWorld-Verified、Mobile use AndroidWorld、OSWorld 2.0、OSWorld-Verified、ScreenSpot Pro、Visual web development Vision2Web：操作電腦、手機或瀏覽器的介面任務。高分代表任務完成較多。

### 工具與代理人

- AA-Briefcase (Elo)、APEX-Agents、Agent's Last Exam (Pass@1)、Agents' Last Exam、Agents' Last Exam (ALE-CLI)、Agents' Last Exam (Pass / Score)、Agents’ Last Exam、Agent’s Last Exam、Automation-Bench (Pass@1)、AutomationBench、AutomationBench (Pass@1)、AutomationBench (v1.0.6)、AutomationBench v1.0.6、Claw-Eval Avg、Claw-Eval Pass^3、ClawEval、CoWorkBench、Finance Agent、Finance Agent v2、JobBench、Long-horizon office work CoWorkBench、OfficeQA Pro、Professional job tasks JobBench、QwenClawBench、SkillsBench、SkillsBench (with skills)、SkillsBench Avg5、SpreadsheetBench、SpreadsheetBench 2、WildClawBench：代理人或辦公室長任務。高分代表完成較多。Pass@1 與另一個 Score 若寫在同一格，圖上不拆。
- BFCL (v4)、BFCL v4、BFCL-V4、MCP Atlas (Public)、MCP-Atlas、MCPMark、MCPMark-Verified、Real-world tool use Toolathlon Verified (Pass@1)、Tool Decathlon、Toolathlon Verified、Toolathlon Verified (Pass@1)、Toolathlon-Verified、VITA-Bench：工具呼叫與 MCP 任務（BFCL、Toolathlon、MCP-Atlas、MCPMark）。高分代表叫對工具或完成任務。
- BabyVision w/ tools (Pass@1)、Chartography w/ tools (Pass@1)、ZeroBench-main w/ tools (Pass@5)：圖文理解、文件、圖表或視覺數學。高分通常較好。OmniDocBench 若寫的是 edit distance，低分較好，那一列的名字裡會標出來。
- BrowseComp、BrowseComp Web browsing、BrowseComp with Search、Browsecomp、Browsecomp-zh：網頁瀏覽或搜尋（BrowseComp、WideSearch、DeepSearch）。高分代表找到的答案較準。各卡的上下文協議可能不同。
- GDPVal-AA v2、GDPval、GDPval-AA 2.1、GDPval-AA v2、GDPval-AA v2 (Elo)：GDPval：辦公產出的評分，卡上有的記 Elo、有的記分數。只跟同一欄的寫法比。高分較好。
- GPQA (no tools)、GPQA (with tools)：GPQA：研究生程度的科學問答，Diamond 是較難子集。高分較好。
- Gaia2：GAIA：多步問答。高分較好。
- HLE (no tools)、HLE (with tools)、HLE no tools、HLE w/ Tools、HLE w/ tool、HLE w/ tools、HLE w/ tools (Pass@1)、Humanity's Last Exam (without tools) Expert-level reasoning：HLE（Humanity's Last Exam）：跨領域難題。有的卡分「無工具／有工具」或「只要文字子集」，不能跟總分混成一根。高分較好。
- Siren AgentDojo Attack Success Rate (↓)、Siren AgentDojo Utility：安全或偏見。卡上寫 lower is better 或帶 ↓ 的項目，低分較好；拒絕有害請求的比例則是高分較好。
- TAU2-Bench、TAU3-Bench、Tau2 (average over 3)、Tau2-Airline(avg@8)、Tau2-Retail(avg@8)、Tau2-Telecom(avg@8)、Tau2-bench Telecom、TauBench V2 Airline、TauBench V2 Average、TauBench V2 Retail、TauBench V2 Telecom、tau3-Banking Agentic tool use、τ³-Banking、τ³-Telecom、τ³-bench (AVG)：τ³ / Tau / TAU2：多輪工具呼叫（航空、零售、銀行、電信等）。高分代表任務完成較多。

### 長上下文

- AA LCR、AA-LCR、AA-LCR Long-context reasoning、Beam128K、LCR Long-context reasoning、LongBench v2、LongBench-V2 (EM)、MMLongBench-Doc、MRCR v2 256K (8-needle)、MRCR v2 8 needle 128k (average)、RULER 128K、RULER 64K、RULER @ 1M、RULER @ 256k、RULER @ 512k：長上下文（AA-LCR、LongBench、RULER、MRCR）。高分代表長文裡仍答得準。長度標記（64K、128K、256K、1M）要分開。

### 多模態與文件

- AI2D_TEST、BabyVision、BabyVision w/ python、CC-OCR、CharXiv (RQ)、CharXiv(RQ)、Charxiv Reasoning、CountBench、DocVQA (LLM-Judge)、Document intelligence OmniDocBench 1.5、ERQA、Embodied intelligence ERQA、General visual reasoning BabyVision、HallusionBench、MMBench EN-DEV-v1.1、MMMU、MMMU Pro、MMMU-Pro、MMMU-Pro (EM)、MMStar、OCRBench、OmniDocBench、OmniDocBench 1.5 (average edit distance, lower is better)、OmniDocBench v1.5、OmniDocBench1.5、Real-world perception RealWorldQA、RealWorldQA、RefCOCO(avg)、RefCOCO-avg (Acc@0.5)、Scientific chart analysis CharXiv (RQ)、VideoMMMU、ZEROBench、ZEROBench_sub、ZeroBench (pass@5)：圖文理解、文件、圖表或視覺數學。高分通常較好。OmniDocBench 若寫的是 edit distance，低分較好，那一列的名字裡會標出來。
- CVBench (EM)：CVBench：視覺理解。高分較好。
- Long video understanding LVBench、Video-MME (w. sub)、VideoMME (w sub.)、VideoMME (w/o sub.)：影片理解。高分較好。有字幕與無字幕是不同設定。

### 安全

- BBQ、StereoSet ICAT、StereoSet language model score、StereoSet stereotype score、StrongREJECT jailbreak rate、StrongREJECT metric、WMDP (Bio)、WMDP (Chem)、XSTest safe refusal、XSTest unsafe refusal：安全或偏見。卡上寫 lower is better 或帶 ↓ 的項目，低分較好；拒絕有害請求的比例則是高分較好。
- CI Memories Violation (↓)：CI Memories：情境隱私。Violation 低分較好；Coverage 高分較好。
- Content & Public Safety：K2 Think 的 Safety-4 巨觀分數。高分代表該安全面向較好；卡上把 Data & Infrastructure 標成 Critical。
- CyberGym、CyberGym (Pass@1)、ExploitBench、ExploitGym、ExploitGym (2h / 6h)、ExploitGym (Pass@1)、MiMo Cyber Bench：資安任務（CyberGym、ExploitGym、ExploitBench、SEC Bench）。高分代表通過較多題。時間預算不同的格子要分開。
- HPCT、Lab Bench (ProtocolQA)、MBCT、VCT：化學與生物預備性評測。高分代表該知識題答對較多；卡上把它們放在風險討論裡，不是本榜的能力名次。

### 其他

- $OneMillion-Bench (expert score)：長任務或專家評分。高分較好。
- AA-Omniscience Accuracy Factual accuracy、AA-Omniscience Non-Hallucination Non-hallucination rate：AA-Omniscience：事實是否答對，以及不亂答的比例。Accuracy 與 Non-Hallucination 是兩列。高分較好。
- Artificial Analysis Intelligence Index v4.1.1：這是模型卡自己引用的 Artificial Analysis 指數。Ling-VL 這格是 v4.1.1 的 42，不是本榜快照 v4.3.2 的 25。
- BIRD Bench、BirdBench：BIRD / BirdBench：自然語言轉 SQL。高分較好。
- BigBench Extra Hard：BigBench / BBEH：多樣任務的推理集合。高分較好。
- CI Memories Coverage：CI Memories：情境隱私。Violation 低分較好；Coverage 高分較好。
- CorpFin v2、Harvey Lab-AA、HealthBench、Legal Research Bench、PLawBench、PRBench-Finance、PRBench-Legal：醫療、法律或金融專業題。高分較好。
- CritPt：CritPt：物理前沿推理。高分較好。
- Data & Infrastructure、Societal Alignment、Truthfulness & Reliability：K2 Think 的 Safety-4 巨觀分數。高分代表該安全面向較好；卡上把 Data & Infrastructure 標成 Critical。
- DeepPlanning、PRDBench、WorkSpaceBench：長程規劃、產品文件或工作區任務。高分較好。
- DeepSearch QA、DeepSearchQA (F1)、Seal-0、WideSearch：網頁瀏覽或搜尋（BrowseComp、WideSearch、DeepSearch）。高分代表找到的答案較準。各卡的上下文協議可能不同。
- EmbSpatialBench、Hypersim、LingoQA、Nuscene、ODInW13、RefSpatialBench、SUNRGBD：空間、駕駛或具身視覺題。高分較好，除非該列另寫低分較好。
- FinCRAFT、FinFIRST、FinSearchComp Verified：金融檢索、研究或代理人任務。這張卡只點名、沒有數字。
- Kimi Code Bench 2.0、MiMo Code Bench、MiMo VisualCoding：廠商自建的程式、資安或視覺題。高分較好。
- LVBench、MLVU、MMVU、MVBench：影片理解。高分較好。有字幕與無字幕是不同設定。
- MAXIFE：指令遵循（IFEval、IFBench、MultiChallenge）。高分代表較常照格式與限制做。
- MLS-Bench-Lite：軟體工程：在真實或仿真的程式庫裡改程式（SWE-bench、DeepSWE、NL2Repo、FrontierSWE 等）。高分代表解掉較多任務。Verified、Pro、Multilingual 是不同題集。
- MedXPertQA MM、MedXpertQA-MM：MedXpertQA：醫學多模態題。高分較好。
- MultiLoKo (LLM-Judge)：MultiLoKo：多語言長知識。高分較好。
- PMC-VQA、SLAKE：醫學圖文問答。高分較好。
- PerceptionBench：視覺問答或感知題。高分較好。
- PostTrainBench：PostTrainBench：後訓練相關任務。高分較好。
- ProfBench：ProfBench：專業任務。高分較好。
- QwenSVGBench、QwenWebBench：廠商自己的網頁、SVG 或代理人題。高分較好。只在該卡的欄位裡比較。
- ResearchRubrics：ResearchRubrics：研究任務的量表。高分較好。
- SEC Bench Pro、SEC-Bench Pro (Pass@1)：SEC Bench：資安修補或利用題。高分較好。
- SaaS-Bench：SaaS 操作任務。高分較好。
- Scale AI Multi-Challenge：多輪挑戰題。高分較好。
- SimpleVQA、VlmsAreBlind：圖文理解、文件、圖表或視覺數學。高分通常較好。OmniDocBench 若寫的是 edit distance，低分較好，那一列的名字裡會標出來。
- TIR-Bench、V*：視覺推理或指向題。卡上若有兩種條件，整格保留，不拆成名次。
- 𝛕3-Banking：τ³ / Tau / TAU2：多輪工具呼叫（航空、零售、銀行、電信等）。高分代表任務完成較多。

## 實測參考

檔案大小與 tok/s 來自下列實測文，不是本榜的 Q4 公式。

- 系列：<https://ithelp.ithome.com.tw/users/20141816/ironman/9217>
- Day 14：<https://ithelp.ithome.com.tw/articles/10405431>
- Day 30：<https://ithelp.ithome.com.tw/articles/10409565>

## 來源

- Artificial Analysis，Intelligence Index v4.3.2（2026-10-03）：<https://artificialanalysis.ai/leaderboards/models>，開源頁 <https://artificialanalysis.ai/models/open-source>，小模型 <https://artificialanalysis.ai/models/open-source/small>，中型 <https://artificialanalysis.ai/models/open-source/medium>
- LMArena Text Arena，頁面日期 2026-10-02：<https://arena.ai/leaderboard/text/>
- RTX 5090、RTX PRO 6000、DGX Spark 的官方記憶體，連結見上文的硬體表
- 兩顆改用實測檔案的模型卡：[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)（Apache-2.0）、[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)（Qwen Community License 1.0）
- 192GB 新增的一列：[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)（MIT）
- 模型卡與圖：[models/](models/Qwen3.8-27B.md)、[charts/index.html](charts/index.html)。卡上的分數是販商自報
