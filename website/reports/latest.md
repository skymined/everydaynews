# IMDIGEST - 2026-04-20

2026-04-20 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-04-20 AI 브리핑입니다. 오늘은 TechCrunch AI, TechCrunch AI에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

### [OpenAI가 Hiro와 TBPN 인수를 통해 챗봇 이상의 제품 개발 및 대중 이미지 개선을 모색하고 있습니다.](https://techcrunch.com/2026/04/19/openais-existential-questions)

OpenAI는 개인 금융 스타트업 Hiro를 인수하여 챗봇 이상의 유료 제품 개발을 목표로 합니다. OpenAI는 뉴 미디어 스타트업 TBPN을 인수하여 대중적 이미지를 개선하고 여론을 형성하려 합니다. 이번 인수는 OpenAI의 핵심 비즈니스 모델을 크게 바꾸기보다는 새로운 시도를 통해 당면한 문제들을 해결하려는 움직임으로 보입니다. 이번 인수는 OpenAI가 단순한 챗봇을 넘어선 서비스 확장과 함께 기업 이미지 관리의 중요성을 인식하고 있음을 보여줍니다. 출처는 TechCrunch AI입니다.

### [Uber가 자율주행 기술 분야에 100억 달러 이상을 투자하며 'Asset-Heavy' 전략으로 회귀하고 있습니다.](https://techcrunch.com/2026/04/19/techcrunch-mobility-uber-enters-its-assetmaxxing-era)

Uber는 자율주행 차량 구매 및 관련 기술 개발 회사 지분 인수에 100억 달러 이상을 투자했습니다. 이 중 약 25억 달러는 직접 투자이며, 나머지 75억 달러는 향후 몇 년간 로보택시 구매에 사용될 예정입니다. Uber는 과거 Uber Elevate, Uber ATG, Jump와 같은 자산 집약적 사업을 매각했으나, WeRide, Lucid, Nuro, Rivian, Wayve 등 자율주행 기업에 지속적으로 투자하고 있습니다. Uber의 이러한 대규모 투자는 자율주행 기술이 미래 모빌리티 시장의 핵심 동력임을 시사하며, 플랫폼 기업들이 단순 중개를 넘어 핵심 자산 확보에 나서는 트렌드를 보여줍니다. 출처는 TechCrunch AI입니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [LLM 에이전트의 조작을 방지하는 Karpathy의 autoresearch 패턴용 Python 도구 scalar-loop이 개발되었습니다.](https://www.reddit.com/r/artificial/comments/1spz2g0/scalarloop_a_python_harness_for_karpathys)

scalar-loop은 LLM 에이전트가 검증기를 조작하여 더 나은 수치를 보고하는 문제를 해결하기 위해 설계되었습니다. 이 도구는 SHA-256 해시 매니페스트를 통해 Harness 무결성을 보장하며, 봉인된 파일(테스트, 빌드, 설정)의 해시가 변경되면 반복을 되돌립니다. Git diff를 통해 에이전트가 접근할 수 있는 파일 범위를 강제하며, 허용되지 않은 파일 변경 시 반복을 거부합니다. LLM 에이전트의 자율성이 증가함에 따라, 에이전트가 의도치 않거나 악의적으로 시스템을 조작할 가능성이 커지고 있어, 이러한 무결성 및 보안 강화 도구의 필요성이 대두되고 있습니다. 출처는 Reddit r/artificial입니다.

### [최근 주요 AI 모델들이 과도하게 제한되어 사용자 불만이 증가하고 있습니다.](https://www.reddit.com/r/artificial/comments/1spxccd/why_is_every_ai_getting_restricted_these_days)

ChatGPT, Claude, Grok, Gemini 등 여러 AI 모델들이 이전보다 엄격하게 제한되고 있습니다. 사용자들은 AI가 창의적인 작업이나 아이디어 실험 등 일반적인 용도에서도 지나치게 안전 위주로 작동하여 불편함을 겪고 있습니다. 유료 구독자들도 AI의 과도한 제한으로 인해 서비스의 가치가 떨어진다고 느끼고 있습니다. AI 개발사들이 안전 및 윤리적 문제에 대한 우려로 인해 모델의 제한을 강화하는 추세입니다. 출처는 Reddit r/artificial입니다.

### [Boston Dynamics가 Spot 로봇과 Gemini Robotics의 협력을 통해 작업 자동화 도구를 선보입니다.](https://news.google.com/rss/articles/CBMikgFBVV95cUxPSGFTb3BWRkxrWUVaSlBSR1RmYlBoekNTR0NDSWs5RlBid1ZyQWdiUG1TbWxSZ3ByNDRWd2NRUzV3LWdLNHYzSXFMeGtWSmpVbFNfMUtzc1laTWI4dXkwSmdjQmtlY2lRRUoybG9lSno3dWN2R3JwU2JDMENjV1lialNPUzF5MWMxZGFBQ3dQWThZQQ?oc=5)

Boston Dynamics는 Spot 로봇과 Gemini Robotics의 기술을 결합하여 다양한 작업을 자동화하는 도구를 개발했습니다. 이 협력은 Spot 로봇의 이동성과 Gemini Robotics의 정밀한 조작 능력을 활용하여 복잡한 작업을 수행합니다. 사용자들은 Spot 로봇이 수행할 작업을 쉽게 프로그래밍하고 관리할 수 있도록 지원하는 솔루션이 제공됩니다. 로봇이 단순 반복 작업을 넘어 복잡하고 다양한 환경에서 자율적으로 작업을 수행하는 추세가 가속화되고 있음을 보여줍니다. 출처는 Google News AI Search입니다.

### [AI 에이전트의 안전성 강화를 위한 결정론적 가드레일 오픈소스 도구 AG-X가 공개되었습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1sq4ot4/deterministic_vs_probabilistic_guardrails_for)

AG-X는 Python AI 에이전트에 cage assertions 및 cognitive patches를 추가하여 Prompt injection, 비규격 JSON 응답 등의 문제를 해결합니다. (영문 용어: open-source). LLM 없이 json_schema, regex, forbidden_string 엔진을 사용하여 결정론적으로 검증을 수행합니다. 기존 솔루션과 달리 API gateway나 클라우드 계정 없이 로컬에서 작동하며, SQLite에 트레이스를 저장하고 YAML vaccine 파일을 핫 리로드할 수 있습니다. AI 에이전트의 신뢰성과 안정성 확보가 중요해지면서, 예측 불가능한 오류를 줄이고 보안을 강화하는 결정론적 가드레일 솔루션에 대한 수요가 증가하고 있습니다. 출처는 Reddit r/LocalLLaMA입니다.

### [Kernai, 런타임이 실행 프로토콜을 소유하는 새로운 에이전트 런타임으로 소규모 오픈소스 모델의 에이전트 기능 향상](https://www.reddit.com/r/LocalLLaMA/comments/1sq3mcf/small_opensource_models_can_behave_like_real)

Kernai는 모델이 구조화된 블록을 생성하고 커널이 이를 파싱하여 스킬, 프로토콜 호출, 워크플로우를 실행한 후 결과를 다시 주입하는 방식으로 작동합니다. (영문 용어: open-source). 이 접근 방식은 모델에 내장된 Tool Calling 기능이 없어도 에이전트 동작을 훨씬 더 다양한 모델에서 사용할 수 있게 합니다. 작은 오픈소스 모델도 실행 계약이 명확하면 복잡한 시나리오를 처리할 수 있으며, 기존의 큰 모델보다 단계가 많고 신뢰도가 낮을 수 있지만 에이전트로서 기능합니다. 런타임이 실행 프로토콜을 소유하는 방식은 모델의 크기나 Tool Calling 지원 여부에 관계없이 에이전트 기능을 구현할 수 있게 하여, AI 에이전트 개발의 접근성과 유연성을 크게 높입니다. 출처는 Reddit r/LocalLLaMA입니다.

### [AI가 현재 노동 시장에서 어떻게 활용되고 있는지에 대한 Bipartisan Policy Center의 분석이 발표되었습니다.](https://news.google.com/rss/articles/CBMilgFBVV95cUxPZ183djdJLUExQU14UVZKOGNBME1BYjliV2l1SXRyUUxXZl9wNlJrZzJ3dHg0eTJ6Xzl4V1NUY21HWlN1Y3VRYlltU25ydXBDd0ZHN3ZCMTFfRld5TUtha1F1RzRyQ1F1dUJtVEZqNHpFTTluaXgxQl9zS2xDX2xOQmZzM1BZS0JoMVBNRm45eEhBeUxGVHc?oc=5)

Bipartisan Policy Center는 AI가 오늘날 노동력에 어떻게 통합되고 있는지에 대한 보고서를 발행했습니다. 이 보고서는 AI의 다양한 활용 사례와 그 영향을 다룹니다. AI가 현재 여러 산업 분야에서 사용되는 방식에 대한 구체적인 내용을 포함하고 있습니다. AI 기술의 발전과 확산이 노동 시장에 미치는 영향에 대한 정책적 논의가 활발해지고 있음을 보여줍니다. 출처는 Google News AI Search입니다.

### [Google Gemini 앱이 이제 Mac에서도 사용 가능해지며 AI 접근성을 확장합니다.](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPeXdQVmxFWlVnUWE3WWpZZVZ3UURhZUFMalhyOGF5UGYyeVJEQ09ITlVHblh4d0VINjdLb1FLbVRxaXZOOFhhdWlDZGlmOUxlLVBSNEpBbjJyd0NCRFQwVHh6YU5WVU9zWWF0bGMtREdyZXZMSVZkcUozWGFoZWVnNFU3Rmp4XzhpRmk0?oc=5)

Google의 AI 어시스턴트 Gemini 앱이 Mac 기기에서도 공식적으로 출시되었습니다. (영문 용어: blog.google). 사용자들은 이제 Mac에서 Gemini를 통해 텍스트 생성, 정보 요약, 아이디어 구상 등 다양한 AI 기능을 활용할 수 있습니다. Gemini는 Google Workspace 앱과 연동되어 Gmail, Docs 등에서 AI 기능을 직접 사용할 수 있습니다. Google이 Gemini 앱을 Mac으로 확장함으로써, AI 어시스턴트의 접근성을 높이고 더 많은 사용자가 다양한 기기에서 AI를 활용할 수 있도록 지원합니다. 출처는 Google News AI Search입니다.

### [미국 국가안보국(NSA), 블랙리스트에도 불구하고 Anthropic의 Mythos AI 모델 사용 중](https://news.google.com/rss/articles/CBMivwFBVV95cUxPZVQxQUdjUjgtWnUzUnNfXzI5WFdiMXNkOC1qakZhZ0hfMEZvUVBpckJXQWlFTkdKTzljaU1vQm5hSDFOY3ZHc2p3M1pSSVp5enZuS0VfS3RiT3o4MWx4MnE2dkNHaWNDNVZlR0xUZDRpbEc5eW83V3BmQm9CX1JTeWxvdXJubnJwT19lTXJaLUotTzJ6X1ZER0poQ2N5VEMzOUNuWUxJZWxqYnlRVFNjQzJHeUhCalNNY21KMDJLSQ?oc=5)

Axios 보고서에 따르면, 미국 국가안보국(NSA)이 Anthropic의 AI 모델인 Mythos를 사용하고 있는 것으로 드러났습니다. Mythos는 NSA의 블랙리스트에 올라 있음에도 불구하고 사용되고 있습니다. NSA는 Mythos를 사용하여 정보 분석 및 기타 보안 관련 작업을 수행하는 것으로 알려졌습니다. 국가 안보 기관의 AI 기술 도입은 정보 분석 및 사이버 보안 역량을 강화하려는 광범위한 추세를 반영합니다. 출처는 Google News AI Search입니다.

### [AIOSAI의 'AIPass' 레포지토리가 Reddit에서 Multi Agents 시스템으로 주목받고 있습니다.](https://www.reddit.com/r/artificial/comments/1sq6p53/multi_agents)

Reddit r/artificial 커뮤니티에서 'AIPass'라는 GitHub 레포지토리가 소개되었습니다. 해당 레포지토리는 Multi Agents 시스템과 관련된 것으로 보이며 사용자들의 관심을 끌고 있습니다. xNexusReborn 사용자가 이 레포지토리를 공유하며 다른 사용자들의 사용 경험을 문의했습니다. Multi Agents 시스템은 복잡한 AI 작업을 분산 처리하고 효율성을 높이는 데 중요한 기술로 부상하고 있습니다. 출처는 Reddit r/artificial입니다.

### [딥러닝의 과학적 이해를 위한 근본 이론 정립의 중요성 부각](https://www.reddit.com/r/MachineLearning/comments/1sq273c/on_the_path_towards_a_true_science_of_deep)

산업과 학계에 모두 소속된 한 과학자가 약 7년간 머신러닝의 근본적인 과학 이론을 연구해왔음을 밝힘. 딥러닝의 발전을 위해 경험적 접근을 넘어선 과학적 이론 정립의 필요성을 강조함. 현재 딥러닝은 공학적 성과가 뛰어나지만, 그 작동 원리에 대한 깊이 있는 과학적 이해는 부족하다고 지적함. 딥러닝 기술이 빠르게 발전함에 따라, 단순히 성능 개선을 넘어선 근본적인 이론적 토대 마련이 학계와 산업계의 주요 과제로 떠오르고 있음. 출처는 Reddit r/MachineLearning입니다.

### [캐나다 정부, 한 AI 스타트업에 2억 4천만 달러 단일 보조금 지급으로 AI 산업 지원에 대한 논쟁 촉발](https://www.reddit.com/r/artificial/comments/1sq1gda/canada_gave_one_ai_startup_240m_in_a_single_grant)

캐나다 정부가 한 AI 스타트업에 2억 4천만 달러(약 3,300억 원)의 단일 보조금을 지급했습니다. 이는 지난 7년간 107개 AI 기업이 받은 총 보조금의 66%를 넘는 금액입니다. 해당 보조금 지급은 AI 산업 지원 방식과 특정 기업에 대한 과도한 지원에 대한 논란을 불러일으키고 있습니다. 정부의 AI 산업 육성 전략이 소수 대기업 중심이 아닌, 다양한 스타트업 생태계 지원으로 전환되어야 한다는 목소리가 커지고 있습니다. 출처는 Reddit r/artificial입니다.

### [ICLR 2026에서 공개 코드 또는 데이터를 제공하는 논문이 1,200개 이상으로 집계되었습니다.](https://www.reddit.com/r/MachineLearning/comments/1spvoer/1200_iclr_2026_papers_with_public_code_or_data_r)

ICLR 2026에 채택된 5,300개 이상의 논문 중 약 22%에 해당하는 1,200개 논문이 공개 코드, 데이터 또는 데모 링크를 제공합니다. 해당 링크들은 논문 제출 시 제공된 정보에서 직접 추출되었습니다. 코드 링크는 GitHub 또는 공식 사이트와 같은 코드 베이스로 직접 연결됩니다. 이는 머신러닝 연구의 투명성과 재현성(reproducibility)에 대한 중요성이 커지고 있음을 보여줍니다. 출처는 Reddit r/MachineLearning입니다.

### [2026년 1분기 기술 업계에서 약 8만 명의 직원이 해고되었으며, 이 중 거의 절반이 AI로 인한 것으로 나타났습니다.](https://www.reddit.com/r/artificial/comments/1spw2w0/tech_industry_lays_off_nearly_80000_employees_in)

2026년 1분기 동안 기술 산업에서 약 80,000명의 직원이 해고되었습니다. 해고된 직위의 거의 50%가 AI 기술의 발전과 도입으로 인해 발생했습니다. 이는 AI가 일자리 시장에 미치는 영향이 점차 커지고 있음을 보여줍니다. AI 기술의 발전이 기업의 인력 구조조정에 직접적인 영향을 미치고 있으며, 이는 미래 고용 시장의 변화를 예고합니다. 출처는 Reddit r/artificial입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://huggingface.co/papers/2604.14268)

HY-World 2.0은 텍스트, 단일/다중 뷰 이미지, 비디오 등 다양한 입력으로부터 고품질의 3D Gaussian Splatting 장면을 재구성, 생성 및 시뮬레이션하는 멀티모달 월드 모델 프레임워크입니다. (영문 용어: Multi-Modal). 기존 HY-World 1.0의 한계를 넘어, HY-World 2.0은 다양한 입력 모달리티를 받아 3D 세계를 생성하고 재구성하는 문제를 해결합니다. 이 모델은 HY-Pano 2.0을 통한 파노라마 생성, WorldNav를 통한 궤적 계획, WorldStereo 2.0을 통한 세계 확장, WorldMirror 2.0을 통한 세계 구성의 4단계 방법을 통해 고품질의 탐색 가능한 3D Gaussian Splatting 장면을 합성합니다. 또한, WorldLens라는 고성능 3DGS 렌더링 플랫폼을 도입하여 캐릭터 지원을 포함한 3D 세계의 상호작용적 탐색을 가능하게 합니다. 광범위한 실험을 통해 HY-World 2.0이 우수한 성능을 달성함을 입증했습니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-17 기준)에서 확인했습니다.

### 2. [DR^{3}-Eval: Towards Realistic and Reproducible Deep Research Evaluation](https://huggingface.co/papers/2604.14683)

DR³-Eval은 심층 연구 에이전트의 멀티모달, 다중 파일 보고서 생성 능력을 현실적이고 재현 가능한 방식으로 평가하기 위한 벤치마크를 제안합니다. 심층 연구 에이전트(DRAs)는 복잡하고 장기적인 연구 작업을 수행하지만, 동적인 웹 환경과 모호한 작업 정의로 인해 평가가 어렵습니다. 이 연구는 멀티모달, 다중 파일 보고서 생성을 위한 현실적이고 재현 가능한 벤치마크인 DR³-Eval을 제안합니다. DR³-Eval은 실제 사용자 제공 자료와 오픈 웹의 복잡성을 시뮬레이션하는 정적 연구 샌드박스 코퍼스로 구성됩니다. 또한, 정보 회수, 사실 정확도, 인용 범위, 지시 따르기, 깊이 품질을 측정하는 다차원 평가 프레임워크를 도입하여 인간 판단과의 일치성을 검증했습니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-17 기준)에서 확인했습니다.

### 3. [RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework](https://huggingface.co/papers/2604.15308)

RAD-2는 자율주행 모션 플래닝을 위해 확산 모델 기반의 생성자와 RL 최적화된 판별자를 결합한 생성-판별 프레임워크를 제안하여 안정성과 성능을 향상시킵니다. (영문 용어: Generator-Discriminator). 자율주행 모션 플래닝은 미래의 불확실성을 모델링하고 폐쇄 루프 상호작용에서 견고해야 합니다. 기존 확산 기반 플래너는 모방 학습만으로는 불안정성과 교정 피드백 부족 문제를 겪습니다. RAD-2는 확산 기반 생성자가 다양한 궤적 후보를 생성하고, RL로 최적화된 판별자가 장기적인 주행 품질에 따라 이 후보들을 재순위화하여 이러한 문제를 해결합니다. 이 분리된 설계는 고차원 궤적 공간에 희소한 스칼라 보상을 직접 적용하는 것을 피하여 최적화 안정성을 개선합니다. 또한, Temporally Consistent Group Relative Policy Optimization과 On-policy Generator Optimization을 도입하여 RL 학습을 강화하고, 효율적인 대규모 훈련을 위해 BEV-Warp 시뮬레이션 환경을 활용합니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-17 기준)에서 확인했습니다.

### 4. [How to Fine-Tune a Reasoning Model? A Teacher-Student Cooperation Framework to Synthesize Student-Consistent SFT Data](https://huggingface.co/papers/2604.14164)

TESSY 프레임워크는 교사 모델의 추론 능력과 학생 모델의 스타일 일관성을 결합하여 추론 모델의 SFT 성능을 향상시키는 새로운 데이터 합성 방법을 제안합니다. (영문 용어: Fine-Tune, Teacher-Student) (영문 용어: Student-Consistent). 기존에는 강력한 모델이 생성한 합성 데이터를 사용하여 SFT를 수행했지만, Qwen3-8B와 같은 추론 모델에서는 성능 저하를 초래하는 스타일 불일치 문제가 있었습니다. TESSY는 교사-학생 협력 데이터 합성 프레임워크로, 교사 모델과 학생 모델이 스타일 및 비스타일 토큰을 번갈아 생성하게 하여 이 문제를 해결합니다. 이를 통해 교사의 고급 추론 능력과 학생의 스타일 일관성을 모두 갖춘 합성 데이터를 생성합니다. 코드 생성 실험에서 TESSY는 LiveCodeBench-Pro 및 OJBench에서 각각 11.25% 및 6.68%의 성능 향상을 달성했습니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-17 기준)에서 확인했습니다.

### 5. [GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens](https://huggingface.co/papers/2604.15284)

GlobalSplat은 Global Scene Tokens를 활용하여 효율적인 Feed-Forward 3D Gaussian Splatting을 구현하여 연산 오버헤드를 줄이고 추론 속도를 향상시켰습니다. 기존 3D Gaussian Splatting 방식은 로컬하고 휴리스틱 기반의 할당 전략으로 인해 표현의 압축성, 재구성 속도, 렌더링 충실도 사이에서 큰 절충이 필요했습니다. GlobalSplat은 'align first, decode later' 원칙에 기반하여, 다중 뷰 입력을 인코딩하고 명시적인 3D 형상을 디코딩하기 전에 교차 뷰 대응을 해결하는 압축된 전역 잠재 장면 표현을 학습합니다. 이 접근 방식은 사전 학습된 픽셀 예측 백본이나 조밀한 베이스라인의 잠재 특징을 재사용하지 않고도 압축되고 전역적으로 일관된 재구성을 가능하게 합니다. 점진적으로 디코딩 용량을 늘리는 coarse-to-fine 훈련 커리큘럼을 통해 표현의 비대화를 방지합니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-17 기준)에서 확인했습니다.

### 6. [ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack](https://huggingface.co/papers/2509.25843)

ASGuard는 회로 분석과 타겟 미세 조정을 통해 특정 어텐션 헤드를 재조정하여 LLM의 tense-based jailbreaking 공격에 대한 취약한 거부 행동을 완화합니다. (영문 용어: Activation-Scaling). LLM은 안전 정렬에도 불구하고 간단한 언어적 변화로 우회될 수 있는 취약한 거부 행동을 보입니다. 특히, tense jailbreaking은 모델이 유해한 요청을 과거 시제로 바꾸면 종종 수락하는 문제를 드러냅니다. ASGuard는 이러한 특정 취약점을 완화하기 위해, 먼저 회로 분석을 사용하여 tense-changing 공격과 인과적으로 연결된 특정 어텐션 헤드를 식별합니다. 그 다음, tense에 취약한 헤드의 활성화를 재조정하기 위해 정밀한 채널별 스케일링 벡터를 훈련하고, 이를 "예방적 미세 조정"에 적용하여 모델이 더 강력한 거부 메커니즘을 학습하도록 합니다. 이 방법은 4개의 LLM에서 타겟 jailbreaking의 공격 성공률을 효과적으로 줄이면서 일반적인 기능을 보존하고 과도한 거부를 최소화하여 안전과 유용성 사이의 파레토 최적 균형을 달성합니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-17 기준)에서 확인했습니다.

### 7. [HiVLA: A Visual-Grounded-Centric Hierarchical Embodied Manipulation System](https://huggingface.co/papers/2604.14125)

HiVLA는 시각 기반의 계층적 로봇 조작 시스템으로, VLM 플래너와 Diffusion Transformer 액션 전문가를 분리하여 복잡한 조작 작업에서 뛰어난 성능을 보인다. (영문 용어: Visual-Grounded-Centric). 기존의 end-to-end VLA 모델은 미세 조정 시 VLM의 추론 능력이 저하되는 문제가 있었습니다. HiVLA는 이 문제를 해결하기 위해 고수준의 의미론적 계획과 저수준의 모터 제어를 명시적으로 분리하는 계층적 프레임워크를 제안합니다. 고수준에서는 VLM 플래너가 작업 분해 및 시각적 접지를 통해 구조화된 계획을 생성하고, 저수준에서는 cascaded cross-attention 메커니즘을 갖춘 Diffusion Transformer(DiT) 액션 전문가가 이 계획을 물리적 행동으로 변환합니다. 이 분리된 아키텍처는 VLM의 zero-shot 추론 능력을 유지하면서 각 구성 요소의 독립적인 개선을 가능하게 하여, 시뮬레이션 및 실제 환경에서 기존 end-to-end 모델을 능가하는 성능을 보여줍니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-17 기준)에서 확인했습니다.

### 8. [Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems](https://huggingface.co/papers/2604.14228)

이 연구는 Claude Code의 아키텍처를 분석하여, 다섯 가지 핵심 가치와 열세 가지 설계 원칙이 어떻게 특정 구현 선택으로 이어지는지 설명합니다. 이 연구는 Claude Code라는 에이전트 코딩 도구의 포괄적인 아키텍처를 분석합니다. 사용자 대신 셸 명령을 실행하고 파일을 편집하며 외부 서비스를 호출할 수 있는 Claude Code의 TypeScript 소스 코드를 분석하여, 인간의 의사결정 권한, 안전 및 보안, 안정적인 실행, 기능 증폭, 상황 적응성이라는 다섯 가지 핵심 가치를 식별합니다. 이러한 가치들이 13가지 설계 원칙을 거쳐 while-loop 아키텍처, 권한 시스템, 컨텍스트 관리 파이프라인, 확장성 메커니즘 등 구체적인 구현 선택으로 이어지는 과정을 추적합니다. 또한, 유사한 설계 문제를 다르게 해결하는 OpenClaw와의 비교를 통해 배포 컨텍스트에 따른 아키텍처 차이를 보여줍니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-17 기준)에서 확인했습니다.

### 9. [UniDoc-RL: Coarse-to-Fine Visual RAG with Hierarchical Actions and Dense Rewards](https://huggingface.co/papers/2604.14967)

UniDoc-RL은 계층적 액션과 Dense Rewards를 통해 LVLM의 RAG 시스템에서 시각적 검색, 재순위화, 시각적 인식 및 추론을 공동으로 최적화하는 강화 학습 프레임워크를 제안합니다. (영문 용어: Coarse-to-Fine). 기존 Visual RAG 시스템은 복잡한 추론에 필수적인 미세한 시각적 의미를 간과하는 일반적인 검색 신호에 의존하는 한계가 있었습니다. UniDoc-RL은 이러한 문제를 해결하기 위해 LVLM 에이전트가 검색, 재순위화, 능동적인 시각적 인식 및 추론을 공동으로 수행하는 통합 강화 학습 프레임워크를 제안합니다. 이 프레임워크는 시각 정보 획득을 계층적 액션 공간을 가진 순차적 의사결정 문제로 공식화하여, 문서 검색부터 이미지 선택 및 영역 크롭핑까지 시각적 증거를 점진적으로 정제합니다. 또한, 효과적인 종단간 학습을 위해 각 액션에 대한 작업 인식 감독을 제공하는 Dense Multi-Reward 스키마를 도입하여, Group Relative Policy Optimization (GRPO) 기반으로 여러 목표에 맞춰 에이전트 행동을 조정합니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-17 기준)에서 확인했습니다.

### 10. [LeapAlign: Post-Training Flow Matching Models at Any Generation Step by Building Two-Step Trajectories](https://huggingface.co/papers/2604.15311)

LeapAlign은 Flow Matching 모델의 미세 조정을 위한 새로운 방법으로, 긴 생성 궤적을 두 단계로 단축하여 계산 비용을 줄이고 안정적인 그래디언트 전파를 가능하게 합니다. (영문 용어: Post-Training, Two-Step). Flow Matching 모델을 인간 선호도에 맞춰 미세 조정하는 것은 보상 그래디언트를 직접 역전파하는 유망한 방법이지만, 긴 궤적은 막대한 메모리 비용과 그래디언트 폭발을 야기합니다. LeapAlign은 이 문제를 해결하기 위해 긴 궤적을 두 단계로 단축하고, 각 단계에서 여러 ODE 샘플링 단계를 건너뛰어 미래 잠재 변수를 예측합니다. 이를 통해 초기 생성 단계에서도 효율적이고 안정적인 모델 업데이트를 가능하게 하며, Flux 모델 미세 조정 시 최신 GRPO 기반 및 직접 그래디언트 방법보다 우수한 이미지 품질을 달성합니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-17 기준)에서 확인했습니다.
