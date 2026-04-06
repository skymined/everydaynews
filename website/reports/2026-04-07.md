# IMDIGEST - 2026-04-07

2026-04-07 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-04-07 AI 브리핑입니다. 오늘은 TechCrunch AI, TechCrunch AI, AWS Machine Learning Blog에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

### [OpenAI가 AI 시대 경제 재편을 위한 정책 제안을 발표하며, 로봇세, 공공 자산 펀드, 주 4일 근무제 등을 제시했습니다.](https://techcrunch.com/2026/04/06/openais-vision-for-the-ai-economy-public-wealth-funds-robot-taxes-and-a-four-day-work-week)

OpenAI는 AI로 인한 경제적 파급 효과에 대응하기 위해 정책 제안을 발표했습니다. 주요 제안에는 AI가 창출하는 부를 분배하기 위한 공공 자산 펀드(public wealth funds)와 로봇세(robot taxes) 도입이 포함됩니다. 노동에서 자본으로 세금 부담을 전환하고, AI 접근성을 확대하여 경제력 집중을 막는 방안을 제시했습니다. AI 기술 발전이 가속화되면서 사회 및 경제 전반에 미칠 영향에 대한 논의가 활발해지고 있으며, OpenAI는 이러한 변화에 대한 선제적인 비전을 제시하고 있습니다. 출처는 TechCrunch AI입니다.

### [구글, 오프라인 AI 받아쓰기 앱 "Google AI Edge Eloquent" iOS에 조용히 출시](https://techcrunch.com/2026/04/06/google-quietly-releases-an-offline-first-ai-dictation-app-on-ios)

구글이 iOS용 오프라인 우선 AI 받아쓰기 앱 "Google AI Edge Eloquent"를 출시했습니다. 이 앱은 Gemma 기반의 ASR(자동 음성 인식) 모델을 다운로드하면 오프라인에서도 받아쓰기가 가능합니다. 실시간 전사 기능과 함께, 받아쓰기 중 "음", "아"와 같은 불필요한 단어를 자동으로 필터링하고 텍스트를 다듬어줍니다. 오프라인 우선 AI 앱의 출시는 개인 정보 보호 및 네트워크 연결에 구애받지 않는 AI 활용의 중요성이 커지고 있음을 보여줍니다. 출처는 TechCrunch AI입니다.

### [AWS, Amazon Quick을 활용하여 AI 기반의 직원 온보딩 에이전트 구축 지원](https://aws.amazon.com/blogs/machine-learning/build-ai-powered-employee-onboarding-agents-with-amazon-quick)

Amazon Quick은 HR 부서가 신규 직원의 온보딩 과정을 자동화하고 효율화할 수 있도록 돕는 완전 관리형 에이전트 서비스입니다. (영문 용어: AI-powered). 이 서비스를 통해 HR 팀은 코딩 없이 온보딩 에이전트를 생성하여 신규 직원의 질문에 답변하고, 기존 도구 전반의 규정 준수를 추적하며, 티켓을 자동으로 처리할 수 있습니다. Amazon Quick은 SharePoint, OneDrive, Confluence와 같은 외부 소스 및 내부 웹사이트, 파일 업로드, Amazon S3 버킷 등에서 색인된 콘텐츠를 활용하는 Knowledge bases를 포함합니다. 기업들이 신규 팀원 온보딩 시 겪는 어려움(수동 작업, 생산성 지연, 일관성 및 규정 준수 문제)을 AI 기반 자동화로 해결하여 HR 효율성을 극대화하는 트렌드를 반영합니다. 출처는 AWS Machine Learning Blog입니다.

### [Amazon SageMaker AI에서 서버리스 모델 커스터마이징을 통해 에이전트의 툴 호출 기능을 가속화합니다.](https://aws.amazon.com/blogs/machine-learning/accelerate-agentic-tool-calling-with-serverless-model-customization-in-amazon-sagemaker-ai)

Amazon SageMaker AI는 서버리스 모델 커스터마이징을 제공하여 AI 에이전트의 툴 호출 시 발생하는 환각, 잘못된 파라미터 전달 등의 문제를 해결합니다. Reinforcement Learning with Verifiable Rewards (RLVR)를 사용하여 모델이 자체적으로 응답을 생성하고, 품질에 대한 보상 신호를 받아 동작을 업데이트합니다. Qwen 2.5 7B Instruct 모델을 RLVR로 미세 조정하여 툴 호출 보상을 기본 모델 대비 57% 향상시켰습니다. AI 에이전트가 실제 프로덕션 환경에서 유용하게 활용되기 위해서는 데이터베이스 쿼리, 워크플로우 트리거, 실시간 데이터 검색 등 툴 호출의 정확성이 필수적입니다. 출처는 AWS Machine Learning Blog입니다.

### [AWS, Amazon Bedrock과 Amazon OpenSearch를 활용한 하이브리드 RAG 솔루션으로 지능형 검색 구축 방법 제시](https://aws.amazon.com/blogs/machine-learning/building-intelligent-search-with-amazon-bedrock-and-amazon-opensearch-for-hybrid-rag-solutions)

AWS는 Amazon Bedrock과 Amazon OpenSearch를 사용하여 시맨틱 및 텍스트 기반 검색을 모두 활용하는 생성형 AI 에이전트 어시스턴트 구현 방법을 소개했습니다. 이 솔루션은 LLM(Large Language Model) 기반의 동적 시스템으로, 복잡한 작업을 처리하고 개방형 대화를 수행하는 Agentic generative AI assistant 구축을 목표로 합니다. Agentic assistant는 실시간 API 호출 및 데이터베이스 조회를 통해 비즈니스별 데이터를 검색하고, 이를 LLM 생성 응답에 통합하거나 함께 제공하여 Retrieval-Augmented Generation(RAG)을 구현합니다. 생성형 AI의 핵심 기술인 RAG 시스템은 LLM의 한계를 보완하고 최신 정보를 반영하여 답변의 정확성과 신뢰성을 높이는 데 필수적입니다. 출처는 AWS Machine Learning Blog입니다.

### [Windward와 AWS가 생성형 AI를 활용하여 해양 이상 징후 분석을 고도화합니다.](https://aws.amazon.com/blogs/machine-learning/from-isolated-alerts-to-contextual-intelligence-agentic-maritime-anomaly-analysis-with-generative-ai)

Windward는 AWS와 협력하여 생성형 AI를 활용한 'Agentic maritime anomaly analysis' 시스템을 개발했습니다. 이 시스템은 AIS 데이터, 원격 감지 신호, 독점 AI 모델 및 생성형 AI를 융합하여 해양 활동에 대한 360도 뷰를 제공합니다. 기존에는 해양 분석가들이 선박 행동 이상 징후를 파악하기 위해 수동으로 데이터를 수집하고 분석하는 데 많은 시간을 소요했습니다. 생성형 AI를 활용하여 복잡한 해양 데이터를 자동으로 분석하고 상황 인식을 가속화함으로써, 국방 및 정보 기관, 법 집행 기관, 상업 리더들이 해양 위협에 선제적으로 대응하고 중요한 자산을 보호할 수 있게 됩니다. 출처는 AWS Machine Learning Blog입니다.

### [OpenAI 출신들이 1억 달러 규모의 벤처 펀드 "Zero Shot"을 결성하여 AI 스타트업에 투자하고 있습니다.](https://techcrunch.com/2026/04/06/openai-alums-have-been-quietly-investing-from-a-new-potentially-100m-fund)

OpenAI의 초기 멤버들이 "Zero Shot"이라는 새로운 벤처 캐피탈 펀드를 결성했습니다. 이 펀드는 1억 달러를 목표로 첫 클로징을 마쳤으며, 이미 여러 스타트업에 투자를 시작했습니다. 공동 창립자로는 DALL·E 및 ChatGPT 출시를 이끌었던 Evan Morikawa, OpenAI의 오리지널 프롬프트 엔지니어 Andrew Mayne, 그리고 OpenAI 연구원 출신 Shawn Jain 등이 포함됩니다. OpenAI의 핵심 인력들이 직접 벤처 펀드를 설립하여 AI 생태계에 재투자하는 것은 AI 기술 발전과 스타트업 성장에 중요한 역할을 할 것입니다. 출처는 TechCrunch AI입니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [로컬 LLM 환경에서 Hermes Agent를 활용한 자율 에이전트 구축의 어려움](https://www.reddit.com/r/LocalLLaMA/comments/1sedb37/trying_to_get_a_chatgptcodexstyle_autonomous)

사용자는 Ollama와 로컬 모델을 사용하여 Hermes Agent를 자율 에이전트처럼 작동시키려 했으나, 챗봇처럼 일반 텍스트만 출력하고 자동화에 필요한 구조화된 명령(structured commands)을 생성하지 못하는 문제에 직면했습니다. ChatGPT/Codex와 같이 신뢰할 수 있는 셸 명령어 실행이나 구조화된 도구 호출(tool calls)을 기대했지만, Hermes Agent는 비실행 가능한 텍스트만 반환했습니다. 문제를 해결하기 위해 출력 필터링, 실행 스크립트 작성 등 여러 시도를 했지만, 에이전트는 여전히 유용한 지시 대신 비셸(non-shell) 텍스트를 생성했습니다. 로컬 LLM 환경에서 자율 에이전트를 구현하려는 시도는 비용 효율성과 데이터 주권 측면에서 중요하지만, 아직 클라우드 기반 모델(OpenAI, Claude)만큼의 성능과 신뢰성을 확보하기 어렵다는 한계를 보여줍니다. 출처는 Reddit r/LocalLLaMA입니다.

### [Gemma 4 모델을 로컬 CUDA 환경에서 BF16 및 GGUF 양자화로 구동하며 성능 벤치마크와 주의사항이 공유되었습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1sebwz2/got_gemma_4_running_locally_on_cuda_both_float)

Gemma 4 모델이 CUDA 환경에서 BF16 (full-precision) 및 GGUF (quantized) 추론 방식으로 로컬 구동에 성공했습니다. RTX 3090 환경에서 BF16은 110 tok/s (short gen) 및 72 tok/s (long gen)를, Q4_K_M GGUF는 170 tok/s (short gen) 및 93 tok/s (long gen)의 성능을 보였습니다. Gemma 4는 attention_scale=1.0을 사용하여 일반 Transformer보다 정밀도 오류에 약 22배 더 민감하며, F16 KV cache나 특정 Flash Attention 버전 사용 시 문제가 발생할 수 있습니다. Gemma 4와 같은 최신 대규모 언어 모델을 소비자용 하드웨어에서 효율적으로 구동하려는 시도는 AI 모델의 접근성을 높이고 개인화된 AI 애플리케이션 개발을 촉진하는 중요한 트렌드입니다. 출처는 Reddit r/LocalLLaMA입니다.

### [Anthropic이 Claude Code for Healthcare를 통해 의료 분야 AI 활용 사례를 제시합니다.](https://news.google.com/rss/articles/CBMiogFBVV95cUxOc29ONWJhLTNhaFI3TDZhZzVFVE9KQzlDZ01NQ3k1ZmxqZ25wYzRVZm9nc2MwQUJCWXFiVlhXZUdidEhzUUtEQ3pBTk44QTUzMmhSbnA5Zmt6TzFWSVQ1NkdzNHpoalNkbWROUlV4OUpGMTJrclJBQ0pZd1otZlF3cERIc2h1c1lBRktyVEZWd0RUMk44aVlVUW1rd3JPTk0xeWc?oc=5)

Anthropic은 Claude Code for Healthcare를 공개하며 의사들이 AI를 활용하는 구체적인 방법을 소개했습니다. 이 이니셔티브는 의료 전문가들이 AI를 통해 진료 효율성을 높이고 환자 치료를 개선할 수 있도록 돕는 데 중점을 둡니다. 의료 분야에서 AI를 활용한 코드 개발 및 적용 사례를 공유하여 실제적인 도움을 제공합니다. 의료 분야에서 AI 도입이 가속화되면서, Anthropic과 같은 선도 기업들이 특정 산업에 특화된 AI 솔루션과 활용 가이드를 제공하는 추세가 강화되고 있습니다. 출처는 Google News AI Search입니다.

### [Deepseek, 검색 페이지 수 대폭 증가 및 UI 변경으로 V4 업데이트 임박 가능성 제기](https://www.reddit.com/r/LocalLLaMA/comments/1sec4jb/deepseek_is_now_searching_a_insanely_high_number)

Deepseek의 웹 검색 기능이 기존 10페이지 내외에서 92페이지까지 대폭 확장되었습니다. 검색 UI가 개선되어 검색 결과 분석을 위한 항목별 분류가 추가되었습니다. 사용자가 프롬프트를 통해 질문했을 때, Deepseek이 검색어 변형 및 결과 개선을 통해 더 많은 웹 페이지를 탐색하여 답변을 확인하는 모습이 관찰되었습니다. Deepseek의 검색 능력 향상은 AI 모델이 더 광범위하고 정확한 정보를 수집하여 답변의 신뢰성과 깊이를 높일 수 있음을 의미합니다. 출처는 Reddit r/LocalLLaMA입니다.

### [Anthropic, Claude 모델에 OpenClaw 사용 시 추가 비용 부과 방침 발표](https://news.google.com/rss/articles/CBMilgFBVV95cUxQLXJQdTRScmxheE9aMVlqZXRrN2dMUktjZ3FrcWRWX2Y2RXV5NWxKa3pLdkJ2RXdnYkFTT3R2Y2FXUVl3cDBxM3MzNjNta2lmSWxOMzRNVWNOVVMtejM4WjVLaGljcGs5VzlaYUpUUjRVbE80YmtQeEJrMm11N2V4d0VUdkxWVVV4enB3dFV3VnpsdHdqZGc?oc=5)

Anthropic은 자사의 Claude 모델을 활용하는 OpenClaw 프로젝트에 대해 추가 비용을 부과할 것이라고 밝혔습니다. OpenClaw는 Anthropic의 AI 모델을 사용하여 게임 'Minecraft'에서 복잡한 작업을 수행하는 에이전트를 훈련하는 데 사용되는 오픈 소스 프로젝트입니다. 이 프로젝트는 AI 에이전트가 게임 내에서 'Loco-Manipulation'과 같은 고급 기술을 습득하도록 돕습니다. AI 모델의 무분별한 사용에 대한 비용 정책이 강화되는 추세로, 오픈 소스 프로젝트라도 상업적 또는 과도한 사용에 대해서는 제약이 생길 수 있음을 시사합니다. 출처는 Google News AI Search입니다.

### [자동화 및 AI가 심리 치료를 지원하는 범위에 대한 논의가 활발합니다.](https://news.google.com/rss/articles/CBMilwFBVV95cUxOM3Z4NmdyZ1NXbzNzbmNiVGRTOWk4QUpGdmk5S3R2bkRfM3N1ckFjbkttMkFBZGE2dXprb3duQmNIdDZpZkRVejQ5TnBaQ0hjSnpmMmM4RnNpNnI0M21MNVpzTHNTOFJfR1RLTk4xN2Z1anl1MVBnOVBoQnI2bl9fQnFBN2NOeU5vd0Jvc1dwaUZ5U2Zmekhj?oc=5)

AI와 자동화 기술이 심리 치료 분야에서 활용될 수 있는 잠재력에 대한 관심이 증가하고 있습니다. (영문 용어: attheu.utah.edu). 기술이 심리 치료의 접근성을 높이고 효율성을 개선할 수 있는 방안이 모색되고 있습니다. 심리 치료 과정에서 AI의 역할과 한계에 대한 심층적인 분석이 이루어지고 있습니다. 정신 건강 서비스에 대한 수요 증가와 전문가 부족 문제를 해결하기 위해 AI 기반 솔루션의 필요성이 부각되고 있습니다. 출처는 Google News AI Search입니다.

### [Nvidia의 HBM 공급 부족 가능성이 제기되며 주가에 미칠 영향에 대한 우려가 커지고 있습니다.](https://news.google.com/rss/articles/CBMihgNBVV95cUxNVnprTmRhWE54SWo3ZjR4V2dXNWdCR082b3JETV9ZdUVxYU1yaV9yYXl0cG5FQkpXaUNpdmZvLUVESHp1UTg4OThud2JSc2lkcDVsWHlMRGNXUU1xYUhSX2tEMDlzSHhVMjE1c0NxTjBINm5xQi03SGI0eXcwTHhFR2lVdUJJYXk5ME9TbnIxaTZiSVlxcWItSjg5bmVXQ0xuQVIwNkFreFVnRldoX05aRFNQSkdWeFBmaWRHa1pHY3BUR3hKSEplQU1MRFlpM0swTnk4aTI1ZjB6eWV2Z1AtdUJwMFp4ZkZJa3AtY3lkVWJrV2hDRlpELWNRY21NYTg1V3RrbzNtcXhlSjRITHl6aEVORWFXVjNka3FhZnp2N1V5alNuc2hQXy1mYWE1NFBnUjRXb3pmd1BFZXBXeEtsSnA3U1VVYmtWcmY4XzA0bHFsdXVJS2lMV0ticndFMWlad0JGNVZQblpDaWVxVFhWMkF2am4xT25OdVlOMV82cG5ldmlkZnc?oc=5)

Barron's에 따르면, 한 애널리스트는 Nvidia가 HBM(고대역폭 메모리) 공급 문제에 직면할 수 있다고 분석했습니다. 이는 Nvidia의 AI 칩 생산에 필요한 핵심 부품인 HBM의 수급 불균형을 의미합니다. HBM 공급 부족은 Nvidia의 AI 칩 출하량과 매출 성장에 부정적인 영향을 미칠 수 있습니다. AI 칩 시장의 폭발적인 성장으로 HBM 수요가 급증하고 있으며, 이는 HBM 제조사들의 생산 능력과 직결되는 문제입니다. 출처는 Google News AI Search입니다.

### [AI가 예상했던 것만큼 물 부족을 심화시키지 않을 수 있다는 연구 결과가 나왔습니다.](https://news.google.com/rss/articles/CBMinwFBVV95cUxNTUl0MEZkTjZhdjJvWDlrVTFZWkkwdTRTdFFuSmVhNFRmUndCZHduNzZoRTlCek44c3ctQ0VMalpYZVQ5M0N0azhtZDZsQjlLM3VJa0lSalBVdmx6aVpWODdfQzR1T3Q2NVhGQUpiUkNwY19Pb0FhMTNTajhEdERoWTFnbldRUEFCdURvcWg1d0dSYjFpblZwQVg4VWY2M2s?oc=5)

AI 기술이 물 사용량에 미치는 영향에 대한 우려가 있었으나, 새로운 연구는 이러한 우려가 과장되었을 수 있음을 시사합니다. 연구는 AI의 물 소비가 다른 산업 분야나 생활 습관에 비해 상대적으로 적을 수 있음을 보여줍니다. 실제 물 부족의 주요 원인은 AI가 아닌 다른 요소들에 있음을 지적합니다. AI 기술의 발전과 확산에 따라 환경적 영향, 특히 물 소비에 대한 논의가 활발해지고 있으며, 이 연구는 기존의 우려에 대한 새로운 관점을 제시합니다. 출처는 Google News AI Search입니다.

### [Wandb 로그를 에이전트 컨텍스트로 쉽게 제공하는 CLI 도구 및 Python SDK 'Cadenza' 공개](https://www.reddit.com/r/MachineLearning/comments/1se1rmd/p_easily_provide_wandb_logs_as_context_to_agents)

기존 Wandb CLI 및 MCP 도구 사용 시 컨텍스트 창 과부하 및 오류 발생 문제를 해결하기 위해 개발되었습니다. AlphaEvolve 알고리즘을 활용하여 Wandb 프로젝트를 가져오고 실행(run)을 인덱싱 및 구조화합니다. 과거 실험에 대한 더 넓은 컨텍스트를 제공하며, 컨텍스트 창을 과부하하지 않습니다. AI 에이전트의 복잡한 실험 관리 및 분석 효율성을 높여, 머신러닝 개발 워크플로우를 개선하는 데 기여합니다. 출처는 Reddit r/MachineLearning입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [Self-Distilled RLVR](https://huggingface.co/papers/2604.03128)

Self-Distilled RLVR(RLSD)은 RLVR과 self-distillation을 결합하여 환경 피드백으로부터 안정적인 정책 방향과 미세한 업데이트를 가능하게 합니다. 기존 RLVR은 환경의 검증 가능한 결과로부터 희소한 신호만 얻는 반면, on-policy distillation(OPD)은 더 큰 모델을 teacher로 사용하여 밀도 높은 신호를 제공합니다. 이 논문은 privileged teacher로부터만 학습 신호를 얻는 on-policy self-distillation(OPSD)이 정보 유출과 불안정한 장기 학습을 초래함을 지적합니다. 이에 RLSD는 self-distillation을 활용하여 토큰 수준의 정책 차이를 통해 미세한 업데이트 크기를 결정하고, RLVR을 사용하여 환경 피드백(예: 응답 정확성)으로부터 신뢰할 수 있는 업데이트 방향을 도출합니다. 이를 통해 RLSD는 RLVR과 OPSD의 장점을 동시에 활용하여 더 높은 수렴 상한과 우수한 학습 안정성을 달성합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 2. [A Simple Baseline for Streaming Video Understanding](https://huggingface.co/papers/2604.02317)

SimpleStream은 최근 N개 프레임만을 사용하는 간단한 슬라이딩 윈도우 방식으로 복잡한 메모리 기반 스트리밍 비디오 이해 모델들을 능가하는 성능을 보여준다. 최근 스트리밍 비디오 이해(Streaming Video Understanding) 방법론들은 긴 비디오 스트림 처리를 위해 복잡한 메모리 메커니즘에 의존하는 경향이 있습니다. 이 연구는 SimpleStream이라는 간단한 슬라이딩 윈도우(sliding-window) 접근 방식을 제안하며, 이는 최신 N개 프레임만을 기성 VLM에 입력하여 기존의 복잡한 메모리 기반 모델들과 동등하거나 더 우수한 성능을 달성합니다. OVO-Bench 및 StreamingBench에서 13개의 주요 비디오 LLM 모델과 비교했을 때, SimpleStream은 단 4개의 최근 프레임만으로도 강력한 성능을 보였습니다. 이는 실시간 인식과 장기 기억 간의 트레이드오프를 시사하며, 미래 벤치마크는 최근 장면 인식과 장거리 기억을 분리하여 평가해야 한다고 주장합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 3. [Token Warping Helps MLLMs Look from Nearby Viewpoints](https://huggingface.co/papers/2604.02870)

Token Warping은 MLLM이 인접한 시점에서 장면을 이해하도록 돕는 새로운 시점 변환 기법으로, 기존 픽셀 기반 방식보다 우수한 시각 추론 성능을 제공합니다. MLLM은 시각 추론에 능숙하지만, 시점 변화에는 취약하며 기존 픽셀 단위 워핑은 깊이 오류에 민감하고 기하학적 왜곡을 유발합니다. 이 연구는 인간의 관점 변환 이론에서 영감을 받아, ViT 기반 MLLM의 이미지 토큰이 시점 변화에 효과적인 기판이 될 수 있는지 탐구합니다. 특히, 타겟 뷰에 조밀한 그리드를 정의하고 각 그리드 포인트에 해당하는 소스 뷰 토큰을 검색하는 backward token warping 방식이 시점 변화에서 더 큰 안정성과 의미론적 일관성을 유지함을 발견했습니다. 제안된 ViewBench 벤치마크 실험을 통해 Token Warping이 MLLM이 인접한 시점에서 안정적으로 추론하도록 하며, 픽셀 단위 워핑을 포함한 모든 기준선보다 지속적으로 우수한 성능을 보임을 입증했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 4. [Agentic-MME: What Agentic Capability Really Brings to Multimodal Intelligence?](https://huggingface.co/papers/2604.03016)

Agentic-MME 벤치마크는 MLLM의 멀티모달 에이전트 능력을 평가하기 위해 최종 답변뿐만 아니라 도구 사용 및 프로세스 효율성을 검증하는 새로운 방법을 제시합니다. 기존 MLLM 평가는 도구 통합의 유연성이 부족하고, 시각 및 검색 도구를 개별적으로 테스트하며, 주로 최종 답변으로만 평가하여 실제 도구 사용 여부나 효율성을 검증하기 어려웠습니다. 이를 해결하기 위해 Agentic-MME는 6개 도메인과 3가지 난이도에 걸쳐 418개의 실제 작업을 포함하며, 2,000개 이상의 단계별 체크포인트를 통해 프로세스 수준의 검증을 가능하게 합니다. 이 벤치마크는 샌드박스 코드 및 API를 지원하는 통합 평가 프레임워크와 인간 참조 궤적을 제공하여, 중간 상태를 감사하고 인간 궤적 대비 과도한 사고(overthinking) 메트릭으로 효율성을 정량화합니다. 실험 결과, 최신 모델인 Gemini3-pro도 Level-3 작업에서 23.0%의 정확도를 보여 실제 멀티모달 에이전트 문제 해결의 어려움을 강조합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 5. [Test-Time Scaling Makes Overtraining Compute-Optimal](https://huggingface.co/papers/2604.01411)

Test-Time Scaling Makes Overtraining Compute-Optimal 논문은 추론 비용을 고려할 때 최적의 사전 학습 결정이 과적합(overtraining) 영역으로 이동함을 밝히는 Train-to-Test (T^2) 스케일링 법칙을 제시합니다. 이 연구는 모델 크기, 훈련 토큰, 추론 샘플 수를 고정된 예산 내에서 최적화하는 Train-to-Test (T^2) 스케일링 법칙을 제안합니다. 기존 Chinchilla와 같은 사전 학습 스케일링 법칙은 추론 시 반복 샘플링 등으로 인해 모델 크기와 샘플 수에 따라 증가하는 추론 비용을 고려하지 않았습니다. T^2 스케일링 법칙은 이러한 추론 비용을 통합하여 사전 학습과 추론 시간 결정을 동시에 최적화하며, 이를 통해 최적의 사전 학습 결정이 과적합 영역으로 크게 이동함을 발견했습니다. 이 결과는 8가지 다운스트림 태스크에서 검증되었으며, 최신 LLM 배포에서도 유효함을 보여줍니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 6. [Communicating about Space: Language-Mediated Spatial Integration Across Partial Views](https://huggingface.co/papers/2603.27183)

COSMIC 벤치마크를 통해 MLLM이 부분적인 시점에서 언어 기반의 공간 통합을 수행하는 능력이 인간에 비해 현저히 떨어진다는 것을 밝혔다. (영문 용어: Language-Mediated). 이 연구는 MLLM이 협업 공간 커뮤니케이션 작업에서 인간과 같은 일관된 공유 공간 모델을 구축하는 데 한계가 있음을 지적한다. 이를 체계적으로 연구하기 위해 두 MLLM 에이전트가 다른 시점에서 3D 실내 환경을 관찰하고 자연어 메시지를 교환하여 공간 쿼리를 해결하는 COSMIC 벤치마크를 도입했다. 실험 결과, MLLM은 공유 앵커 객체 식별에는 신뢰할 수 있지만, 관계형 추론 및 전역적으로 일관된 맵 구축에서는 성능이 크게 저조했다. 인간은 95%의 정확도를 달성하는 반면, 최신 모델인 Gemini-3-Pro-Thinking은 72%의 정확도를 보여 MLLM의 개선 여지가 크다는 것을 확인했다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 7. [InCoder-32B-Thinking: Industrial Code World Model for Thinking](https://huggingface.co/papers/2604.03144)

InCoder-32B-Thinking은 산업용 코드 개발에서 하드웨어 제약 조건에 대한 전문가 추론이 부족한 문제를 해결하기 위해 오류 기반 추론 체인과 도메인별 실행 추적 데이터를 학습하여 고품질 코드 추론 및 성능을 생성하는 모델입니다. 산업용 소프트웨어 개발은 칩 설계, GPU 최적화, 임베디드 시스템 등에서 하드웨어 제약 조건 및 타이밍 의미론에 대한 엔지니어의 추론 과정을 보여주는 전문가 추론 추적 데이터가 부족합니다. 이 연구는 Error-driven Chain-of-Thought (ECoT) 합성 프레임워크와 산업용 코드 세계 모델 (ICWM)의 데이터를 사용하여 InCoder-32B-Thinking을 제안합니다. ECoT는 환경 오류 피드백을 통한 다중 턴 대화에서 사고 내용을 합성하여 오류 수정 프로세스를 명시적으로 모델링하며, ICWM은 Verilog 시뮬레이션, GPU 프로파일링 등 도메인별 실행 추적 데이터를 학습하여 코드가 하드웨어 동작에 미치는 인과 관계를 파악하고 실행 결과를 예측하여 자체 검증을 가능하게 합니다. InCoder-32B-Thinking은 14개의 일반 벤치마크(LiveCodeBench v5에서 81.3%)와 9개의 산업용 벤치마크(CAD-Coder에서 84.0%, KernelBench에서 38.0%)에서 최고 수준의 오픈 소스 결과를 달성했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 8. [AgentSocialBench: Evaluating Privacy Risks in Human-Centered Agentic Social Networks](https://huggingface.co/papers/2604.01487)

AgentSocialBench는 인간 중심의 에이전트 기반 소셜 네트워크에서 LLM 에이전트의 프라이버시 위험을 체계적으로 평가하는 최초의 벤치마크를 제시합니다. (영문 용어: Human-Centered). 인간 중심의 에이전트 기반 소셜 네트워크는 다중 에이전트 조정 및 정보 중개로 인해 고유한 프라이버시 문제를 야기합니다. 이 연구는 이러한 환경에서 프라이버시 위험을 체계적으로 평가하기 위한 벤치마크인 AgentSocialBench를 도입합니다. 실험 결과, 에이전트 기반 소셜 네트워크에서의 프라이버시는 단일 에이전트 설정보다 본질적으로 더 어려우며, 도메인 간 및 사용자 간 조정이 지속적인 정보 유출 압력을 생성함을 보여줍니다. 또한, 민감한 정보를 추상화하도록 지시하는 프라이버시 지침이 역설적으로 에이전트가 해당 정보를 더 많이 논의하게 만드는 '추상화 역설' 현상을 발견했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 9. [Swift-SVD: Theoretical Optimality Meets Practical Efficiency in Low-Rank LLM Compression](https://huggingface.co/papers/2604.01609)

Swift-SVD는 LLM 압축에서 최적의 low-rank 근사를 효율적인 공분산 집계 및 고유값 분해를 통해 달성하여, 더 빠르고 정확한 모델 압축을 가능하게 합니다. 거대 언어 모델(LLM)의 배포는 메모리 및 대역폭 제약으로 인해 어려움을 겪습니다. 기존 SVD 기반 압축 방법은 이론적으로 최적이지만 비효율적이거나, 효율적이지만 최적의 재구성 오류를 달성하지 못하는 한계가 있었습니다. Swift-SVD는 활성화 인지(activation-aware) 방식의 closed-form 압축 프레임워크로, 입력 배치에 대한 출력 활성화의 공분산을 점진적으로 집계한 후 단일 고유값 분해를 수행하여 이러한 문제를 해결합니다. 이 방법은 훈련 없이 빠르고 최적의 layer-wise low-rank 근사를 제공하며, 6개의 LLM과 8개의 데이터셋에 대한 실험에서 최첨단 baseline 대비 우수한 압축 정확도와 3-70배 빠른 압축 속도를 보여주었습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 10. [AgentHazard: A Benchmark for Evaluating Harmful Behavior in Computer-Use Agents](https://huggingface.co/papers/2604.02947)

AgentHazard는 컴퓨터 사용 에이전트의 유해 행위를 평가하기 위한 벤치마크로, 개별적으로는 무해해 보이지만 연속적인 행동을 통해 해를 끼치는 에이전트의 안전 문제를 다룹니다. (영문 용어: Computer-Use). 컴퓨터 사용 에이전트는 텍스트 생성에서 벗어나 도구, 파일 및 실행 환경에서 지속적인 작업을 수행할 수 있어 새로운 안전 문제를 야기합니다. 이 에이전트들은 개별적으로는 합리적인 단계들이 모여 무단 행동과 같은 유해한 결과를 초래할 수 있습니다. AgentHazard는 이러한 문제를 해결하기 위해 2,653개의 인스턴스로 구성된 벤치마크를 제공하며, 에이전트가 누적된 컨텍스트, 반복적인 도구 사용, 중간 작업 및 단계 간의 종속성에서 발생하는 해를 인식하고 중단할 수 있는지 평가합니다. Claude Code, OpenClaw, IFlow 등의 시스템을 Qwen3, Kimi, GLM, DeepSeek 모델로 평가한 결과, 현재 시스템들이 여전히 매우 취약하며 모델 정렬만으로는 자율 에이전트의 안전을 보장하기 어렵다는 것을 보여줍니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.
