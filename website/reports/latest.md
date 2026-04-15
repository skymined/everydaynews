# IMDIGEST - 2026-04-16

2026-04-16 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-04-16 AI 브리핑입니다. 오늘은 Google DeepMind Blog, TechCrunch AI, TechCrunch AI에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

### [Google DeepMind, Gemini 3.1 Flash TTS 출시로 AI 음성 기술 발전 주도](https://deepmind.google/blog/gemini-3-1-flash-tts-the-next-generation-of-expressive-ai-speech)

Google DeepMind가 Gemini 3.1 Flash TTS를 출시하며, 향상된 제어 가능성, 표현력, 그리고 품질을 제공합니다. 이 모델은 Gemini API, Google AI Studio, Vertex AI를 통해 개발자와 기업에 미리보기로 제공되며, Google Vids를 통해 Workspace 사용자도 이용할 수 있습니다. Artificial Analysis TTS 리더보드에서 1,211점의 Elo 점수를 기록하며 높은 음성 품질과 낮은 비용의 이상적인 조합으로 평가받았습니다. 이번 출시는 AI 음성 애플리케이션 개발의 새로운 지평을 열며, 개발자와 기업이 더욱 자연스럽고 표현력 있는 AI 음성을 활용할 수 있도록 지원합니다. 출처는 Google DeepMind Blog입니다.

### [OpenAI가 기업용 Agents SDK를 업데이트하여 더 안전하고 강력한 AI 에이전트 구축을 지원합니다.](https://techcrunch.com/2026/04/15/openai-updates-its-agents-sdk-to-help-enterprises-build-safer-more-capable-agents)

OpenAI가 기업이 자사 모델 기반의 AI 에이전트를 구축할 수 있도록 Agents SDK를 업데이트했습니다. 새로운 SDK는 에이전트가 통제된 환경에서 작동하도록 돕는 샌드박스 기능을 도입하여 예측 불가능한 에이전트의 위험을 줄입니다. 업데이트된 SDK는 또한 개발자들이 Frontier 모델과 함께 작동하는 에이전트를 배포하고 테스트할 수 있도록 in-distribution harness를 제공합니다. 이번 업데이트는 기업들이 AI 에이전트를 안전하고 효율적으로 비즈니스에 통합하려는 수요가 증가함에 따라, 에이전트의 안정성과 제어 가능성을 높이는 데 중점을 둡니다. 출처는 TechCrunch AI입니다.

### [Google이 Mac용 Gemini 네이티브 앱을 출시하여 경쟁사들과의 격차를 줄였습니다.](https://techcrunch.com/2026/04/15/google-rolls-out-a-native-gemini-app-for-mac)

Google이 Mac 사용자를 위한 네이티브 Gemini 앱을 공식 출시했습니다. 사용자들은 Option + Space 단축키를 통해 어떤 앱에서든 Gemini를 즉시 호출하여 도움을 받을 수 있습니다. 이 앱은 화면 공유 기능을 통해 로컬 파일을 포함한 현재 보고 있는 콘텐츠에 대한 질문과 요약 기능을 제공합니다. Google이 OpenAI 및 Anthropic과 같은 경쟁사들의 Mac 앱 출시에 발맞춰 데스크톱 AI 접근성을 강화하고 있습니다. 출처는 TechCrunch AI입니다.

### [인도 스타트업 Emergent, 메시징 기반 AI 에이전트 'Wingman' 출시하며 AI 에이전트 시장 진출](https://techcrunch.com/2026/04/15/indias-vibe-coding-startup-emergent-enters-openclaw-like-ai-agent-space)

인도의 vibe-coding 스타트업 Emergent가 메시징 기반의 자율 AI 에이전트 'Wingman'을 출시했습니다. (영문 용어: OpenClaw-like). Wingman은 WhatsApp 및 Telegram과 같은 메시징 플랫폼을 통해 작동하며, 이메일, 캘린더, 업무용 소프트웨어 등 연결된 도구에서 백그라운드로 작업을 수행합니다. Emergent는 이전에 자연어 프롬프트를 통해 풀스택 애플리케이션을 구축할 수 있는 vibe-coding 플랫폼으로 8백만 명 이상의 빌더와 150만 명의 월간 활성 사용자를 확보했습니다. OpenClaw 및 Anthropic의 Claude와 같은 도구들이 대중화하면서 백그라운드에서 작업을 완료하는 자율 AI 에이전트 소프트웨어 카테고리가 성장하고 있으며, Emergent도 이 경쟁에 합류했습니다. 출처는 TechCrunch AI입니다.

### [AWS Trainium과 vLLM을 활용한 추론 가속화로 LLM 디코딩 비용을 절감합니다.](https://aws.amazon.com/blogs/machine-learning/accelerating-decode-heavy-llm-inference-with-speculative-decoding-on-aws-trainium-and-vllm)

AWS Trainium2와 vLLM을 사용하여 Speculative Decoding을 구현함으로써 디코딩 위주의 LLM 워크로드에서 토큰 생성 속도를 최대 3배까지 가속화합니다. (영문 용어: decode-heavy). Speculative Decoding은 작은 draft model이 여러 토큰을 동시에 제안하고, target model이 이를 한 번의 forward pass로 검증하여 순차적인 디코딩 단계를 줄이는 방식입니다. Qwen3 모델을 vLLM, Kubernetes, AWS AI Chips에 배포하여 inter-token latency를 단축하는 실질적인 벤치마크 결과를 제시합니다. 생성형 AI 애플리케이션의 확산으로 디코딩 단계가 추론 비용의 대부분을 차지하게 되면서, 이를 효율적으로 처리하는 기술의 중요성이 커지고 있습니다. 출처는 AWS Machine Learning Blog입니다.

### [브라질 의료기관 Rede Mater Dei de Saúde, Amazon Bedrock AgentCore를 활용하여 AI 에이전트 기반의 수익 주기 모니터링 시스템을 구축했습니다.](https://aws.amazon.com/blogs/machine-learning/rede-mater-dei-de-saude-monitoring-ai-agents-in-the-revenue-cycle-with-amazon-bedrock-agentcore)

Rede Mater Dei de Saúde는 브라질의 주요 의료기관으로, 12개의 AI 에이전트 스위트를 Amazon Bedrock AgentCore를 사용하여 구현했습니다. 이 시스템은 에이전트 런타임, 도구 통합, 메모리 관리 및 생산 AI 에이전트를 위한 내장된 관찰 기능을 제공합니다. 브라질 의료 부문은 2024년 청구 거부율이 11.89%에서 15.89%로 증가하여 최대 100억 헤알의 미수익이 발생했습니다. 의료 분야에서 AI 에이전트 시스템의 도입이 증가함에 따라, 복잡한 운영 환경에서 AI 에이전트의 모니터링, 추적 및 거버넌스 능력이 운영 지속 가능성에 필수적인 요소가 되고 있습니다. 출처는 AWS Machine Learning Blog입니다.

### [Peter Thiel이 투자한 스타트업 Objection, AI를 활용하여 언론 기사의 진실성을 심사하는 서비스 출시](https://techcrunch.com/2026/04/15/can-ai-judge-journalism-a-thiel-backed-startup-says-yes-even-if-it-risks-chilling-whistleblowers)

Aron D’Souza가 설립한 Objection은 AI를 이용해 언론 보도의 진실 여부를 판정하는 소프트웨어 서비스를 시작했습니다. (영문 용어: Thiel-backed). 누구나 2,000달러를 지불하면 기사에 이의를 제기할 수 있으며, 이는 해당 주장에 대한 공개 조사로 이어집니다. Objection은 Peter Thiel과 Balaji Srinivasan, 그리고 Social Impact Capital 및 Off Piste Capital로부터 수백만 달러의 시드 투자를 유치했습니다. AI가 단순한 콘텐츠 생성 및 분석을 넘어, 언론의 진실성 판단과 같은 복잡하고 논쟁적인 영역으로 확장되고 있음을 보여줍니다. 출처는 TechCrunch AI입니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [Anthropic, 에이전트의 '두뇌'와 '손'을 분리하여 확장성 높은 Managed Agent 시스템 구축](https://news.google.com/rss/articles/CBMiYkFVX3lxTE5LY3VWakFxdE02bVBBdDNrSEJaY2NqV1ZkZ3hfNUxBeWFXZDdrU21vTTdnSFdNUGNPRVpSMWVyVGp6MWlQWTFYU2JIcVZDdDcwMXcwRlpYNExMeWZBMGxXOWJ3?oc=5)

Anthropic은 에이전트의 '두뇌'(추론 및 계획)와 '손'(도구 사용 및 환경 상호작용)을 분리하는 새로운 아키텍처를 제안했습니다. 이 분리된 접근 방식은 에이전트의 각 구성 요소를 독립적으로 확장하고 개선할 수 있게 합니다. 이를 통해 복잡한 작업을 수행하는 에이전트의 안정성과 효율성을 높이는 것을 목표로 합니다. AI 에이전트의 복잡성이 증가함에 따라, 모듈화된 설계는 확장성 및 관리 용이성 측면에서 중요한 트렌드로 부상하고 있습니다. 출처는 Google News AI Search입니다.

### [Anthropic의 AI 챗봇 Claude와 협업 도구 Cowork에 서비스 중단 발생](https://news.google.com/rss/articles/CBMibkFVX3lxTFAzYjd3cFVvOTVTblYtRXRTVTVQMHpzdE5aeTFkU0tiVURDak1LTTdnUGFTSWRTQ2lYNlQyN3MzbWdudmxobEpMdWNYWWxSZlJob1JzZzFkWm9IS1RmTjd1alRCRnY3NjVPYy1WYWFR?oc=5)

Anthropic은 자사의 AI 챗봇 Claude와 협업 플랫폼 Cowork에서 서비스 중단(outage)이 발생했음을 확인했습니다. 사용자들은 Claude에 접속하거나 Cowork 기능을 사용하는 데 어려움을 겪었습니다. AI 서비스의 안정성과 신뢰성은 사용자 경험에 매우 중요하며, 이러한 서비스 중단은 기업의 평판과 직결될 수 있습니다. 출처는 Google News AI Search입니다.

### [Google Gemini 앱이 이제 Mac에서도 사용 가능해지며 AI 접근성을 확장합니다.](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPeXdQVmxFWlVnUWE3WWpZZVZ3UURhZUFMalhyOGF5UGYyeVJEQ09ITlVHblh4d0VINjdLb1FLbVRxaXZOOFhhdWlDZGlmOUxlLVBSNEpBbjJyd0NCRFQwVHh6YU5WVU9zWWF0bGMtREdyZXZMSVZkcUozWGFoZWVnNFU3Rmp4XzhpRmk0?oc=5)

Google의 AI 어시스턴트 Gemini 앱이 Mac 기기에서도 공식적으로 출시되었습니다. (영문 용어: blog.google). 사용자들은 이제 Mac에서 Gemini를 통해 텍스트 생성, 정보 요약, 아이디어 구상 등 다양한 AI 기능을 활용할 수 있습니다. Gemini는 Google Workspace 앱과 연동되어 Gmail, Docs 등에서 AI 기능을 직접 사용할 수 있습니다. Google이 Gemini 앱을 Mac으로 확장함으로써, AI 어시스턴트의 접근성을 높이고 더 많은 사용자가 다양한 기기에서 AI를 활용할 수 있도록 지원합니다. 출처는 Google News AI Search입니다.

### [신발 브랜드 Allbirds, AI 기업으로의 전환 발표](https://news.google.com/rss/articles/CBMihwFBVV95cUxObUR2S1pFMDVnSFQ2WFk4ZFZ6T1BSQk85cGlDMnBEUGlpb0gyWnNId2RNUnF6VkRMSHNJZmEtYlVoeTNwTjJ1SmlFa1FKNVMxVUp1bl9mNU1TaTFaUnpTSFRuNDNwZDlaUjJ4ckF6X3FtUVhlNVNma1VGYkNzQktBc1AyQ0wxMFHSAYwBQVVfeXFMUFBwdllIalJaRzRiYm9QZlhMVWd6bUNYajZZWGx5MnFKTzFmX2NjU2RlNUlnRkFUSmFNRHR2aHdteXR5UlYyUFVRZm9hTEJwYXZRTHN3R0NPQTR5SG9Ub2xrQ0RybG9DR3ZwQXg0MnphbkVxREFfMXhDSFFkczJvNXNLX0pXX0xWM0xhR1Q?oc=5)

Allbirds가 신발 사업을 중단하고 AI 기업으로 전환한다고 발표했습니다. 이러한 변화는 CBS News를 통해 보도되었습니다. 전통적인 소비재 기업이 AI 기술 분야로 사업 모델을 완전히 전환하는 이례적인 사례입니다. 출처는 Google News AI Search입니다.

### [미국 변호사들이 AI 챗봇 사용에 대한 경고를 발표하며, AI와의 대화 내용이 법정에서 불리하게 사용될 수 있다고 강조했습니다.](https://news.google.com/rss/articles/CBMixgFBVV95cUxPR2ZtWkI5VERwRTZkZDVXU3VuVUxiY2N6N3FfYlNpNUZ6OFViQVhvTmwtYVpTb1VjM1NCWWVfM2Q2dkI3YzdZb3NyTkR0VG5TNXNveWlQTGlrYWlqYmEwTWYxVk12TkRQbTlxYTlLaXJZbzU2UkFwVjZsSnlnT1RWVm5MdDU4RW56Rnc1cEZybnR4anQ0dGsyNTdwV0Vpay1TajV4d2RPZ0ZldzdfRmRMdHRoOFgtVVJfVFU2SnNteHdmSFVnZWc?oc=5)

미국 변호사들은 AI 챗봇과의 대화 내용이 법정에서 사용자에게 불리한 증거로 활용될 수 있다고 경고했습니다. 이는 AI가 생성한 정보의 신뢰성과 개인 정보 보호 문제에 대한 우려를 제기합니다. 변호사들은 기업 및 개인 사용자들에게 AI 챗봇 사용 시 주의를 기울일 것을 권고하고 있습니다. AI 기술의 확산과 함께 AI가 생성하는 데이터의 법적 효력 및 개인 정보 보호 문제가 중요한 쟁점으로 부상하고 있습니다. 출처는 Google News AI Search입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [ClawGUI: A Unified Framework for Training, Evaluating, and Deploying GUI Agents](https://huggingface.co/papers/2604.11784)

ClawGUI는 GUI 에이전트 개발의 주요 과제를 해결하기 위해 통합된 강화 학습, 표준화된 평가, 크로스 플랫폼 배포 기능을 제공하는 오픈소스 프레임워크입니다. GUI 에이전트는 시각적 인터페이스를 통해 애플리케이션과 상호작용하지만, 기존 개발은 환경 불안정성, 평가 프로토콜 불일치, 실제 사용자 배포의 어려움으로 인해 병목 현상을 겪었습니다. ClawGUI는 이러한 문제를 해결하기 위해 ClawGUI-RL을 통해 병렬 가상 환경 및 실제 물리 장치 지원과 GiGPO를 통합한 RL 인프라를 제공합니다. 또한 ClawGUI-Eval은 6개 벤치마크에 걸쳐 표준화된 평가 파이프라인을 구축하고, ClawGUI-Agent는 Android, HarmonyOS, iOS 등 다양한 플랫폼에 에이전트를 배포할 수 있도록 지원합니다. 이 통합 파이프라인을 통해 학습된 ClawGUI-2B는 MobileWorld GUI-Only 벤치마크에서 17.1%의 성공률을 달성하며 기존 MAI-UI-2B를 능가하는 성능을 보였습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 2. [KnowRL: Boosting LLM Reasoning via Reinforcement Learning with Minimal-Sufficient Knowledge Guidance](https://huggingface.co/papers/2604.12627)

KnowRL은 Constrained Subset Search를 통해 최소한의 지식 가이던스로 LLM의 추론 능력을 강화하는 지식 기반 강화 학습 프레임워크를 제안합니다. (영문 용어: Minimal-Sufficient). 기존 LLM의 추론 능력 향상을 위한 강화 학습(RL) 방법은 어려운 문제에서 보상 희소성(reward sparsity) 문제가 있었고, 힌트 기반 RL은 토큰 추가로 인한 중복성 및 비효율성을 야기했습니다. KnowRL은 힌트 설계를 '최소한의 충분한 가이던스' 문제로 보고, 지식을 원자적인 지식 포인트(KP)로 분해한 뒤 Constrained Subset Search(CSS)를 사용하여 상호작용을 고려한 압축된 부분집합을 구성합니다. 이를 통해 KnowRL-Nemotron-1.5B는 8가지 추론 벤치마크에서 기존 RL 및 힌트 기반 모델들을 능가하며, 1.5B 스케일에서 새로운 SOTA를 달성했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 3. [Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe](https://huggingface.co/papers/2604.13016)

이 논문은 LLM의 On-Policy Distillation(OPD) 성공 여부를 결정하는 두 가지 핵심 조건과 그 메커니즘을 분석하고, 실패하는 OPD를 개선하기 위한 실용적인 전략을 제안합니다. LLM의 On-Policy Distillation(OPD)은 핵심적인 후속 훈련 기술이지만, 그 훈련 역학은 잘 이해되지 않았습니다. 이 연구는 OPD 성공을 위한 두 가지 조건을 제시합니다: 학생 및 교사 모델 간의 호환 가능한 사고 패턴 공유, 그리고 교사가 학생의 훈련 데이터를 넘어선 새로운 능력을 제공해야 한다는 것입니다. 저자들은 토큰 수준 메커니즘 분석을 통해 성공적인 OPD가 학생이 방문한 상태에서 높은 확률 토큰에 대한 점진적인 정렬로 특징지어진다는 것을 보여줍니다. 또한, 실패하는 OPD를 복구하기 위한 오프-정책 콜드 스타트와 교사 정렬 프롬프트 선택이라는 두 가지 실용적인 전략을 제안합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 4. [Turing Test on Screen: A Benchmark for Mobile GUI Agent Humanization](https://huggingface.co/papers/2604.09574)

모바일 GUI 에이전트의 인간화를 위한 벤치마크인 "Turing Test on Screen"을 제안하여 디지털 플랫폼의 탐지를 피하면서 작업 성능을 유지하는 방법을 연구합니다. 이 연구는 자율 GUI 에이전트가 디지털 플랫폼의 탐지 시스템에 의해 감지되는 문제를 해결하기 위해 '인간화' 능력이 필요하다고 주장합니다. 이를 위해 에이전트와 탐지기 간의 MinMax 최적화 문제로 상호작용을 모델링하고, 모바일 터치 역학에 대한 고품질 데이터셋을 수집했습니다. 연구 결과, 기존 LMM 기반 에이전트가 부자연스러운 움직임으로 쉽게 탐지됨을 확인하고, 모방성과 유틸리티 간의 균형을 측정하는 Agent Humanization Benchmark (AHB)를 구축했습니다. 최종적으로 휴리스틱 노이즈 및 데이터 기반 행동 매칭과 같은 방법을 제안하여 성능 저하 없이 높은 모방성을 달성할 수 있음을 입증했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 5. [SPPO: Sequence-Level PPO for Long-Horizon Reasoning Tasks](https://huggingface.co/papers/2604.08865)

SPPO는 긴 Chain-of-Thought 추론 작업에서 PPO의 불안정성과 GRPO의 높은 계산 비용 문제를 해결하기 위해 Sequence-Level Contextual Bandit 문제로 재구성한 강화 학습 알고리즘입니다. (영문 용어: Long-Horizon). 기존 PPO는 긴 Chain-of-Thought(CoT) 추론에서 시간적 신용 할당의 불안정성으로 인해 어려움을 겪으며, GRPO와 같은 대안은 계산 오버헤드가 큽니다. SPPO는 추론 과정을 Sequence-Level Contextual Bandit 문제로 재구성하여 이러한 문제를 해결합니다. 이 방법은 디커플링된 스칼라 가치 함수를 사용하여 낮은 분산의 이점 신호를 도출하며, 다중 샘플링 없이도 효율적인 학습이 가능합니다. 수학 벤치마크 실험에서 SPPO는 표준 PPO를 크게 능가하고 계산 비용이 많이 드는 그룹 기반 방법과 유사한 성능을 보이며, 추론 LLM 정렬을 위한 리소스 효율적인 프레임워크를 제공합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 6. [Toward Autonomous Long-Horizon Engineering for ML Research](https://huggingface.co/papers/2604.13018)

AiScientist는 계층적 오케스트레이션과 내구성 있는 상태 관리를 결합하여 자율적인 장기 ML 연구 엔지니어링을 가능하게 합니다. (영문 용어: Long-Horizon). 기존의 자율 AI 연구는 장기적인 ML 연구 엔지니어링에서 일관된 진행을 유지하기 어렵다는 문제가 있었습니다. AiScientist는 이러한 문제를 해결하기 위해 계층적 오케스트레이션과 File-as-Bus 워크스페이스를 결합한 시스템을 제안합니다. 이를 통해 상위 Orchestrator는 단계별 제어를 유지하고, 전문화된 에이전트는 분석, 계획, 코드와 같은 내구성 있는 아티팩트를 기반으로 작업을 수행합니다. 결과적으로 AiScientist는 PaperBench 및 MLE-Bench Lite 벤치마크에서 기존 베이스라인 대비 우수한 성능을 달성했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 7. [BERT-as-a-Judge: A Robust Alternative to Lexical Methods for Efficient Reference-Based LLM Evaluation](https://huggingface.co/papers/2604.09497)

BERT-as-a-Judge는 LLM 평가에서 기존의 어휘 기반 방식의 한계를 극복하고, LLM-as-a-Judge의 높은 비용 문제를 해결하며, 참조 기반 생성 모델 평가의 정확도와 효율성을 높이는 새로운 접근 방식입니다. (영문 용어: Reference-Based). 기존 LLM 평가 방식인 어휘 기반(lexical) 방법은 모델의 문제 해결 능력과 포맷 준수 여부를 혼동하여 인간 판단과 상관관계가 낮다는 문제가 있었습니다. 이를 해결하기 위해 BERT-as-a-Judge는 인코더 기반 접근 방식을 도입하여 출력 문구의 변화에 강건하게 답변의 정확성을 평가합니다. 이 방법은 합성으로 주석이 달린 질문-후보-참조 트리플렛에 대한 경량 훈련만으로 가능하며, 어휘 기반 방식보다 우수하고 대규모 LLM 심사위원과 유사한 성능을 보이며 신뢰할 수 있고 확장 가능한 평가를 가능하게 합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 8. [Lyra 2.0: Explorable Generative 3D Worlds](https://huggingface.co/papers/2604.13036)

Lyra 2.0은 공간 망각 및 시간적 드리프트 문제를 해결하여 대규모 3D 장면 생성을 위한 탐색 가능한 지속형 비디오 생성 프레임워크를 제시합니다. 기존 비디오 생성 모델은 긴 카메라 궤적과 큰 시점 변화가 있는 대규모 3D 환경 생성 시 공간 망각(spatial forgetting)과 시간적 드리프트(temporal drifting) 문제로 인해 성능이 저하됩니다. Lyra 2.0은 이러한 문제를 해결하기 위해 프레임별 3D 지오메트리를 사용하여 과거 프레임을 검색하고 타겟 시점과의 밀집된 대응 관계를 설정하여 공간 망각을 방지합니다. 또한, 모델이 자체적으로 저하된 출력을 수정하도록 학습시키는 self-augmented histories를 통해 시간적 드리프트를 해결합니다. 이를 통해 Lyra 2.0은 대규모의 지속적이고 탐색 가능한 3D 세계를 생성할 수 있습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 9. [Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://huggingface.co/papers/2604.12374)

Nemotron 3 Super는 NVFP4로 사전 학습되고 LatentMoE 아키텍처와 MTP 레이어를 활용하여 추론 속도를 가속화한 120B 파라미터 하이브리드 Mamba-Attention Mixture-of-Experts 모델입니다. (영문 용어: Mamba-Transformer). 기존 모델들은 대규모 언어 모델의 추론 효율성과 정확도 사이에서 균형을 맞추는 데 어려움이 있었습니다. Nemotron 3 Super는 LatentMoE 아키텍처와 MTP 레이어를 도입하여 이 문제를 해결합니다. 이 모델은 NVFP4로 사전 학습되었으며, 25조 토큰으로 학습된 후 SFT 및 RL을 통해 후속 학습되었습니다. 결과적으로 Nemotron 3 Super는 유사한 정확도를 유지하면서도 GPT-OSS-120B 및 Qwen3.5-122B 대비 각각 최대 2.2배 및 7.5배 높은 추론 처리량을 달성합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 10. [Towards Long-horizon Agentic Multimodal Search](https://huggingface.co/papers/2604.12890)

LMM-Searcher는 파일 기반 시각 표현 메커니즘과 점진적 시각 로딩을 통해 장기적인 에이전트 기반 멀티모달 검색에서 이질적인 정보와 높은 토큰 비용 문제를 해결합니다. (영문 용어: Long-horizon). 기존 멀티모달 딥 검색 에이전트는 복잡한 작업을 해결하는 데 잠재력이 있지만, 장기적인 관점에서 이질적인 정보 관리와 높은 토큰 비용이 문제였습니다. LMM-Searcher는 시각 자산을 외부 파일 시스템에 저장하고 경량 텍스트 식별자로 매핑하는 파일 기반 시각 표현 메커니즘을 제안합니다. 이를 통해 컨텍스트 오버헤드를 줄이면서 멀티모달 정보를 보존하고, 온디맨드 시각 로딩 전략으로 능동적인 인식을 가능하게 합니다. 이 방법은 100턴 검색 범위까지 확장 가능하며, MM-BrowseComp 및 MMSearch-Plus와 같은 챌린징한 장기 벤치마크에서 최첨단 성능을 달성했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.
