# المِقياس الكامل — 329 مساراً، بدقة 7+8=15

- نجح: **64** | صحيح: **49** | فشل: **265**
- g4f: 272 (33 نجح/24 صحيح) | freellmpool: 40 (16/16) | kilo مباشر: 17 (15/9)

## 1) أسرع 25 صحيحاً

-  0.33s  freellmpool  `spread`
-  0.34s  freellmpool  `llm7/codestral-latest`
-  0.38s  freellmpool  `llm7/default`
-  0.63s  g4f          `LLM7`
-  0.90s  freellmpool  `llm7/fast`
-  0.95s  kilo-direct  `inclusionai/ling-3.0-flash-vl:free`
-  0.95s  freellmpool  `kilo/poolside/laguna-s-2.1:free`
-  0.99s  kilo-direct  `nex-agi/nex-n2.5-mini:free`
-  1.01s  freellmpool  `quality`
-  1.03s  freellmpool  `kilo/inclusionai/ling-3.0-flash-fin:free`
-  1.05s  kilo-direct  `inclusionai/ling-3.0-flash-fin:free`
-  1.18s  g4f          `CohereForAI_C4AI_Command`
-  1.20s  kilo-direct  `nvidia/nemotron-3-ultra-550b-a55b:free`
-  1.25s  freellmpool  `kilo/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
-  1.26s  g4f          `command-r7b`
-  1.27s  g4f          `command-r`
-  1.28s  freellmpool  `agent`
-  1.29s  g4f          `command-r-plus24`
-  1.32s  kilo-direct  `cohere/north-mini-code:free`
-  1.37s  g4f          `command-a`
-  1.47s  g4f          `command-a25`
-  1.49s  g4f          `command-r7b-arabic25`
-  1.50s  g4f          `command-r24`
-  1.56s  kilo-direct  `nex-agi/nex-n2.5-pro:free`
-  1.59s  g4f          `HuggingSpace`

## 2) كل الصحيحة — freellmpool

-  0.33s `spread`
-  0.34s `llm7/codestral-latest`
-  0.38s `llm7/default`
-  0.90s `llm7/fast`
-  0.95s `kilo/poolside/laguna-s-2.1:free`
-  1.01s `quality`
-  1.03s `kilo/inclusionai/ling-3.0-flash-fin:free`
-  1.25s `kilo/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
-  1.28s `agent`
-  1.65s `kilo/cohere/north-mini-code:free`
-  2.12s `fast`
-  3.15s `kilo/nvidia/nemotron-3.5-lightning:free`
-  4.11s `kilo/nvidia/nemotron-3-super-120b-a12b:free`
-  4.70s `auto`
-  5.00s `kilo/nvidia/nemotron-3-ultra-550b-a55b:free`
- 26.32s `fair`

## 3) كل الصحيحة — kilo مباشر

-  0.95s `inclusionai/ling-3.0-flash-vl:free`
-  0.99s `nex-agi/nex-n2.5-mini:free`
-  1.05s `inclusionai/ling-3.0-flash-fin:free`
-  1.20s `nvidia/nemotron-3-ultra-550b-a55b:free`
-  1.32s `cohere/north-mini-code:free`
-  1.56s `nex-agi/nex-n2.5-pro:free`
-  1.64s `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
-  2.86s `nvidia/nemotron-3-super-120b-a12b:free`
-  4.58s `poolside/laguna-s-2.1:free`

## 4) كل الصحيحة — g4f

-  0.63s `LLM7`
-  1.18s `CohereForAI_C4AI_Command`
-  1.26s `command-r7b`
-  1.27s `command-r`
-  1.29s `command-r-plus24`
-  1.37s `command-a`
-  1.47s `command-a25`
-  1.49s `command-r7b-arabic25`
-  1.50s `command-r24`
-  1.59s `HuggingSpace`
-  1.82s `command-r7b24`
-  1.84s `Yqcloud`
-  3.27s `gpt-4`
-  4.20s `BraveSearch`
-  4.42s `Gemini`
-  4.99s `gemini-3.5-flash-thinking`
-  5.07s `gemini-3.5-flash`
-  5.12s `gemini-2.5-flash`
-  5.31s `gemini-3.5-flash-thinking-lite`
-  5.64s `gemini-3.6-flash`
-  5.64s `gemini-auto`
-  5.80s `gemini-3.5-flash-lite`
-  5.92s `gemini-3.1-flash-lite`
-  6.34s `gemini-flash-lite`

## 5) فئات الفشل (265)

- 213  g4f: المزوّد لا يخدم بلا مصادقة
-  21  502/503 مقطعي
-  18  401: يحتاج مصادقة
-   9  timeout
-   2  404: موديل غير موجود
-   2  429: rate limit

## 6) التوصيات

- الأسرع: llm7/codestral (0.34s) و llm7/default (0.38s) و freellmpool spread (0.33s)
- توازن سرعة/قدرة: kilo nvidia/nemotron-3-ultra-550b (1.2s مباشراً) و g4f gpt-4/Yqcloud (3.3s) و g4f gemini-3.5-flash-thinking
- الأغلبية الفاشلة في g4f هي نماذج تتطلب مصادقة حقيقية، لا عطل في مجموعتنا