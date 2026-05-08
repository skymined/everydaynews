# IMDIGEST - 2026-05-09

2026-05-09 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-05-09 AI 브리핑입니다. 오늘은 NVIDIA Developer Blog, Microsoft Research Blog, NVIDIA Developer Blog에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

### [NVIDIA Developer Blog발 'Streaming Tokens and Tools: Multi-Turn Agentic Harness Support in NVIDIA Dynamo' 관련 AI 업데이트](https://developer.nvidia.com/blog/streaming-tokens-and-tools-multi-turn-agentic-harness-support-in-nvidia-dynamo)

원문에서 확인된 핵심 내용: An agentic exchange must preserve a structured interaction: assistant turns interleave reasoning with one or more tool calls, and subsequent user turns return the corresponding too. 원문에서 확인된 핵심 내용: Reasoning replay is model- and turn-dependent: some reasoning should be retained, while some should be dropped. 원문에서 확인된 핵심 내용: The inference engine is responsible for supporting this more expressive interaction model and for producing correctly segmented API results. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 NVIDIA Developer Blog입니다.

### [Microsoft Research Blog발 'Building realistic electric transmission grid dataset at scale: a pipeline from open dataset' 관련 AI 업데이트](https://www.microsoft.com/en-us/research/blog/building-realistic-electric-transmission-grid-dataset-at-scale-a-pipeline-from-open-dataset)

원문에서 확인된 핵심 내용: At a glance - We construct geographically grounded, electrically coherent power grid models entirely from publicly available data and release a dataset spanning 48 U.S. 원문에서 확인된 핵심 내용: states and multi-state interconnections. 원문에서 확인된 핵심 내용: The models support AC optimal power flow (AC‑OPF) analysis, enabling physics-based study of congestion, capacity, and demand siting without restricted data. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 Microsoft Research Blog입니다.

### [NVIDIA Developer Blog발 'Improving Bash Generation in Small Language Models with Grammar-Constrained Decoding' 관련 AI 업데이트](https://developer.nvidia.com/blog/improving-bash-generation-in-small-language-models-with-grammar-constrained-decoding)

원문에서 확인된 핵심 내용: Bash is one of the most flexible and powerful interfaces exposed to AI agents. 원문에서 확인된 핵심 내용: In the right system, a model that emits grep , curl , tar , or a shell pipeline is producing an executable action that can read files, mutate a workspace, open network connections,. 원문에서 확인된 핵심 내용: For the NVIDIA AI Red Team, this makes command generation a useful research target. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 NVIDIA Developer Blog입니다.

### [Hugging Face Blog발 'CyberSecQwen-4B: Why Defensive Cyber Needs Small, Specialized, Locally-Runnable Models' 관련 AI 업데이트](https://huggingface.co/blog/lablab-ai-amd-developer-hackathon/cybersecqwen-4b)

원문에서 확인된 핵심 내용: Frontier models are very good at very many things. 원문에서 확인된 핵심 내용: They are also expensive to call, ship every prompt off to someone else's datacenter, and are explicitly trained to refuse the messy edge cases a real defender lives in incident wri. 원문에서 확인된 핵심 내용: Defensive cybersecurity is not a place where any of those tradeoffs are acceptable. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 Hugging Face Blog입니다.

### [Hugging Face Blog발 'EMO: Pretraining mixture of experts for emergent modularity' 관련 AI 업데이트](https://huggingface.co/blog/allenai/emo)

원문에서 확인된 핵심 내용: Today we're releasing EMO, a new mixture-of-experts (MoE) model pretrained end-to-end so that modular structure emerges directly from the data without relying on human-defined prio. 원문에서 확인된 핵심 내용: EMO lets you use a small subset of its experts - just 12.5% of the total - for a given task while keeping near full-model performance, and still works as a strong general-purpose m. 원문에서 확인된 핵심 내용: Large language models are typically trained and deployed as monolithic systems: a single model is initialized, pretrained, fine-tuned, and served as one unified entity. 오늘 AI 흐름에서 제품, 연구, 커뮤니티 반응을 함께 읽을 수 있는 참고 신호입니다. 출처는 Hugging Face Blog입니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [Reddit r/artificial발 'Compiled every national AI strategy in Asia — Vietnam has the most comprehensive standalone law, Japan has no penalties, Korea just eliminated Naver from sovereign LLM competition for using Qwen weights' 관련 AI 업데이트](https://www.reddit.com/r/artificial/comments/1t7h9gt/compiled_every_national_ai_strategy_in_asia)

원문에서 확인된 핵심 내용: Compiled a tracker of every national AI strategy in Asia. 원문에서 확인된 핵심 내용: Headline is that ten major Asian economies now have dedicated AI legislation or comprehensive national strategies, and they're all quite distinct from Western legislation like the. 원문에서 확인된 핵심 내용: Clear that Asian governments treat AI as infrastructure, not a sector to regulate from a distance. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 Reddit r/artificial입니다.

### [Reddit r/artificial발 'AI tooling is starting to feel like PC modding culture' 관련 AI 업데이트](https://www.reddit.com/r/artificial/comments/1t7gfud/ai_tooling_is_starting_to_feel_like_pc_modding)

원문에서 확인된 핵심 내용: I think local AI setups are about to split into two completely different communities. 원문에서 확인된 핵심 내용: One side cares about actual production workflows: agents automation APIs inference efficiency data quality reproducibility The other side mostly treats it like PC modding: model co. 원문에서 확인된 핵심 내용: I just think it explains why AI discussions online feel so weird lately. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 Reddit r/artificial입니다.

### [Reddit r/MachineLearning발 'Interactive KL Divergence Visualisation [P]' 관련 AI 업데이트](https://www.reddit.com/r/MachineLearning/comments/1t7lmu4/interactive_kl_divergence_visualisation_p)

원문에서 확인된 핵심 내용: I built a small interactive explorer for building intuition about KL divergence: https://robotchinwag.com/posts/kl-divergence-visualisation/ You control two skew-normal distributio. 원문에서 확인된 핵심 내용: It’s good for exploring how it changes with a mean offset, skew, truncation and discretisation. 원문에서 확인된 핵심 내용: It run entirely close side. 오늘 AI 흐름에서 제품, 연구, 커뮤니티 반응을 함께 읽을 수 있는 참고 신호입니다. 출처는 Reddit r/MachineLearning입니다.

### [Google News AI Search발 'Embodied AI: China’s ambitious path to transform its robotics industry - Mercator Institute for China Studies (MERICS)' 관련 AI 업데이트](https://news.google.com/rss/articles/CBMimgFBVV95cUxQV3k0WTE5WXhMYTF4SmVTQV9xbXR4SGo1c0w4WkEyV2FiMDJnQTFpNENGYWtUT0pqV09EYWFVU09fbnQ0S0x6WHlaMWtnSkZFdFpxQ1BzOExCSHp4SUZJOFJDLVNIa1MxRk45d2kzUnEtUVJKUlZ5dW1zbGlDR1pZMjdIVEtGamYxNUNSNUE0REplZGVUelBmUjJ3?oc=5)

원문에서 확인된 핵심 내용: Embodied AI: China’s ambitious path to transform its robotics industry &nbsp;&nbsp; Mercator Institute for China Studies (MERICS). 오늘 AI 흐름에서 제품, 연구, 커뮤니티 반응을 함께 읽을 수 있는 참고 신호입니다. 출처는 Google News AI Search입니다.

### [Reddit r/artificial발 'I like ChatGPT, I like AI' 관련 AI 업데이트](https://www.reddit.com/r/artificial/comments/1t7kzq1/i_like_chatgpt_i_like_ai)

원문에서 확인된 핵심 내용: &#32; submitted by &#32; /u/TheOnlyVibemaster [link] &#32; [comments]. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 Reddit r/artificial입니다.

### [Reddit r/MachineLearning발 'Formalizing statistical learning theory in Lean 4 [R]' 관련 AI 업데이트](https://www.reddit.com/r/MachineLearning/comments/1t7bgve/formalizing_statistical_learning_theory_in_lean_4)

원문에서 확인된 핵심 내용: I’ve been working on a Lean 4 project focused on formalizing parts of statistical learning theory: FormalSLT repository Current results include: finite-class ERM bounds Rademacher. 원문에서 확인된 핵심 내용: I’m trying to keep: explicit assumptions scoped theorem statements zero sorry close alignment with standard SLT presentations Compared to some existing Lean SLT efforts that focus. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 Reddit r/MachineLearning입니다.

### [Google News AI Search발 'OpenAI adds AI pets to its Codex coding tool - Mashable' 관련 AI 업데이트](https://news.google.com/rss/articles/CBMiggFBVV95cUxPNjkyaU5iZHNPekpUVXVsOXRuNmdpekhhbU1zVWhXQThMQXhzbWxscE9xdnA1WGJ1OXRPN2RKdUxVdGlOMVVDNDN1MXBReEhmaDFkVDdkeEJRNS13LV9nTFpCWmg4eVNzQkFjaXpWWHg1WHVDem56V3VoN2JuVjROa2lB?oc=5)

원문에서 확인된 핵심 내용: OpenAI adds AI pets to its Codex coding tool &nbsp;&nbsp; Mashable. 오늘 AI 흐름에서 제품, 연구, 커뮤니티 반응을 함께 읽을 수 있는 참고 신호입니다. 출처는 Google News AI Search입니다.

### [Google News AI Search발 'Wall Street sees 'changing of the guard in AI' as Intel, AMD shares soar while Nvidia lags - CNBC' 관련 AI 업데이트](https://news.google.com/rss/articles/CBMipgFBVV95cUxNNFBsdk9WTUhFWTBZTElxNHRLQnBWYll6MWI0OFZ3cWZ3dFVSNkV6MFZIYW5zZGRPaFNwYmJfNmRiNl9hVFdDc2N5aC1FX0FWZV80d3ZKZDVlT3dpWkFseUJDalBySU1iWl90emo4N1pDVE1QYVRybVlyanNZbGdvdndmZ0NGLWh4UHRNSWxpeFdybzB5X0lZbzg5WWx3emJhMUZubTRB0gGrAUFVX3lxTE9mczV3bkZjVHJQNWN3RWtjQ3JrSHgwZjdad3hHRHVFSWFhWE80a005YlVTUVdkZVAzWDlVQUFTTFlKZVhTSXNtcnEtMHZWM1BUalNxUkZnXzdpSXFxR1hNdUg5MU16Ni1oMU9Ia3N2WTU2SkJzckVSMUZzUWV0WEpCX0NPTm9wWmVNYW8xUnZYMjVmeDVKbE9NQjRCNXkwNlBvaWZpLWZ6ZXNmTQ?oc=5)

원문에서 확인된 핵심 내용: Wall Street sees 'changing of the guard in AI' as Intel, AMD shares soar while Nvidia lags &nbsp;&nbsp; CNBC. 오늘 AI 흐름에서 제품, 연구, 커뮤니티 반응을 함께 읽을 수 있는 참고 신호입니다. 출처는 Google News AI Search입니다.

### [Google News AI Search발 'The University of Michigan may have landed the steal of the AI era - Business Insider' 관련 AI 업데이트](https://news.google.com/rss/articles/CBMijwFBVV95cUxPMkZMNFg4dHFSY3drZUdYODZDRlIzMjNnaTdaQXNLbWNCM3dNVzhzUzlxTWl6alpsSmxtZ0NBb3g3WUlGbHg1RG5yRDVsQWxaNWtiMnpLdl9jV3ZsWmNUbEUxQ1l1Y29STW9TcmVvRFE4N0VxYk9rY2NMVXYyYldDdEczREJtQmpGS3p0Znl4OA?oc=5)

원문에서 확인된 핵심 내용: The University of Michigan may have landed the steal of the AI era &nbsp;&nbsp; Business Insider. 오늘 AI 흐름에서 제품, 연구, 커뮤니티 반응을 함께 읽을 수 있는 참고 신호입니다. 출처는 Google News AI Search입니다.

### [Google News AI Search발 'Anthropic signs $1.8 billion AI cloud deal with Akamai, Bloomberg News reports - Reuters' 관련 AI 업데이트](https://news.google.com/rss/articles/CBMivAFBVV95cUxPRWh0a2p2a3dybEdNaXVMdEtRaU5TYVlYY0FlNFUwN20xNGtXVTdQbVlYVHRjby1aamRNWWxzVGJEUTdaUHNrcjI2RXdLS1NWbHZIdVVnVWpQMW9fcFVGQUh0T1d0MnVoVUlKNlJOdGRmMEN6UzdfSG14VGlkU0lsNHdZamZJVWJWM1U4TWNFMWdQeDBhdDJiTWRCTm94WnpkcEI3U0lUNEI4M0hwcklJR0lSZzhkU1N5TnFtYQ?oc=5)

원문에서 확인된 핵심 내용: Anthropic signs $1.8 billion AI cloud deal with Akamai, Bloomberg News reports &nbsp;&nbsp; Reuters. 오늘 AI 흐름에서 제품, 연구, 커뮤니티 반응을 함께 읽을 수 있는 참고 신호입니다. 출처는 Google News AI Search입니다.

### [Google News AI Search발 'Talking AI and digital humanities with librarian Mary Ton - Smile Politely' 관련 AI 업데이트](https://news.google.com/rss/articles/CBMinAFBVV95cUxOX21BZlFGTlZXOUFfRjc5MElFSzJNVUxFR3ZYSUVPU3RnakRCN2RQX1M2R2VmWkhWa2hTX183WXJsaFo0OFNQalVNX3duWVNyc0dScGJ1VE9JaTN6V2NEQVVVR2NHcGpwMk02dU9iVnF1bktTQ2dnQ2JrNFFXWmxWTi1aNV90V0lWbTRRdzhEcUszS2dyU1hlZXlyRzU?oc=5)

원문에서 확인된 핵심 내용: Talking AI and digital humanities with librarian Mary Ton &nbsp;&nbsp; Smile Politely. 오늘 AI 흐름에서 제품, 연구, 커뮤니티 반응을 함께 읽을 수 있는 참고 신호입니다. 출처는 Google News AI Search입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning](https://huggingface.co/papers/2605.06130)

이 논문은 에이전트 영역에서 새 시스템 또는 프레임워크을 제안하거나 검증하려는 연구입니다. 문제의식은 에이전트 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 시스템 또는 프레임워크을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning Abstract Skill1 is a unified framework that trains a single policy to simultaneously evolve skill sel 추가로 눈에 띄는 주장: A persistent skill library allows language model agents to reuse successful strategies across tasks. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 2. [Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction](https://huggingface.co/papers/2605.05242)

이 논문은 에이전트 영역에서 새 데이터셋 또는 데이터 생성 방식을 제안하거나 검증하려는 연구입니다. 문제의식은 에이전트 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 데이터셋 또는 데이터 생성 방식을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction Abstract Direct corpus interaction enables more effective agentic search by allowi 추가로 눈에 띄는 주장: Modern retrieval systems, whether lexical or semantic, expose a corpus through a fixed similarity interface that compresses access into a single top-k retrieval step before reasoni. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 3. [Continuous Latent Diffusion Language Model](https://huggingface.co/papers/2605.06548)

이 논문은 생성 모델 영역에서 새 모델 또는 방법론을 제안하거나 검증하려는 연구입니다. 문제의식은 생성 모델 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 모델 또는 방법론을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: Continuous Latent Diffusion Language Model Abstract Cola DLM presents a hierarchical latent diffusion language model that uses text-to-latent mapping, global semantic prior modelin 추가로 눈에 띄는 주장: Large language models have achieved remarkable success under the autoregressive paradigm, yet high-quality text generation need not be tied to a fixed left-to-right order. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 4. [MiA-Signature: Approximating Global Activation for Long-Context Understanding](https://huggingface.co/papers/2605.06416)

이 논문은 검색 결합형 모델 영역에서 새 시스템 또는 프레임워크을 제안하거나 검증하려는 연구입니다. 문제의식은 검색 결합형 모델 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 시스템 또는 프레임워크을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: MiA-Signature: Approximating Global Activation for Long-Context Understanding Abstract Researchers propose a compressed representation method for global activation patterns in larg 추가로 눈에 띄는 주장: A growing body of work in cognitive science suggests that reportable conscious access is associated with global ignition over distributed memory systems, while such activation is o. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 5. [RaguTeam at SemEval-2026 Task 8: Meno and Friends in a Judge-Orchestrated LLM Ensemble for Faithful Multi-Turn Response Generation](https://huggingface.co/papers/2605.04523)

이 논문은 검색 결합형 모델 영역에서 새 시스템 또는 프레임워크을 제안하거나 검증하려는 연구입니다. 문제의식은 검색 결합형 모델 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 시스템 또는 프레임워크을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: RaguTeam at SemEval-2026 Task 8: Meno and Friends in a Judge-Orchestrated LLM Ensemble for Faithful Multi-Turn Response Generation Abstract A heterogeneous ensemble of seven large 추가로 눈에 띄는 주장: We present our winning system for Task~B (generation with reference passages) in SemEval-2026 Task~8: MTRAGEval. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 6. [MARBLE: Multi-Aspect Reward Balance for Diffusion RL](https://huggingface.co/papers/2605.06507)

이 논문은 생성 모델 영역에서 새 벤치마크 또는 평가 방법을 제안하거나 검증하려는 연구입니다. 문제의식은 생성 모델 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 벤치마크 또는 평가 방법을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: MARBLE: Multi-Aspect Reward Balance for Diffusion RL Abstract A novel gradient-space optimization framework called MARBLE addresses limitations in multi-reward reinforcement learni 추가로 눈에 띄는 주장: Reinforcement learning fine-tuning has become the dominant approach for aligning diffusion models with human preferences. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 7. [When to Trust Imagination: Adaptive Action Execution for World Action Models](https://huggingface.co/papers/2605.06222)

이 논문은 로보틱스 영역에서 새 모델 또는 방법론을 제안하거나 검증하려는 연구입니다. 문제의식은 로보틱스 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 모델 또는 방법론을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: When to Trust Imagination: Adaptive Action Execution for World Action Models Abstract World Action Models (WAMs) have recently emerged as a promising paradigm for robotic manipulat 추가로 눈에 띄는 주장: However, current WAMs typically execute a fixed number of predicted actions after each model inference, leaving the robot blind to whether the imagined future remains consistent wi. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 8. [Continuous-Time Distribution Matching for Few-Step Diffusion Distillation](https://huggingface.co/papers/2605.06376)

이 논문은 생성 모델 영역에서 새 모델 또는 방법론을 제안하거나 검증하려는 연구입니다. 문제의식은 생성 모델 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 모델 또는 방법론을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: Continuous-Time Distribution Matching for Few-Step Diffusion Distillation Abstract Continuous-Time Distribution Matching migrates diffusion model distillation from discrete to cont 추가로 눈에 띄는 주장: Step distillation has become a leading technique for accelerating diffusion models, among which Distribution Matching Distillation (DMD) and Consistency Distillation are two repres. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 9. [SkillOS: Learning Skill Curation for Self-Evolving Agents](https://huggingface.co/papers/2605.06614)

이 논문은 에이전트 영역에서 새 시스템 또는 프레임워크을 제안하거나 검증하려는 연구입니다. 문제의식은 에이전트 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 시스템 또는 프레임워크을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: SkillOS: Learning Skill Curation for Self-Evolving Agents Abstract SkillOS enables self-evolving LLM agents to learn complex long-term skill curation policies through reinforcement 추가로 눈에 띄는 주장: LLM-based agents are increasingly deployed to handle streaming tasks, yet they often remain one-off problem solvers that fail to learn from past interactions. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 10. [Nonsense Helps: Prompt Space Perturbation Broadens Reasoning Exploration](https://huggingface.co/papers/2605.05566)

이 논문은 AI 연구 영역에서 새 모델 또는 방법론을 제안하거나 검증하려는 연구입니다. 문제의식은 AI 연구 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다. 핵심 접근은 새 모델 또는 방법론을 통해 기존 한계를 줄이려는 것입니다. 원문 초록 기준 핵심 설명: Nonsense Helps: Prompt Space Perturbation Broadens Reasoning Exploration Abstract LoPE addresses the zero-advantage problem in reinforcement learning with verifiable rewards by usi 추가로 눈에 띄는 주장: Reinforcement learning with verifiable rewards, particularly Group Relative Policy Optimization (GRPO), has significantly advanced the reasoning capabilities of Large Language Mode. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.
