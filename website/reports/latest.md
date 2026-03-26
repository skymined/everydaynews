# IMDIGEST - 2026-03-27

2026-03-27 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-03-27 AI 브리핑입니다. 오늘은 Microsoft Research Blog, Google DeepMind Blog, Microsoft Research Blog에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

### [Microsoft Research, 시각 정보를 기반으로 계획을 수정하는 Embodied AI 에이전트 평가 벤치마크 AsgardBench 공개](https://www.microsoft.com/en-us/research/blog/asgardbench-a-benchmark-for-visually-grounded-interactive-planning)

Microsoft Research는 Embodied AI 에이전트가 시각적 피드백을 기반으로 계획을 수립하고 업데이트하는 능력을 평가하는 벤치마크 AsgardBench를 발표했습니다. AsgardBench는 에이전트가 시각적 관찰을 사용하여 작업이 전개됨에 따라 계획을 수정할 수 있는지 여부를 중점적으로 측정합니다. 12가지 작업 유형에 걸쳐 108개의 제어된 작업 인스턴스를 포함하며, 에이전트가 관찰한 내용을 기반으로 계획을 조정해야 합니다. 기존 Embodied AI 벤치마크들이 지각, 탐색, 물리적 제어를 동시에 테스트하여 AI 에이전트의 의사결정 능력을 정확히 평가하기 어려웠던 한계를 극복합니다. 출처는 Microsoft Research Blog입니다.

### [Google DeepMind, Gemini 3.1 Flash Live 출시로 오디오 AI의 자연스러움과 신뢰성 향상](https://deepmind.google/blog/gemini-3-1-flash-live-making-audio-ai-more-natural-and-reliable)

Google DeepMind가 실시간 대화 기능을 강화한 Gemini 3.1 Flash Live를 공개했습니다. Gemini 3.1 Flash Live는 개발자, 기업, 일반 사용자에게 더욱 직관적인 음성 중심 AI 경험을 제공합니다. ComplexFuncBench Audio 벤치마크에서 90.8%, Scale AI의 Audio MultiChallenge에서 36.1%의 점수로 이전 모델 대비 성능이 향상되었습니다. 이번 출시는 음성 중심 AI 기술이 더욱 발전하여 실제 대화와 유사한 자연스러움과 복잡한 작업 처리 능력을 갖추게 됨을 보여줍니다. 출처는 Google DeepMind Blog입니다.

### [Microsoft Research, 로봇 조작을 위한 공간 기반 장기 Task Planning 벤치마크 GroundedPlanBench 공개](https://www.microsoft.com/en-us/research/blog/groundedplanbench-spatially-grounded-long-horizon-task-planning-for-robot-manipulation)

Microsoft Research는 로봇이 복잡한 작업을 수행할 때 '무엇을 할지'와 '어디서 할지'를 동시에 결정하는 능력을 평가하는 GroundedPlanBench를 개발했습니다. (영문 용어: long-horizon). 기존 VLM 기반 로봇 플래너는 자연어 계획의 모호성 때문에 장기적이고 복잡한 작업에서 어려움을 겪었습니다. GroundedPlanBench는 VLM이 다양한 실제 로봇 시나리오에서 행동을 계획하고 발생 위치를 결정할 수 있는지 평가합니다. 이 벤치마크는 로봇이 실제 환경에서 더욱 정확하고 효율적으로 복잡한 작업을 수행할 수 있도록 VLM의 계획 및 공간 추론 능력을 향상시키는 데 기여할 것입니다. 출처는 Microsoft Research Blog입니다.

### [TechCrunch AI발 'OpenAI abandons yet another side quest: ChatGPT’s erotic mode' 관련 AI 업데이트](https://techcrunch.com/2026/03/26/openai-abandons-yet-another-side-quest-chatgpts-erotic-mode)

원문에서 확인된 핵심 내용: OpenAI has put the kibosh on yet another project — at least for the time being. 원문에서 확인된 핵심 내용: On Thursday, the Financial Times reported that the AI company would be “indefinitely” pausing plans to develop an “erotic” mode for ChatGPT. 원문에서 확인된 핵심 내용: The proposed “adult mode,” which CEO Sam Altman first floated in October, had inspired considerable controversy from tech watchdog groups as well as from OpenAI’s own staff. 새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다. 출처는 TechCrunch AI입니다.

### [AWS, Amazon Bedrock Guardrails를 활용하여 사용자 연령 및 상황에 맞는 AI 응답을 제공하는 솔루션을 발표했습니다.](https://aws.amazon.com/blogs/machine-learning/building-age-responsive-context-aware-ai-with-amazon-bedrock-guardrails)

AWS는 Amazon Bedrock Guardrails를 사용하여 사용자 연령, 역할, 도메인 지식에 따라 AI 응답을 맞춤화하는 서버리스 솔루션을 구현했습니다. (영문 용어: age-responsive, context-aware). 이 솔루션은 동적 Guardrail 선택, Amazon Bedrock Guardrails를 통한 중앙 집중식 정책 시행, 그리고 모니터링 및 감사 기능을 제공합니다. 기존의 Prompt Engineering이나 애플리케이션 레벨 로직의 한계(우회 가능성, 복잡성)를 극복하고 안전하고 적절한 AI 상호작용을 목표로 합니다. 생성형 AI 애플리케이션이 다양한 사용자 그룹에 배포됨에 따라, 각 AI 응답이 특정 사용자에게 적절하고 안전한지 확인하는 것이 중요해지고 있습니다. 출처는 AWS Machine Learning Blog입니다.

### [위키피디아, AI 생성 텍스트의 문서 작성 사용을 금지하며 편집 정책 강화](https://techcrunch.com/2026/03/26/wikipedia-cracks-down-on-the-use-of-ai-in-article-writing)

위키피디아는 최근 정책 변경을 통해 LLM(Large Language Models)을 사용하여 문서 콘텐츠를 생성하거나 재작성하는 것을 금지했습니다. 이전에는 LLM이 새로운 위키피디아 문서를 처음부터 생성하는 데 사용되어서는 안 된다는 모호한 지침이 있었으나, 이번 업데이트로 더 명확해졌습니다. 새로운 정책은 편집자가 자신의 글에 대한 기본적인 copyedit을 제안하고 인간 검토 후 일부를 통합하는 데 LLM을 사용하는 것은 허용합니다. AI가 편집 및 미디어 분야에 진출함에 따라, 신뢰성과 정확성을 중시하는 플랫폼들이 AI 사용에 대한 명확한 가이드라인을 수립하려는 움직임이 확산되고 있습니다. 출처는 TechCrunch AI입니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [Mac Studio M3 Ultra와 듀얼 DGX Spark에서 Qwen3.5 397B 모델을 로컬로 구동한 결과가 비교 분석되었습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1s4lmep/dual_dgx_sparks_vs_mac_studio_m3_ultra_512gb)

Mac Studio M3 Ultra 512GB는 MLX 6-bit quantization을 사용하여 323GB 모델을 512GB 통합 메모리에 로드, 30-40 tok/s의 토큰 생성 속도를 보였습니다. 듀얼 DGX Spark는 INT4 AutoRound quantization을 사용하여 각 128GB 노드에 98GB 모델을 로드, vLLM TP=2를 통해 27-28 tok/s의 토큰 생성 속도를 기록했습니다. Mac Studio는 800 GB/s의 높은 메모리 대역폭으로 대규모 모델의 부드러운 토큰 생성을 지원하지만, Prefill 속도가 느리고 배치 임베딩에 약점을 보였습니다. 개인용 AI 어시스턴트 운영 비용 절감을 위해 고가의 클라우드 API 대신 로컬 LLM 구축을 시도하는 사용자들이 늘고 있으며, 이는 온프레미스 AI 솔루션에 대한 수요 증가를 반영합니다. 출처는 Reddit r/LocalLLaMA입니다.

### [Mac Mini M4 (16GB)에서 GGUF 모델 벤치마크 결과, MoE 모델이 Dense 모델보다 압도적인 성능을 보임](https://www.reddit.com/r/LocalLLaMA/comments/1s4l4x4/update_on_general_reasoning_for_local_16gb_m4)

Mac Mini M4 (16GB)에서 331개의 GGUF 모델을 벤치마크하여 로컬 모델 선택에 대한 가이드라인을 제시했습니다. (영문 용어: Qwen3.5). 331개 모델 중 31개는 16GB 환경에서 사용 불가능하며, 27B+ Dense 모델은 모두 메모리 스레싱으로 성능이 저하됩니다. 모델 가중치와 KV 캐시가 약 14GB를 초과하면 성능이 급격히 저하됩니다. 로컬 환경에서 제한된 메모리를 가진 디바이스 (예: 16GB Mac M4)에서 LLM을 효율적으로 운영하기 위한 최적의 모델 아키텍처를 제시하여, 개인 사용자 및 개발자에게 실질적인 모델 선택 기준을 제공합니다. 출처는 Reddit r/LocalLLaMA입니다.

### [Google이 Gemini 3.1 Flash Live를 통해 실시간 대화형 AI 에이전트 구축을 지원합니다.](https://news.google.com/rss/articles/CBMioAFBVV95cUxOVlhwLXdDX1R5YmkyZjVmY0t0X2IwbTQ5YVNhazdvWmNCV2ZXbTRIZU5pa3h6WTQ4eDljOGJodkh1RjQ4dWFIUnczajZ6UDdEdUpEcTRBZ2tYUjg1eVdCbm0yNDcwU1F2aFJ0bGplRTR4SVp6RXR1UkIwaExicjFXTmlMTWRIbS1ZTkE0SnVWalQtcWd3YUp2MkxYTlV1SVRO?oc=5)

Google은 개발자들이 Gemini 3.1 Flash Live를 활용하여 실시간 대화형 에이전트를 구축할 수 있도록 지원합니다. (영문 용어: real-time, blog.google). Gemini 3.1 Flash Live는 낮은 지연 시간과 높은 처리량을 제공하여 실시간 상호작용에 최적화되어 있습니다. 이 기술은 고객 서비스, 교육, 엔터테인먼트 등 다양한 분야에서 활용될 수 있습니다. 실시간 상호작용은 사용자 경험을 크게 향상시키며, AI 에이전트의 활용 범위를 넓히는 핵심 요소입니다. 출처는 Google News AI Search입니다.

### [로컬 LLM 에이전트 평가 시 최종 결과물만으로는 에이전트의 내부 비효율성을 간과할 수 있습니다.](https://www.reddit.com/r/MachineLearning/comments/1s4i6h5/d_why_evaluating_only_final_outputs_is_misleading)

Ollama와 LangChain을 활용한 로컬 에이전트 개발 중, 최종 결과는 정확하더라도 에이전트가 내부적으로 비효율적인 작업을 수행하는 문제점이 발견되었습니다. 에이전트가 잘못된 도구를 호출하거나, 불필요한 도구를 사용하거나, 루프에 빠지는 등 비효율적인 프로세스를 거쳐도 최종 결과가 올바르면 평가에서 통과될 수 있습니다. 이는 에이전트의 효율성, 위험성, 추론 과정 등을 평가하기 위해서는 최종 결과뿐만 아니라 에이전트의 실행 과정(trace)을 분석하는 것이 중요함을 시사합니다. LLM 에이전트의 활용이 증가함에 따라, 단순히 최종 결과의 정확성을 넘어 에이전트의 내부 작동 효율성과 안정성을 평가하는 방법론의 중요성이 부각되고 있습니다. 출처는 Reddit r/MachineLearning입니다.

### [Google Cloud, B200 GPU에서 Qwen 3.5 27B 모델을 초당 100만 토큰으로 서빙하는 데 성공하며 대규모 LLM 추론 성능의 새로운 기준을 제시했습니다.](https://www.reddit.com/r/MachineLearning/comments/1s4hxgu/d_1m_tokenssecond_serving_qwen_35_27b_on_b200)

Google Cloud는 96개의 B200 GPU와 vLLM v0.18.0을 사용하여 Qwen 3.5 27B 모델(dense, FP8)의 총 처리량을 1.1M tok/s까지 끌어올렸습니다. (영문 용어: tokens/second). DP=8 구성이 TP=8보다 처리량을 거의 4배 증가시켰으며, B200 GPU에서는 모델 크기가 작아 Tensor Parallelism의 효과가 미미했습니다. MTP-1(Multi-Tenant Preemption)이 GPU 활용률에 가장 큰 영향을 미쳤으며, Inference Gateway를 통한 KV-cache-aware routing은 ClusterIP round-robin 대비 약 35%의 오버헤드를 발생시켰습니다. 이번 성과는 대규모 언어 모델(LLM)의 추론 비용을 획기적으로 절감하고 실시간 서비스 가능성을 높여, AI 애플리케이션의 상용화 및 확산에 중요한 전환점이 될 것입니다. 출처는 Reddit r/MachineLearning입니다.

### [AI 에이전트의 LLM 디버깅 및 보안 강화를 위한 새로운 관측, 모니터링, 보안 도구가 개발되었습니다.](https://www.reddit.com/r/artificial/comments/1s49zeq/need_some_ai_agents)

새로운 도구는 Hallucinations, Prompt Injection, Bias, Toxicity, PII leak 등 다양한 LLM 관련 문제를 추적합니다. Prompt blocking, 토큰 및 비용 계산을 포함한 trace tree와 같은 기능을 제공합니다. 통합 방식은 Proxy API (2줄 변경)와 SDK (전체 에이전트 추적 및 관측) 두 가지를 지원합니다. AI 에이전트 개발이 활발해지면서 LLM의 예측 불가능한 동작(Hallucinations, Bias 등)과 보안 취약점(Prompt Injection, PII leak)을 해결하기 위한 전문 도구의 필요성이 커지고 있습니다. 출처는 Reddit r/artificial입니다.

### [AI 에이전트의 광범위한 접근 권한에 대한 보안 우려가 제기되고 있습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1s4lhec/are_you_giving_your_ai_agents_full_access_to)

현재 대부분의 AI 에이전트는 사람의 인증 모델을 기반으로 구축되어, 토큰이 부여되면 광범위한 접근 권한을 얻게 됩니다. 이는 AI 에이전트의 개별 행동에 대한 세부적인 제어가 어렵고, 활동 제한 및 감사 가능성이 낮다는 문제를 야기합니다. 초기 API 통합에서 발생했던 실수와 유사하게, AI 에이전트의 기능이 강력해질수록 이러한 보안 위험은 더욱 심각해질 수 있습니다. AI 에이전트의 활용이 증가함에 따라, 이들에게 부여되는 접근 권한의 범위와 그에 따른 보안 취약점에 대한 논의가 중요해지고 있습니다. 출처는 Reddit r/LocalLLaMA입니다.

### [Energy-Based Models(EBMs)가 OOD(Out-of-Distribution) 데이터 처리에서 기존 MLP와 차별점을 보이며 더 나은 성능을 제공합니다.](https://www.reddit.com/r/MachineLearning/comments/1s4gp7d/d_ood_and_spandrels_or_what_you_should_know_about)

Energy-Based Models(EBMs)는 변수 구성에 스칼라 에너지(호환성 척도)를 할당하여 종속성을 포착합니다. EBMs는 주어진 훈련 데이터와 동일한 파라미터 수에도 불구하고 기존 MLP와는 다른 방식으로 수렴합니다. EBMs는 훈련 세트 경계 근처의 OOD 포인트를 분류하는 방식에서 MLP와 가장 큰 차이를 보입니다. EBMs는 OOD 데이터에 대한 더 나은 처리 능력을 통해 모델의 견고성과 신뢰성을 향상시킬 수 있는 잠재력을 보여줍니다. 출처는 Reddit r/MachineLearning입니다.

### [Apple이 iOS 27 업데이트에서 Siri를 경쟁 AI 비서들에게 개방할 계획입니다.](https://news.google.com/rss/articles/CBMixAFBVV95cUxQcENnNEV5S0c0QVlDMGNqdTkwSFdZS24yNk9pc0FPTDNCaWpUcGZPOHlfYWlJaU44TmJtOUFra1NPQ3FqWWRUV3ZxOXFjM2xQR1ZoZUJsamRERU9KbEZldUxQa1NKR29lTmlDSlJRYl9ESnhpcFljT3QtcG51ZklYTlJTU1FROExkdlFvNGJvRDJoYld0NWhLLU5ncml1XzFNa0toOGNLVU9oaTZRdVhSUlpucVRUUk5xMGhKWlpzcjctTENp?oc=5)

Apple은 iOS 27 업데이트를 통해 Siri를 다른 AI 비서들과 통합할 예정입니다. (영문 용어: Bloomberg.com). 이번 개방으로 사용자는 Siri를 호출하여 ChatGPT와 같은 타사 AI 비서를 사용할 수 있게 됩니다. 이는 Apple의 AI 전략 변화를 보여주는 중요한 움직임입니다. Apple이 자사 생태계의 핵심인 Siri를 개방함으로써 AI 시장의 경쟁이 더욱 심화될 것으로 예상됩니다. 출처는 Google News AI Search입니다.

### [Meta가 텍사스 AI 데이터 센터에 대한 투자를 100억 달러 이상으로 6배 이상 확대합니다.](https://news.google.com/rss/articles/CBMipAFBVV95cUxQQzlUNzhaWENtQV9WLW1FTVBXYTVJT1JXWUY2VGdyQTBDak5feTBqdXJYWWlMVE1ubDJZSGpzVno3dEZ0TVpkYkNzS2F2Z0NMd2Q1V2h0UURmRjRueXhZOUdZSHRrV2tENWRDNlJyWnpMaUpjQTdXVlIxbHpVcEJWc2RfZnh6UkJsOU02ajV6QVpTZkpIUTJVTWdOYzNGaFp2NVJnZdIBqgFBVV95cUxPQ3dkTE9xS3oySy1mOW02T0swWDlieDRsRkgxVGk5RG1JSzNnUXJrTU9IQS1GNVdLeGhxallaN3dya1Q3ZF9rbG9QWDBqeHB0TG5LYkt6MVd5WHo1YktqcnNac2FKdzRZOWNYNHEyNGlNdVdXTEszVmZnWU1VRnlBZzBHN1ZQXzNtdFhBOWdiTWh2UTBONmJaQndNWlBIQ1dQaXdiN0dNZmc0Zw?oc=5)

Meta는 텍사스주 템플에 위치한 AI 데이터 센터에 대한 투자액을 기존 15억 달러에서 100억 달러 이상으로 대폭 증액했습니다. 이 데이터 센터는 Meta의 AI 모델 훈련 및 서비스 운영에 필수적인 인프라를 제공할 예정입니다. 이번 투자는 텍사스 지역에 상당한 경제적 파급 효과를 가져올 것으로 예상됩니다. Meta의 이번 대규모 투자는 AI 기술 개발 및 인프라 구축 경쟁이 심화되고 있음을 보여줍니다. 출처는 Google News AI Search입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents](https://huggingface.co/papers/2603.24440)

CUA-Suite는 컴퓨터 사용 에이전트(CUA)의 데스크톱 자동화 발전을 위해 대규모의 인간 주석 비디오 시연 데이터셋을 제공합니다. (영문 용어: Human-annotated, Computer-Use). 컴퓨터 사용 에이전트(CUA)는 복잡한 데스크톱 워크플로우를 자동화할 잠재력이 크지만, 고품질의 연속적인 인간 시연 비디오 부족으로 발전이 지연되고 있습니다. 기존 데이터셋은 스크린샷 위주로 구성되어 연속적인 상호작용 정보를 담지 못했습니다. CUA-Suite는 약 10,000개의 작업과 87개 애플리케이션에 걸쳐 55시간 분량의 연속 30fps 화면 녹화, 커서 추적, 다층 추론 주석을 포함하는 VideoCUA를 핵심으로 제공합니다. 이 데이터셋은 에이전트 프레임워크에 필요한 모든 정보를 손실 없이 변환할 수 있는 풍부한 정보를 제공하며, UI-Vision 벤치마크와 GroundCUA 데이터셋도 함께 제공하여 CUA의 grounding 및 planning 능력을 평가하고 개선하는 데 기여합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 2. [EVA: Efficient Reinforcement Learning for End-to-End Video Agent](https://huggingface.co/papers/2603.22918)

EVA는 반복적인 계획 및 주의 메커니즘을 통해 적응형 추론을 가능하게 하는 효율적인 End-to-End Video Agent를 위한 강화 학습 프레임워크입니다. 기존 MLLM 기반 비디오 이해 방식은 긴 비디오 토큰 시퀀스와 중복 프레임으로 인해 비효율적이며, 수동으로 설계된 워크플로우에 의존했습니다. EVA는 iterative summary-plan-action-reflection 추론을 통해 '계획-이후-인지(planning-before-perception)'를 가능하게 하여, 에이전트가 무엇을, 언제, 어떻게 볼지 자율적으로 결정합니다. 이러한 에이전트 훈련을 위해 SFT, KTO, GRPO로 구성된 3단계 학습 파이프라인을 설계했으며, 이를 통해 지도 모방 학습과 강화 학습을 연결합니다. EVA는 6가지 비디오 이해 벤치마크에서 기존 MLLM 대비 6-12%, 기존 적응형 에이전트 대비 1-3%의 성능 향상을 달성했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 3. [UI-Voyager: A Self-Evolving GUI Agent Learning via Failed Experience](https://huggingface.co/papers/2603.24533)

UI-Voyager는 Rejection Fine-Tuning과 Group Relative Self-Distillation을 통해 실패 경험으로부터 학습하여 GUI 자동화 작업의 효율성과 성능을 향상시키는 자가 진화 모바일 GUI 에이전트입니다. (영문 용어: Self-Evolving). 기존 모바일 GUI 에이전트는 실패한 궤적으로부터의 비효율적인 학습과 긴 GUI 작업에서 희소한 보상에 따른 모호한 신용 할당 문제를 겪습니다. UI-Voyager는 이러한 문제를 해결하기 위해 두 단계의 자가 진화 방식을 제안합니다. 첫 번째 단계에서는 Rejection Fine-Tuning을 사용하여 데이터와 모델이 완전히 자율적인 루프에서 지속적으로 공동 진화하도록 합니다. 두 번째 단계에서는 Group Relative Self-Distillation을 도입하여 그룹 롤아웃에서 중요한 분기점을 식별하고 성공적인 궤적에서 밀집된 단계별 감독을 구성하여 실패한 궤적을 수정합니다. AndroidWorld 벤치마크에서 81.0%의 Pass@1 성공률을 달성하며 인간 수준의 성능을 뛰어넘었습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 4. [T-MAP: Red-Teaming LLM Agents with Trajectory-aware Evolutionary Search](https://huggingface.co/papers/2603.22341)

T-MAP은 Trajectory-aware Evolutionary Search를 통해 LLM 에이전트의 안전 장치를 우회하고 유해한 결과를 초래하는 적대적 프롬프트를 발견합니다. (영문 용어: Red-Teaming). 기존의 레드팀 노력은 LLM의 유해한 텍스트 출력에 초점을 맞췄지만, T-MAP은 다단계 도구 실행을 통해 발생하는 에이전트별 취약점을 포착합니다. 이 방법은 실행 궤적(execution trajectories)을 활용하여 적대적 프롬프트 발견을 안내하며, 안전 가드레일을 우회하고 실제 도구 상호작용을 통해 유해한 목표를 달성하는 공격을 자동으로 생성합니다. T-MAP은 다양한 MCP 환경에서 Attack Realization Rate (ARR) 측면에서 기준선보다 훨씬 뛰어난 성능을 보이며 GPT-5.2, Gemini-3-Pro와 같은 최신 모델에도 효과적임을 입증했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 5. [Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?](https://huggingface.co/papers/2603.24472)

Self-distillation이 LLM의 수학적 추론 능력을 저하시키는 원인이 모델의 불확실성 표현 억제에 있음을 밝히고, 특히 OOD(Out-of-Distribution) 작업에서 성능 저하가 심화됨을 Qwen3-8B, DeepSeek-Distill-Qwen-7B, Olmo3-7B-Instruct 모델을 통해 분석했습니다. 이 연구는 LLM의 Self-distillation이 수학적 추론 성능을 저하시킬 수 있는 문제를 다룹니다. 저자들은 이러한 성능 저하의 원인이 모델이 추론 과정에서 불확실성을 표현하는 'epistemic verbalization'을 억제하기 때문임을 밝혀냈습니다. 특히, 풍부한 정보로 Teacher 모델을 조건화하면 불확실성 표현이 억제되어 In-domain 최적화에는 유리하지만, 불확실성 표현이 중요한 OOD(Out-of-Distribution) 작업에서는 성능이 최대 40%까지 저하됨을 확인했습니다. 이는 견고한 추론을 위해 적절한 수준의 불확실성 표현이 필수적임을 시사합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 6. [GameplayQA: A Benchmarking Framework for Decision-Dense POV-Synced Multi-Video Understanding of 3D Virtual Agents](https://huggingface.co/papers/2603.24329)

GameplayQA는 3D 가상 환경에서 멀티모달 LLM의 인식 및 추론 능력을 평가하기 위한 POV-Synced 멀티플레이어 게임플레이 비디오 기반 벤치마킹 프레임워크를 제시합니다. (영문 용어: Decision-Dense, Multi-Video). 기존 벤치마크는 3D 환경에서 자율 에이전트의 빠른 상태 변화 인식, 올바른 엔티티에 대한 행동 귀속, 동시 다중 에이전트 행동 추론 능력을 충분히 평가하지 못했습니다. GameplayQA는 이러한 문제를 해결하기 위해 멀티플레이어 3D 게임플레이 비디오에 초당 1.22개의 레이블로 상태, 행동, 이벤트를 조밀하게 주석 처리하고, Self, Other Agents, World의 삼원 시스템으로 구성된 2.4K 진단 QA 쌍을 제공합니다. 이 프레임워크는 모델이 환각을 일으키는 부분을 세분화하여 분석할 수 있는 방해 요소 분류 체계를 포함합니다. 최신 MLLM 평가 결과, 인간 성능과의 상당한 격차가 드러났으며, 특히 시간적 및 교차 비디오 접지, 에이전트 역할 귀속, 게임의 의사결정 밀도 처리에서 공통적인 실패가 관찰되었습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 7. [When Models Judge Themselves: Unsupervised Self-Evolution for Multimodal Reasoning](https://huggingface.co/papers/2603.21289)

Unsupervised Self-Evolution 프레임워크는 레이블링된 데이터 없이도 멀티모달 추론 모델의 성능을 향상시키기 위해 self-consistency 신호와 Group Relative Policy Optimization(GRPO)을 활용합니다. 멀티모달 대규모 언어 모델은 추론 작업에서 좋은 성능을 보이지만, 고품질의 주석 데이터나 teacher 모델 증류에 크게 의존하여 확장성이 제한됩니다. 이 연구는 이러한 문제를 해결하기 위해 사람의 주석이나 외부 보상 모델 없이 안정적인 성능 향상을 달성하는 비지도 학습 기반의 self-evolution 프레임워크를 제안합니다. 이 프레임워크는 여러 추론 궤적을 샘플링하고, Actor의 self-consistency 신호를 훈련 사전으로 사용하며, bounded Judge 기반 변조를 통해 궤적의 품질을 지속적으로 재조정합니다. 또한, Group Relative Policy Optimization(GRPO)을 사용하여 레이블링되지 않은 데이터로 훈련함으로써 수학적 추론 벤치마크에서 일관된 성능 향상과 일반화를 보여줍니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 8. [Understanding the Challenges in Iterative Generative Optimization with LLMs](https://huggingface.co/papers/2603.23994)

LLM 기반 반복 생성 최적화(Iterative Generative Optimization)의 성공에 결정적인 영향을 미치는 숨겨진 설계 선택 사항들을 분석하고 실용적인 가이드를 제공합니다. LLM을 활용한 반복 생성 최적화는 코드, 워크플로우, 프롬프트와 같은 아티팩트를 실행 피드백을 통해 개선하는 유망한 접근 방식이지만, 실제 적용에서는 취약성을 보입니다. 이 연구는 이러한 취약성이 아티팩트 수정 방법과 학습 증거 제공 방식에 대한 '숨겨진' 설계 결정에서 비롯된다고 주장합니다. MLAgentBench, Atari, BigBench Extra Hard 케이스 스터디를 통해 시작 아티팩트, 실행 추적의 신용 범위, 시행착오 배치와 같은 요소들이 최적화 성공 여부를 결정함을 밝히고, 이러한 설계 선택에 대한 실용적인 지침을 제시합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 9. [SpectralSplats: Robust Differentiable Tracking via Spectral Moment Supervision](https://huggingface.co/papers/2603.24036)

SpectralSplats는 3D Gaussian Splatting 기반 트래킹에서 발생하는 vanishing gradient 문제를 해결하기 위해 최적화 목표를 주파수 도메인으로 전환하고 Frequency Annealing 스케줄을 도입합니다. 3D Gaussian Splatting(3DGS)은 실시간 사실적인 novel view synthesis를 가능하게 하여 모델 기반 비디오 트래킹에 유용하지만, 렌더러의 미분 가능성을 활용하는 것이 불안정하다는 문제가 있습니다. 특히, 카메라 정렬이 심하게 어긋나면 가우시안 프리미티브의 국소적 특성 때문에 그래디언트가 소실되어 최적화가 어려워집니다. SpectralSplats는 이 "vanishing gradient" 문제를 해결하기 위해 최적화 목표를 공간 도메인에서 주파수 도메인으로 전환합니다. Spectral Moments라는 전역 복소수 사인파 특징을 통해 렌더링된 이미지를 감독함으로써, 픽셀 오버랩이 전혀 없을 때도 유효한 방향성 그래디언트가 존재하도록 전역적인 attraction basin을 구축합니다. 또한, 높은 주파수와 관련된 주기적인 지역 최소값을 피하면서 전역적 볼록성에서 정밀한 공간 정렬로 최적화가 원활하게 전환되도록 Frequency Annealing 스케줄을 제안합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 10. [The Pulse of Motion: Measuring Physical Frame Rate from Visual Dynamics](https://huggingface.co/papers/2603.14375)

Visual Chronometer는 비디오의 시각적 역학을 통해 실제 물리적 프레임 속도(PhyFPS)를 추정하여 생성형 비디오 모델의 시간적 모호성을 해결합니다. 기존 생성형 비디오 모델은 다양한 실제 속도의 비디오로 훈련되어 시간적 모호성, 즉 '시간 측정 환각(chronometric hallucination)'을 겪으며, 이는 생성된 비디오의 물리적 움직임 속도를 불분명하고 불안정하게 만듭니다. 이 문제를 해결하기 위해, 본 연구는 입력 비디오의 시각적 역학으로부터 직접 PhyFPS를 복구하는 예측기인 Visual Chronometer를 제안합니다. 제어된 시간적 리샘플링을 통해 훈련된 이 방법은 움직임 자체에 내포된 실제 시간 스케일을 추정하며, PhyFPS-Bench-Real 및 PhyFPS-Bench-Gen 벤치마크를 통해 최신 비디오 생성기가 심각한 PhyFPS 불일치와 시간적 불안정성을 겪고 있음을 보여줍니다. 최종적으로 PhyFPS 보정을 적용하면 AI 생성 비디오의 인간이 인지하는 자연스러움이 크게 향상됨을 입증합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.
