# IMDIGEST - 2026-04-18

2026-04-18 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-04-18 AI 브리핑입니다. 오늘은 TechCrunch AI, NVIDIA Developer Blog, AWS Machine Learning Blog에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

### [Anthropic, Claude Design 출시로 아이디어를 시각화하는 새로운 AI 도구 선보여](https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals)

Anthropic이 Claude Design을 출시하여 사용자가 Claude를 활용해 프로토타입, 슬라이드, 원페이지 문서 등 다양한 시각 자료를 생성할 수 있게 되었습니다. 이 도구는 디자인 배경이 없는 창업가나 제품 관리자가 아이디어를 쉽게 공유할 수 있도록 돕기 위해 개발되었습니다. 사용자는 원하는 내용을 설명하면 Claude가 초기 버전을 생성하고, 이후 직접 편집하거나 요청하여 시각 자료를 세부적으로 조정할 수 있습니다. AI가 단순 텍스트 생성을 넘어 시각적 콘텐츠 제작 영역으로 확장되며, 전문 디자인 지식 없이도 아이디어를 빠르게 시각화할 수 있는 'AI 기반 디자인 보조 도구'의 중요성이 커지고 있습니다. 출처는 TechCrunch AI입니다.

### [NVIDIA, 로컬 AI 에이전트 구축을 위한 오픈소스 스택 NemoClaw 공개](https://developer.nvidia.com/blog/build-a-secure-always-on-local-ai-agent-with-nvidia-nemoclaw-and-openclaw)

NVIDIA는 OpenClaw와 NVIDIA NemoClaw를 활용하여 안전하고 항상 작동하는 로컬 AI 에이전트를 구축하는 방법을 소개했습니다. (영문 용어: Always-On). NemoClaw는 NVIDIA OpenShell을 오케스트레이션하여 메시징 플랫폼을 AI 코딩 에이전트에 연결하는 자체 호스팅 게이트웨이인 OpenClaw를 실행하는 오픈소스 레퍼런스 스택입니다. 이 스택은 모델 추론부터 안전하고 상호작용적인 에이전트 배포까지 완전한 파이프라인을 제공하며, 가이드 온보딩, 라이프사이클 관리, 이미지 강화 및 버전 관리된 청사진을 포함합니다. AI 에이전트가 질문-답변 시스템을 넘어 파일을 읽고 API를 호출하며 다단계 워크플로우를 구동하는 자율 비서로 진화함에 따라, 데이터 프라이버시 및 제어 문제로 인한 보안 위험이 증가하고 있습니다. 출처는 NVIDIA Developer Blog입니다.

### [Amazon Bedrock에서 Amazon Nova Model Distillation을 활용하여 비디오 시맨틱 검색 의도를 최적화합니다.](https://aws.amazon.com/blogs/machine-learning/optimize-video-semantic-search-intent-with-amazon-nova-model-distillation-on-amazon-bedrock)

AWS는 Amazon Bedrock에서 Model Distillation 기술을 사용하여 대규모 교사 모델(Amazon Nova Premier)의 라우팅 인텔리전스를 소규모 학생 모델(Amazon Nova Micro)로 전송하는 방법을 제시했습니다. 이 접근 방식은 추론 비용을 95% 이상 절감하고 지연 시간을 50% 단축하면서도 미묘한 라우팅 품질을 유지합니다. 기존 Anthropic Claude Haiku 모델은 높은 정확도를 제공하지만, 엔드투엔드 검색 시간을 2-4초로 증가시켜 전체 지연 시간의 75%를 차지했습니다. 기업들이 비디오 콘텐츠의 증가와 함께 복잡한 메타데이터를 효율적으로 검색하고 관리해야 하는 필요성이 커지고 있습니다. 출처는 AWS Machine Learning Blog입니다.

### [AI 기술 발전과 투자 가속화로 인해 AI 업계 내부자와 외부자 간의 격차가 심화되고 있습니다.](https://techcrunch.com/podcast/tokenmaxxing-openais-shopping-spree-and-the-ai-anxiety-gap)

OpenAI는 금융 앱부터 토크쇼까지 다양한 분야의 기업들을 인수하며 사업 확장을 가속화하고 있습니다. 한 신발 회사가 AI 인프라 기업으로 리브랜딩하는 등 전통 산업에서도 AI 전환이 활발합니다. Anthropic은 공개하기에는 너무 강력하다고 주장하는 모델을 개발했지만, 연준 의장 Jerome Powell에게는 시연했습니다. AI 기술의 급격한 발전과 막대한 투자가 이루어지면서 AI 산업의 핵심 플레이어와 일반 대중 간의 정보 및 이해 격차가 커지고 있습니다. 출처는 TechCrunch AI입니다.

### [AWS 마케팅팀이 Agentic AI 솔루션을 활용하여 웹페이지 콘텐츠 게시 시간을 95% 단축했습니다.](https://aws.amazon.com/blogs/machine-learning/from-hours-to-minutes-how-agentic-ai-gave-marketers-time-back-for-what-matters)

AWS 마케팅의 TAA(Technology, AI, and Analytics) 팀은 Gradial과 협력하여 Amazon Bedrock 기반의 Agentic AI 솔루션을 구축했습니다. 이 솔루션은 콘텐츠 게시 워크플로우를 가속화하여 웹페이지 조립 시간을 최대 4시간에서 약 10분으로 단축했습니다. 솔루션은 엔터프라이즈 CMS(Content Management Systems) 전반에 걸쳐 품질 표준을 유지하면서 수동 작업을 줄이고 검토 주기를 단축하며 콘텐츠 품질을 향상시켰습니다. Agentic AI는 마케팅 콘텐츠 제작 및 게시 워크플로우의 비효율성을 해결하여 생산성을 크게 향상시키는 핵심 기술로 부상하고 있습니다. 출처는 AWS Machine Learning Blog입니다.

### [NVIDIA와 Hugging Face, 합성 데이터를 활용한 빠르고 정확한 다국어 OCR 모델 Nemotron OCR v2 공개](https://huggingface.co/blog/nvidia/nemotron-ocr-v2)

NVIDIA와 Hugging Face가 합성 데이터를 이용해 훈련된 다국어 OCR 모델 Nemotron OCR v2를 발표했습니다. Nemotron OCR v2는 6개 언어에 걸쳐 1,200만 개의 합성 훈련 이미지를 사용하여 비영어권 언어에서 NED 점수를 0.56~0.92에서 0.035~0.069로 크게 개선했습니다. 이 모델은 공유 Detection Backbone 아키텍처를 통해 중복 계산을 제거하여 단일 A100 GPU에서 초당 34.7 페이지를 처리하는 빠른 속도를 자랑합니다. 합성 데이터 생성은 실제 데이터 수집 및 라벨링의 한계를 극복하고, 다양한 레이아웃과 엣지 케이스를 제어하여 모델의 일반화 성능을 향상시키는 중요한 방법론으로 부상하고 있습니다. 출처는 Hugging Face Blog입니다.

### [OpenAI, 핵심 사업 집중을 위해 Sora 개발자 Bill Peebles와 과학 연구 책임자 Kevin Weil 등 주요 인력 이탈](https://techcrunch.com/2026/04/17/kevin-weil-and-bill-peebles-exit-openai-as-company-continues-to-shed-side-quests)

OpenAI의 비디오 생성 AI 툴 Sora의 개발자 Bill Peebles와 과학 연구 이니셔티브를 이끌던 Kevin Weil이 회사를 떠났습니다. 이들의 이탈은 OpenAI가 엔터프라이즈 AI와 향후 출시될 "superapp"에 집중하기 위해 "side quests"를 정리하는 과정에서 발생했습니다. Sora는 월 100만 달러의 컴퓨팅 비용 손실로 인해 지난달 서비스가 중단되었으며, OpenAI for Science는 다른 연구팀에 흡수되었습니다. OpenAI가 수익성이 낮거나 핵심 사업과 거리가 있는 프로젝트들을 정리하고, 엔터프라이즈 AI 솔루션과 통합 플랫폼 개발에 역량을 집중하려는 전략적 변화를 보여줍니다. 출처는 TechCrunch AI입니다.

### [Amazon Bedrock, AI 추론 비용에 대한 세분화된 비용 할당 기능 도입](https://aws.amazon.com/blogs/machine-learning/introducing-granular-cost-attribution-for-amazon-bedrock)

Amazon Bedrock이 AI 추론 비용을 호출한 IAM principal(IAM user, role, federated identity 등)에 자동으로 할당합니다. 이 기능은 AWS Billing에 통합되며, 모델에 관계없이 작동하고 기존 워크플로우 변경이 필요 없습니다. 선택적 Cost Allocation Tags를 사용하여 AWS Cost Explorer 및 AWS Cost and Usage Reports (CUR 2.0)에서 팀, 프로젝트 또는 사용자 지정 차원별로 비용을 집계할 수 있습니다. AI 추론 비용이 클라우드 지출에서 상당한 비중을 차지함에 따라, 누가 어떤 비용을 발생시키는지 파악하는 것이 Chargeback, 비용 최적화 및 재무 계획에 필수적입니다. 출처는 AWS Machine Learning Blog입니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [Anthropic, 최신 AI 모델 Claude Opus 4.7 출시](https://news.google.com/rss/articles/CBMicEFVX3lxTFBoQkkwMnB2b0tyeFllX3Iwa2FrRXNZbW5Dem5ERGlLVzFkbGNycUN1UXVEMnhYVlVmaGNTNDZuSTVWZ3d3alpjN29LbkprZV9qTjg1QVFKdURnYk9FYlFTQWFReVRNdEJPaHdTWlhGUTM?oc=5)

Anthropic이 새로운 플래그십 AI 모델인 Claude Opus 4.7을 공개했습니다. Claude Opus 4.7은 이전 버전보다 향상된 성능과 안전 기능을 제공합니다. 사용자들은 Claude Opus 4.7을 통해 더 복잡한 추론과 다국어 처리 능력을 경험할 수 있습니다. 이번 출시는 AI 모델의 성능 경쟁이 심화되고 있음을 보여주며, 특히 안전성과 윤리적 AI 개발에 대한 Anthropic의 노력을 강조합니다. 출처는 Google News AI Search입니다.

### [로컬 LLM이 막혔을 때 온라인 대형 모델에 도움을 요청하는 방법에 대한 논의가 활발합니다.](https://www.reddit.com/r/LocalLLaMA/comments/1soetup/is_there_a_way_for_a_local_model_to_independently)

사용자가 로컬에서 실행되는 모델이 특정 작업, 특히 코딩 관련 문제에 직면했을 때 Claude나 Gemini와 같은 대규모 온라인 모델에 자율적으로 조언을 구할 수 있는지에 대해 질문했습니다. 이는 로컬 모델의 한계를 보완하고 더 복잡한 문제 해결 능력을 향상시키기 위한 아이디어입니다. 현재 이러한 기능을 직접적으로 지원하는 모델이나 프레임워크는 명확히 제시되지 않았습니다. 로컬 LLM의 활용이 증가하면서, 온디바이스 AI의 한계를 극복하고 클라우드 기반 AI의 강점을 결합하려는 시도가 중요해지고 있습니다. 출처는 Reddit r/LocalLLaMA입니다.

### [AI 에이전트의 코드 생성 품질, 최신 정보 반영 여부에 대한 사용자 경험 공유](https://www.reddit.com/r/artificial/comments/1sobysx/what_is_the_current_landscape_on_ai_agents)

Reddit 사용자들은 AI 에이전트가 생성하는 코드의 최신 버전 반영 여부와 품질에 대해 논의하고 있습니다. FastAPI 프로젝트 샘플 요청 시 AI 에이전트가 deprecated된 코드를 제공한 사례가 공유되었습니다. 사용자들은 AI 에이전트에게 특정 프레임워크 버전을 명시해야 하는지, 그리고 '최신 버전 사용'과 같은 지시가 효과적인지에 대해 궁금해하고 있습니다. AI 에이전트의 코드 생성 능력은 개발 생산성 향상에 중요한 역할을 하지만, 최신 기술 및 라이브러리 업데이트를 얼마나 잘 반영하는지가 핵심 과제로 부상하고 있습니다. 출처는 Reddit r/artificial입니다.

### [Google Gemini 앱이 이제 Mac에서도 사용 가능해지며 AI 접근성을 확장합니다.](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPeXdQVmxFWlVnUWE3WWpZZVZ3UURhZUFMalhyOGF5UGYyeVJEQ09ITlVHblh4d0VINjdLb1FLbVRxaXZOOFhhdWlDZGlmOUxlLVBSNEpBbjJyd0NCRFQwVHh6YU5WVU9zWWF0bGMtREdyZXZMSVZkcUozWGFoZWVnNFU3Rmp4XzhpRmk0?oc=5)

Google의 AI 어시스턴트 Gemini 앱이 Mac 기기에서도 공식적으로 출시되었습니다. (영문 용어: blog.google). 사용자들은 이제 Mac에서 Gemini를 통해 텍스트 생성, 정보 요약, 아이디어 구상 등 다양한 AI 기능을 활용할 수 있습니다. Gemini는 Google Workspace 앱과 연동되어 Gmail, Docs 등에서 AI 기능을 직접 사용할 수 있습니다. Google이 Gemini 앱을 Mac으로 확장함으로써, AI 어시스턴트의 접근성을 높이고 더 많은 사용자가 다양한 기기에서 AI를 활용할 수 있도록 지원합니다. 출처는 Google News AI Search입니다.

### [Anthropic이 Claude Design을 출시하며 AI 모델의 디자인 역량을 강화합니다.](https://news.google.com/rss/articles/CBMia0FVX3lxTE9JT2syNlBSbmRUM0xtZzl3bG02dTRicmR2N0J3UDRpQ29zY0tSeEhoUmp5dEJyWmhfY0I2MzVEbjY3NkV4UTJtYzhKbDB6Ri1PSGJDSnJhY3o3T1JfU3FMcEVFUjFjbkNVaGR3?oc=5)

Anthropic이 새로운 AI 모델인 Claude Design을 공개했습니다. Claude Design은 디자인 관련 작업을 수행하고 이해하는 데 특화된 기능을 제공합니다. 이번 출시는 Anthropic의 AI 기술 확장 전략의 일환입니다. AI가 단순 텍스트 생성을 넘어 시각적, 디자인 관련 작업 영역으로 그 활용 범위를 넓히고 있음을 보여줍니다. 출처는 Google News AI Search입니다.

### [Anthropic CEO, 새로운 AI 모델 보안 우려로 백악관 방문](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPZk9iMkZSZEx1YWxvRXFzRm9vYWV4RWRaYlJFWjBYSFF2MHhITy10a0ZfbDNrTnptZDY4UTR6UmJZT2NSanpFSGZsMTJKRUdaRmZyOTVrTTF0Z2lKRXItVXpMNHlaak11aVlZbklIcVkwcWppdWs1T0lyakwxU3VTOFU1b1huWXd1?oc=5)

Anthropic의 CEO가 새로운 AI 모델과 관련된 해킹 우려로 백악관을 방문했습니다. 이번 방문은 AI 기술의 발전과 함께 제기되는 보안 문제에 대한 논의의 일환입니다. Anthropic은 최근 새로운 AI 모델을 발표하며 기술적 진보를 이루었으나, 이에 따른 잠재적 위험도 함께 부각되고 있습니다. AI 기술의 급속한 발전이 국가 안보 및 사이버 보안과 같은 거시적 문제와 직접적으로 연관되고 있음을 보여줍니다. 출처는 Google News AI Search입니다.

### [Anthropic CEO 다리오 아모데이, 백악관 방문으로 AI 규제 논의에 참여](https://news.google.com/rss/articles/CBMimgFBVV95cUxOTGRzSHhnbEhCQjM5UWpyQllSNzBfRWhMdGFPQ2N2VmNDNVh1NFZoVnNqMEFyS19MZkZGTVBKelFuckZEc2x2Z2ZuVnFDallPR3Rmeng0em5tT1kzZC13YXhyZ0xZdlV2N2tJS1RhYVdEbjRPSWRpOTB2NVY1VWhqalZFRHpYMkNJZEs3Y0hXYmxvR2pENURpZnV3?oc=5)

Anthropic의 CEO 다리오 아모데이가 백악관에 도착하여 AI 관련 논의에 참여했습니다. 이번 방문은 AI 기술의 급속한 발전과 함께 정부의 규제 필요성이 대두되는 시점에 이루어졌습니다. AI 기술 개발을 선도하는 기업의 리더가 직접 정부와 소통하며, AI 산업의 미래 방향과 규제 프레임워크 구축에 중요한 영향을 미칠 것으로 예상됩니다. 출처는 Google News AI Search입니다.

### [LLM 에이전트가 자체 시스템 버그를 진단하고 우회하여 문제를 해결했습니다.](https://www.reddit.com/r/MachineLearning/comments/1so4moo/my_agent_diagnosed_a_bug_in_its_own_system_and)

Springdrift 프로젝트의 LLM 에이전트 런타임인 Curragh가 작동 중 writer agent가 등록되지 않은 버그를 발견했습니다. Curragh는 에러 메시지 "[Agent error: Pipeline: agent writer not available]"와 sensorium의 활성 에이전트 목록을 통해 writer agent가 없음을 인지했습니다. 일반적인 세션 기반 에이전트와 달리, Curragh는 진단 도구 호출 없이도 passive context로 라이브 에이전트 명단을 활용하여 문제를 파악했습니다. 이는 LLM 에이전트의 자율적인 문제 해결 능력과 시스템 내구성을 향상시키는 중요한 발전입니다. 출처는 Reddit r/MachineLearning입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://huggingface.co/papers/2604.14268)

HY-World 2.0은 텍스트, 단일/다중 뷰 이미지, 비디오 등 다양한 입력으로부터 고품질의 3D Gaussian Splatting 장면을 재구성, 생성 및 시뮬레이션하는 멀티모달 월드 모델 프레임워크입니다. (영문 용어: Multi-Modal). 기존 HY-World 1.0의 한계를 넘어, HY-World 2.0은 다양한 입력 모달리티를 받아 3D 세계를 생성하고 재구성하는 문제를 해결합니다. 이 모델은 HY-Pano 2.0을 통한 파노라마 생성, WorldNav를 통한 궤적 계획, WorldStereo 2.0을 통한 세계 확장, WorldMirror 2.0을 통한 세계 구성의 4단계 방법을 통해 고품질의 탐색 가능한 3D Gaussian Splatting 장면을 합성합니다. 또한, WorldLens라는 고성능 3DGS 렌더링 플랫폼을 도입하여 캐릭터 지원을 포함한 3D 세계의 상호작용적 탐색을 가능하게 합니다. 광범위한 실험을 통해 HY-World 2.0이 우수한 성능을 달성함을 입증했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 2. [RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework](https://huggingface.co/papers/2604.15308)

RAD-2는 자율주행 모션 플래닝을 위해 확산 모델 기반의 생성자와 RL 최적화된 판별자를 결합한 생성-판별 프레임워크를 제안하여 안정성과 성능을 향상시킵니다. (영문 용어: Generator-Discriminator). 자율주행 모션 플래닝은 미래의 불확실성을 모델링하고 폐쇄 루프 상호작용에서 견고해야 합니다. 기존 확산 기반 플래너는 모방 학습만으로는 불안정성과 교정 피드백 부족 문제를 겪습니다. RAD-2는 확산 기반 생성자가 다양한 궤적 후보를 생성하고, RL로 최적화된 판별자가 장기적인 주행 품질에 따라 이 후보들을 재순위화하여 이러한 문제를 해결합니다. 이 분리된 설계는 고차원 궤적 공간에 희소한 스칼라 보상을 직접 적용하는 것을 피하여 최적화 안정성을 개선합니다. 또한, Temporally Consistent Group Relative Policy Optimization과 On-policy Generator Optimization을 도입하여 RL 학습을 강화하고, 효율적인 대규모 훈련을 위해 BEV-Warp 시뮬레이션 환경을 활용합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 3. [DR^{3}-Eval: Towards Realistic and Reproducible Deep Research Evaluation](https://huggingface.co/papers/2604.14683)

DR³-Eval은 심층 연구 에이전트의 멀티모달, 다중 파일 보고서 생성 능력을 현실적이고 재현 가능한 방식으로 평가하기 위한 벤치마크를 제안합니다. 심층 연구 에이전트(DRAs)는 복잡하고 장기적인 연구 작업을 수행하지만, 동적인 웹 환경과 모호한 작업 정의로 인해 평가가 어렵습니다. 이 연구는 멀티모달, 다중 파일 보고서 생성을 위한 현실적이고 재현 가능한 벤치마크인 DR³-Eval을 제안합니다. DR³-Eval은 실제 사용자 제공 자료와 오픈 웹의 복잡성을 시뮬레이션하는 정적 연구 샌드박스 코퍼스로 구성됩니다. 또한, 정보 회수, 사실 정확도, 인용 범위, 지시 따르기, 깊이 품질을 측정하는 다차원 평가 프레임워크를 도입하여 인간 판단과의 일치성을 검증했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 4. [How to Fine-Tune a Reasoning Model? A Teacher-Student Cooperation Framework to Synthesize Student-Consistent SFT Data](https://huggingface.co/papers/2604.14164)

TESSY 프레임워크는 교사 모델의 추론 능력과 학생 모델의 스타일 일관성을 결합하여 추론 모델의 SFT 성능을 향상시키는 새로운 데이터 합성 방법을 제안합니다. (영문 용어: Fine-Tune, Teacher-Student). 기존에는 강력한 모델이 생성한 합성 데이터를 사용하여 SFT를 수행했지만, Qwen3-8B와 같은 추론 모델에서는 성능 저하를 초래하는 스타일 불일치 문제가 있었습니다. TESSY는 교사-학생 협력 데이터 합성 프레임워크로, 교사 모델과 학생 모델이 스타일 및 비스타일 토큰을 번갈아 생성하게 하여 이 문제를 해결합니다. 이를 통해 교사의 고급 추론 능력과 학생의 스타일 일관성을 모두 갖춘 합성 데이터를 생성합니다. 코드 생성 실험에서 TESSY는 LiveCodeBench-Pro 및 OJBench에서 각각 11.25% 및 6.68%의 성능 향상을 달성했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 5. [ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack](https://huggingface.co/papers/2509.25843)

ASGuard는 회로 분석과 타겟 미세 조정을 통해 특정 어텐션 헤드를 재조정하여 LLM의 tense-based jailbreaking 공격에 대한 취약한 거부 행동을 완화합니다. (영문 용어: Activation-Scaling). LLM은 안전 정렬에도 불구하고 간단한 언어적 변화로 우회될 수 있는 취약한 거부 행동을 보입니다. 특히, tense jailbreaking은 모델이 유해한 요청을 과거 시제로 바꾸면 종종 수락하는 문제를 드러냅니다. ASGuard는 이러한 특정 취약점을 완화하기 위해, 먼저 회로 분석을 사용하여 tense-changing 공격과 인과적으로 연결된 특정 어텐션 헤드를 식별합니다. 그 다음, tense에 취약한 헤드의 활성화를 재조정하기 위해 정밀한 채널별 스케일링 벡터를 훈련하고, 이를 "예방적 미세 조정"에 적용하여 모델이 더 강력한 거부 메커니즘을 학습하도록 합니다. 이 방법은 4개의 LLM에서 타겟 jailbreaking의 공격 성공률을 효과적으로 줄이면서 일반적인 기능을 보존하고 과도한 거부를 최소화하여 안전과 유용성 사이의 파레토 최적 균형을 달성합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 6. [HiVLA: A Visual-Grounded-Centric Hierarchical Embodied Manipulation System](https://huggingface.co/papers/2604.14125)

HiVLA는 시각 기반의 계층적 로봇 조작 시스템으로, VLM 플래너와 Diffusion Transformer 액션 전문가를 분리하여 복잡한 조작 작업에서 뛰어난 성능을 보인다. (영문 용어: Visual-Grounded-Centric). 기존의 end-to-end VLA 모델은 미세 조정 시 VLM의 추론 능력이 저하되는 문제가 있었습니다. HiVLA는 이 문제를 해결하기 위해 고수준의 의미론적 계획과 저수준의 모터 제어를 명시적으로 분리하는 계층적 프레임워크를 제안합니다. 고수준에서는 VLM 플래너가 작업 분해 및 시각적 접지를 통해 구조화된 계획을 생성하고, 저수준에서는 cascaded cross-attention 메커니즘을 갖춘 Diffusion Transformer(DiT) 액션 전문가가 이 계획을 물리적 행동으로 변환합니다. 이 분리된 아키텍처는 VLM의 zero-shot 추론 능력을 유지하면서 각 구성 요소의 독립적인 개선을 가능하게 하여, 시뮬레이션 및 실제 환경에서 기존 end-to-end 모델을 능가하는 성능을 보여줍니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 7. [GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens](https://huggingface.co/papers/2604.15284)

GlobalSplat은 Global Scene Tokens를 활용하여 효율적인 Feed-Forward 3D Gaussian Splatting을 구현하여 연산 오버헤드를 줄이고 추론 속도를 향상시켰습니다. 기존 3D Gaussian Splatting 방식은 로컬하고 휴리스틱 기반의 할당 전략으로 인해 표현의 압축성, 재구성 속도, 렌더링 충실도 사이에서 큰 절충이 필요했습니다. GlobalSplat은 'align first, decode later' 원칙에 기반하여, 다중 뷰 입력을 인코딩하고 명시적인 3D 형상을 디코딩하기 전에 교차 뷰 대응을 해결하는 압축된 전역 잠재 장면 표현을 학습합니다. 이 접근 방식은 사전 학습된 픽셀 예측 백본이나 조밀한 베이스라인의 잠재 특징을 재사용하지 않고도 압축되고 전역적으로 일관된 재구성을 가능하게 합니다. 점진적으로 디코딩 용량을 늘리는 coarse-to-fine 훈련 커리큘럼을 통해 표현의 비대화를 방지합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 8. [UniDoc-RL: Coarse-to-Fine Visual RAG with Hierarchical Actions and Dense Rewards](https://huggingface.co/papers/2604.14967)

UniDoc-RL은 계층적 액션과 Dense Rewards를 통해 LVLM의 RAG 시스템에서 시각적 검색, 재순위화, 시각적 인식 및 추론을 공동으로 최적화하는 강화 학습 프레임워크를 제안합니다. (영문 용어: Coarse-to-Fine). 기존 Visual RAG 시스템은 복잡한 추론에 필수적인 미세한 시각적 의미를 간과하는 일반적인 검색 신호에 의존하는 한계가 있었습니다. UniDoc-RL은 이러한 문제를 해결하기 위해 LVLM 에이전트가 검색, 재순위화, 능동적인 시각적 인식 및 추론을 공동으로 수행하는 통합 강화 학습 프레임워크를 제안합니다. 이 프레임워크는 시각 정보 획득을 계층적 액션 공간을 가진 순차적 의사결정 문제로 공식화하여, 문서 검색부터 이미지 선택 및 영역 크롭핑까지 시각적 증거를 점진적으로 정제합니다. 또한, 효과적인 종단간 학습을 위해 각 액션에 대한 작업 인식 감독을 제공하는 Dense Multi-Reward 스키마를 도입하여, Group Relative Policy Optimization (GRPO) 기반으로 여러 목표에 맞춰 에이전트 행동을 조정합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 9. [Switch-KD: Visual-Switch Knowledge Distillation for Vision-Language Models](https://huggingface.co/papers/2604.14629)

Switch-KD는 Visual-Switch Knowledge Distillation 프레임워크를 통해 Vision-Language Models의 효율적인 지식 증류를 가능하게 하여, 대규모 VLM의 배포 문제를 해결합니다. Vision-Language Models(VLMs)는 뛰어난 성능에도 불구하고 큰 모델 크기로 인해 배포에 어려움이 있습니다. Switch-KD는 이러한 문제를 해결하기 위해 시각-언어 지식 전이를 공유된 텍스트-확률 공간에서 통합하는 새로운 지식 증류 프레임워크를 제안합니다. 이 프레임워크는 학생 모델의 시각적 출력을 교사 모델의 언어 경로로 전환하여 암묵적인 시각 지식 전이를 위한 교차 모달 확률 참조를 구축하는 Visual-Switch Distillation과, 교사와 학생의 분포 구조를 보존하면서 정보성 확률 영역을 적응적으로 정렬하는 Dynamic Bi-directional Logits Difference (DBiLD) loss로 구성됩니다. Switch-KD를 통해 0.5B TinyLLaVA는 3B 교사 모델로부터 풍부한 멀티모달 지식을 효과적으로 증류하여 10개의 멀티모달 벤치마크에서 평균 3.6점의 성능 향상을 달성했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 10. [TRACER: Trace-Based Adaptive Cost-Efficient Routing for LLM Classification](https://huggingface.co/papers/2604.14531)

TRACER는 LLM 분류 작업을 위해 프로덕션 트레이스를 활용하여 ML 서rogate를 훈련하고, 원본 LLM과의 일치도가 특정 임계값을 초과할 때만 서rogate를 활성화하여 비용 효율적인 라우팅을 제공하는 오픈소스 시스템입니다. (영문 용어: Trace-Based, Cost-Efficient). 이 연구는 LLM 분류 작업의 추론 비용을 줄이기 위한 TRACER라는 시스템을 제안합니다. TRACER는 LLM의 프로덕션 로그에서 얻은 입력-출력 쌍을 사용하여 경량 ML 서rogate 모델을 훈련합니다. 이 서rogate는 원본 LLM과의 예측 일치도가 사용자 지정 임계값(α)을 넘을 때만 활성화되어 트래픽의 상당 부분을 처리하며, 이를 통해 LLM 호출 비용을 절감합니다. 또한, TRACER는 서rogate가 어떤 입력 영역을 처리하고 언제 LLM으로 작업을 넘기는지에 대한 해석 가능성 아티팩트를 제공하여 라우팅 경계를 투명하게 만듭니다. 77개 클래스 및 150개 클래스 벤치마크에서 TRACER는 높은 서rogate 커버리지를 달성하며, 특정 경우에는 LLM을 완전히 대체할 수 있음을 보여주었습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.
