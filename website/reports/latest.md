# IMDIGEST - 2026-04-23

2026-04-23 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-04-23 AI 브리핑입니다. 오늘은 OpenAI News, TechCrunch AI, AWS Machine Learning Blog에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

### [OpenAI, 미국 의료 전문가들을 위한 ChatGPT for Clinicians 무료 제공](https://openai.com/index/making-chatgpt-better-for-clinicians)

OpenAI가 미국 내 검증된 의사, 간호사, 약사에게 'ChatGPT for Clinicians'를 무료로 제공합니다. 이 프로그램은 임상 진료, 문서화, 연구 등 의료 분야의 다양한 작업을 지원합니다. 의료 전문가들은 ChatGPT를 통해 환자 치료 및 행정 업무 효율성을 높일 수 있습니다. 의료 분야에서 AI 활용이 증가하는 추세에 맞춰, OpenAI는 의료 전문가들의 AI 접근성을 높여 의료 서비스 혁신을 가속화하고 있습니다. 출처는 OpenAI News입니다.

### [Google, 기업용 AI 에이전트 구축 및 관리 플랫폼 'Gemini Enterprise Agent Platform' 발표](https://techcrunch.com/2026/04/22/google-makes-an-interesting-choice-with-its-new-agent-building-tool-for-enterprises)

Google은 Google Cloud Next 컨퍼런스에서 기업이 AI 에이전트를 대규모로 구축하고 관리할 수 있는 'Gemini Enterprise Agent Platform'을 공개했습니다. (영문 용어: agent-building). 이 플랫폼은 IT 및 기술 팀에 특화되어 있으며, 비즈니스 사용자들은 'Gemini Enterprise app'을 통해 에이전트를 활용하거나 직접 구축할 수 있습니다. Google의 Gemini LLM과 Nano Banana 2 이미지 생성기는 물론, Anthropic의 Claude (Opus, Sonnet, Haiku 포함) 등 다양한 기반 모델을 지원합니다. 기업용 AI 에이전트 시장에서 Amazon Bedrock AgentCore 및 Microsoft Foundry와 경쟁하며, 기업의 AI 도입 가속화를 목표로 합니다. 출처는 TechCrunch AI입니다.

### [AWS Batch와 Parakeet-TDT를 활용하여 대규모 다국어 오디오 전사를 비용 효율적으로 구현하는 방법이 제시되었습니다.](https://aws.amazon.com/blogs/machine-learning/cost-effective-multilingual-audio-transcription-at-scale-with-parakeet-tdt-and-aws-batch)

NVIDIA Parakeet-TDT-0.6B-v3 모델을 AWS Batch와 GPU 가속 인스턴스에 배포하여 대규모 다국어 오디오 전사 비용 효율성을 높였습니다. (영문 용어: Cost-effective). Parakeet-TDT의 Token-and-Duration Transducer 아키텍처는 텍스트 토큰과 지속 시간을 동시에 예측하여 불필요한 처리 과정을 건너뛰고 실시간보다 훨씬 빠른 추론 속도를 제공합니다. Amazon S3에 업로드된 오디오 파일을 자동으로 처리하는 확장 가능한 이벤트 기반 전사 파이프라인 구축 방법을 안내하며, Amazon EC2 Spot Instances 및 buffered streaming inference를 통해 추가 비용 절감 방안을 제시합니다. 대규모 미디어 라이브러리 보관, 컨택 센터 녹음 분석, AI 학습 데이터 준비 등 다양한 분야에서 ASR 서비스의 확장성 및 비용 효율성 문제가 중요해지면서, 이를 해결하기 위한 기술적 접근이 주목받고 있습니다. 출처는 AWS Machine Learning Blog입니다.

### [Google Cloud, AI 칩 시장에서 Nvidia와 경쟁하기 위해 8세대 TPU 8t 및 TPU 8i 공개](https://techcrunch.com/2026/04/22/google-cloud-next-new-tpu-ai-chips-compete-with-nvidia)

Google Cloud는 모델 학습용 TPU 8t와 추론용 TPU 8i 두 가지 새로운 8세대 AI 칩(TPU)을 출시했습니다. 새로운 TPU는 이전 세대 대비 최대 3배 빠른 AI 모델 학습 속도와 80% 향상된 비용 대비 성능을 제공합니다. Google은 100만 개 이상의 TPU를 단일 클러스터로 함께 작동시킬 수 있는 기능을 강조하며, 에너지 효율성과 비용 절감을 목표로 합니다. 클라우드 제공업체들이 AI 워크로드 증가에 따라 Nvidia 의존도를 줄이고 자체 AI 칩 개발을 가속화하는 추세를 보여줍니다. 출처는 TechCrunch AI입니다.

### [Amazon SageMaker AI, 생성형 AI 추론 최적화 추천 기능 도입으로 배포 시간 단축](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-now-supports-optimized-generative-ai-inference-recommendations)

Amazon SageMaker AI가 생성형 AI 모델의 추론 최적화 추천 기능을 지원합니다. 이 기능은 GPU 구성, 최적화 기법, 수동 벤치마킹에 소요되던 시간을 단축하여 모델 배포를 가속화합니다. NVIDIA Dynamo의 모듈형 구성 요소인 NVIDIA AIPerf를 벤치마킹 도구로 활용하여 상세하고 일관된 성능 지표를 제공합니다. 생성형 AI 모델의 프로덕션 배포에 대한 기업들의 수요가 증가함에 따라, 배포 과정의 복잡성과 시간을 줄이는 솔루션의 중요성이 커지고 있습니다. 출처는 AWS Machine Learning Blog입니다.

### [AWS, Amazon Bedrock AgentCore에 새로운 기능을 추가하여 에이전트 개발을 간소화합니다.](https://aws.amazon.com/blogs/machine-learning/get-to-your-first-working-agent-in-minutes-announcing-new-features-in-amazon-bedrock-agentcore)

Amazon Bedrock AgentCore는 에이전트 개발자가 인프라 구축 대신 에이전트 로직에 집중할 수 있도록 돕는 새로운 기능을 발표했습니다. LangGraph, LlamaIndex, CrewAI, Strands Agents 등 기존 프레임워크 및 모델과의 연동을 지원합니다. 에이전트의 오케스트레이션 레이어를 실행하는 데 필요한 컴퓨팅, 샌드박스, 보안 연결, 영구 스토리지, 오류 복구 등의 인프라 구축 과정을 간소화합니다. 이는 AI 에이전트 개발의 진입 장벽을 낮춰 더 많은 개발자가 혁신적인 에이전트 애플리케이션을 신속하게 구축하고 배포할 수 있도록 지원합니다. 출처는 AWS Machine Learning Blog입니다.

### [Google이 Chrome에 AI 기반의 "auto browse" 기능을 도입하여 기업 환경에서 AI 동료처럼 활용할 수 있도록 합니다.](https://techcrunch.com/2026/04/22/google-turns-chrome-into-an-ai-coworker-for-the-workplace)

Google은 Google Cloud Next 행사에서 기업용 Chrome에 Gemini 기반의 "auto browse" 에이전트 기능을 발표했습니다. (영문 용어: co-worker). 이 기능은 Chrome 사용자가 열려 있는 브라우저 탭의 실시간 맥락을 이해하고, 여행 예약, 데이터 입력, 회의 일정 잡기 등 웹 기반 작업을 AI가 처리하도록 돕습니다. 예시로는 Google Doc의 내용을 기반으로 CRM 시스템에 정보 입력, 여러 탭에서 공급업체 가격 비교, 후보자 포트폴리오 요약 등이 있습니다. Google은 가장 많이 사용되는 앱 중 하나인 웹 브라우저에 AI를 통합하여 기업 생산성 도구 시장에서의 경쟁력을 강화하고 있습니다. 출처는 TechCrunch AI입니다.

### [Google 포토의 Auto frame 기능에 AI 기반의 새로운 이미지 재구성 기술이 도입되었습니다.](https://research.google/blog/its-all-about-the-angle-your-photos-re-composed)

Google 포토의 Auto frame 기능에 새로운 이미지 편집 방식이 적용되었습니다. (영문 용어: re-composed). 이 기술은 머신러닝 모델로 장면의 공간적 레이아웃을 이해하고, 생성형 AI를 사용하여 새로운 시점에서 사진을 재구성합니다. 기존 사진 편집 도구와 달리, 사진을 3D 장면으로 해석하여 촬영 후에도 카메라 위치를 변경하는 효과를 낼 수 있습니다. 사용자들이 촬영 후에도 사진의 구도나 시점을 자유롭게 변경할 수 있게 되어, '거의 완벽한' 사진을 더욱 완벽하게 만들 수 있는 가능성을 열었습니다. 출처는 Google Research Blog입니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [Anthropic, 최신 AI 모델 Claude Opus 4.7 출시](https://news.google.com/rss/articles/CBMicEFVX3lxTFBoQkkwMnB2b0tyeFllX3Iwa2FrRXNZbW5Dem5ERGlLVzFkbGNycUN1UXVEMnhYVlVmaGNTNDZuSTVWZ3d3alpjN29LbkprZV9qTjg1QVFKdURnYk9FYlFTQWFReVRNdEJPaHdTWlhGUTM?oc=5)

Anthropic이 새로운 플래그십 AI 모델인 Claude Opus 4.7을 공개했습니다. Claude Opus 4.7은 이전 버전보다 향상된 성능과 안전 기능을 제공합니다. 사용자들은 Claude Opus 4.7을 통해 더 복잡한 추론과 다국어 처리 능력을 경험할 수 있습니다. 이번 출시는 AI 모델의 성능 경쟁이 심화되고 있음을 보여주며, 특히 안전성과 윤리적 AI 개발에 대한 Anthropic의 노력을 강조합니다. 출처는 Google News AI Search입니다.

### [텍스트 임베딩 기반의 LLM 에이전트를 위한 5가지 구성 요소로 이루어진 내재적 호기심 보상 함수가 개발되었습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1st05ix/r_intrinsic_curiosity_on_text_embeddings_a)

기존 LLM 에이전트의 탐색 동기 부족 문제를 해결하기 위해 텍스트 임베딩 공간에서 작동하는 새로운 내재적 호기심(Intrinsic Curiosity) 보상 함수가 고안되었습니다. 이 보상 함수는 예측 오류(prediction error), 학습 진행도(learning progress), 참신성(novelty), Empowerment, 그리고 S(미공개)의 5가지 구성 요소로 이루어져 있습니다. 각 구성 요소는 개별적으로 정규화된 후 합산되어 [0,1] 범위로 tanh-squash됩니다. LLM 에이전트가 단순히 질문에 답하는 것을 넘어, 스스로 탐색하고 학습하며 새로운 지식을 추구하는 자율적인 행동을 유도하는 데 기여할 수 있습니다. 출처는 Reddit r/LocalLLaMA입니다.

### [OpenAI가 ChatGPT에 Workspace Agents를 도입하여 기업 생산성 도구를 통합합니다.](https://news.google.com/rss/articles/CBMic0FVX3lxTE14N1RKNWtPajlOcGJKUUh4V2JpWl83OE1PSHpSOENDSE5scTlyYlhzQi1OZGxKOWc5VjRaY2c4MzNyS0x5azRXUkpxR2FScmVqTGN0LTN0ODEzdS1HZDE4aHhfeHVVbjgtZjZqVVIta3pYbm8?oc=5)

OpenAI가 ChatGPT에 Workspace Agents를 도입했습니다. Workspace Agents는 기업 사용자가 ChatGPT를 통해 Google Drive, Microsoft Outlook, Salesforce 등 다양한 비즈니스 애플리케이션과 상호작용할 수 있도록 합니다. 이 기능은 사용자가 일상적인 업무를 자동화하고 데이터에 더 쉽게 접근할 수 있도록 돕습니다. 이는 ChatGPT가 단순한 챗봇을 넘어 기업 생산성 플랫폼으로 확장하려는 OpenAI의 전략을 보여줍니다. 출처는 Google News AI Search입니다.

### [AI 과학자, 과학적 추론 없이 결과 도출: 연구 결과에 따르면 AI는 증거를 무시하고 신념을 업데이트하지 않는 경향이 있습니다.](https://www.reddit.com/r/MachineLearning/comments/1st02fw/ai_scientists_produce_results_without_reasoning)

연구에 따르면 AI 과학자는 25,000번의 실험 중 68%에서 증거를 수집한 후 이를 완전히 무시했습니다. AI는 71%의 경우 신념을 전혀 업데이트하지 않았으며, 모순되는 데이터에 직면했을 때 가설을 수정한 경우는 26%에 불과했습니다. 인간 과학자와 달리 AI는 문제 유형에 관계없이 동일한 '규율 없는 루프'를 반복적으로 실행합니다. 이는 AI 연구 에이전트 개발의 근본적인 한계를 보여주며, 현재의 접근 방식으로는 진정한 과학적 추론 능력을 갖추기 어렵다는 것을 시사합니다. 출처는 Reddit r/MachineLearning입니다.

### [HydraLM, 긴 컨텍스트 추론에서 획기적인 디코딩 속도와 메모리 효율성을 달성했습니다.](https://www.reddit.com/r/MachineLearning/comments/1sszogy/hydralm_22_faster_decoding_and_16_smaller_state)

HydraLM은 1M 토큰 테스트에서 90% 깊이에 있는 사실도 1.00의 검색 정확도를 보였습니다. (영문 용어: long-context). 추론 시 최대 1.8배 빠른 speculative decoding을 제공하며, 99.8%의 FLOP 절감 효과를 보고했습니다. 긴 컨텍스트에서 22배 빠른 디코딩과 16배 작은 state memory를 통해 상당한 성능 향상을 이루었습니다. 대규모 언어 모델(LLM)의 긴 컨텍스트 처리 능력은 AI 애플리케이션의 복잡성과 효율성을 크게 향상시킬 수 있습니다. 출처는 Reddit r/MachineLearning입니다.

### [Google Gemini 앱이 이제 Mac에서도 사용 가능해지며 AI 접근성을 확장합니다.](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPeXdQVmxFWlVnUWE3WWpZZVZ3UURhZUFMalhyOGF5UGYyeVJEQ09ITlVHblh4d0VINjdLb1FLbVRxaXZOOFhhdWlDZGlmOUxlLVBSNEpBbjJyd0NCRFQwVHh6YU5WVU9zWWF0bGMtREdyZXZMSVZkcUozWGFoZWVnNFU3Rmp4XzhpRmk0?oc=5)

Google의 AI 어시스턴트 Gemini 앱이 Mac 기기에서도 공식적으로 출시되었습니다. (영문 용어: blog.google). 사용자들은 이제 Mac에서 Gemini를 통해 텍스트 생성, 정보 요약, 아이디어 구상 등 다양한 AI 기능을 활용할 수 있습니다. Gemini는 Google Workspace 앱과 연동되어 Gmail, Docs 등에서 AI 기능을 직접 사용할 수 있습니다. Google이 Gemini 앱을 Mac으로 확장함으로써, AI 어시스턴트의 접근성을 높이고 더 많은 사용자가 다양한 기기에서 AI를 활용할 수 있도록 지원합니다. 출처는 Google News AI Search입니다.

### [Anthropic이 Claude Code for Healthcare를 통해 의료 분야 AI 활용 사례를 제시합니다.](https://news.google.com/rss/articles/CBMiogFBVV95cUxOc29ONWJhLTNhaFI3TDZhZzVFVE9KQzlDZ01NQ3k1ZmxqZ25wYzRVZm9nc2MwQUJCWXFiVlhXZUdidEhzUUtEQ3pBTk44QTUzMmhSbnA5Zmt6TzFWSVQ1NkdzNHpoalNkbWROUlV4OUpGMTJrclJBQ0pZd1otZlF3cERIc2h1c1lBRktyVEZWd0RUMk44aVlVUW1rd3JPTk0xeWc?oc=5)

Anthropic은 Claude Code for Healthcare를 공개하며 의사들이 AI를 활용하는 구체적인 방법을 소개했습니다. 이 이니셔티브는 의료 전문가들이 AI를 통해 진료 효율성을 높이고 환자 치료를 개선할 수 있도록 돕는 데 중점을 둡니다. 의료 분야에서 AI를 활용한 코드 개발 및 적용 사례를 공유하여 실제적인 도움을 제공합니다. 의료 분야에서 AI 도입이 가속화되면서, Anthropic과 같은 선도 기업들이 특정 산업에 특화된 AI 솔루션과 활용 가이드를 제공하는 추세가 강화되고 있습니다. 출처는 Google News AI Search입니다.

### [구글이 엔터프라이즈 수익 창출 전략의 핵심으로 AI 에이전트를 내세우고 있습니다.](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNaC1SX002a0pCeURJUGFrcmxHQmNlM2k2dldpYVFzTDgxQjhlaWp4NmJja1FHNS1sdkt3SzFFcWxpVlJJekVQUFdsTFJob3lLb1h1Rk1XSXpDRGR0VXVZWDI3UUhWVnFBelV4SVNYSVRtNkVta3dIMFNucGZCMGdSaERNTkU3Rk5TeTlpT1FsQ29PaXdwRDlIU2ZtamVSNGZYOFU0ZDdlMUU?oc=5)

구글은 AI 에이전트를 통해 기업 고객을 위한 맞춤형 솔루션 제공을 강화하고 있습니다. (영문 용어: money-making). 이는 기업의 복잡한 작업을 자동화하고 효율성을 높이는 데 중점을 둡니다. 구글 클라우드 서비스를 통해 AI 에이전트 기능을 제공하여 기업의 디지털 전환을 지원합니다. AI 에이전트는 단순한 챗봇을 넘어 자율적으로 작업을 수행하고 의사결정을 내리는 방향으로 발전하며, 기업 생산성 향상의 핵심 동력이 되고 있습니다. 출처는 Google News AI Search입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [Tstars-Tryon 1.0: Robust and Realistic Virtual Try-On for Diverse Fashion Items](https://huggingface.co/papers/2604.19748)

Tstars-Tryon 1.0은 상업적 규모의 가상 피팅 시스템으로, 다양한 패션 아이템에 대해 견고하고 사실적인 Try-On 결과를 제공하며 실시간 성능을 달성합니다. 기존 가상 Try-On 방식은 복잡한 실제 환경의 요구사항을 충족하는 데 어려움이 있었습니다. Tstars-Tryon 1.0은 통합 시스템 설계와 다단계 훈련 패러다임을 통해 이러한 문제를 해결합니다. 이 시스템은 극한의 포즈, 조명 변화, 모션 블러와 같은 어려운 조건에서도 높은 성공률을 유지하며, 의류의 질감과 재료 특성을 충실히 보존하는 사실적인 결과를 생성합니다. 또한, 8가지 패션 카테고리에 걸쳐 유연한 다중 이미지 구성을 지원하고, 상업적 배포를 위한 추론 속도 최적화를 통해 실시간에 가까운 생성을 제공합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 2. [CoInteract: Physically-Consistent Human-Object Interaction Video Synthesis via Spatially-Structured Co-Generation](https://huggingface.co/papers/2604.19636)

CoInteract는 Diffusion Transformer 기반의 프레임워크로, Human-Aware Mixture-of-Experts와 Spatially-Structured Co-Generation을 통해 물리적으로 일관된 사람-객체 상호작용(HOI) 비디오를 합성합니다. (영문 용어: Physically-Consistent, Human-Object). 기존 확산 모델은 사람-객체 상호작용 비디오 합성 시 손이나 얼굴과 같은 민감한 영역의 구조적 안정성과 물리적 접촉의 타당성(예: 손과 객체의 상호 관통 방지)에서 실패하는 경우가 많았습니다. CoInteract는 이러한 문제를 해결하기 위해 Diffusion Transformer 백본에 두 가지 보완적인 디자인을 도입합니다. 첫째, Human-Aware Mixture-of-Experts를 통해 토큰을 영역별 전문가에게 라우팅하여 미세한 구조적 충실도를 향상시킵니다. 둘째, Spatially-Structured Co-Generation이라는 듀얼 스트림 훈련 패러다임을 제안하여 RGB 외형 스트림과 보조 HOI 구조 스트림을 공동으로 모델링하여 상호작용 기하학적 사전 지식을 주입합니다. 이를 통해 CoInteract는 구조적 안정성, 논리적 일관성 및 상호작용 현실성에서 기존 방법보다 뛰어난 성능을 보여줍니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 3. [AgentSPEX: An Agent SPecification and EXecution Language](https://huggingface.co/papers/2604.13346)

AgentSPEX는 LLM 에이전트 워크플로우를 위한 명시적인 제어 흐름과 모듈형 구조를 제공하는 도메인 특화 언어 및 프레임워크를 제안합니다. 기존 LLM 에이전트 시스템은 반응형 프롬프팅에 의존하여 제어 흐름과 중간 상태가 암묵적이며 에이전트 제어가 어려웠습니다. LangGraph나 DSPy와 같은 오케스트레이션 프레임워크는 Python 코드와 워크플로우 로직이 강하게 결합되어 유지보수 및 수정이 어렵다는 문제가 있었습니다. AgentSPEX는 명시적인 제어 흐름, 모듈형 구조, 타입이 지정된 단계, 분기 및 루프, 병렬 실행, 재사용 가능한 서브모듈을 지원하여 이러한 문제를 해결합니다. 이를 통해 연구 및 과학 연구를 위한 에이전트를 제공하고 7가지 벤치마크에서 평가되었으며, 사용자 연구를 통해 기존 프레임워크보다 해석 가능하고 접근하기 쉬운 워크플로우 작성 패러다임을 제공함을 입증했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 4. [AnyRecon: Arbitrary-View 3D Reconstruction with Video Diffusion Model](https://huggingface.co/papers/2604.19747)

AnyRecon은 비디오 Diffusion 모델을 활용하여 임의의 희소한 입력으로부터 확장 가능한 3D 재구성을 가능하게 합니다. (영문 용어: Arbitrary-View). 희소한 뷰 3D 재구성은 캐주얼한 캡처로부터 장면을 모델링하는 데 중요하지만, 기존의 비생성적 방법론은 어려움이 있었습니다. AnyRecon은 영구적인 장면 메모리와 기하학적 인식을 활용한 컨디셔닝을 통해 이러한 문제를 해결합니다. 이 방법은 4단계 Diffusion distillation과 context-window sparse attention을 결합하여 효율성을 높이고, 불규칙한 입력, 큰 시점 차이, 긴 궤적에 걸쳐 강력하고 확장 가능한 재구성을 보여줍니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 5. [TEMPO: Scaling Test-time Training for Large Reasoning Models](https://huggingface.co/papers/2604.19295)

TEMPO는 대규모 추론 모델의 Test-time training(TTT) 시 발생하는 성능 정체 및 다양성 저하 문제를 해결하기 위해 정책 개선과 비평가 재보정을 번갈아 수행하는 프레임워크를 제안합니다. 기존의 Test-time training(TTT) 방식은 추론 시점에 모델 파라미터를 조정하여 성능을 향상시키지만, 자체 생성 보상 신호의 드리프트로 인해 성능 정체와 다양성 저하가 빠르게 발생합니다. TEMPO는 이러한 문제를 해결하기 위해 레이블 없는 질문에 대한 정책 개선과 레이블이 지정된 데이터셋에 대한 주기적인 비평가 재보정을 번갈아 수행하는 EM(Expectation-Maximization) 알고리즘 기반 프레임워크를 제안합니다. 이 교대 절차를 통해 이전 방법들이 중요한 재보정 단계를 생략한 불완전한 변형이었음을 밝히고, 재보정 단계를 다시 도입함으로써 ELBO(Evidence Lower Bound)를 강화하여 지속적인 성능 향상을 가능하게 합니다. 다양한 모델(Qwen3, OLMO3)과 추론 작업에서 TEMPO는 OLMO3-7B의 AIME 2024 성능을 33.0%에서 51.1%로, Qwen3-14B의 성능을 42.3%에서 65.8%로 향상시키면서 높은 다양성을 유지합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 6. [PlayCoder: Making LLM-Generated GUI Code Playable](https://huggingface.co/papers/2604.19742)

PlayCoder는 LLM이 생성한 GUI 코드의 논리적 정확성을 향상시키기 위해 다중 에이전트 접근 방식을 사용하는 프레임워크를 제안합니다. (영문 용어: LLM-Generated). 대규모 언어 모델(LLM)은 GUI 애플리케이션, 특히 게임 생성에서 논리적 오류를 자주 발생시킵니다. 이 문제를 해결하기 위해 PlayEval 벤치마크와 PlayCoder 프레임워크가 개발되었습니다. PlayCoder는 LLM 기반 에이전트인 PlayTester를 활용하여 GUI 애플리케이션의 상호작용 흐름과 UI 로직을 평가하고, 반복적인 수정을 통해 기능적 정확성을 개선합니다. 이를 통해 기존 LLM의 낮은 Play@k 점수를 극복하고 논리적으로 올바른 GUI 애플리케이션 생성을 목표로 합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 7. [ShadowPEFT: Shadow Network for Parameter-Efficient Fine-Tuning](https://huggingface.co/papers/2604.19254)

ShadowPEFT는 깊이 공유 섀도우 모듈을 통해 레이어 수준의 정제를 수행하여 기존 LoRA와 같은 저랭크 적응 방식보다 적은 계산 오버헤드로 경쟁력 있는 성능을 제공하는 PEFT 프레임워크입니다. 기존 PEFT(Parameter-Efficient Fine-Tuning) 방식인 LoRA는 개별 가중치에 독립적인 저랭크 섭동을 삽입하여 적응을 수행했지만, 이는 지역적인 파라미터화를 초래했습니다. ShadowPEFT는 이러한 문제를 해결하기 위해 깊이 공유 섀도우 모듈을 통해 레이어 수준의 정제를 수행하는 중앙 집중식 PEFT 프레임워크를 제안합니다. 이 방식은 각 트랜스포머 레이어에서 병렬 섀도우 상태를 유지하고 이를 반복적으로 발전시켜 더 풍부한 은닉 상태를 만듭니다. 결과적으로 ShadowPEFT는 LoRA 및 DoRA와 유사한 학습 가능한 파라미터 예산 내에서 생성 및 이해 벤치마크에서 동등하거나 더 우수한 성능을 보여주었습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 8. [Chat2Workflow: A Benchmark for Generating Executable Visual Workflows with Natural Language](https://huggingface.co/papers/2604.19667)

Chat2Workflow는 자연어로부터 실행 가능한 시각적 워크플로우를 생성하는 벤치마크와 에이전트 프레임워크를 제시하여, 산업 수준의 자동화 달성에 있어 LLM의 한계를 드러냅니다. 실행 가능한 시각적 워크플로우는 산업 배포에서 신뢰성과 제어 가능성을 제공하지만, 현재는 수동으로 구축되어 비용과 시간이 많이 소요됩니다. 이 연구는 대규모 언어 모델이 이러한 다중 라운드 상호작용 프로세스를 자동화할 수 있는지 연구하기 위해 Chat2Workflow 벤치마크를 도입했습니다. 이 벤치마크는 실제 비즈니스 워크플로우를 기반으로 하며, Dify 및 Coze와 같은 플랫폼에 직접 배포 가능한 워크플로우 생성을 목표로 합니다. 실험 결과, 최신 LLM은 높은 수준의 의도는 파악하지만, 복잡하거나 변경되는 요구사항 하에서는 정확하고 안정적인 실행 가능한 워크플로우를 생성하는 데 어려움을 겪는 것으로 나타났습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 9. [AJ-Bench: Benchmarking Agent-as-a-Judge for Environment-Aware Evaluation](https://huggingface.co/papers/2604.18240)

AJ-Bench는 Agent-as-a-Judge의 환경 인지 평가 능력을 체계적으로 측정하기 위한 벤치마크를 제시합니다. (영문 용어: Environment-Aware). 기존 LLM-as-a-Judge 모델은 복잡한 환경에서 에이전트 행동을 검증하는 데 한계가 있었습니다. 이 연구는 Agent-as-a-Judge가 환경 및 도구와 상호작용하여 검증 가능한 증거를 확보하는 능력을 평가하기 위해 AJ-Bench 벤치마크를 도입했습니다. AJ-Bench는 검색, 데이터 시스템, GUI 세 가지 도메인에 걸쳐 155개 작업과 516개의 주석이 달린 궤적을 포함하며, 정보 획득, 상태 검증, 프로세스 검증 능력을 평가합니다. 실험 결과, LLM-as-a-Judge 기준선보다 일관된 성능 향상을 보였지만, 에이전트 기반 검증에는 여전히 많은 과제가 남아 있음을 보여주었습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 10. [Dual-View Training for Instruction-Following Information Retrieval](https://huggingface.co/papers/2604.18845)

Dual-View Training은 polarity reversal 기반의 데이터 합성 전략을 통해 Instruction-Following Information Retrieval 시스템의 지시 준수 능력을 45% 향상시킵니다. 기존 검색 시스템은 주로 의미론적 관련성에 초점을 맞춰 쿼리 관련 문서와 지시 준수 문서 간의 구분을 어려워했습니다. 이 연구는 polarity reversal을 활용한 dual-view 데이터 합성 전략을 제안합니다. 이는 LLM을 사용하여 주어진 쿼리, 지시 준수 문서, 그리고 지시 위반 문서에 대해 두 문서의 관련성 레이블을 뒤바꾸는 보완적인 지시를 생성합니다. 이러한 방식으로 동일한 문서 쌍을 보완적인 지시 하에 제시함으로써, 검색 모델이 고정된 주제 단서에 의존하지 않고 지시를 통해 후보 문서를 재고하도록 훈련시킵니다. 이 방법은 FollowIR 벤치마크에서 45%의 성능 향상을 달성하며, 유사하거나 더 큰 규모의 범용 임베딩 모델을 능가합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.
