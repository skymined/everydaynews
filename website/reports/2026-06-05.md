# IMDIGEST - 2026-06-05

> 2026-06-05 KST 기준 수집. AI 제품, 연구, 인프라, 커뮤니티 신호를 짧게 읽히는 브리핑으로 정리했습니다.

2026-06-05 AI 브리핑입니다. 오늘은 AWS Machine Learning Blog, TechCrunch AI, TechCrunch AI에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 브리핑 노트

- **핵심 흐름:** AWS Machine Learning Blog, TechCrunch AI, TechCrunch AI에서 확인된 제품, 연구, 인프라 변화를 먼저 배치했습니다.
- **현장 신호:** 커뮤니티와 검색에서 함께 떠오른 항목 11개를 별도 섹션으로 묶었습니다.
- **논문 큐:** Hugging Face 인기 논문 10편을 방법과 의미 중심으로 압축했습니다.

## 주요 뉴스

### [NVIDIA Nemotron 3 Ultra가 Amazon SageMaker JumpStart에서 사용 가능해졌다](https://aws.amazon.com/blogs/machine-learning/nvidia-nemotron-3-ultra-now-available-on-amazon-sagemaker-jumpstart)

- **핵심:** NVIDIA의 새로운 모델인 Nemotron 3 Ultra가 Amazon SageMaker JumpStart에서 이용할 수 있게 되었다. 이 모델은 550억 개의 총 파라미터와 55억 개의 활성 파라미터로 구성되어 있으며, NVFP4 정밀도를 지원한다. Nemotron 3 Ultra는 장기적인 자율 에이전트 작업을 위한 최적화된 모델로서, 기존 모델 대비 5배 더 빠른 추론 속도와 최대 30% 저렴한 비용을 제공한다.
- **맥락:** Nemotron 3 Ultra는 장기적인 자율 에이전트 작업에 특화된 모델로서, AI 분야에서의 효율성과 비용 효과를 크게 향상시킬 것으로 기대된다.
- **출처:** AWS Machine Learning Blog
- **키워드:** `nvidia` · `nemotron-3-ultra` · `sagemaker-jumpstart`

### [헬로 로봇, 실내에서 사용 가능한 Stretch 4세대 출시](https://techcrunch.com/2026/06/04/is-silicon-valley-ready-to-put-robots-in-peoples-homes-hello-robot-is)

- **핵심:** 헬로 로봇은 실내에서 작동하는 Stretch 4세대를 지난 달에 발표했습니다. Stretch는 인간형 외관을 갖추고 있지만, 팔이 장착된 기계식 머리와 휠 기반의 이동 시스템을 가지고 있습니다. 헬로 로봇은 실내에서 실제 사람들과 함께 일할 수 있는 로봇 개발에 중점을 두고 있습니다.
- **맥락:** Stretch는 AI 기술 발전에도 불구하고 아직 부족한 훈련 데이터 문제를 해결하기 위해 실제 환경에서의 배포가 필요하다는 트렌드를 보여줍니다.
- **출처:** TechCrunch AI
- **키워드:** `Stretch` · `헬로 로봇` · `실내 로봇`

### [Airbnb의 Brian Chesky CEO, 새로운 AI 연구소 설립 계획](https://techcrunch.com/2026/06/04/airbnbs-brian-chesky-plans-to-launch-a-new-ai-lab)

- **핵심:** Airbnb의 Brian Chesky CEO가 자체 AI 연구소 설립을 준비 중이다. 이번 움직임은 기존 AI 모델 활용에 머무르지 않고 사용자 인터랙션과 디자인 중심의 자체 연구 역량을 키우려는 시도로 읽힌다.
- **맥락:** 플랫폼 기업들이 외부 모델 연동을 넘어 자체 AI 연구 조직을 갖추려는 경쟁이 더 선명해지고 있다.
- **출처:** TechCrunch AI
- **키워드:** `airbnb` · `ai lab` · `brian chesky`

### [Apple, Poke가 메시지 비즈니스 플랫폼에 첫 AI 에이전트로 승인](https://techcrunch.com/2026/06/04/apple-approves-poke-as-the-first-ai-agent-on-its-messages-for-business-platform)

- **핵심:** Poke는 Apple의 Messages for Business 플랫폼에서 처음으로 승인받은 AI 에이전트입니다. Poke는 사용자가 텍스트 메시지처럼 간단하게 AI를 활용할 수 있도록 설계되었습니다. Poke는 스마트홈 제어, 일정 관리 등 다양한 기능을 제공하며, 약 1억 개의 메시지를 전송했습니다.
- **맥락:** 이러한 승인은 Apple이 비즈니스와 소비자 간의 텍스트 메시지 통신에 AI를 통합하려는 노력의 첫 단계입니다.
- **출처:** TechCrunch AI
- **키워드:** `apple` · `ai agent` · `messages for business` · `poke`

### [스마트폰 카메라로 심장 건강 모니터링 가능](https://research.google/blog/towards-passive-heart-health-monitoring-via-smartphone-camera)

- **핵심:** Google Research가 스마트폰의 전면 카메라를 이용해 사용자의 심박수와 휴식 시 심박수를 측정하는 연구 시스템을 발표했습니다. 이 시스템은 사용자가 평소에 스마트폰을 사용할 때 얼굴 영상을 기록하고 이를 통해 심장 건강을 모니터링합니다.
- **맥락:** 이 기술은 저자원 환경이나 심장질환 위험이 높은 사람들에게도 접근성을 제공하며, 웨어러블 디바이스를 대체하거나 보완할 수 있습니다.
- **출처:** Google Research Blog
- **키워드:** `heart rate` · `smartphone camera` · `deep learning` · `health monitoring`

## 커뮤니티 시그널

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목만 따로 모았습니다.

### [AMD FX-8350 CPU와 Python 스크립트로 ARC-AGI-3에서 4.76% 성과 달성](https://www.reddit.com/r/MachineLearning/comments/1tx6g3i/scrap_the_llms_scoring_476_on_the_brand_new_arc3)

- **핵심:** 2012년 출시된 AMD FX-8350 CPU와 2014년 NVIDIA GTX 970 GPU를 사용해 ARC-AGI-3 테스트에서 4.76%의 점수를 획득. LLM이나 트랜스포머 네트워크 없이 순수한 Python 스크립트만으로 성과를 내는 실험 진행.
- **맥락:** 대규모 AI 모델과 고성능 하드웨어에 의존하지 않고도 효과적인 결과를 얻을 수 있다는 새로운 접근법이 주목받음.
- **출처:** Reddit r/MachineLearning
- **키워드:** `ARC-AGI-3` · `LLM` · `Python 스크립트` · `AMD FX-8350`

### [로컬 모델 성능 평가 방법론 제안](https://www.reddit.com/r/LocalLLaMA/comments/1tx2und/benchmarking_local_models)

- **핵심:** 연구자가 로컬 모델을 위한 사용자 정의 워크플로를 평가하는 방법에 대해 질문. 사용자의 개인화된 또는 회사별 특화된 작업 흐름에 대한 벤치마크 필요성 강조.
- **맥락:** 개인화 및 기업 맞춤형 모델 성능 테스트의 중요성이 증가함.
- **출처:** Reddit r/LocalLLaMA
- **키워드:** `로컬모델` · `벤치마크` · `사용자정의`

### [에어비앤비의 브라이언 체스키가 새로운 AI 연구소를 설립할 예정](https://news.google.com/rss/articles/CBMijAFBVV95cUxPRS1vWHRMRUR6RDBXUzFRc2xUSnF4QXpKMUIxajI0eFNRYndvS1lEMzNsYVlTR1FrZzJCdXdjYld0ZDA2Si1jSFQ1Vkp3TzRZS1E4ZkYycEpCUG4xOGcybGVDRHdyMW1qeHJCb18yRV9BeHZERjhybUJFTFNYWi1WTTNCQ2VRYU9Ia2VtNg?oc=5)

- **핵심:** 브라이언 체스키는 에어비앤비에서 새로운 AI 연구소를 설립할 계획을 밝혔다. 이 연구소는 에어비앤비의 기술 혁신과 서비스 향상을 목표로 한다.
- **맥락:** AI 기술의 발전에 따른 업계 경쟁 심화와 관련된 동향을 반영한다.
- **출처:** Google News AI Search
- **키워드:** `에어비앤비` · `브라이언 체스키` · `AI 연구소`

### [LLM 신뢰성 라이브러리 개발로 추론 비용 절반으로 줄여](https://www.reddit.com/r/MachineLearning/comments/1twtdob/we_built_a_sourceavailable_llm_reliability)

- **핵심:** 신뢰성 기술을 통합한 LLM 라이브러리를 구축하여 추론 비용을 절반으로 줄임. (영문 용어: source-available). 28가지 신뢰성 기법과 세 가지 적응형 라우터를 단일 API로 통합하였음.
- **맥락:** LLM의 정확성을 향상시키면서 비용을 절감할 수 있는 획기적인 접근 방식을 제공함으로써 연구 및 개발에 큰 도움이 됨.
- **출처:** Reddit r/MachineLearning
- **키워드:** `LLM` · `신뢰성 라이브러리` · `추론 비용` · `적응형 라우터`

### [Reddit에서 LLM 구축 워크숍 영상 공유](https://www.reddit.com/r/LocalLLaMA/comments/1tx7gzu/hi_reddit_i_posted_my_build_your_own_llm_workshop)

- **핵심:** Reddit r/LocalLLaMA에 GPT2와 Qwen3.6 스타일의 대규모 언어 모델(LLM)을 직접 만드는 워크숍 동영상이 게시되었다. 워크숍은 기계 학습 기본, 딥 뉴럴 네트워크, 트랜스포머 아키텍처 등 다양한 주제를 다룬다.
- **맥락:** LLM 구축에 대한 접근성을 높여 개발자 커뮤니티에서의 협업과 지식 공유가 활성화될 것으로 기대된다.
- **출처:** Reddit r/LocalLLaMA
- **키워드:** `LLM` · `워크숍` · `GPT2` · `Qwen3.6`

### [Sam Altman 등 AI 업계 리더들이 생물 무기 방지 법안 촉구 서명](https://www.reddit.com/r/artificial/comments/1tx7brf/sam_dario_and_demis_hassabis_have_signed_a_joint)

- **핵심:** OpenAI의 Sam Altman, Anthropic의 Dario Amodei, 그리고 Google DeepMind의 Demis Hassabis가 공동으로 생물무기를 막는 법률 제정을 요구하는 편지를 작성했다. 이 편지는 회사들이 합성 DNA와 RNA를 주문할 때 안전장치를 필요로 한다고 주장하며, 의회에 제출되었다.
- **맥락:** AI 업계 리더들은 생물학적 위협을 줄이는 데 기술의 역할이 중요하다는 인식이 확산되고 있다.
- **출처:** Reddit r/artificial
- **키워드:** `biosecurity` · `synthetic biology` · `ai ethics`

### [그래프 에이전트를 활용한 지식 그래프의 상호작용적 사용](https://www.reddit.com/r/LocalLLaMA/comments/1tx33sx/graph_agent)

- **핵심:** 사용자가 클릭하면 노드에 연결된 문서에서 관련 문단으로 이동하거나 여러 문서에서 관련 문단을 강조 표시할 수 있는 그래프 에이전트가 개발되었습니다. 이 그래프 에이전트는 지식 그래프를 편집하고 계산하며 애니메이션화하는 기능을 제공합니다.
- **맥락:** 지식 그래프와 인터랙티브 에이전트의 통합은 복잡한 데이터 관계를 시각적으로 이해하고 탐색할 수 있는 새로운 방법을 제시합니다.
- **출처:** Reddit r/LocalLLaMA
- **키워드:** `knowledge_graph` · `interactive_agent` · `graph_animation`

### [ChatGPT, 더 나은 기억력으로 도움이 되는 대화 지원](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBOd2FyMkVXZ01LRFZHMHZ2Wk1HeTlSOEMtNGd0azhKMi1tT0JZWkZVaHR3UUdFS0NMUzZpNEtIcExsaVo3Y1BON3ExVWR6a3F3bkp6Y1FvV2s0bGZCWFE?oc=5)

- **핵심:** OpenAI가 ChatGPT의 기억력을 향상시켜 사용자에게 더욱 유용한 정보를 제공한다. 새로운 기능 'Dreaming'을 통해 ChatGPT는 과거 대화 내용을 더 잘 기억하고 활용할 수 있다.
- **맥락:** 개선된 기억력은 ChatGPT의 응답 정확도와 유용성을 크게 향상시켜 사용자 경험을 개선한다.
- **출처:** Google News AI Search
- **키워드:** `chatgpt` · `openai` · `memory` · `dreaming`

### [Cloudflare, 봇과 에이전트 트래픽이 인간 웹 트래픽을 넘어섰다고 경고](https://www.reddit.com/r/artificial/comments/1tx2nlt/cloudflare_warns_bot_and_agentic_traffic_has)

- **핵심:** Cloudflare 관련 게시글은 봇과 에이전트 트래픽이 인간 웹 트래픽을 넘어섰다는 관측을 공유했다. AI 에이전트와 자동화 봇이 웹 사용량의 주요 축으로 부상하고 있다는 신호다.
- **맥락:** 웹 서비스 운영자는 사람과 자동화 트래픽을 구분하고, 보안·분석·과금 체계를 다시 설계해야 하는 압력을 받게 된다.
- **출처:** Reddit r/artificial
- **키워드:** `cloudflare` · `warns` · `bot` · `and`

### [LAM과 에이전트의 정의를 구분하는 방법은?](https://www.reddit.com/r/artificial/comments/1tx06q3/what_is_the_proper_definition_of_an_lam_vs_agent)

- **핵심:** Reddit 사용자들이 LAM과 에이전트(Agent)의 개념을 어떻게 구분해야 하는지 논의 중이다. 게시글은 두 용어가 종종 혼용되므로, 작업 범위와 자율성 기준을 더 명확히 해야 한다고 지적한다.
- **맥락:** 정확한 용어 사용은 기술적 이해와 커뮤니케이션을 향상시키며, 이를 통해 AI 개발과 응용 분야에서 혼란을 줄일 수 있다.
- **출처:** Reddit r/artificial
- **키워드:** `LAM` · `Agent` · `AI`

### [5천 달러로 구매할 수 있는 최고의 인공지능 주식](https://news.google.com/rss/articles/CBMingFBVV95cUxQdFA1S1NoOVNoTlZRYjRUWWdUVnl2TDA3c0psYzE3cjAzalltU2pNSERxb2JRR0hWTnM3UjBRMXk1QTRtVDlyRklyYmtiV29KeFNDQWYtU1dqdkRvcW5zSUE4eDdHNVNMQkdJMmF0bWN0TWxjcWlJR1Z5ZEY5MGJqV24tLTI1cC1CYWVLakwzRzJ0X2VXdi15ZHVXelFNUQ?oc=5)

- **핵심:** Yahoo Finance가 추천하는 5개의 AI 관련 주식을 소개함. 이 목록은 투자자가 5,000달러로 시작하여 AI 분야에서 성장 가능성을 탐색할 수 있도록 돕는다.
- **맥락:** AI 기술 발전과 함께 인공지능 산업의 중요성이 높아짐에 따라 관련 주식 투자 관심도 증가.
- **출처:** Google News AI Search
- **키워드:** `ai stocks` · `investment guide` · `yahoo finance`

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [VideoKR: Towards Knowledge- and Reasoning-Intensive Video Understanding](https://huggingface.co/papers/2606.05259)

- **한 줄:** VideoKR는 전문 영역 비디오와 human-in-the-loop 예제 생성으로 지식·추론 중심 비디오 이해를 평가하는 데이터셋과 벤치마크를 제시합니다.
- **아이디어:** VideoKR는 전문 영역 비디오 이해에서 단순 장면 인식보다 지식 활용과 추론 능력이 중요하다는 문제의식에서 출발합니다. 145K개 이상의 신규 비디오와 315K개의 비디오 추론 예제를 구축해 모델이 실제 비디오 이해와 지식 집약적 추론을 수행하는지 평가합니다.
- **출처:** Hugging Face Papers (Top today)
- **키워드:** `VideoKR` · `knowledge-intensive video understanding` · `human-in-the-loop`

### 2. [Personal AI Agent for Camera Roll VQA](https://huggingface.co/papers/2606.05275)

- **한 줄:** 개인 카메라 롤의 시각적 질문-답변을 위한 대화형 인공지능 에이전트를 개발하였습니다.
- **아이디어:** 연구진은 개인 카메라 롤에서 사진을 찾아내어 사용자의 질문에 답하는 대화형 AI 에이전트를 제작했습니다. 이 에이전트는 거대한 시각적 데이터셋을 탐색할 수 있는 계층 메모리와 특화된 도구를 갖추고 있으며, 이를 통해 개인화된 사진 정보를 효과적으로 찾아낼 수 있습니다. 또한 camroll이라는 새로운 데이터셋을 구축하여 해당 에이전트의 성능을 평가하였습니다.
- **출처:** Hugging Face Papers (Top today)
- **키워드:** `Camera Roll VQA` · `Hierarchical Memory` · `Conversational AI Agent`

### 3. [Unsupervised Skill Discovery for Agentic Data Analysis](https://huggingface.co/papers/2606.06416)

- **한 줄:** DataCOPE는 비지도 학습을 통해 데이터 분석 기술을 발견하고 개선하는 프레임워크를 제안한다.
- **아이디어:** 데이터 분석에서 효과적인 기술을 발견하는 것은 비용이 많이 들고 성공 기준이 다양해 어렵다. DataCOPE는 데이터 분석 에이전트가 탐색 궤적을 만들고, 비지도 검증자가 신호를 추출하며, 기술 관리자가 대조적 기술 증류를 수행하도록 구성한다. 보고서형 분석과 논리형 분석 모두에서 기존 기준보다 성능 향상을 보였다고 주장한다.
- **출처:** Hugging Face Papers (Top today)
- **키워드:** `Unsupervised Skill Discovery` · `Data Analysis` · `Verifier-Guided Exploration`

### 4. [Latent Reasoning with Normalizing Flows](https://huggingface.co/papers/2606.06447)

- **한 줄:** NF-CoT은 정규화 흐름을 사용하여 대형 언어 모델의 중간 계산을 효율적으로 수행합니다.
- **아이디어:** 대형 언어 모델에서 연역적 추론을 개선하기 위해 NF-CoT은 정규화 흐름(normalizing flows)을 사용해 중간 계산을 확률적이고 효율적인 방식으로 처리합니다. 이를 통해 원래의 KV 캐시와 호환되며, 잠재적 사고를 확률적으로 왼쪽에서 오른쪽으로 디코딩할 수 있습니다.
- **출처:** Hugging Face Papers (Top today)
- **키워드:** `Latent Reasoning` · `Normalizing Flows` · `Large Language Models`

### 5. [Imagine Before You Predict: Interleaved Latent Visual Reasoning for Video Event Prediction](https://huggingface.co/papers/2606.05769)

- **한 줄:** Future-L1은 비디오 이벤트 예측에서 중간 시점의 시각적 의미를 보존하는 혼합 시각-언어 모델을 제시합니다.
- **아이디어:** 비디오 이벤트 예측(VEP)에서는 모델이 부분적인 영상 증거로부터 미래 상태를 추론해야 합니다. 기존 비디오 MLLM은 중간 미래 추론을 텍스트 공간에만 표현해 미세한 동작, 구조, 상호작용 정보를 잃기 쉽습니다. Future-L1은 언어 토큰과 연속적인 시각 latent vector를 번갈아 사용해 중간 시점의 시각 의미를 보존하면서 미래 예측을 개선합니다.
- **출처:** Hugging Face Papers (Top today)
- **키워드:** `Video Event Prediction` · `Interleaved Latent Visual Reasoning` · `FutureBench`

### 6. [World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis](https://huggingface.co/papers/2606.05979)

- **한 줄:** World-Language-Action 모델은 텍스트 지시와 로봇 상태 예측을 통합하여 효율적인 장기 작업 실행과 교차 체험 학습을 가능하게 한다.
- **아이디어:** World-Language-Action (WLA) 모델은 텍스트 지시, 이미지 및 로봇 상태를 입력으로 받아 텍스트 하위 작업, 하위 목표 이미지, 로봇 동작을 예측한다. WLA는 자동회귀 트랜스포머 백본을 사용하여 세계 모델링과 언어 추론 능력을 결합하며, 이로 인해 복잡한 장기 작업 해결이 가능하다. WLA는 World Expert를 통해 물리 동역학을 감독하고 Action Expert의 상태-동작 상관 관계 특성을 쉽게 캐릭터화한다.
- **출처:** Hugging Face Papers (Top today)
- **키워드:** `World-Language-Action` · `autoregressive Transformer` · `cross-embodiment learning`

### 7. [Discrete-WAM: Unified Discrete Vision-Action Token Editing for World-Policy Learning](https://huggingface.co/papers/2606.05645)

- **한 줄:** Discrete-WAM은 자율 주행에서 구성적 인과 추론을 가능하게 하는 통합된 이산 비전-액션 토큰 편집 방법을 제시합니다. (영문 용어: Vision-Action, World-Policy).
- **아이디어:** 자율 주행에서는 주행 중 발생하는 다양한 상황에 대한 인과 관계를 이해해야 합니다. 그러나 대부분의 end-to-end 방법은 직접 상태에서 액션으로의 매핑만 사용하여 인과적 동역학을 모델링하지 못합니다. Discrete-WAM은 미래 비주얼 상태와 자동차 행동을 이산 토큰으로 표현해 구성적 인과 추론을 가능하게 하며, 공유된 이산 확산 프레임워크를 통해 세계 모델링 및 정책 결정을 통합합니다.
- **출처:** Hugging Face Papers (Top today)
- **키워드:** `Discrete-WAM` · `자율 주행` · `인과 추론`

### 8. [MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery](https://huggingface.co/papers/2606.06473)

- **한 줄:** MLEvolve는 LLM 기반의 멀티 에이전트 프레임워크로, 개선된 탐색 메커니즘, 기억 시스템 및 적응형 코딩 전략을 통해 장기적인 머신 러닝 알고리즘 발견을 가능하게 한다. (영문 용어: Self-Evolving).
- **아이디어:** MLEvolve는 LLM 기반의 멀티 에이전트 프레임워크로, 정보 분리를 해결하고 메모리 없는 탐색 및 계층적 제어 부족 문제를 극복한다. 이를 위해 그래프 기반 참조 엣지와 엔트로피에 영감을 받은 진보적인 스케줄링을 통해 교차 분기 정보 흐름을 가능하게 한다. 또한 Retrospective Memory 시스템을 도입하여 에이전트가 경험을 쌓아가는 것을 지원한다. MLE-Bench 평가에서 MLEvolve는 다양한 차원에서 최고의 성능을 보여주며, AlphaEvolve와 같은 전문 알고리즘 발견 방법들보다 수학적 알고리즘 최적화 작업에서도 우수한 성과를 내었다.
- **출처:** Hugging Face Papers (Top today)
- **키워드:** `LLM` · `Multi-Agent Framework` · `Progressive MCGS`

### 9. [OPRD: On-Policy Representation Distillation](https://huggingface.co/papers/2606.06021)

- **한 줄:** OPRD는 학생 모델과 교사 모델의 은닉 표현을 맞춰 On-Policy Representation Distillation을 개선하는 방법입니다.
- **아이디어:** 기존 on-policy distillation은 주로 출력 공간에서 학생과 교사 모델을 맞추기 때문에 샘플 변동성과 정보 손실 문제가 남습니다. OPRD는 같은 rollout에 대한 선택 층 표현을 정렬해 구조 정보를 더 잘 전달하고, 추론 성능과 학습 효율을 높이는 것을 목표로 합니다.
- **출처:** Hugging Face Papers (Top today)
- **키워드:** `oprd` · `on-policy` · `representation` · `distillation`

### 10. [Flash-WAM: Modality-Aware Distillation for World Action Models](https://huggingface.co/papers/2606.05254)

- **한 줄:** Flash-WAM은 모달성에 맞는 일치 함수를 선택하여 세계 동작 모델의 실시간 추론을 가능하게 한다. (영문 용어: Modality-Aware).
- **아이디어:** 세계 동작 모델(WAM)은 미래 비디오와 로봇 동작을 생성하지만, 많은 노이즈 제거 단계가 필요해 실시간 제어를 어렵게 한다. Flash-WAM은 각 모달성에 맞는 일치 함수를 선택하여 저노이즈 상태의 동작 스트림과 고노이즈 상태의 비디오 스트림을 처리하며, 이로 인해 실제 시간 내에서 추론을 가능하게 한다.
- **출처:** Hugging Face Papers (Top today)
- **키워드:** `Flash-WAM` · `World Action Models` · `Modality-Aware Distillation`
