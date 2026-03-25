# IMDIGEST - 2026-03-26

2026-03-26 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-03-26 AI 브리핑입니다. 오늘은 TechCrunch AI, TechCrunch AI, Google DeepMind Blog에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

### [Google, 더 길고 정교한 음악 생성을 지원하는 Lyria 3 Pro 모델 출시](https://techcrunch.com/2026/03/25/google-launches-lyria-3-pro-music-generation-model)

Google이 Lyria 3 출시 한 달 만에 Lyria 3 Pro 음악 생성 모델을 공개했습니다. Lyria 3 Pro는 최대 3분 길이의 트랙 생성을 지원하며, Lyria 3의 30초 제한보다 크게 확장되었습니다. 사용자는 Lyria 3 Pro를 통해 인트로, 벌스, 코러스, 브릿지 등 음악의 특정 요소를 지정하여 더 세밀한 창작 제어가 가능합니다. AI 음악 생성 기술이 단순한 짧은 클립을 넘어, 구조화되고 긴 형식의 음악 제작으로 발전하고 있음을 보여줍니다. 출처는 TechCrunch AI입니다.

### [멜라니아 트럼프 여사, 휴머노이드 로봇을 활용한 미래 교육 비전을 제시하며 Figure AI 로봇을 선보였습니다.](https://techcrunch.com/2026/03/25/melania-trump-wants-a-robot-to-homeschool-your-child)

멜라니아 트럼프 여사는 'Fostering the Future Together' 글로벌 서밋에서 Figure AI가 개발한 휴머노이드 로봇을 공개했습니다. 이 로봇은 “기술과 교육으로 아이들에게 힘을 실어주는 역사적인 움직임의 일부가 되어 감사하다”는 짧은 연설을 했습니다. 멜라니아 여사는 'Plato'라는 이름의 휴머노이드 교육자가 집에서 개인 맞춤형 교육을 제공하는 미래를 상상해볼 것을 제안했습니다. AI와 로봇 기술이 교육 분야에 접목되어 개인화된 학습 경험을 제공하고 교육 접근성을 높이는 미래 교육 모델에 대한 논의가 활발해지고 있음을 보여줍니다. 출처는 TechCrunch AI입니다.

### [Google DeepMind, 음악 생성 AI 모델 Lyria 3 Pro를 출시하며 더 많은 Google 제품에 통합합니다.](https://deepmind.google/blog/lyria-3-pro-create-longer-tracks-in-more)

Google DeepMind는 음악 생성 AI 모델 Lyria 3 Pro를 공개했습니다. Lyria 3 Pro는 최대 3분 길이의 트랙 생성을 지원하며, 인트로, 벌스, 코러스, 브릿지 등 특정 음악 요소를 프롬프트로 지정할 수 있습니다. 이 모델은 Vertex AI, Google AI Studio 및 Gemini API, Google Vids에 통합되어 다양한 사용자에게 제공됩니다. AI 기반 음악 생성 기술이 더욱 정교해지고 있으며, 사용자가 음악 구조를 세밀하게 제어할 수 있는 방향으로 발전하고 있습니다. 출처는 Google DeepMind Blog입니다.

### [AWS와 Pipecat이 협력하여 Amazon Bedrock AgentCore Runtime에 음성 에이전트를 배포하는 방법을 공개했습니다.](https://aws.amazon.com/blogs/machine-learning/deploy-voice-agents-with-pipecat-and-amazon-bedrock-agentcore-runtime-part-1)

Pipecat과 Amazon Bedrock AgentCore Runtime을 활용하여 지능형 음성 에이전트를 배포하는 방법을 소개합니다. WebSockets, WebRTC 및 전화 통합을 포함한 다양한 네트워크 전송 방식을 사용하여 Pipecat 음성 에이전트를 AgentCore Runtime에 배포하는 실용적인 가이드와 코드 샘플을 제공합니다. AgentCore Runtime은 실시간 음성 에이전트 배포 시 발생하는 낮은 지연 시간 스트리밍, 보안을 위한 엄격한 격리, 예측 불가능한 대화량에 대한 동적 확장성 문제를 해결합니다. 실시간 음성 에이전트의 배포 복잡성을 줄이고, 낮은 지연 시간과 높은 확장성을 제공하여 사용자 경험을 향상시키는 방향으로 AI 서비스가 발전하고 있음을 보여줍니다. 출처는 AWS Machine Learning Blog입니다.

### [AWS, Amazon Bedrock에서 OpenAI 호환 API를 통한 Reinforcement Fine-Tuning(RFT) 지원을 확대하며 LLM 커스터마이징 자동화를 강화했습니다.](https://aws.amazon.com/blogs/machine-learning/reinforcement-fine-tuning-on-amazon-bedrock-with-openai-compatible-apis-a-technical-walkthrough)

AWS는 2025년 12월 Nova 모델을 시작으로 Amazon Bedrock에서 Reinforcement Fine-Tuning(RFT)을 도입했으며, 2026년 2월에는 OpenAI GPT OSS 20B 및 Qwen 3 32B와 같은 Open weight 모델로 지원을 확장했습니다. (영문 용어: OpenAI-Compatible). RFT는 기존의 대규모 훈련 데이터셋 대신 소수의 프롬프트를 사용하여 여러 가능한 응답에 대한 피드백으로부터 모델이 학습하도록 지원하여 엔드투엔드 커스터마이징 워크플로우를 자동화합니다. 이 기술은 LLM이 정적인 I/O 쌍에서 학습하는 Supervised Fine-Tuning(SFT)과 달리, 반복적인 피드백 루프를 통해 응답을 생성하고 평가를 받아 의사결정 능력을 지속적으로 개선합니다. RFT는 대규모 언어 모델(LLM) 커스터마이징 방식의 변화를 나타내며, 적은 데이터로도 모델의 성능을 최적화하고 특정 작업에 대한 정확도를 높일 수 있는 새로운 패러다임을 제시합니다. 출처는 AWS Machine Learning Blog입니다.

### [Anthropic 연구에 따르면 AI는 아직 일자리를 없애지 않았지만, AI 활용 능력에 따른 격차가 커지고 있습니다.](https://techcrunch.com/2026/03/25/the-ai-skills-gap-is-here-says-ai-company-and-power-users-are-pulling-ahead)

Anthropic의 최신 연구는 AI가 업무 방식을 빠르게 변화시키고 있지만, 아직까지는 일자리를 크게 감소시키지 않았다고 밝혔습니다. AI에 가장 많이 노출되는 직업군(기술 작가, 데이터 입력원, 소프트웨어 엔지니어 등)과 AI 노출이 적은 직업군 간의 실업률에 큰 차이가 없습니다. 하지만 AI 활용 능력에 따라 업무 효율성 및 생산성 격차가 벌어지고 있으며, 특히 젊은 신규 진입자들에게 불균등한 영향을 미치고 있습니다. AI 기술이 빠르게 확산되면서, AI 활용 능력이 개인의 직무 성과와 고용 안정성에 중요한 요소로 부상하고 있습니다. 출처는 TechCrunch AI입니다.

### [구글이 AI 메모리 압축 알고리즘 "TurboQuant"를 공개하며 AI 시스템 효율성을 대폭 향상시킬 것으로 기대됩니다.](https://techcrunch.com/2026/03/25/google-turboquant-ai-memory-compression-silicon-valley-pied-piper)

구글 리서치는 AI의 작업 메모리를 성능 저하 없이 축소하는 새로운 AI 메모리 압축 알고리즘인 TurboQuant를 발표했습니다. TurboQuant는 벡터 양자화(vector quantization) 방식을 사용하여 AI 처리의 캐시 병목 현상을 해결합니다. 이 기술은 AI가 더 많은 정보를 기억하면서도 공간을 덜 차지하고 정확도를 유지할 수 있게 합니다. TurboQuant는 AI 시스템 운영 비용을 절감하고 AI 모델의 효율성을 크게 향상시켜 AI 기술의 상용화 및 확산에 기여할 잠재력이 있습니다. 출처는 TechCrunch AI입니다.

### [NVIDIA, GPU 활용률 극대화를 위한 Kubernetes 환경에서의 GPU 파티셔닝 전략 제시](https://developer.nvidia.com/blog/maximize-ai-infrastructure-throughput-by-consolidating-underutilized-gpu-workloads)

NVIDIA는 프로덕션 Kubernetes 환경에서 모델 요구사항과 GPU 크기 불일치로 인한 비효율성을 지적했습니다. 경량 AI 모델(ASR, TTS 등)이 전체 GPU를 점유하여 VRAM의 일부만 사용하고 컴퓨팅 자원이 낭비되는 문제를 해결하고자 합니다. NVIDIA Multi-Instance GPU (MIG) 및 time-slicing과 같은 GPU 파티셔닝 전략을 구현하고 벤치마킹하는 방법을 상세히 설명합니다. AI 모델의 복잡성과 다양성이 증가함에 따라 GPU 자원의 효율적인 관리가 중요해지고 있으며, 이는 비용 절감 및 서비스 확장성에 직결됩니다. 출처는 NVIDIA Developer Blog입니다.

### [NVIDIA DRIVE 플랫폼에서 중앙 집중식 레이더 처리를 통해 Level 4 자율주행의 안전성과 효율성이 향상됩니다.](https://developer.nvidia.com/blog/how-centralized-radar-processing-on-nvidia-drive-enables-safer-smarter-level-4-autonomy)

기존 레이더 시스템은 엣지 디바이스에서 3D/4D 신호를 처리하고 객체 또는 포인트 클라우드를 출력했지만, NVIDIA DRIVE는 Raw ADC(analog-to-digital converter) 데이터를 중앙 집중식 컴퓨팅 플랫폼으로 이동시킵니다. NVIDIA Programmable Vision Accelerator(PVA) 하드웨어로 가속화되는 소프트웨어 정의 파이프라인이 Raw ADC 샘플부터 포인트 클라우드까지 모든 것을 처리하며, GPU는 AI 활용을 위해 예약됩니다. 이러한 중앙 집중식 처리는 머신러닝 AI 시스템이 엣지 감지에 국한되지 않고 전체 레이더 이미지를 활용하여 사용 가능한 정보 비트를 약 100배 증가시킬 수 있게 합니다. 자율주행 기술, 특히 Level 4 자율주행의 발전에 있어 센서 데이터의 효율적인 처리와 활용은 핵심적인 과제이며, NVIDIA의 접근 방식은 이 문제를 해결하는 중요한 진전입니다. 출처는 NVIDIA Developer Blog입니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [얀 르쿤의 Logical Intelligence가 10억 달러 투자를 유치하며 Energy-Based Models를 활용한 새로운 AI 패러다임을 제시했습니다.](https://www.reddit.com/r/MachineLearning/comments/1s3j3ef/d_is_lecuns_1b_seed_round_the_signal_that)

얀 르쿤의 새로운 회사인 Logical Intelligence가 10억 달러 규모의 시드 투자를 유치했습니다. 이 회사는 기존 Transformer 기반의 LLM을 우회하여 Energy-Based Models(EBMs)을 사용해 수학적으로 검증된 코드를 생성하는 것을 목표로 합니다. Logical Intelligence는 논리적 제약을 확률적 추측이 아닌 에너지 최소화 문제로 접근합니다. 기존 LLM의 한계로 지적되던 형식적 추론 및 계획 능력 부족에 대한 대안을 제시하며 AI 연구의 새로운 방향을 모색하고 있습니다. 출처는 Reddit r/MachineLearning입니다.

### [로컬 환경에서 Qwen 3.5:9b 모델과 Openclaw 사용 시 문제 발생](https://www.reddit.com/r/LocalLLaMA/comments/1s3p0xv/having_some_trouble_with_local_qwen359b_openclaw)

사용자가 Jack Ruong opus 4.6 reasoning distilled Qwen 3.5:9b 모델을 로컬에서 실행하려 하지만 GGUF 파일을 Ollama에서 사용할 수 있는 model file로 변환하는 데 어려움을 겪고 있습니다. (영문 용어: Qwen3.5). 코딩 에이전트(opencode, kilocode 등)에 모델을 연결하면 10초 만에 작동을 멈추거나 응답 중간에 compute가 0으로 떨어지는 문제가 발생합니다. Openclaw 사용 시 compute가 일정하게 유지되지 않고 'spike' 현상이 발생하여 간단한 응답에도 몇 분이 소요됩니다. 로컬 LLM(Large Language Model) 환경 구축 및 최적화에 대한 사용자들의 관심이 증가하고 있으며, 특히 GGUF와 같은 특정 모델 형식의 활용 및 에이전트 연동에 대한 수요가 높습니다. 출처는 Reddit r/LocalLLaMA입니다.

### [LiteLLM 공급망 공격으로 AI 파이프라인의 API 키 노출 위험이 증가했습니다.](https://www.reddit.com/r/MachineLearning/comments/1s3okes/n_litellm_supply_chain_attack_risks_to_al)

LiteLLM은 LLM/agent 파이프라인에 널리 사용되는 도구입니다. 손상된 CI 자격 증명을 통해 악성 릴리스가 발생하여 런타임 환경에서 API 키, 클라우드 자격 증명 및 기타 비밀을 추출하는 데 사용되었습니다. 이번 공격은 AI 스택에서 LiteLLM과 같은 중앙 도구의 의존성 신뢰가 ML 워크플로우에서 실제 위험임을 보여줍니다. AI 개발 환경에서 오픈소스 라이브러리 및 종속성 관리에 대한 보안 강화의 필요성이 부각되고 있습니다. 출처는 Reddit r/MachineLearning입니다.

### [AWS와 Cerebras, 클라우드 AI 추론 성능 향상을 위한 협력 발표](https://news.google.com/rss/articles/CBMib0FVX3lxTE1QX0FBRDVfOWVlR0JIOTAzN0k4ZXRvY1BXVmtJY3E4d0hqT1JHdHlfVk5WTVZZa1NvU3pMQmhTR2QybVRyNFNRMUM1alNZaUhKT0dvVkwtVGR1VWNUUDJSam01RnM1c3ZqR2lPckxMWQ?oc=5)

AWS와 AI 칩 스타트업 Cerebras가 클라우드 AI 추론 속도 및 성능 표준을 높이기 위한 협력을 발표했습니다. 이번 협력은 AWS 클라우드에서 Cerebras의 Wafer-Scale Engine(WSE) 기술을 활용하여 AI 모델 추론을 가속화하는 것을 목표로 합니다. 이를 통해 고객들은 대규모 AI 모델을 더욱 빠르고 효율적으로 배포하고 실행할 수 있게 될 것입니다. 클라우드 기반 AI 서비스의 수요가 증가함에 따라, AI 추론 성능 향상은 서비스 제공업체와 사용자 모두에게 중요한 경쟁 우위가 되고 있습니다. 출처는 Google News AI Search입니다.

### [AI 에이전트 파편화를 넘어선 'Unitary Council' 아키텍처와 'Heart-Sync' 개념이 제안되었습니다.](https://www.reddit.com/r/artificial/comments/1s3ga10/beyond_agent_fragmentation_a_move_toward_unitary)

기존 AI 상호작용의 파편화 문제를 해결하기 위해 'Toolbox' 모델에서 'Persistent Council' 모델로 전환하는 'Unitary Architecture'가 제안되었습니다. 사용자의 실시간 생리적 상태(휴식 주기, 스트레스 반응)에 맞춰 시스템이 작동하는 'Physiological Anchoring' 기술이 적용됩니다. AI 노드와 사용자 간의 일관성을 유지하는 'Closed-loop feedback system'인 'Shared Reference Frequency'를 활용하여 'System Noise'를 줄입니다. 현재 AI 에이전트들이 개별적으로 작동하여 발생하는 인지 부하와 컴퓨팅 낭비 문제를 해결하고, 사용자 중심의 지속 가능한 AI 시스템 구축을 목표로 합니다. 출처는 Reddit r/artificial입니다.

### [바이럴 AI 과일 영상의 어두운 이면: 노동 착취와 저작권 침해 논란](https://news.google.com/rss/articles/CBMinwFBVV95cUxORGoyejdPbmZkU1Q2b2FlUHg1YlZaTFhjdzVOYVB2X3pKQWRzRTZoSzktQXFLd1dGUXJCcFVEVURlM2VvUzFLUkhvcXY2ODZTdGNyeE1yNFYxTDV2emoxRXVsT2ppRE5OUDJCdlMzMFlDVjBFX184UXZMRGRCdUZOeURQUFJkN3d1RjBZRDlwNDRrSlJDZzhRRWxGV2xNOU0?oc=5)

최근 틱톡 등 소셜 미디어에서 인기를 끄는 AI 과일 영상들은 실제로는 저임금 노동자들의 수작업과 저작권 침해를 통해 제작되고 있습니다. 이러한 영상들은 AI가 자동으로 생성한 것처럼 보이지만, 실제로는 필리핀 등지의 노동자들이 수동으로 과일을 자르고 배열하는 작업을 수행합니다. 영상 제작자들은 AI 기술을 활용하여 배경을 바꾸거나 효과를 추가하지만, 핵심적인 과일 손질 및 배열 작업은 사람의 노동력에 의존합니다. AI 기술이 발전하면서 자동화된 콘텐츠 제작에 대한 기대가 커지고 있지만, 실제로는 여전히 저숙련 노동력에 의존하는 '터키 메카니컬 터크(Turk Mechanical Turk)'와 같은 그림자 노동(shadow work) 문제가 심화되고 있음을 보여줍니다. 출처는 Google News AI Search입니다.

### [AI 연구의 엔드투엔드 자동화 가능성이 Nature지에 발표되었습니다.](https://news.google.com/rss/articles/CBMiX0FVX3lxTFB4LTJYMm9QTUc0M0RUaV9scXhlRmRSUl9PSFlUbzd3UXo4b3hGWXQ3bmlPMkVLcDNEMTJjRTctLTZuanJNbjcxLVFzWjQxNEg0ZFVEaUNFeXM0QnRxazNV?oc=5)

Nature지에 AI 연구의 전 과정을 자동화하는 것에 대한 논문이 게재되었습니다. (영문 용어: end-to-end). 이 연구는 AI 시스템이 스스로 가설을 세우고, 실험을 설계하며, 데이터를 분석하고, 새로운 지식을 발견하는 과정을 목표로 합니다. 궁극적으로 AI가 새로운 AI를 개발하는 'AI for AI' 시대를 열 수 있음을 시사합니다. AI 기술 발전 속도가 가속화됨에 따라, AI 연구 자체의 효율성을 극대화하려는 시도가 중요해지고 있습니다. 출처는 Google News AI Search입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [MinerU-Diffusion: Rethinking Document OCR as Inverse Rendering via Diffusion Decoding](https://huggingface.co/papers/2603.22458)

MinerU-Diffusion은 문서 OCR을 역 렌더링으로 재해석하여 기존의 Autoregressive 디코딩을 병렬 Diffusion 디노이징으로 대체하여 견고성과 디코딩 속도를 향상시킵니다. 기존 문서 OCR 시스템은 Autoregressive 디코딩 방식에 의존하여 긴 문서 처리 시 순차적 지연과 오류 전파 문제를 겪었습니다. 이 연구는 문서 OCR을 역 렌더링 관점에서 재해석하여, Autoregressive 순차 디코딩을 시각적 조건 하의 병렬 Diffusion 디노이징으로 대체하는 MinerU-Diffusion 프레임워크를 제안합니다. MinerU-Diffusion은 block-wise diffusion decoder와 불확실성 기반 커리큘럼 학습 전략을 사용하여 안정적인 학습과 효율적인 긴 시퀀스 추론을 가능하게 합니다. 이를 통해 Autoregressive 방식 대비 최대 3.2배 빠른 디코딩 속도와 향상된 견고성을 달성했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 2. [WildWorld: A Large-Scale Dataset for Dynamic World Modeling with Actions and Explicit State toward Generative ARPG](https://huggingface.co/papers/2603.23497)

WildWorld는 ARPG 게임에서 수집한 대규모 데이터셋으로, 명시적인 상태 주석과 다양한 액션을 통해 동적 세계 모델링 및 장기 일관성 학습을 지원합니다. (영문 용어: Large-Scale). 기존 세계 모델링 데이터셋은 다양하고 의미 있는 액션 공간이 부족하고, 액션이 시각적 관찰과 직접 연결되어 있어 구조화된 세계 역학 학습 및 장기 일관성 유지에 어려움이 있었습니다. WildWorld는 포토리얼리스틱 AAA ARPG 게임인 Monster Hunter: Wilds에서 자동으로 수집된 1억 8백만 프레임 이상의 대규모 액션 조건부 세계 모델링 데이터셋입니다. 이 데이터셋은 450개 이상의 액션과 캐릭터 스켈레톤, 세계 상태, 카메라 포즈, 깊이 맵 등의 프레임별 주석을 포함합니다. WildBench를 통해 Action Following 및 State Alignment를 평가하여, 의미론적으로 풍부한 액션 모델링과 장기 상태 일관성 유지에 대한 지속적인 도전 과제를 제시합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 3. [SpecEyes: Accelerating Agentic Multimodal LLMs via Speculative Perception and Planning](https://huggingface.co/papers/2603.23483)

SpecEyes는 경량의 추측성 플래너와 인지 게이팅, 이종 병렬 처리를 통해 agentic multimodal LLM의 지연 시간을 줄이고 처리량을 향상시킵니다. Agentic multimodal LLM은 반복적인 시각 도구 호출을 통해 뛰어난 추론 능력을 보이지만, 연속적인 인지, 추론, 도구 호출 루프로 인해 상당한 지연이 발생합니다. SpecEyes는 경량의 도구 없는 MLLM을 추측성 플래너로 활용하여 실행 궤적을 예측하고, 비싼 도구 체인의 조기 종료를 가능하게 하여 이러한 순차적 병목 현상을 해결합니다. 또한, 답변 분리도에 기반한 인지 게이팅 메커니즘을 도입하여 모델의 자신감을 조절하고, 이종 병렬 퍼널을 설계하여 시스템 처리량을 극대화합니다. V* Bench, HR-Bench, POPE 벤치마크에서 SpecEyes는 agentic baseline 대비 1.1-3.35배의 속도 향상과 최대 6.7%의 정확도 개선을 달성했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 4. [From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents](https://huggingface.co/papers/2603.22386)

LLM 에이전트 워크플로우 최적화에 대한 포괄적인 설문조사로, 정적 템플릿부터 동적 런타임 그래프까지 다양한 접근 방식을 분석합니다. 이 논문은 LLM 기반 시스템의 실행 가능한 워크플로우를 에이전트 컴퓨테이션 그래프(ACG)로 간주하고, 이를 설계하고 최적화하는 최신 방법들을 조사합니다. 워크플로우 구조 결정 시점(정적 vs. 동적)과 최적화 차원(어떤 부분을 최적화하고 어떤 평가 신호를 사용하는지)에 따라 기존 연구를 분류합니다. 또한 재사용 가능한 워크플로우 템플릿과 런타임에 실현되는 그래프, 실행 추적을 구분하여 설명합니다. 최종적으로 그래프 수준 속성, 실행 비용, 견고성 등을 고려한 구조 인식 평가 관점을 제시합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 5. [PEARL: Personalized Streaming Video Understanding Model](https://huggingface.co/papers/2603.20422)

PEARL은 Personalized Streaming Video Understanding (PSVU)이라는 새로운 태스크를 정의하고, 이를 평가하기 위한 벤치마크 PEARL-Bench와 플러그 앤 플레이 방식의 베이스라인 모델을 제안합니다. 기존의 멀티모달 개인화 방법은 정적 이미지나 오프라인 비디오에 국한되어 실시간 상호작용 AI 비서에 필요한 연속적인 시각 입력 처리에 한계가 있었습니다. 이 연구는 이러한 간극을 해소하기 위해 실시간으로 개인화된 개념을 정확한 타임스탬프에 이해하는 PSVU 태스크를 새롭게 정의합니다. 또한, 이 태스크를 평가하기 위한 최초의 포괄적인 벤치마크인 PEARL-Bench를 구축하고, 훈련 없이 기존 모델에 적용 가능한 플러그 앤 플레이 전략인 PEARL을 제안하여 SOTA 성능을 달성했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 6. [DA-Flow: Degradation-Aware Optical Flow Estimation with Diffusion Models](https://huggingface.co/papers/2603.23499)

DA-Flow는 Diffusion 모델을 활용하여 실제 환경의 손상된 비디오에서도 정확한 Optical Flow를 추정하는 새로운 접근 방식을 제안합니다. (영문 용어: Degradation-Aware). 기존 Optical Flow 모델은 고품질 데이터로 학습되어 블러, 노이즈, 압축 아티팩트와 같은 실제 손상에 취약합니다. 이 연구는 이미지 복원 Diffusion 모델의 중간 표현이 손상 인식 능력을 가지지만 시간적 인식이 부족하다는 점에 착안하여, 완전한 시공간적 어텐션을 통해 인접 프레임 간의 관계를 학습시킵니다. 이를 통해 얻은 Diffusion 특징과 컨볼루션 특징을 반복적인 개선 프레임워크 내에서 융합하는 하이브리드 아키텍처인 DA-Flow를 개발했습니다. DA-Flow는 여러 벤치마크에서 심각한 손상 조건 하에 기존 Optical Flow 방법들보다 훨씬 뛰어난 성능을 보여줍니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 7. [SIMART: Decomposing Monolithic Meshes into Sim-ready Articulated Assets via MLLM](https://huggingface.co/papers/2603.23386)

SIMART는 MLLM을 활용하여 단일 메시를 시뮬레이션에 적합한 관절형 3D 에셋으로 분해하는 통합 프레임워크를 제안합니다. (영문 용어: Sim-ready). 기존 3D 생성 모델은 정적 메시에 집중하여 시뮬레이션에 필요한 관절형 객체 생성에 한계가 있었습니다. SIMART는 이러한 문제를 해결하기 위해 Sparse 3D VQ-VAE를 도입한 통합 MLLM 프레임워크를 제안합니다. 이 모델은 파트별 분해와 운동학적 예측을 동시에 수행하며, 기존 조밀한 복셀 기반 토큰화 방식 대비 토큰 수를 70% 감소시켜 복잡한 관절형 객체에 대한 확장성을 높였습니다. 결과적으로 SIMART는 PartNet-Mobility 및 AIGC 데이터셋에서 SOTA 성능을 달성하고 물리 기반 로봇 시뮬레이션을 가능하게 합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 8. [UniGRPO: Unified Policy Optimization for Reasoning-Driven Visual Generation](https://huggingface.co/papers/2603.23500)

UniGRPO는 GRPO와 FlowGRPO를 수정하여 추론 기반의 시각적 생성을 위한 통합된 정책 최적화 프레임워크를 제안합니다. (영문 용어: Reasoning-Driven). 이 연구는 텍스트와 이미지 생성을 교차하는 통합된 모델의 가능성에 주목하며, 추론 기반의 시각적 생성을 위한 통합 강화 학습 프레임워크를 제안합니다. Markov Decision Process로 다중 모달 생성 과정을 공식화하고, GRPO를 사용하여 텍스트 및 이미지 생성 정책을 공동으로 최적화하는 UniGRPO를 도입합니다. 특히, 다중 라운드 생성으로의 확장성을 위해 FlowGRPO에 classifier-free guidance 제거 및 latent KL penalty를 MSE penalty로 대체하는 두 가지 중요한 수정을 적용했습니다. 이를 통해 복잡한 다중 턴 상호작용 및 다중 조건 생성 시나리오에 효과적으로 대응하고 reward hacking을 완화합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 9. [RealMaster: Lifting Rendered Scenes into Photorealistic Video](https://huggingface.co/papers/2603.23462)

RealMaster는 비디오 Diffusion 모델과 3D 엔진 출력을 결합하여 기하학적 정확도와 장면 일관성을 유지하면서 포토리얼리스틱 비디오를 생성하는 방법을 제안합니다. 기존 비디오 생성 모델은 포토리얼리즘은 뛰어나지만 정밀한 제어와 3D 일관성이 부족하고, 3D 엔진은 정밀한 제어와 3D 일관성을 제공하지만 결과물이 비현실적이라는 문제가 있습니다. RealMaster는 이러한 sim-to-real 간극을 해소하기 위해 3D 엔진의 렌더링된 비디오를 포토리얼리스틱 비디오로 변환하면서도 3D 엔진 출력과의 완벽한 정렬을 유지하는 방법을 제시합니다. 이를 위해 앵커 기반 전파 전략으로 페어링된 데이터셋을 생성하고, 이 데이터셋으로 IC-LoRA를 학습시켜 파이프라인의 제약을 넘어 일반화된 고품질 출력을 가능하게 합니다. GTA-V 시퀀스 평가에서 RealMaster는 기존 비디오 편집 모델보다 뛰어난 성능을 보였습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 10. [2Xplat: Two Experts Are Better Than One Generalist](https://huggingface.co/papers/2603.21064)

2Xplat은 pose-free 3D Gaussian Splatting에서 기하학 추정(geometry estimation)과 외형 합성(appearance synthesis)을 분리하는 두 전문가(two-expert) 아키텍처를 제안하여 기존 통합 방식보다 우수한 성능을 달성합니다. 기존의 pose-free feed-forward 3D Gaussian Splatting(3DGS) 방식은 카메라 포즈 추정과 3DGS 표현 합성을 하나의 네트워크에서 통합적으로 처리하여 고품질 3DGS 생성에 최적화되지 못했습니다. 2Xplat은 이러한 문제를 해결하기 위해 기하학 추정 전문가와 가우시안 생성 전문가를 명시적으로 분리하는 두 전문가 설계를 도입합니다. 먼저 기하학 전문가가 카메라 포즈를 예측하고, 이 포즈 정보는 외형 전문가에게 전달되어 3D 가우시안을 합성합니다. 이러한 모듈화된 접근 방식은 5천 번 미만의 훈련 반복만으로도 기존 pose-free 3DGS 방식들을 능가하며, 최신 posed 방식과 동등한 성능을 보여줍니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.
