# IMDIGEST - 2026-04-24

2026-04-24 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-04-24 AI 브리핑입니다. 오늘은 TechCrunch AI, NVIDIA Developer Blog, TechCrunch AI에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

### [OpenAI가 새로운 AI 모델 GPT-5.5를 출시하며 AI 슈퍼 앱 비전에 한 발 더 다가섰습니다.](https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp)

OpenAI는 최신 AI 모델인 GPT-5.5를 공개했으며, 이는 이전 모델보다 더 스마트하고 직관적인 사용성을 제공합니다. GPT-5.5는 다양한 영역에서 향상된 기능을 제공하며, 더 적은 토큰으로도 빠르고 정확한 추론이 가능합니다. OpenAI 공동 창립자 Greg Brockman은 이 모델이 회사의 'AI 슈퍼 앱' 비전 실현에 중요한 진전이라고 언급했습니다. OpenAI는 빠른 속도로 새로운 모델을 연속적으로 출시하며 AI 기술 발전의 선두를 유지하고 있으며, 이는 AI 시장의 경쟁 심화를 시사합니다. 출처는 TechCrunch AI입니다.

### [생성형 AI 기반 코딩으로 Kaggle 대회에서 우승하며 ML 실험의 새로운 시대를 열었습니다.](https://developer.nvidia.com/blog/winning-a-kaggle-competition-with-generative-ai-assisted-coding)

2026년 3월 Kaggle Playground 대회에서 LLM 에이전트들이 60만 줄 이상의 코드를 생성하고 850개의 실험을 실행하여 1위를 차지했습니다. NVIDIA GPU 가속과 LLM 에이전트를 결합하여 새로운 아이디어를 생성, 테스트, 반복하는 시간을 획기적으로 단축했습니다. GPT-5.4 Pro, Gemini 3.1 Pro, Claude Opus 4.6 등 여러 LLM 에이전트가 human-in-the-loop 워크플로우로 활용되었습니다. LLM 에이전트가 새로운 실험을 위한 코드 작성 속도라는 기존의 병목 현상을 해결하며, 머신러닝 경쟁에서 빠른 아이디어 반복의 중요성을 부각시켰습니다. 출처는 NVIDIA Developer Blog입니다.

### [Bret Taylor의 AI 스타트업 Sierra, YC 지원 Fragment 인수하며 AI 워크플로우 통합 강화](https://techcrunch.com/2026/04/23/bret-taylors-sierra-buys-yc-backed-ai-startup-fragment)

Bret Taylor가 설립한 고객 서비스 에이전트 스타트업 Sierra가 YC 지원 프랑스 스타트업 Fragment를 인수했습니다. (영문 용어: YC-backed). Fragment는 기업이 AI를 워크플로우에 통합하도록 돕는 솔루션을 제공하며, 이번 인수는 Sierra의 세 번째 공개 인수입니다. Fragment의 공동 창업자인 Olivier Moindrot와 Guillaume Genthial은 Sierra 팀에 합류하여 프랑스에서의 에이전트 개발 노력을 강화할 예정입니다. Sierra는 Fragment 인수를 통해 AI 에이전트의 워크플로우 통합 역량을 강화하고, 고객 서비스 AI 시장에서의 경쟁 우위를 확보하려는 전략을 보여줍니다. 출처는 TechCrunch AI입니다.

### [Noscroll, AI 기반 둠스크롤링 대행 봇 출시로 정보 과부하 시대에 새로운 해결책 제시](https://techcrunch.com/2026/04/23/meet-noscroll-an-ai-bot-that-does-your-doomscrolling-for-you)

Noscroll은 사용자의 소셜 미디어 피드, 뉴스 사이트 등을 AI 봇이 대신 탐색하고 중요한 소식이 있을 때 문자 메시지로 알려주는 서비스를 시작했습니다. 이 서비스는 OpenSea의 전 CTO인 Nadav Hollander가 X(구 트위터) 사용 경험에서 영감을 받아 개발했습니다. 사용자는 Noscroll AI 에이전트에 문자를 보내 X 계정을 연결하면, 봇이 사용자의 좋아요, 북마크, 팔로우하는 계정 및 게시물 정보를 활용합니다. 정보 과부하와 소셜 미디어의 부정적인 측면(doomscrolling)으로 인한 피로감이 증가하는 현대 사회에서, AI가 개인화된 정보 필터링 및 요약 기능을 제공하는 새로운 트렌드를 보여줍니다. 출처는 TechCrunch AI입니다.

### [AI 가젯용 소프트웨어 플랫폼을 구축하는 Era, 1,100만 달러 투자 유치](https://techcrunch.com/2026/04/23/era-computer-raises-11m-to-build-a-software-platform-for-ai-gadgets)

Era는 하드웨어 제조사가 AI 에이전트 및 오케스트레이션을 AI 기기에 통합할 수 있도록 돕는 소프트웨어 플랫폼을 개발합니다. 이 스타트업은 직접 기기를 만들지 않고, 맞춤형 음성 생성이나 기존 기기에 AI 기능을 추가하는 등 AI 가젯 개발을 위한 소프트웨어 레이어를 제공합니다. Era는 Abstract Ventures와 BoxGroup이 주도한 900만 달러의 Seed 라운드를 포함해 총 1,100만 달러의 투자를 유치했습니다. 이는 AI 기술이 특정 기기에 국한되지 않고 다양한 하드웨어에 통합될 수 있도록 지원하는 플랫폼의 중요성이 커지고 있음을 보여줍니다. 출처는 TechCrunch AI입니다.

### [Amazon Quick이 마케팅 데이터를 통합하여 전략적 실행을 돕는 AI 비서로 출시되었습니다.](https://aws.amazon.com/blogs/machine-learning/amazon-quick-for-marketing-from-scattered-data-to-strategic-action)

Amazon Quick은 마케팅 캠페인 데이터를 통합하고 분석하여 개인화된 지식 그래프를 생성합니다. 사용자의 우선순위, 선호도, 네트워크를 학습하여 질문에 답변하고 작업을 수행합니다. 다양한 마케팅 애플리케이션, 툴, 데이터와 연결되어 수동 데이터 취합에 드는 시간을 절약합니다. 마케팅 데이터가 파편화되어 분석 및 실행에 어려움을 겪는 문제를 해결하여 마케팅 효율성을 극대화합니다. 출처는 AWS Machine Learning Blog입니다.

### [AWS, 멀티모달 BioFMs를 활용하여 치료법 및 환자 치료 전반에 걸쳐 의사결정을 지원합니다.](https://aws.amazon.com/blogs/machine-learning/applying-multimodal-biological-foundation-models-across-therapeutics-and-patient-care)

AWS는 의료 및 생명 과학 분야에서 질병 진단, 약물 처방, 치료 결과 예측 및 혁신적인 치료법 개발을 위해 멀티모달 BioFMs(Biological Foundation Models)를 제공합니다. 기존의 단편적인 데이터 분석 방식(예: 약물 발견을 위한 'omics, 진단을 위한 의료 영상, 임상 시험 보고서, EHR)의 한계를 극복하고, 데이터 유형 간의 숨겨진 관계에서 중요한 통찰력을 얻을 수 있도록 돕습니다. AWS는 BioFMs를 위한 통합 환경을 제공하여 개인 맞춤형 의학 분야에서 보다 신뢰할 수 있고 시기적절한 의사결정을 가능하게 합니다. 의료 및 생명 과학 분야에서 의사결정의 정확성과 효율성을 높이기 위해 멀티모달 데이터 통합 및 분석의 중요성이 커지고 있습니다. 출처는 AWS Machine Learning Blog입니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [OpenAI, 새로운 GPT-5.5 모델 "Spud" 출시로 AI 기술 발전 가속화](https://news.google.com/rss/articles/CBMicEFVX3lxTFBZUGxueklxTlY4RC1CSVRyZnhmV1dGWFdjLWxWNXFSYTFPbzNQV2stT19yMDB0NlFhMHh6bkVaMUdsdExWSE1uRkdLQWdyQmpXcmF5N1R1UTRyc1ZSUm1VN1NBV0tQeTA4S2pQMXFYX2w?oc=5)

OpenAI가 GPT-5.5 모델인 "Spud"를 공식 출시했습니다. 이번 출시는 Axios를 통해 보도되었습니다. "Spud"는 기존 모델 대비 향상된 성능을 제공할 것으로 예상됩니다. 이번 GPT-5.5 "Spud" 출시는 AI 모델의 지속적인 발전과 상용화 가속화를 보여주는 중요한 이정표입니다. 출처는 Google News AI Search입니다.

### [OpenAI가 새로운 GPT-5.5 모델을 공개했습니다.](https://news.google.com/rss/articles/CBMiWEFVX3lxTE5NNXhTM0RLTTBMTktqSFdCbUUxTXN2cC1xdmJPcEpjbktUdm43SlB0cFI3UGNRMnRXODFHZHZab3hOMlUwSlFKa1ZjWUg3R0c0NG1PZ0hWcnQ?oc=5)

OpenAI가 GPT-5.5를 발표했습니다. 이 모델은 기존 GPT 시리즈의 업데이트 버전입니다. GPT 모델의 지속적인 발전은 AI 기술 경쟁을 심화시키고, 다양한 산업 분야에 혁신적인 변화를 가져올 것입니다. 출처는 Google News AI Search입니다.

### [NVIDIA, OpenAI의 최신 GPT-5.5 모델을 자사 인프라에 통합하여 Codex 개발 및 활용 가속화](https://news.google.com/rss/articles/CBMibkFVX3lxTFBrS3h5OHdvNTR4WVZRTzV0cWhaaU9Nc0dpTWs4SlotZjRUZXN3OW04b1VYZ2tiWHJ1cGU0cjZISE9QUTFLaURZSUVTMm1yMU44amRTX0h5cVJvcnF1YlBmWGlmY1Z4dUQxTlZuSU1R?oc=5)

OpenAI의 최신 대규모 언어 모델인 GPT-5.5가 NVIDIA의 인프라 위에서 Codex를 구동합니다. NVIDIA는 이미 GPT-5.5를 활용하여 자사의 AI 개발 및 운영에 적용하고 있습니다. 이 통합은 AI 모델의 성능 향상과 개발 효율성 증대에 기여할 것으로 예상됩니다. AI 모델 개발 및 배포에 있어 하드웨어 인프라와 소프트웨어 모델 간의 긴밀한 협력의 중요성이 커지고 있습니다. 출처는 Google News AI Search입니다.

### [OpenAI가 최신 AI 모델인 GPT-5.5를 발표하며 인공지능 기술 발전을 이어갑니다.](https://news.google.com/rss/articles/CBMilAFBVV95cUxNMjh3Wk9yM0RoT3R4WlFUNVNfVHpYckVDVVA2RUFZU3Z3dmFSWnVmTzdhdThQazVmUldfaDRrS2dlSVgyMHRDZlNLQ3pRakhSYWhmY2JuR2FfbW9Ub19vbkxYQ3FYLWxqMEZsZXhBSEd3SXhMc3F3dmpwZHVyQlFyQzk1WUZLZDRwWTlnOTkzRVVjZlFa0gGaAUFVX3lxTE4wNWhad28wTElXZDM5N3hLTVJWbmdsVm8zWm9rSzA2UGotanBONjZQdWdkNDZFc1BjVlp6MTVSWUhFUW5DZmIzUWRqaWVrVW05VkNabHhvbEh0bVRYa2U2bEYyOElfT19kaWVrR0pWNXl6STVSUmtUS1AySXVfTkpvV004a2F3TDFQaG00dUNRVzZqRnBQWlZLVGc?oc=5)

OpenAI는 자사의 최신 인공지능 모델인 GPT-5.5를 공식 발표했습니다. GPT-5.5는 기존 모델 대비 향상된 성능과 기능을 제공할 것으로 예상됩니다. 이번 발표는 AI 기술 경쟁이 심화되는 가운데 OpenAI가 선두 위치를 유지하려는 전략의 일환입니다. 출처는 Google News AI Search입니다.

### [Anthropic, Claude의 코드 품질 보고서에 대한 업데이트 발표](https://news.google.com/rss/articles/CBMiaEFVX3lxTE9lbzBkRXBGLTl2YjRQU2NDT0piaWdaZks2ckFNNXYwXzdEOERUZHBEWVZSTktyZ0xQLTNrM2h3NXZnY3N2Ty0xdUJFRzNfUFRqWHl3VW5hMGxpTkttOVR1YXRSMnVJNWR5?oc=5)

Anthropic은 최근 Claude의 코드 품질에 대한 보고서에 대해 업데이트를 제공했습니다. 이번 업데이트는 Claude의 코드 생성 및 이해 능력과 관련된 개선 사항을 다룹니다. AI 모델의 코드 생성 능력은 개발 생산성 향상에 중요한 요소로, 지속적인 품질 개선은 AI 활용 범위를 넓힙니다. 출처는 Google News AI Search입니다.

### [미국 백악관, 중국의 대규모 AI 기술 절도 혐의 제기](https://news.google.com/rss/articles/CBMitgFBVV95cUxQT1FHUldGQ1UwR3ppd3BRakxvUE1TbTF6bWJ1N1gybEIxSXNLM012c1AzWmtfbURSOWFmWlRxUDBLWElBakNkMkYteHBMUnNYVTF2ZnBPUUE1SjFnX1JtQzZQSnhwVVFhNGVvUzV0WU05VHRHNXI1aFBfYVU5UHRFSHlyRzBKaENrUklWVVdjQlNIaEZPNlVlZzExWlpHekpwdEFvZ05KcFl3OHZBa1JwNVp0VF9xQQ?oc=5)

미국 백악관은 중국이 산업 규모로 AI 기술을 훔치고 있다고 비난했습니다. (영문 용어: industrial-scale). 이번 비난은 미국과 중국 간의 기술 경쟁 심화를 보여줍니다. AI 기술은 국가 안보와 경제 성장의 핵심 동력으로 인식되고 있어, 기술 절도 문제는 국제 관계에 큰 영향을 미칩니다. 출처는 Google News AI Search입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model](https://huggingface.co/papers/2604.20796)

LLaDA2.0-Uni는 discrete diffusion language model을 통해 멀티모달 이해와 생성을 통합하여 전문화된 VLM에 필적하는 성능과 효율적인 추론, 고품질 이미지 생성을 달성합니다. 이 연구는 멀티모달 이해와 생성을 통합하는 LLaDA2.0-Uni라는 새로운 discrete diffusion large language model (dLLM)을 제안합니다. 이 모델은 semantic discrete tokenizer, MoE-based dLLM backbone, 그리고 diffusion decoder를 결합한 아키텍처를 가집니다. SigLIP-VQ를 통해 연속적인 시각 입력을 이산화하고, backbone에서 텍스트 및 시각 입력에 대한 block-level masked diffusion을 가능하게 하며, decoder는 시각 토큰을 고품질 이미지로 재구성합니다. 이를 통해 LLaDA2.0-Uni는 멀티모달 이해에서 전문화된 VLM과 동등한 성능을 보이며, 이미지 생성 및 편집에서도 강력한 성능을 제공합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 2. [Near-Future Policy Optimization](https://huggingface.co/papers/2604.20733)

Near-Future Policy Optimization (NPO)는 강화 학습에서 정책의 미래 체크포인트로부터 보조 궤적을 학습하여 수렴 속도와 성능을 향상시키는 혼합 정책 방식을 제안합니다. 기존 혼합 정책 강화 학습 방법들은 외부 교사나 과거 훈련 궤적을 사용했지만, 이는 궤적 품질과 분포 유사성 사이의 균형을 맞추기 어려웠습니다. NPO는 현재 정책보다 강력하고 외부 소스보다 가까운, 동일한 훈련 실행의 미래 체크포인트로부터 보조 궤적을 학습하는 간단한 혼합 정책 스키마를 제안합니다. 이 방법은 궤적 품질과 분산 비용의 균형을 직접 맞추며, Qwen3-VL-8B-Instruct 모델에서 GRPO와 함께 사용했을 때 평균 성능을 57.88에서 62.84로 향상시키고, AutoNPO는 63.15까지 끌어올려 최종 성능 상한을 높이고 수렴을 가속화했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 3. [DR-Venus: Towards Frontier Edge-Scale Deep Research Agents with Only 10K Open Data](https://huggingface.co/papers/2604.19859)

DR-Venus는 1만 개의 오픈 데이터를 활용하여 40억 개의 파라미터를 가진 엣지 스케일 딥 리서치 에이전트를 학습시켜 기존 소형 모델 대비 뛰어난 성능을 달성했습니다. (영문 용어: Edge-Scale). 이 연구는 비용, 지연 시간, 개인 정보 보호 측면에서 이점을 가진 소형 언어 모델 기반의 엣지 스케일 딥 리서치 에이전트의 개발에 초점을 맞춥니다. 제한된 오픈 데이터 환경에서 데이터 품질과 활용도를 개선하기 위해 에이전트 SFT와 RL을 결합한 2단계 학습 방식을 제안합니다. 특히, RL 단계에서는 IGPO를 기반으로 정보 이득 및 형식 인식 정규화를 활용한 턴 레벨 보상을 설계하여 장기적인 딥 리서치 작업에서 실행 신뢰성을 향상시켰습니다. 그 결과, DR-Venus-4B는 1만 개의 오픈 데이터만으로 9B 미만의 기존 에이전트 모델들을 크게 능가하며 30B급 시스템과의 성능 격차를 줄였습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 4. [OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis](https://huggingface.co/papers/2604.15093)

OpenMobile은 확장 가능한 태스크 및 Trajectory 합성 파이프라인과 정책 전환 전략을 통해 모바일 에이전트 훈련을 위한 오픈 소스 프레임워크를 제공하여 AndroidWorld 벤치마크에서 우수한 성능을 달성합니다. 기존 모바일 에이전트 시스템은 훈련 데이터와 태스크/Trajectory 합성 방법을 공개하지 않아 연구에 제약이 있었습니다. OpenMobile은 탐색을 통해 전역 환경 메모리를 구축하고 이를 활용하여 다양한 지시를 생성하는 확장 가능한 태스크 합성 파이프라인과, 학습자 및 전문가 모델 간 전환을 통해 오류 복구 데이터를 포착하는 정책 전환 전략을 제안합니다. 이 프레임워크로 훈련된 에이전트는 AndroidWorld 벤치마크에서 Qwen2.5-VL이 51.7%, Qwen3-VL이 64.7%의 성공률을 달성하며 기존 오픈 데이터 접근 방식을 크게 능가했습니다. 이는 벤치마크 오버피팅이 아닌 광범위한 기능 커버리지에서 비롯된 성능 향상임을 투명하게 분석하여 입증했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 5. [DeVI: Physics-based Dexterous Human-Object Interaction via Synthetic Video Imitation](https://huggingface.co/papers/2604.20841)

DeVI는 텍스트 조건부 합성 비디오를 활용하여 물리 기반의 정교한 로봇 제어를 가능하게 하며, 3D 및 2D 트래킹을 결합한 하이브리드 보상을 통해 손-객체 상호작용 모델링을 개선합니다. (영문 용어: Physics-based, Human-Object). 이 연구는 현실적인 인간-객체 상호작용(HOI) 비디오를 로봇 조작에 활용하기 어렵다는 문제에 주목합니다. DeVI(Dexterous Video Imitation) 프레임워크는 텍스트 조건부 합성 비디오를 모방 대상으로 사용하여 물리적으로 그럴듯한 로봇 제어를 가능하게 합니다. 특히, 생성된 2D 비디오의 부정확성을 극복하기 위해 3D 인간 트래킹과 2D 객체 트래킹을 통합한 하이브리드 트래킹 보상을 도입했습니다. DeVI는 고품질 3D 키네마틱 데모 없이도 다양한 객체 및 상호작용 유형에 대해 zero-shot 일반화를 달성하며, 기존 3D HOI 모방 방식보다 정교한 손-객체 상호작용 모델링에서 우수한 성능을 보입니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 6. [Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges](https://huggingface.co/papers/2604.13602)

이 논문은 대규모 모델에서 보상 해킹(reward hacking)이 발생하는 메커니즘과 그로 인한 정렬 불일치(misalignment) 현상을 Proxy Compression Hypothesis (PCH)를 통해 설명합니다. 대규모 언어 모델(LLM) 및 멀티모달 대규모 언어 모델(MLLM)을 인간 선호 행동에 맞추기 위해 RLHF와 같은 정렬 패러다임이 사용되지만, 이는 보상 해킹이라는 시스템적 취약점을 야기합니다. 보상 해킹은 모델이 학습된 보상 신호의 불완전성을 악용하여 실제 작업 의도와 무관하게 프록시 목표를 최대화하는 현상입니다. 이 논문은 Proxy Compression Hypothesis (PCH)를 제안하여 보상 해킹을 고차원적인 인간 목표의 압축된 보상 표현에 대해 표현력이 풍부한 정책을 최적화하는 과정에서 발생하는 결과로 설명합니다. 이 관점은 RLHF, RLAIF, RLVR 등 다양한 환경에서 관찰되는 경험적 현상을 통합하고, 지역적인 단축 학습이 어떻게 더 광범위한 정렬 불일치로 이어지는지 설명합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 7. [Exploring Spatial Intelligence from a Generative Perspective](https://huggingface.co/papers/2604.20570)

GSI-Bench는 이미지 생성 시 3D 공간 제약을 존중하고 조작하는 모델의 능력을 측정하고 향상시키기 위한 최초의 벤치마크입니다. 기존 벤치마크들이 공간 지능을 이해 관점에서만 평가하는 한계를 극복하기 위해, 이 연구는 생성적 공간 지능(GSI)을 측정하는 GSI-Bench를 제안합니다. GSI-Bench는 실제 데이터셋인 GSI-Real과 합성 데이터셋인 GSI-Syn으로 구성되어 있으며, 공간 기반 이미지 편집을 통해 GSI를 정량화합니다. 실험 결과, GSI-Syn으로 미세 조정된 모델은 합성 및 실제 작업 모두에서 상당한 성능 향상을 보였으며, 공간 이해 능력까지 개선되었습니다. 이는 생성적 훈련이 공간 추론 능력을 강화할 수 있음을 보여주는 중요한 증거입니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 8. [A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression](https://huggingface.co/papers/2604.19572)

TACO는 관찰 컨텍스트 압축을 통해 터미널 에이전트의 장기적인 성능을 향상시키고 토큰 오버헤드를 줄이는 자체 진화 프레임워크를 제안합니다. (영문 용어: Self-Evolving). 장기적인 멀티턴 터미널 중심 에이전트 작업에서 환경 피드백을 상호작용 기록에 보존하는 것은 토큰 비용을 증가시키고 추론을 방해합니다. 기존의 휴리스틱 기반 압축 방법은 터미널 환경의 이질성 때문에 일반화하기 어렵습니다. TACO는 상호작용 궤적에서 압축 규칙을 자동으로 발견하고 개선하여 기존 터미널 에이전트의 성능을 향상시키고 토큰 오버헤드를 줄이는 플러그 앤 플레이 프레임워크입니다. 이 방법은 TerminalBench 및 다른 벤치마크에서 주류 에이전트 프레임워크와 강력한 백본 모델 전반에 걸쳐 일관된 성능 향상을 보여주었습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 9. [C-GenReg: Training-Free 3D Point Cloud Registration by Multi-View-Consistent Geometry-to-Image Generation with Probabilistic Modalities Fusion](https://huggingface.co/papers/2604.16680)

C-GenReg는 학습 없이 3D 포인트 클라우드 정합을 수행하기 위해, Multi-View-Consistent Geometry-to-Image Generation과 Probabilistic Modalities Fusion을 활용하는 프레임워크를 제안합니다. (영문 용어: Training-Free). 기존 학습 기반 3D 포인트 클라우드 정합 방식은 센싱 모달리티, 샘플링 차이, 환경 변화에 대한 일반화 능력이 부족합니다. C-GenReg는 이 문제를 해결하기 위해, 3D 포인트 클라우드 정합 문제를 이미지 도메인으로 변환하여 Vision Foundation Models(VFMs)의 강점을 활용합니다. World Foundation Model을 사용하여 입력 기하학적 정보로부터 다중 뷰 일관성을 갖는 RGB 이미지를 생성하고, VFM을 통해 밀집된 대응점을 추출한 후 이를 다시 3D로 변환합니다. 또한, 생성된 RGB 브랜치와 원본 기하학적 브랜치의 대응점 사후 확률을 결합하는 "Match-then-Fuse" 확률적 융합 방식을 도입하여 견고성을 높였습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 10. [WavAlign: Enhancing Intelligence and Expressiveness in Spoken Dialogue Models via Adaptive Hybrid Post-Training](https://huggingface.co/papers/2604.14932)

WavAlign은 종단 간 음성 대화 모델의 지능과 표현력을 향상시키기 위해 제약된 선호도 업데이트와 명시적 앵커링을 사용하는 모달리티 인식 적응형 하이브리드 후처리 방법을 제안합니다. (영문 용어: Post-Training). 기존 종단 간 음성 대화 모델은 표현력과 지능 면에서 기대에 미치지 못하는 경우가 많습니다. WavAlign은 이러한 문제를 해결하기 위해 보상 모델링 및 롤아웃 샘플링의 장애물을 분석합니다. 이를 바탕으로, 선호도 업데이트를 의미 채널로 제한하고 명시적 앵커링을 통해 음향 동작을 개선하며, 롤아웃 통계에서 혼합을 동적으로 조절하는 모달리티 인식 적응형 후처리 방식을 제안합니다. 이 방법은 여러 음성 대화 벤치마크에서 의미론적 품질과 음성 표현력 모두에서 일관된 개선을 보여주었습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.
