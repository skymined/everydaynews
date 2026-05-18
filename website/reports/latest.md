# IMDIGEST - 2026-05-19

2026-05-19 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-05-19 AI 브리핑입니다. 오늘은 AWS Machine Learning Blog, Hugging Face Blog, TechCrunch AI에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

### [AWS Machine Learning Blog발 'Prompting Amazon Nova 2 for content moderation' 관련 AI 업데이트](https://aws.amazon.com/blogs/machine-learning/prompting-amazon-nova-2-for-content-moderation)

원문에서 확인된 핵심 내용: Prompting Amazon Nova 2 for content moderation If you moderate user-generated content at scale, you need a system that catches policy violations accurately without over-flagging le. 원문에서 확인된 핵심 내용: A moderation system that misses harmful content puts you at risk, while one that flags too aggressively frustrates your audience. 원문에서 확인된 핵심 내용: Every organization defines its own policies, so a single classifier rarely works for every use case. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 AWS Machine Learning Blog입니다.

### [Hugging Face Blog발 'Fine-Tuning NVIDIA Cosmos Predict 2.5 with LoRA/DoRA for Robot Video Generation' 관련 AI 업데이트](https://huggingface.co/blog/nvidia/cosmos-fine-tuning-for-robot-video-generation)

원문에서 확인된 핵심 내용: NVIDIA Cosmos Predict 2.5 is a large-scale world model capable of generating physically plausible videos conditioned on text, images, or video clips. 원문에서 확인된 핵심 내용: To adapt it to a specific domain, such as robot manipulation or a particular camera viewpoint, teams still need targeted fine-tuning. 원문에서 확인된 핵심 내용: Training robot policies requires demonstration data, but collecting real-robot trajectories is slow and expensive. 오늘 AI 흐름에서 제품, 연구, 커뮤니티 반응을 함께 읽을 수 있는 참고 신호입니다. 출처는 Hugging Face Blog입니다.

### [TechCrunch AI발 'SandboxAQ brings its drug discovery models to Claude — no PhD in computing required' 관련 AI 업데이트](https://techcrunch.com/2026/05/18/sandboxaq-brings-its-drug-discovery-models-to-claude-no-phd-in-computing-required)

원문에서 확인된 핵심 내용: Drug discovery is one of the most expensive failures in modern industry. 원문에서 확인된 핵심 내용: Finding a single viable molecule can take a decade and cost billions, and most candidates still don’t make it. 원문에서 확인된 핵심 내용: A generation of AI startups has promised to fix that — most have made the problem less painful for researchers, who are already technically sophisticated enough to use the tools. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 TechCrunch AI입니다.

### [AWS Machine Learning Blog발 'Build custom code-based evaluators in Amazon Bedrock AgentCore' 관련 AI 업데이트](https://aws.amazon.com/blogs/machine-learning/build-custom-code-based-evaluators-in-amazon-bedrock-agentcore)

원문에서 확인된 핵심 내용: Build custom code-based evaluators in Amazon Bedrock AgentCore Special thanks to everyone who contributed to this launch: Stephanie Yuan, Lefan Zhang, Ritvika Pillai, Irene Wang, C. 원문에서 확인된 핵심 내용: Moving prototype agents to production requires measuring quality across multiple dimensions. 원문에서 확인된 핵심 내용: Amazon Bedrock AgentCore Evaluations provides large language model (LLM)-as-a-Judge checks and extensible code-based evaluators that capture domain-specific requirements you need f. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 AWS Machine Learning Blog입니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [Google News AI Search발 'Replace your OpenAI subscription with lifetime access to Gemini, Claude, and even GPT for $80 - Mashable' 관련 AI 업데이트](https://news.google.com/rss/articles/CBMikAFBVV95cUxOcGxHZXE4aGdQLUE0Nk1fRGRONy1DSGVhNGVXN05pVlhqUWI2RkVZbnMwRTZxTkFlTEh3bmd4cloxUTN6VFVYRjBYbEhSRURWNl95TGdDU2hWZVZEOFk0am9MTmQ5cndPOFFkUGlmT25fbkNGaGYyMEc5MXFzdXQwTlRYMlNFWGMtd3ZtODllN1M?oc=5)

원문에서 확인된 핵심 내용: Replace your OpenAI subscription with lifetime access to Gemini, Claude, and even GPT for $80 &nbsp;&nbsp; Mashable. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 Google News AI Search입니다.

### [Reddit r/MachineLearning발 'Rewriting model inference with CUDA kernels: the bottleneck was not just GEMM [P]' 관련 AI 업데이트](https://www.reddit.com/r/MachineLearning/comments/1tgyx41/rewriting_model_inference_with_cuda_kernels_the)

원문에서 확인된 핵심 내용: I’ve been working on a CUDA-first inference runtime for small-batch / realtime ML workloads. 원문에서 확인된 핵심 내용: The core idea is simple: instead of treating PyTorch / TensorRT / generic graph runtimes as the main execution path, I rewrite the model inference path directly with C++/CUDA kerne. 원문에서 확인된 핵심 내용: This started from robotics / VLA workloads, but the problem is more general. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 Reddit r/MachineLearning입니다.

### [Reddit r/artificial발 'Cloudflare just published what they found after running Anthropic's Mythos Preview against 50+ of their own repos and the results are worth reading' 관련 AI 업데이트](https://www.reddit.com/r/artificial/comments/1tgy0j4/cloudflare_just_published_what_they_found_after)

원문에서 확인된 핵심 내용: If you missed the Project Glasswing announcement last month: Anthropic built a security-focused model that autonomously found thousands of high-severity vulnerabilities across ever. 원문에서 확인된 핵심 내용: Instead they gave access to ~40 organizations to use it defensively . 원문에서 확인된 핵심 내용: Cloudflare just posted their honest breakdown of the experience. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 Reddit r/artificial입니다.

### [Google News AI Search발 'Who’s Winning Enterprise AI Now: Claude Up 128%, Gemini Up 48%, OpenAI Down 8%, Grok Still A Rounding Error - SaaStr' 관련 AI 업데이트](https://news.google.com/rss/articles/CBMiwAFBVV95cUxOZU9JVFJRUkppVVhJMWdIZ050ZTFCWnVsTXNnY1BWY2ZZZWNrSzVhWEZ6c1NLS25Rd2gyYTdoVllPRGhSWnRrY0JvekNmdUprSTNIdThmZGJzWF9hTmVoTjJzckhxVjhQR1BsV1dYcnQ0ZXpvRk85UXJMM2hmSEl0bUFLQm82Y0U2Z3BQOV9kUWJGaGlSSm5xeGM4dEkteVY3VXk3YTljaDBia0UxQUJIQ0RUSUo4TnFWeV9MMms0ckY?oc=5)

원문에서 확인된 핵심 내용: Who’s Winning Enterprise AI Now: Claude Up 128%, Gemini Up 48%, OpenAI Down 8%, Grok Still A Rounding Error &nbsp;&nbsp; SaaStr. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 Google News AI Search입니다.

### [Reddit r/MachineLearning발 'Witchcraft, fast local semantic search on top of SQLite [P]' 관련 AI 업데이트](https://www.reddit.com/r/MachineLearning/comments/1tgqyo8/witchcraft_fast_local_semantic_search_on_top_of)

원문에서 확인된 핵심 내용: Witchcraft ( https://github.com/dropbox/witchcraft ) , an open source project that I built at Dropbox, is a from-scratch re-implementation of Stanford's XTR-Warp semantic search en. 원문에서 확인된 핵심 내용: It runs completely stand-alone on your device, needs no API keys, no vector database, no chunking strategy, no fancy re-rankers, and it is lightning fast (20ms p.95 end-to-end sear. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 Reddit r/MachineLearning입니다.

### [Reddit r/MachineLearning발 'Is the future of coding agents JEPA? [D]' 관련 AI 업데이트](https://www.reddit.com/r/MachineLearning/comments/1tgq9v2/is_the_future_of_coding_agents_jepa_d)

원문에서 확인된 핵심 내용: I heard Yann LeCun explain JEPA (Joint Embedding Predictive Architecture) recently and I started thinking about using it for coding agents. 원문에서 확인된 핵심 내용: Most coding agents today work by throwing a huge amount of text into a frontier LLM and asking it to generate the next patch. 원문에서 확인된 핵심 내용: That is astonishingly useful, but it also feels architecturally wrong. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 Reddit r/MachineLearning입니다.

### [Reddit r/LocalLLaMA발 '21 GPU's benchmarked running a small TTS model (vram peak: 5GB)' 관련 AI 업데이트](https://www.reddit.com/r/LocalLLaMA/comments/1th2f5w/21_gpus_benchmarked_running_a_small_tts_model)

원문에서 확인된 핵심 내용: I rented different GPUs on vast.ai for a few minutes each to benchmark a small TTS model, OmniVoice, with a peak VRAM usage of about 5 GB. 원문에서 확인된 핵심 내용: I wanted to see how various mostly consumer GPUs would stack up against my own RTX 3090. 원문에서 확인된 핵심 내용: This is by no means an extensive or scientific analysis, but I think it gives a rough estimate of how these GPUs perform relative to each other. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 Reddit r/LocalLLaMA입니다.

### [Reddit r/LocalLLaMA발 'Is the llama.cpp nixos flake just broken?' 관련 AI 업데이트](https://www.reddit.com/r/LocalLLaMA/comments/1th0yim/is_the_llamacpp_nixos_flake_just_broken)

원문에서 확인된 핵심 내용: I can't seem to build any of the latest releases. 원문에서 확인된 핵심 내용: I'm not sure if something has changed and I haven't kept up, but only way to get a working build is to pin to like a 3 week old commit. 원문에서 확인된 핵심 내용: Quick browser of the issues on github do turn up a couple of build failures, but they're not confirmed and don't seem to get any attention so I'm not sure if it's just an isolated. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 Reddit r/LocalLLaMA입니다.

### [Reddit r/artificial발 'Microsoft Copilot Cowork is Now Available - AI Moving From Chat to Real Work Execution' 관련 AI 업데이트](https://www.reddit.com/r/artificial/comments/1tgwudn/microsoft_copilot_cowork_is_now_available_ai)

원문에서 확인된 핵심 내용: Microsoft has officially introduced Copilot Cowork, and this feels like a major step forward in the AI workspace evolution. 원문에서 확인된 핵심 내용: Instead of just answering prompts like a chatbot, Copilot Cowork is designed to actually help users complete work. 원문에서 확인된 핵심 내용: Microsoft is positioning it as an AI coworker that can understand workflows, execute tasks, coordinate processes, conduct research, generate documents, and work across enterprise t. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 Reddit r/artificial입니다.

### [Google News AI Search발 'Jury Rejects Musk’s Claims Against OpenAI - WSJ' 관련 AI 업데이트](https://news.google.com/rss/articles/CBMioAFBVV95cUxPZVJhUWNncmpfRUdxeGJhRlZsLVlKVFlURVljZndIdHlIb2llMmgyM2xRTTdWV1BaTFMwWWkzYWUxMXpjakJCeUtqbkJlbkZuSEF0TzJtdU0zd2E5Tm9EcU9ReHk0QXJaUmVQOEdRQURTX3JkMVpfNUxLYUNnT0VVQlNtZ0U5bWRGR0VKYlJfSWFPRVRPM0VsV1l1ZXJtc0df?oc=5)

원문에서 확인된 핵심 내용: Jury Rejects Musk’s Claims Against OpenAI &nbsp;&nbsp; WSJ. 오늘 AI 흐름에서 제품, 연구, 커뮤니티 반응을 함께 읽을 수 있는 참고 신호입니다. 출처는 Google News AI Search입니다.

### [Google News AI Search발 'OpenAI defeats Elon Musk's lawsuit, removes obstacle to IPO - Reuters' 관련 AI 업데이트](https://news.google.com/rss/articles/CBMilgFBVV95cUxPZUxNM3REVGdHdjAzd3g4WEtOb3gxTmdsRGxIZXJ0bUFZZGdKLXAxVUZEQUhCTFFWbUhsdnFKdy1Hd3N2YncxcERpcEloNUZEbkdOZldab3lGRVdLMENiZTJwUlZ4MWZoV1BRTUJpcTJ5V3p6SVlYVC1pdU9CbFoyZG1Vd1JqZ183eElQMDVlYzNaYzk0VXc?oc=5)

원문에서 확인된 핵심 내용: OpenAI defeats Elon Musk's lawsuit, removes obstacle to IPO &nbsp;&nbsp; Reuters. 오늘 AI 흐름에서 제품, 연구, 커뮤니티 반응을 함께 읽을 수 있는 참고 신호입니다. 출처는 Google News AI Search입니다.

### [Google News AI Search발 'Elon Musk loses US lawsuit against OpenAI - Al Jazeera' 관련 AI 업데이트](https://news.google.com/rss/articles/CBMihgFBVV95cUxOb0RzTHY5RGEwX0d3dFJhMHBueGpPNk1TTWFvVTNkRjdaVng1d1Qyb0RzTTJSYmlRbmpjOXFtMzFFTVJ6bjk5dlRhaGlwd1gyaTQyQURsVGZ2OThod0JjRndJUFhrZ2VmM3VvUHNBZXhtM09GWlh4ME9qNUJqbkNoSFp0UUp3UdIBiwFBVV95cUxQVjduZEFDdHR1NVFYZ25aZlZPQ1gxVng3TlJQZndwQWt0T2QtZ3M4REV1R0JhZ0h4eXVnMTlodnJEdU1jYk1wMmxjbnZidi0xMlJudGsyUk9lUktMTWh3amRKR1pYVEstQUpPWmItWGN0Z19iLWFSTVlvTmlkdWYxRVh2d2dzNGhLdG9Z?oc=5)

원문에서 확인된 핵심 내용: Elon Musk loses US lawsuit against OpenAI &nbsp;&nbsp; Al Jazeera. 오늘 AI 흐름에서 제품, 연구, 커뮤니티 반응을 함께 읽을 수 있는 참고 신호입니다. 출처는 Google News AI Search입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [CiteVQA: Benchmarking Evidence Attribution for Trustworthy Document Intelligence](https://huggingface.co/papers/2605.12882)

이 논문은 멀티모달 영역에서 새 벤치마크 또는 평가 방법을 제안하거나 검증하려는 연구입니다. 문제의식은 멀티모달 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 벤치마크 또는 평가 방법을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: CiteVQA: Benchmarking Evidence Attribution for Trustworthy Document Intelligence Abstract CiteVQA introduces a benchmark for document vision-language models that evaluates both ans 추가로 눈에 띄는 주장: Multimodal Large Language Models (MLLMs) have significantly advanced document understanding, yet current Doc-VQA evaluations score only the final answer and leave the supporting ev. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 2. [PhysBrain 1.0 Technical Report](https://huggingface.co/papers/2605.15298)

이 논문은 로보틱스 영역에서 새 모델 또는 방법론을 제안하거나 검증하려는 연구입니다. 문제의식은 로보틱스 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 모델 또는 방법론을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: PhysBrain 1.0 Technical Report Abstract PhysBrain 1.0 leverages human egocentric video to generate physical commonsense supervision for vision-language-action models, achieving sta 추가로 눈에 띄는 주장: Vision-language-action models have advanced rapidly, but robot trajectories alone provide limited coverage for learning broad physical understanding. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 3. [MMSkills: Towards Multimodal Skills for General Visual Agents](https://huggingface.co/papers/2605.13527)

이 논문은 에이전트 영역에서 새 시스템 또는 프레임워크을 제안하거나 검증하려는 연구입니다. 문제의식은 에이전트 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 시스템 또는 프레임워크을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: MMSkills: Towards Multimodal Skills for General Visual Agents Abstract Multimodal procedural knowledge frameworks enable visual agents to leverage external reusable skills through 추가로 눈에 띄는 주장: Reusable skills have become a core substrate for improving agent capabilities, yet most existing skill packages encode reusable behavior primarily as textual prompts, executable co. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 4. [FashionChameleon: Towards Real-Time and Interactive Human-Garment Video Customization](https://huggingface.co/papers/2605.15824)

이 논문은 생성 모델 영역에서 새 시스템 또는 프레임워크을 제안하거나 검증하려는 연구입니다. 문제의식은 생성 모델 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 시스템 또는 프레임워크을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: FashionChameleon: Towards Real-Time and Interactive Human-Garment Video Customization Abstract FashionChameleon enables real-time interactive multi-garment video customization thro 추가로 눈에 띄는 주장: Human-centric video customization, particularly at the garment level, has shown significant commercial value. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 5. [Learning to Foresee: Unveiling the Unlocking Efficiency of On-Policy Distillation](https://huggingface.co/papers/2605.11739)

이 논문은 AI 연구 영역에서 새 모델 또는 방법론을 제안하거나 검증하려는 연구입니다. 문제의식은 AI 연구 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 모델 또는 방법론을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: Learning to Foresee: Unveiling the Unlocking Efficiency of On-Policy Distillation Abstract On-policy distillation efficiency arises from early establishment of stable update trajec 추가로 눈에 띄는 주장: On-policy distillation (OPD) has emerged as an efficient post-training paradigm for large language models. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 6. [DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo](https://huggingface.co/papers/2605.16257)

이 논문은 로보틱스 영역에서 새 벤치마크 또는 평가 방법을 제안하거나 검증하려는 연구입니다. 문제의식은 로보틱스 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 벤치마크 또는 평가 방법을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo Abstract DexJoCo presents a benchmark and toolkit for dexterous manipulation with 11 functional 추가로 눈에 띄는 주장: Achieving human-level manipulation requires dexterous robotic hands capable of complex object interactions. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 7. [Distilling Long-CoT Reasoning through Collaborative Step-wise Multi-Teacher Decoding](https://huggingface.co/papers/2605.02290)

이 논문은 AI 연구 영역에서 새 시스템 또는 프레임워크을 제안하거나 검증하려는 연구입니다. 문제의식은 AI 연구 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 시스템 또는 프레임워크을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: Distilling Long-CoT Reasoning through Collaborative Step-wise Multi-Teacher Decoding Abstract CoRD is a collaborative multi-teacher decoding framework that synthesizes reasoning tr 추가로 눈에 띄는 주장: Distilling large reasoning models is essential for making Long-CoT reasoning practical, as full-scale inference remains computationally prohibitive. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 8. [InsightTok: Improving Text and Face Fidelity in Discrete Tokenization for Autoregressive Image Generation](https://huggingface.co/papers/2605.14333)

이 논문은 AI 연구 영역에서 새 연구 접근을 제안하거나 검증하려는 연구입니다. 문제의식은 AI 연구 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 연구 접근을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: InsightTok: Improving Text and Face Fidelity in Discrete Tokenization for Autoregressive Image Generation Abstract InsightTok improves discrete visual tokenization for better text 추가로 눈에 띄는 주장: Text and faces are among the most perceptually salient and practically important patterns in visual generation, yet they remain challenging for autoregressive generators built on d. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 9. [Flash-GRPO: Efficient Alignment for Video Diffusion via One-Step Policy Optimization](https://huggingface.co/papers/2605.15980)

이 논문은 생성 모델 영역에서 새 시스템 또는 프레임워크을 제안하거나 검증하려는 연구입니다. 문제의식은 생성 모델 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 시스템 또는 프레임워크을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: Flash-GRPO: Efficient Alignment for Video Diffusion via One-Step Policy Optimization Abstract Flash-GRPO improves training efficiency for video diffusion models by addressing tempo 추가로 눈에 띄는 주장: Group Relative Policy Optimization has emerged as essential for aligning video diffusion models with human preferences, but faces a critical computational bottleneck: training a 14. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 10. [Nudging Beyond the Comfort Zone: Efficient Strategy-Guided Exploration for RLVR](https://huggingface.co/papers/2605.15726)

이 논문은 AI 연구 영역에서 새 시스템 또는 프레임워크을 제안하거나 검증하려는 연구입니다. 문제의식은 AI 연구 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 시스템 또는 프레임워크을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: Nudging Beyond the Comfort Zone: Efficient Strategy-Guided Exploration for RLVR Abstract NudgeRL framework enhances reinforcement learning with verifiable rewards through structure 추가로 눈에 띄는 주장: Reinforcement learning with verifiable rewards (RLVR) has emerged as a scalable paradigm for improving the reasoning capabilities of large language models. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.
