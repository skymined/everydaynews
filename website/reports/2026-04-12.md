# IMDIGEST - 2026-04-12

2026-04-12 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-04-12 AI 브리핑입니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

오늘은 이 섹션에 담을 공식 발표형 뉴스가 많지 않았습니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [macOS용 스토리지 및 메모리 벤치마크 도구인 AmorphousDiskMark와 AmorphousMemoryMark가 MIT 라이선스로 오픈소스화되었습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1siv4qy/amorphousmemorymark_which_benchmarks_memory)

AmorphousDiskMark와 AmorphousMemoryMark는 macOS에서 스토리지 및 메모리 성능을 측정하는 표준 도구입니다. (영문 용어: open-source). AmorphousDiskMark는 CrystalDiskMark와 유사하게 순차 및 랜덤 읽기/쓰기 속도를 측정합니다. AmorphousMemoryMark는 memmove, rep movsb/stosb 등 다양한 방법을 통해 메모리 처리량을 GB/s 단위로 벤치마킹합니다. 오픈소스화로 인해 이 도구들의 장기적인 보존과 지속적인 개발이 보장됩니다. 출처는 Reddit r/LocalLLaMA입니다.

### [Bain & Company가 Agentic AI 플랫폼의 세 가지 핵심 레이어를 제시하며 AI 시스템 구축의 중요성을 강조합니다.](https://news.google.com/rss/articles/CBMifkFVX3lxTFBucGQzdjd6V0h0R0ZUcUdNU21GN3RESnFrVzF2MldTUW12Tkw4Tkw3RnhXTW9DSndHanEyZnhmTm1hX2JkYklrZi1oVVc3YWlGVDBGMWNBdHZyRVRqX0dXSTVKNmZ1ZUlHYjFnNExIcnlHckFNdlRId1lRaXJzUQ?oc=5)

Bain & Company는 Agentic AI 플랫폼을 구축하기 위한 세 가지 핵심 레이어인 'Foundation Models', 'Agentic Capabilities', 'Enterprise Integration'을 제시했습니다. 'Foundation Models'는 AI 시스템의 기반이 되는 대규모 언어 모델 등을 의미하며, 'Agentic Capabilities'는 AI가 자율적으로 목표를 설정하고 실행하는 능력을 말합니다. 'Enterprise Integration'은 이러한 AI 역량을 기업의 기존 시스템 및 워크플로우에 통합하는 과정을 포함합니다. Agentic AI는 단순한 도구를 넘어 자율적으로 의사결정하고 행동하는 AI 시스템으로 진화하고 있으며, 이는 기업의 운영 방식과 비즈니스 모델에 근본적인 변화를 가져올 잠재력을 가지고 있습니다. 출처는 Google News AI Search입니다.

### [llama.cpp에서 Gemma 4 E4B 모델의 툴 호출 기능이 불안정하다는 사용자 보고가 있었습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1siw1mq/trying_to_use_gemma4_e4b_q4_k_m_using_llamacpp_it)

사용자는 RTX 4050 GPU 환경에서 llama.cpp의 llama-server를 통해 Gemma 4 E4B (Q4_K_M GGUF) 모델을 사용하고 있습니다. 모델은 정상적으로 실행되고 GPU 오프로드도 잘 작동하지만, Continue VS Code extension에서 툴 호출이 제대로 작동하지 않습니다. 툴 호출 시 원시 JSON이나 일반 텍스트를 출력하거나 아예 툴을 사용하지 않는 문제가 발생합니다. 이는 로컬 환경에서 LLM을 활용하는 개발자들이 겪는 실제적인 문제로, llama.cpp와 같은 경량 런타임에서 모델의 고급 기능(툴 호출)을 안정적으로 사용하는 데 어려움이 있음을 보여줍니다. 출처는 Reddit r/LocalLLaMA입니다.

### [AMD의 GAIA, 채팅을 통해 커스텀 AI 에이전트 구축 기능 추가 및 진정한 데스크톱 앱으로 진화](https://www.reddit.com/r/artificial/comments/1sitbvu/amds_gaia_now_allows_building_custom_ai_agents)

AMD의 GAIA가 이제 채팅 인터페이스를 통해 사용자가 직접 AI 에이전트를 구축할 수 있는 기능을 제공합니다. GAIA는 더 이상 웹 기반이 아닌, 진정한 데스크톱 애플리케이션으로 전환되었습니다. 이는 사용자가 AI를 더욱 쉽게 맞춤 설정하고 활용할 수 있도록 하여 AI의 접근성과 개인화를 크게 향상시킬 것입니다. 출처는 Reddit r/artificial입니다.

### [AI 비디오 생성 분야에서 'Live AI video generation' 용어의 기술적 의미와 정의에 대한 논의가 활발합니다.](https://www.reddit.com/r/MachineLearning/comments/1siqg5d/is_live_ai_video_generation_a_meaningful)

'Live AI video generation'은 실시간 입력 스트림에 지속적으로 반응하여 프레임을 생성하거나 변환하는 기술을 의미합니다. 빠른 비디오 생성(fast video generation)과 달리, Live AI video generation은 아키텍처, 지연 시간 제약 등 기술적으로 근본적인 차이가 있습니다. 현재 많은 미디어와 벤더들이 'live' 또는 'real-time'이라는 용어를 혼용하여 사용하고 있어 명확한 정의가 필요하다는 지적이 있습니다. AI 비디오 생성 기술이 발전함에 따라, 실제 실시간 상호작용이 가능한 'Live AI video generation'의 기술적 난이도와 활용 가치에 대한 관심이 증가하고 있습니다. 출처는 Reddit r/MachineLearning입니다.

### [Anthropic, AI 시대 핵심 소프트웨어 보안 강화를 위한 'Project Glasswing' 발표](https://news.google.com/rss/articles/CBMiS0FVX3lxTFBfQUdtMDZYaEtZV0JMSk1ZSzdqTl9mV3dQTnZYcVEzaHo4cV8yUEl2a25QMWRXenFTYUQ3NF9WakR5WXVwaDRTZC1ZYw?oc=5)

Anthropic은 AI 시대에 필수적인 소프트웨어의 보안을 강화하기 위해 'Project Glasswing'을 시작했습니다. 이 프로젝트는 AI 시스템의 기반이 되는 소프트웨어의 취약점을 식별하고 해결하는 데 중점을 둡니다. Anthropic은 AI 모델의 안전성뿐만 아니라 이를 구동하는 인프라의 보안도 중요하게 다루고 있습니다. AI 기술이 발전함에 따라 AI 시스템을 구성하는 소프트웨어의 보안 취약점이 새로운 위협으로 부상하고 있으며, 이에 대한 선제적 대응의 중요성이 커지고 있습니다. 출처는 Google News AI Search입니다.

### [일상적인 사용을 위한 Qwen 3.5 35B, 27B 또는 Gemma 4 31B 모델 선택에 대한 논의가 활발합니다.](https://www.reddit.com/r/LocalLLaMA/comments/1siw62t/qwen_35_35b_27b_or_gemma_4_31b_for_everyday_use)

사용자들은 5080 GPU와 64GB RAM 환경에서 가장 지능적이면서도 원활하게 작동하는 LLM을 찾고 있습니다. 주요 고려 대상 모델은 Qwen 3.5 35B, Qwen 3.5 27B, 그리고 Gemma 4 31B입니다. 사용자들은 각 모델의 성능, 효율성, 그리고 특정 하드웨어 사양에서의 실행 가능성에 대해 의견을 교환하고 있습니다. 개인용 하드웨어에서 고성능 LLM을 구동하려는 수요가 증가하면서, 사용자들은 자신의 시스템에 최적화된 모델을 적극적으로 탐색하고 있습니다. 출처는 Reddit r/LocalLLaMA입니다.

### [LLM 이후 AI 분야의 가장 큰 발전은 'Loco-Manipulation' 기술의 등장입니다.](https://news.google.com/rss/articles/CBMieEFVX3lxTFBOY2N6cGREMU53QVAzbzNtTGFaVFdfQnFuQ1hJV0dGcWVNLVZUZjVQdFJHVWJ6Yl9QSXA4Wkh4SDVpMjlQcldybElVc0duUFhuYUptSk5jTlZkWXdCTEJzUnMwVldDWWVraC1Ra1hkSVZ1OGpxQkc3MQ?oc=5)

Loco-Manipulation은 로봇이 움직이면서 물체를 조작하는 기술을 의미합니다. 이 기술은 로봇이 복잡한 환경에서 다양한 작업을 수행할 수 있도록 합니다. 기존 로봇 기술의 한계를 뛰어넘어, 로봇이 더욱 유연하고 지능적으로 상호작용할 수 있게 합니다. Loco-Manipulation은 로봇이 실제 세계에서 더욱 실용적으로 활용될 수 있는 가능성을 열어줍니다. 출처는 Google News AI Search입니다.

### [Anthropic, 기독교 지도자들과 AI의 윤리적, 존재론적 함의 논의](https://news.google.com/rss/articles/CBMikgFBVV95cUxNei1fZGN3LVZXTnlFNUkyQ2dnY2h1czhMQzFWUnhZaDdUamtnWlRBX2ZjWjQ2WktfdzJGdDNja0RObWRQYklBNlVQVnFsMVJMTFJBNEd0LW13emN5MVNFMEhjekx4N2ZLM0JLQkQzU0dwNWpaclVSbnpUd2dnWDludDg4QXJOcXoyU0JIVi1qTHdaQQ?oc=5)

Anthropic은 워싱턴 D.C.에서 기독교 지도자들과 만나 AI가 인간의 영적, 도덕적 가치와 어떻게 조화를 이룰 수 있는지에 대해 논의했습니다. 이번 회동은 AI 기술 개발에 있어 종교적 관점과 윤리적 고려사항을 통합하려는 Anthropic의 노력을 보여줍니다. 참석자들은 AI가 '신의 자녀'가 될 수 있는지와 같은 심오한 질문들을 탐구하며, AI의 잠재적 영향에 대한 다양한 시각을 교환했습니다. AI 기술이 사회 전반에 미치는 영향이 커지면서, 기술 기업들이 종교 및 윤리 단체들과의 대화를 통해 AI 개발의 윤리적, 철학적 기반을 강화하려는 추세가 나타나고 있습니다. 출처는 Google News AI Search입니다.

### [FlashAttention의 각 버전(FA1-FA4)별 알고리즘 차이를 쉽게 이해할 수 있는 PyTorch 교육용 구현체가 공개되었습니다.](https://www.reddit.com/r/MachineLearning/comments/1sim6y1/flashattention_fa1fa4_in_pytorch_educational)

FlashAttention-PyTorch 레포지토리에 FA1, FA2, FA3, FA4의 교육용 PyTorch 구현이 업데이트되었습니다. 이 구현체는 최적화된 커널이 아닌, 각 버전의 알고리즘 아이디어와 설계 변경 사항을 이해하는 데 중점을 둡니다. FA1은 tiled online softmax baseline, FA2는 split-Q 및 deferred normalization, FA3는 explicit staged pipeline과 FP8 forward path를 특징으로 합니다. FlashAttention의 발전 과정을 CUDA 커널 수준의 복잡성 없이 순수 PyTorch 코드로 이해할 수 있게 하여, 연구자와 개발자들이 핵심 아이디어를 쉽게 파악하도록 돕습니다. 출처는 Reddit r/MachineLearning입니다.

### [AI와 자동화가 심리치료를 어디까지 지원할 수 있을지에 대한 논의가 활발합니다.](https://www.reddit.com/r/artificial/comments/1sinj89/how_far_can_automation_and_ai_support)

Reddit r/artificial 커뮤니티에서 AI와 자동화가 심리치료를 얼마나 지원할 수 있는지에 대한 질문이 제기되었습니다. 이는 AI 기술이 헬스케어, 특히 정신 건강 분야에 미칠 영향에 대한 대중의 관심을 보여줍니다. AI 기술의 발전이 심리치료와 같은 전문적인 인간 중심 서비스 영역으로 확장될 가능성을 탐색하고 있습니다. 출처는 Reddit r/artificial입니다.

### [17세 인도 학생, 적응형 시험 스케줄링 연구 논문으로 arXiv cs.CY 승인 요청](https://www.reddit.com/r/artificial/comments/1simhzr/arxiv_cscy_endorsement_request_for_adaptive)

인도의 17세 학생이 적응형 시험 스케줄링에 대한 연구 논문을 작성하고 arXiv cs.CY 카테고리에 제출했습니다. 이 논문은 학생의 학습 규율을 확률적 변수로 보고, 시험 준비를 계획 문제가 아닌 제어 문제로 접근합니다. 시뮬레이션 결과, 제안된 우선순위 기반 적응형 스케줄링은 정적 스케줄 대비 절반의 학습 시간으로도 고우선순위 토픽 커버율 85.7%를 달성했습니다(정적 스케줄은 42.9%). 기존 학습 플래너의 한계(규율 측정 및 보고에 대한 가정)를 지적하고, 학생 행동을 피드백 루프에 통합하는 새로운 접근 방식을 제시하여 교육 기술 분야에 시사하는 바가 큽니다. 출처는 Reddit r/artificial입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [SkillClaw: Let Skills Evolve Collectively with Agentic Evolver](https://huggingface.co/papers/2604.08377)

SkillClaw는 다중 사용자 LLM 에이전트 시스템에서 사용자 상호작용을 집계하여 재사용 가능한 스킬을 자율적으로 업데이트하고 개선하는 집단 스킬 진화 프레임워크를 제안합니다. 기존 LLM 에이전트 시스템에서 스킬은 배포 후 정적 상태로 유지되어 사용자 간에 유사한 워크플로우와 실패 모드가 반복적으로 발생했습니다. SkillClaw는 이러한 문제를 해결하기 위해 다중 사용자 및 시간 경과에 따른 상호작용을 스킬 개선의 주요 신호로 활용합니다. 이 프레임워크는 사용 중 생성된 궤적을 지속적으로 집계하고, 자율적인 Evolver가 반복적인 행동 패턴을 식별하여 기존 스킬을 개선하거나 새로운 기능을 추가함으로써 스킬 세트를 업데이트합니다. 이를 통해 사용자 간 지식 전달과 누적 역량 개선이 가능하며, WildClawBench 실험에서 Qwen3-Max의 성능을 크게 향상시키는 것을 보여주었습니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 2. [Rethinking Generalization in Reasoning SFT: A Conditional Analysis on Optimization, Data, and Model Capability](https://huggingface.co/papers/2604.06628)

이 연구는 SFT(Supervised Finetuning)가 추론 작업에서 일반화되지 않는다는 통념을 재고하며, 최적화, 데이터, 모델 역량에 따라 조건부적인 교차 도메인 일반화가 가능함을 밝힙니다. 기존에는 SFT가 추론 작업에서 일반화되지 않고 암기만 한다고 여겨졌습니다. 본 연구는 긴 CoT(Chain-of-Thought) 감독을 통한 SFT가 최적화 역학, 훈련 데이터, 기본 모델 역량에 따라 조건부적인 교차 도메인 일반화를 보임을 발견했습니다. 특히, 충분한 훈련 시 성능 저하 후 회복 및 개선되는 'dip-and-recovery' 패턴을 보이며, 검증된 고품질의 긴 CoT 데이터가 일관된 교차 도메인 이득을 제공합니다. 또한, 강력한 모델은 전이 가능한 절차적 패턴을 내재화하지만, 이러한 일반화는 추론 능력 향상과 안전성 저하라는 비대칭적인 결과를 가져옵니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 3. [HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents](https://huggingface.co/papers/2604.07430)

HY-Embodied-0.5는 Mixture-of-Transformers 아키텍처와 반복적인 후속 학습을 통해 실제 환경 에이전트의 시각 인지 및 추론 능력을 향상시킨 Embodied Foundation Model 제품군입니다. (영문 용어: Real-World). 이 연구는 일반 VLM과 Embodied Agent 간의 격차를 해소하기 위해 공간적, 시간적 시각 인지 및 예측, 상호작용, 계획을 위한 Embodied 추론 능력을 강화한 HY-Embodied-0.5 모델을 제안합니다. 모델은 모달리티별 컴퓨팅을 가능하게 하는 Mixture-of-Transformers(MoT) 아키텍처를 채택하여 미세한 시각 인지 능력을 향상시키고, 반복적인 자기 진화 후속 학습 패러다임을 도입하여 추론 능력을 개선합니다. 또한, 대규모 모델의 고급 기능을 소규모 모델로 전이시키는 on-policy distillation을 활용하여 효율적인 엣지 배포 모델과 복잡한 추론 모델 두 가지를 제공합니다. 22개 벤치마크에서 시각 인지, 공간 추론, Embodied 이해도에 걸쳐 광범위한 평가를 통해 접근 방식의 효과를 입증했습니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 4. [When Numbers Speak: Aligning Textual Numerals and Visual Instances in Text-to-Video Diffusion Models](https://huggingface.co/papers/2604.08546)

NUMINA는 텍스트-투-비디오 확산 모델에서 텍스트 프롬프트에 지정된 객체 수를 정확하게 생성하지 못하는 문제를 해결하기 위해 훈련 없이 레이아웃 불일치를 식별하고 어텐션 변조를 통해 재생성을 유도하는 프레임워크입니다. (영문 용어: Text-to-Video). 텍스트-투-비디오 확산 모델은 프롬프트에 명시된 객체 수를 정확하게 생성하는 데 어려움을 겪습니다. NUMINA는 이러한 수치적 불일치를 개선하기 위해 훈련이 필요 없는 '식별-안내' 프레임워크를 제안합니다. 이 프레임워크는 판별적인 self- 및 cross-attention 헤드를 선택하여 계산 가능한 잠재 레이아웃을 도출하고, 이를 보수적으로 개선한 다음 cross-attention을 변조하여 재생성을 안내합니다. CountBench에서 NUMINA는 기존 모델의 카운팅 정확도를 최대 7.4% 향상시키며, CLIP 정렬도 개선하고 시간적 일관성을 유지합니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 5. [ClawBench: Can AI Agents Complete Everyday Online Tasks?](https://huggingface.co/papers/2604.08523)

ClawBench는 AI 에이전트가 복잡한 온라인 작업을 수행할 수 있는지 평가하기 위해 153개의 실제 웹 작업을 포함하는 새로운 벤치마크를 제시합니다. 이 연구는 AI 에이전트가 이메일 자동화를 넘어 일상생활의 다양한 온라인 작업을 처리할 수 있는지 평가하는 문제를 제기합니다. 이를 위해 ClawBench는 구매, 예약, 구직 신청 등 144개 플랫폼에 걸쳐 153개의 실제 다단계 웹 작업을 포함하는 평가 프레임워크를 도입합니다. 이 벤치마크는 기존 벤치마크와 달리 실제 운영 웹사이트에서 동적인 상호작용과 복잡성을 유지하며 에이전트를 평가합니다. 평가 결과, 7개의 최신 모델(예: Claude Sonnet 4.6) 모두 이러한 작업의 극히 일부만 완료할 수 있었으며, 이는 AI 에이전트의 일반적인 보조 기능에 대한 상당한 개선이 필요함을 시사합니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 6. [MegaStyle: Constructing Diverse and Scalable Style Dataset via Consistent Text-to-Image Style Mapping](https://huggingface.co/papers/2604.08364)

MegaStyle은 대규모 생성 모델의 일관된 텍스트-이미지 스타일 매핑 능력을 활용하여 다양하고 확장 가능한 스타일 데이터셋을 구축하고, 이를 통해 효과적인 스타일 표현 추출을 위한 style-supervised contrastive learning을 제안합니다. (영문 용어: Text-to-Image). 기존 스타일 데이터셋의 일관성 부족과 다양성 한계를 해결하기 위해, MegaStyle은 대규모 생성 모델이 특정 스타일 설명에 따라 일관된 이미지를 생성할 수 있다는 점에 착안했습니다. 이 파이프라인은 170K 스타일 프롬프트와 400K 콘텐츠 프롬프트를 조합하여 대규모 스타일 데이터셋인 MegaStyle-1.4M을 구축합니다. 이 데이터셋을 기반으로 style-supervised contrastive learning을 통해 스타일 인코더 MegaStyle-Encoder를 학습시켜 표현력이 풍부한 스타일별 표현을 추출하고, FLUX 기반의 스타일 전이 모델 MegaStyle-FLUX를 훈련합니다. 결과적으로 MegaStyle-1.4M은 스타일 데이터셋의 일관성, 다양성 및 고품질의 중요성을 입증하며, MegaStyle-Encoder와 MegaStyle-FLUX는 신뢰할 수 있는 스타일 유사도 측정 및 일반화 가능한 스타일 전이를 제공합니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 7. [OpenVLThinkerV2: A Generalist Multimodal Reasoning Model for Multi-domain Visual Tasks](https://huggingface.co/papers/2604.08539)

OpenVLThinkerV2는 Gaussian GRPO를 활용하여 다양한 시각 작업에서 안정적인 학습과 지각-추론 균형을 달성하는 범용 멀티모달 추론 모델입니다. (영문 용어: Multi-domain). 멀티모달 모델 학습의 주요 과제인 다양한 시각 작업 보상 토폴로지의 극심한 분산과 지각-추론 균형 문제를 해결하기 위해 Gaussian GRPO(G^2RPO)를 제안합니다. G^2RPO는 선형 스케일링 대신 비선형 분포 매칭을 사용하여 이점 분포를 표준 정규 분포로 수렴시켜 태스크 간 기울기 균등성을 보장하고 학습 안정성을 높입니다. 또한, 응답 길이 조절(response length shaping)과 엔트로피 조절(entropy shaping)을 통해 지각과 추론 능력의 균형을 맞추어 OpenVLThinkerV2의 성능을 향상시킵니다. 이 모델은 이러한 방법론을 통합하여 다양한 시각 작업에서 뛰어난 성능을 보입니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 8. [LPM 1.0: Video-based Character Performance Model](https://huggingface.co/papers/2604.07823)

LPM 1.0은 실시간 대화형 캐릭터 퍼포먼스 생성을 위해 정체성 일관성을 유지하며 상호작용적이고 무한 길이의 비디오 합성을 가능하게 하는 대규모 멀티모달 모델입니다. (영문 용어: Video-based). 기존 비디오 모델들은 높은 표현력, 실시간 추론, 장기적인 정체성 안정성을 동시에 달성하기 어려웠습니다. LPM 1.0은 이러한 '퍼포먼스 트릴레마'를 해결하기 위해 단일 인물 전이중 오디오-비주얼 대화 퍼포먼스에 중점을 둡니다. 엄격한 필터링과 멀티모달 데이터셋 구축을 통해 17B 파라미터 Diffusion Transformer (Base LPM)를 훈련하여 높은 제어력과 정체성 일관성을 가진 퍼포먼스를 생성합니다. 이를 인과적 스트리밍 생성기 (Online LPM)로 증류하여 낮은 지연 시간과 무한 길이의 상호작용을 가능하게 합니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 9. [DMax: Aggressive Parallel Decoding for dLLMs](https://huggingface.co/papers/2604.08302)

DMax는 Diffusion Language Model(dLLM)의 병렬 디코딩 중 오류 축적을 줄이고 생성 품질을 유지하면서 효율성을 높이는 새로운 패러다임을 제시합니다. 기존의 마스크 기반 dLLM은 이진 마스크-토큰 전환을 통해 디코딩했지만, DMax는 마스크 임베딩에서 토큰 임베딩으로의 점진적인 자기 개선으로 디코딩을 재구성합니다. 이 접근 방식의 핵심은 마스크된 입력과 모델의 잘못된 예측 모두에서 깨끗한 토큰을 복구할 수 있도록 모델을 훈련하는 On-Policy Uniform Training이라는 새로운 훈련 전략입니다. 또한, Soft Parallel Decoding을 제안하여 각 중간 디코딩 상태를 예측된 토큰 임베딩과 마스크 임베딩 간의 보간으로 표현함으로써 임베딩 공간에서 반복적인 자기 수정이 가능하게 합니다. 결과적으로 DMax는 GSM8K 및 MBPP 벤치마크에서 정확도를 유지하면서 TPF(Tokens Per Forward)를 크게 향상시키는 효과를 보여주었습니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 10. [KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation](https://huggingface.co/papers/2604.08455)

KnowU-Bench는 사용자 선호도 추론 및 능동적 지원 능력을 평가하는 개인화된 모바일 에이전트 벤치마크를 제시합니다. 기존 벤치마크는 사용자 선호도를 정적인 기록이나 고정된 컨텍스트에서 평가하여, 에이전트가 상호작용을 통해 누락된 선호도를 이끌어내거나 실시간 GUI 환경에서 언제 개입할지 결정하는 능력을 측정하지 못했습니다. KnowU-Bench는 재현 가능한 Android 에뮬레이션 환경에서 구축된 온라인 벤치마크로, 에이전트에게 사용자 프로필을 숨기고 행동 로그만 노출하여 진정한 선호도 추론을 강제합니다. 또한, LLM 기반 사용자 시뮬레이터를 통해 다중 턴 선호도 도출 및 능동적 동의 처리를 지원하며, GUI 실행, 동의 협상, 거부 후 제약 등 능동적 의사결정 체인 전반을 평가합니다. 이 벤치마크는 개인화된 모바일 에이전트의 실제 성능 저하를 드러냅니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.
