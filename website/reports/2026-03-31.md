# IMDIGEST - 2026-03-31

2026-03-31 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-03-31 AI 브리핑입니다. 오늘은 AWS Machine Learning Blog, TechCrunch AI, AWS Machine Learning Blog에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

### [AWS, Amazon Bedrock AgentCore 및 Amazon Nova Sonic 2.0을 활용한 에이전트형 AI 영화 비서로 초개인화된 시청 경험을 제공합니다.](https://aws.amazon.com/blogs/machine-learning/deliver-hyper-personalized-viewer-experiences-with-an-agentic-ai-movie-assistant-using-amazon-bedrock-agentcore-and-amazon-nova-sonic-2-0)

AWS는 Amazon Bedrock AgentCore와 Amazon Nova Sonic 2.0을 사용하여 초개인화된 시청 경험을 제공하는 에이전트형 AI 영화 비서를 소개했습니다. (영문 용어: hyper-personalized). 이 AI 비서는 사용자의 기분, 시간대, 사회적 상황 등 맥락에 따른 요구를 파악하여 기존 추천 시스템의 한계를 극복합니다. 사용자는 AI 에이전트에게 특정 장면이나 테마에 대해 질문하고, 실시간 피드백을 통해 콘텐츠와 개인 선호도를 모두 이해하는 큐레이터와 같은 경험을 할 수 있습니다. 기존 ML 기반 추천 시스템의 한계를 넘어, 생성형 AI의 맥락 이해 및 대화 능력을 결합하여 사용자에게 더욱 몰입감 있고 개인화된 콘텐츠 탐색 경험을 제공하는 트렌드를 반영합니다. 출처는 AWS Machine Learning Blog입니다.

### [미국인들의 AI 도구 사용은 증가했지만, 결과에 대한 신뢰도는 오히려 하락했습니다.](https://techcrunch.com/2026/03/30/ai-trust-adoption-poll-more-americans-adopt-tools-fewer-say-they-can-trust-the-results)

Quinnipiac University의 설문조사에 따르면, 미국인의 76%가 AI를 거의 또는 가끔만 신뢰한다고 응답했습니다. AI 도구를 사용해본 적 없는 미국인의 비율은 2025년 4월 33%에서 현재 27%로 감소했습니다. 응답자의 51%가 연구 목적으로 AI를 사용하며, 글쓰기, 업무, 데이터 분석에도 활용하고 있습니다. AI 기술의 확산에도 불구하고, 사용자들이 AI 생성 정보의 정확성과 신뢰성에 대한 우려를 여전히 크게 가지고 있음을 보여줍니다. 출처는 TechCrunch AI입니다.

### [Ring, Amazon Bedrock Knowledge Bases를 활용하여 글로벌 고객 지원을 확장하고 비용을 절감합니다.](https://aws.amazon.com/blogs/machine-learning/how-ring-scales-global-customer-support-with-amazon-bedrock-knowledge-bases)

Amazon의 홈 보안 자회사인 Ring은 Amazon Bedrock Knowledge Bases를 사용하여 다국어 RAG 기반 지원 챗봇을 구축했습니다. 이 새로운 시스템은 기존의 규칙 기반 챗봇이 가진 제한된 대화 패턴과 다양한 고객 문의 처리의 어려움을 해결했습니다. Ring은 이 솔루션을 통해 각 추가 로케일로 확장하는 데 드는 비용을 21% 절감했으며, 10개 국제 지역에서 일관된 고객 경험을 유지했습니다. 기업들이 글로벌 시장으로 확장함에 따라, 다국어 고객 지원 시스템의 효율성과 비용 절감은 중요한 과제가 되고 있습니다. 출처는 AWS Machine Learning Blog입니다.

### [폭스바겐 그룹, AWS Generative AI Innovation Center와 협력하여 마케팅 이미지 생성 및 평가 파이프라인 구축](https://aws.amazon.com/blogs/machine-learning/reimagine-marketing-at-volkswagen-group-with-generative-ai)

폭스바겐 그룹은 10개 브랜드에 걸쳐 연간 수천 개의 마케팅 자산을 생산하며, 각 이미지가 브랜드 표준을 정확히 반영해야 하는 과제에 직면했습니다. AWS Generative AI Innovation Center는 폭스바겐 그룹의 마케팅 및 기술팀과 협력하여 생성형 AI를 활용한 솔루션을 개발했습니다. 이 솔루션은 Amazon SageMaker AI 엔드포인트에 호스팅된 이미지 생성 모델과 Amazon Bedrock으로 구동되는 이미지 평가 기능을 갖춘 엔드투엔드 마케팅 이미지 생성 및 평가 파이프라인입니다. 생성형 AI를 활용하여 대규모 마케팅 콘텐츠 제작의 효율성을 극대화하고, 동시에 브랜드 일관성과 정확성을 유지하는 새로운 접근 방식을 제시합니다. 출처는 AWS Machine Learning Blog입니다.

### [AWS SageMaker AI와 LSTM 네트워크를 활용하여 태양 플레어 감지 시스템을 구축하는 방법이 소개되었습니다.](https://aws.amazon.com/blogs/machine-learning/build-a-solar-flare-detection-system-on-sagemaker-ai-lstm-networks-and-esa-stix-data)

AWS는 SageMaker AI와 LSTM 네트워크를 사용하여 태양 플레어 감지 시스템을 구축하는 방법을 제시했습니다. 이 시스템은 ESA STIX(Spectrometer/Telescope for Imaging X-rays)에서 수집한 다중 채널 X-ray 데이터를 분석합니다. 저(4–10 keV), 중(10–25 keV), 고(25+ keV) 에너지 대역의 X-ray 데이터에서 이상 패턴을 감지하는 데 중점을 둡니다. 태양 활동 모니터링을 위한 방대한 X-ray 측정 데이터의 효율적인 처리와 미묘한 변화 감지를 위해 고급 딥러닝 아키텍처, 특히 LSTM 네트워크의 중요성이 커지고 있습니다. 출처는 AWS Machine Learning Blog입니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [AI 에이전트의 API 자격 증명 보안 관리에 대한 개발자들의 고민이 커지고 있습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1s84kpi/how_are_you_actually_handling_api_credential)

AI 에이전트 개발 시 Stripe, Twilio, Firebase 등 외부 서비스 API 키를 .env 파일에 저장하는 방식이 일반적입니다. 현재 방식은 API 키 유출 시 모든 서비스가 동시에 침해될 위험이 있으며, 에이전트별 접근 범위 제한 및 감사 추적 기능이 부족합니다. HashiCorp Vault나 AWS Secrets Manager와 같은 솔루션은 소규모 팀에게는 과도하거나 맞춤형 통합이 필요하다는 인식이 있습니다. AI 에이전트의 활용이 증가하면서 프로덕션 환경에서의 API 자격 증명 보안 및 관리의 중요성이 부각되고 있습니다. 출처는 Reddit r/LocalLLaMA입니다.

### [AI 코딩 에이전트의 컨텍스트 파일을 자동 생성하고 동기화하는 오픈소스 CLI 도구 Caliber가 250개 이상의 GitHub 스타를 달성했습니다.](https://www.reddit.com/r/artificial/comments/1s80vw7/we_open_sourced_a_tool_that_auto_generates_your)

Caliber는 AI 코딩 에이전트(Claude Code, Cursor, OpenAI Codex 등)가 사용하는 컨텍스트 파일을 코드베이스에서 자동으로 생성하고 관리하는 오픈소스 CLI 도구입니다. 이 도구는 코드베이스를 스캔하여 스택, 명명 규칙, 아키텍처를 파악하고, 프로젝트에 최적화된 컨텍스트 파일을 자동으로 작성합니다. Git hooks를 통해 코드베이스 변경 시 컨텍스트 파일을 자동으로 업데이트하여 항상 최신 상태를 유지합니다. AI 코딩 에이전트의 성능은 제공되는 컨텍스트의 품질에 크게 좌우되는데, Caliber는 이 컨텍스트 작성 및 유지보수의 어려움을 해결하여 AI 개발 생산성을 향상시킵니다. 출처는 Reddit r/artificial입니다.

### [IAB, Agentic AI를 활용한 AI 기반 비디오 성과에 대한 새로운 가이드라인 발표](https://news.google.com/rss/articles/CBMid0FVX3lxTE8xclQ0NzFnbmdINzVVY1dwYUNhX2ZfWmY5dzhpM3MyZUJ2MFlHUHkyQnlIM0dTTjAxdVJ1WjNrQXJKM2tlTnVNWHhPdFFaNHVaQ1FTNlF4MmphUVpqVGpYZDJUMzhwWlo2cERVdVF1Sk8zWnh6Vmd3?oc=5)

IAB는 Agentic AI를 활용하여 비디오 광고의 성과를 최적화하는 새로운 접근 방식을 제시했습니다. (영문 용어: AI-Powered). 이 가이드라인은 AI가 광고 캠페인에서 더욱 능동적인 역할을 수행하도록 돕는 방법을 다룹니다. Agentic AI는 광고 목표 달성을 위해 스스로 판단하고 행동하는 AI 시스템을 의미합니다. AI 기술이 광고 산업 전반에 걸쳐 더욱 심층적으로 통합되고 있으며, 특히 비디오 광고 분야에서 그 영향력이 커지고 있습니다. 출처는 Google News AI Search입니다.

### [AI 에이전트의 사고 사례, 공격 벡터, 실패 모드 및 방어 도구를 정리한 GitHub 리스트가 공개되었습니다.](https://www.reddit.com/r/MachineLearning/comments/1s836un/d_awesome_ai_agent_incidents_a_curated_list_of)

'Awesome AI Agent Incidents'라는 이름의 GitHub 리포지토리가 AI 에이전트 관련 사고 사례를 큐레이션하여 제공합니다. 이 리스트는 AI 에이전트의 다양한 공격 벡터와 실패 모드를 포함하고 있습니다. 자율 AI 에이전트의 방어 도구에 대한 정보도 함께 제공됩니다. AI 에이전트의 활용이 증가함에 따라 발생할 수 있는 잠재적 위험과 취약점에 대한 인식을 높이는 데 기여합니다. 출처는 Reddit r/MachineLearning입니다.

### [프러시아 장군의 장교 유형론을 통해 AI 오정렬(Misalignment) 문제를 분석하는 새로운 관점이 제시되었습니다.](https://www.reddit.com/r/artificial/comments/1s84kuj/von_hammersteins_ghost_what_a_prussian_generals)

Reddit 사용자가 Anthropic 연구팀의 AI 모델 오정렬 행동 일반화 논문을 접하고, 바이마르 공화국 시절의 군사 조직 재편 문제와 유사성을 발견했습니다. 폰 함머슈타인(Von Hammerstein) 장군의 장교 유형론을 AI의 오정렬 문제에 적용하여 분석하는 아이디어를 제시했습니다. AI 연구자가 아닌 개인이 군사 역사 및 시스템 설계 지식을 바탕으로 AI 오정렬에 대한 독창적인 접근법을 제안했습니다. AI의 안전성 및 오정렬 문제는 중요한 연구 분야이며, 다양한 학문 분야의 관점을 통해 해결책을 모색하는 시도가 늘고 있습니다. 출처는 Reddit r/artificial입니다.

### [NVIDIA GTC에서 World Model이 AI의 차세대 핵심 기술로 부상하며 LLM의 한계를 넘어설 것으로 전망됩니다.](https://www.reddit.com/r/artificial/comments/1s828dj/world_models_will_be_the_next_big_thing_byebye)

NVIDIA GTC 컨퍼런스에서 World Model이 AI 연구 커뮤니티의 주요 화두로 떠올랐습니다. (영문 용어: bye-bye). World Model은 단순히 다음 토큰을 예측하는 것을 넘어, 세상이 작동하는 방식을 내부적으로 표현하고 환경을 시뮬레이션하며 인과 관계를 추론할 수 있는 AI 시스템입니다. Jensen Huang은 GTC에서 AI의 다음 개척지는 현실을 이해하고 시뮬레이션할 수 있는 World Model이라고 강조했습니다. World Model은 LLM의 텍스트 패턴 매칭 한계를 넘어 현실 세계를 이해하고 시뮬레이션하는 능력을 제공하여 AI 발전의 새로운 패러다임을 제시합니다. 출처는 Reddit r/artificial입니다.

### [캘리포니아 주지사 뉴섬, AI 보호 및 책임 있는 사용 강화를 위한 행정 명령 서명](https://news.google.com/rss/articles/CBMigAJBVV95cUxNWUdqM2NTdE1BcENPWnNXTzJzcjVjOTJwc25fbVg3NEZOaTZKSTZubngwYWNLMDUzeS0tUDh3eVVrMnlIMHpPM3Naa2dWTUJkbUQ2LVp5Zm9fanNDMHBoVUx5YU12NDdnZDlCZG1aNHk1V0hQcmhDUERnc3Vkd2ZFV0w3eUVyVXlVTWlNMEFFVkR0RWhreTZMMnpDSHgwU0U1VmxlcFhhRHpTNjA1OVV0ak92ZWExb1kzeDV3RjJQc3Uxc3NXTHRMOVZuRHlfMnhNMDd6eXBNRnRXUzhUNndVVm4ydUd3c1hfaFIwZl9mX3dDMzBPQ0pHanpta1o4U0xG?oc=5)

캘리포니아 주지사 개빈 뉴섬이 AI 보호 및 책임 있는 사용을 강화하는 행정 명령을 발표했습니다. (영문 용어: first-of-its-kind, CA.gov). 이 행정 명령은 미국 내에서 AI 보호를 위한 최초의 주 차원 조치입니다. 트럼프 행정부가 AI 관련 보호 조치를 완화하는 움직임에 대응하여 이루어졌습니다. 이번 조치는 연방 정부의 AI 규제 공백 속에서 주 정부가 선제적으로 AI의 윤리적이고 안전한 사용을 위한 기준을 마련하려는 시도로 볼 수 있습니다. 출처는 Google News AI Search입니다.

### [ML 파이프라인에 Unix 철학을 적용하여 모듈화된 교체 가능한 스테이지를 구현하는 오픈소스 프로토타입이 공개되었습니다.](https://www.reddit.com/r/MachineLearning/comments/1s7v4j4/p_unix_philosophy_for_ml_pipelines_modular)

오픈소스 프로토타입은 PII redaction, chunking, dedup, embeddings, eval 등 각 스테이지를 독립적인 플러그인으로 구성했습니다. 각 스테이지는 Unix 도구 간의 파이프처럼 typed contract를 가지며, 이를 통해 스테이지 간의 명확한 인터페이스를 제공합니다. `Feature("docs__pii_redacted__chunked__deduped__embedded__evaluated", ...)`와 같이 `__`를 스테이지 경계로 사용하여 각 부분을 쉽게 교체할 수 있습니다. 기존 ML 파이프라인에서 특정 컴포넌트 변경 시 전체 시스템에 미치는 영향을 파악하기 어려웠던 문제를 해결하여, 개별 스테이지의 성능 변화를 직접 비교할 수 있게 합니다. 출처는 Reddit r/MachineLearning입니다.

### [마이크로소프트, AI 기능 업그레이드 및 Copilot Cowork를 얼리 액세스 고객에게 출시](https://news.google.com/rss/articles/CBMivwFBVV95cUxOOXI4dFM4bkM2N0RZYVVOM1dQeEl0YmVRZjVWMHk2YWpQT3BPbkFhQzNqT0dZNWdxdzFza1dKdG1rUmROajVjWEtWUlQxeDR0cWFwcDlZSHBPbVBHcm9TdEhBbG4zTmZIT1lJajJsVFFkN3hKTEh3cDRTSDlsaHZYY3RCQTFOXzMzaVN1WFNqQnBQMGVmbVRyTERLbkp5Y2RFZmNNU3FHZ2JrRng2dmFuSU9DMzJsdlZzVWJRZDZTRQ?oc=5)

마이크로소프트는 AI 기능을 업그레이드하고 Copilot Cowork를 얼리 액세스 고객에게 제공하기 시작했습니다. (영문 용어: early-access, reuters.com). 이번 업데이트는 AI 기반의 협업 도구인 Copilot의 기능을 확장하여 업무 생산성을 향상시키는 데 중점을 둡니다. 기업들이 AI를 활용하여 업무 효율성을 극대화하려는 트렌드에 맞춰, 마이크로소프트는 Copilot을 통해 AI 기반 협업 솔루션 시장에서의 리더십을 강화하고 있습니다. 출처는 Google News AI Search입니다.

### [GPU-native radiomics 라이브러리 fastrad가 PyRadiomics 대비 최대 25배 빠른 속도를 제공하며, 모든 IBSI feature class를 지원합니다.](https://www.reddit.com/r/MachineLearning/comments/1s82qdb/p_fastrad_gpunative_radiomics_library_25_faster)

fastrad는 PyTorch-native 라이브러리로, 기존 radiomics feature extraction의 de facto 표준인 PyRadiomics의 CPU-only 한계를 극복했습니다. (영문 용어: IBSI-compliant). fastrad는 모든 8가지 IBSI feature class(first-order, shape 2D/3D, GLCM, GLRLM, GLSZM, GLDM, NGTDM)를 native tensor operation으로 구현했습니다. RTX 4070 Ti에서 PyRadiomics 대비 End-to-end 처리 속도가 0.116초 대 2.90초로 25배 빨라졌으며, 단일 클래스에서는 최대 49.3배의 속도 향상을 보였습니다. 의료 영상 분석에서 radiomics feature extraction의 속도 병목 현상을 해결하여, 대규모 데이터셋 처리 및 실시간 분석의 가능성을 크게 확장합니다. 출처는 Reddit r/MachineLearning입니다.

### [AI 안전 현황을 네 가지 가상 그래프로 분석한 Reddit 게시물](https://www.reddit.com/r/artificial/comments/1s7xlir/the_state_of_ai_safety_in_four_fake_graphs)

Reddit r/artificial에 게시된 AI 안전에 대한 분석 자료입니다. AI 안전의 현재 상태를 네 가지 가상의 그래프를 통해 시각적으로 제시합니다. 사용자 tekz가 제출한 링크와 댓글을 포함하고 있습니다. AI 안전에 대한 대중의 관심과 논의가 활발함을 보여줍니다. 출처는 Reddit r/artificial입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [Out of Sight but Not Out of Mind: Hybrid Memory for Dynamic Video World Models](https://huggingface.co/papers/2603.25716)

Hybrid Memory는 동적 비디오 월드 모델이 움직이는 객체에 대한 능동적인 추적과 정적 배경을 위한 아카이브 저장을 결합하여, 가려진 동안에도 동적 주체를 일관되게 추적할 수 있도록 합니다. 기존 비디오 월드 모델은 환경을 정적인 것으로 간주하여, 동적 객체가 시야에서 사라졌다가 다시 나타날 때 추적에 어려움을 겪었습니다. 이 문제를 해결하기 위해 Hybrid Memory는 정적 배경을 위한 아카이브 저장과 동적 주체를 위한 능동적 추적을 동시에 수행하는 새로운 패러다임을 제안합니다. 이를 위해 토큰화된 메모리와 시공간적 검색 메커니즘을 활용하는 HyDRA 아키텍처를 도입했습니다. HM-World 데이터셋을 통해 실험한 결과, 이 방법은 동적 주체 일관성과 전반적인 생성 품질에서 최신 기술보다 뛰어난 성능을 보였습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 2. [ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling](https://huggingface.co/papers/2603.25746)

ShotStream은 인과적 아키텍처 설계, 듀얼 캐시 메모리 메커니즘, 그리고 2단계 증류를 통해 실시간 대화형 다중 샷 비디오 생성을 가능하게 합니다. (영문 용어: Multi-Shot). 기존의 양방향 아키텍처는 대화형 스토리텔링에 필수적인 다중 샷 비디오 생성에서 높은 지연 시간과 제한된 상호작용성을 가졌습니다. ShotStream은 이 문제를 해결하기 위해 다음 샷 생성을 이전 컨텍스트에 조건화하는 새로운 인과적 다중 샷 아키텍처를 제안합니다. 이는 전역 및 로컬 컨텍스트 캐시를 활용하는 듀얼 캐시 메모리 메커니즘과 오류 누적을 완화하는 2단계 증류 전략을 통해 시각적 일관성을 유지하고 효율적인 실시간 프레임 생성을 가능하게 합니다. 결과적으로 사용자는 스트리밍 프롬프트를 통해 진행 중인 내러티브를 동적으로 지시할 수 있습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 3. [PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference](https://huggingface.co/papers/2603.25730)

PackForcing은 계층적 KV-cache 관리와 시공간 압축을 통해 짧은 비디오 훈련만으로도 긴 비디오를 효율적으로 생성할 수 있게 합니다. 기존 Autoregressive 비디오 확산 모델은 긴 비디오 생성 시 KV-cache의 선형적 증가, 시간적 반복, 오류 누적 등의 문제로 인해 효율성이 저해되었습니다. PackForcing은 이러한 문제를 해결하기 위해 기록 컨텍스트를 Sink, Mid, Recent 세 가지 유형으로 나누어 관리하는 새로운 KV-cache 전략을 제안합니다. 이 방법은 초기 앵커 프레임을 보존하고, 중간 컨텍스트를 시공간적으로 압축하며, 최근 토큰은 전체 해상도로 유지하여 시간적 일관성을 확보합니다. 결과적으로 PackForcing은 단일 H200 GPU에서 2분 길이의 832x480 비디오를 16 FPS로 일관성 있게 생성하며, 4GB의 KV 캐시만으로 24배의 시간적 외삽을 가능하게 합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 4. [Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills](https://huggingface.co/papers/2603.25158)

Trace2Skill은 LLM 에이전트의 확장 가능한 스킬 생성을 위해 다양한 실행 궤적을 병렬로 분석하고 이를 전이 가능한 선언적 스킬로 통합하는 프레임워크입니다. (영문 용어: Trajectory-Local). 기존 LLM 에이전트의 스킬 생성 방식은 수동 작성의 확장성 문제나 자동 생성의 취약성 문제를 겪었습니다. Trace2Skill은 인간 전문가가 스킬을 작성하는 방식처럼, 다양한 실행 경험을 전체적으로 분석하여 포괄적인 가이드로 증류합니다. 이 프레임워크는 병렬 서브 에이전트를 통해 궤적별 교훈을 추출하고 귀납적 추론을 통해 통합된 스킬 디렉토리로 만듭니다. 이를 통해 기존 스킬을 심화하거나 새로운 스킬을 생성할 수 있으며, spreadsheet, VisionQA, math reasoning과 같은 복잡한 도메인에서 강력한 성능 향상을 보였습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 5. [MedOpenClaw: Auditable Medical Imaging Agents Reasoning over Uncurated Full Studies](https://huggingface.co/papers/2603.24649)

MedOpenClaw는 VLM이 표준 의료 뷰어 내에서 동적으로 작동하도록 설계된 감사 가능한 런타임으로, 실제 임상 진단 환경에서 3D 의료 볼륨을 탐색하는 능력을 평가합니다. 기존 의료 영상 VLM 평가는 수동으로 선별된 2D 이미지에 의존하여 실제 임상 진단의 핵심 과제인 3D 볼륨 탐색 능력을 간과했습니다. 이를 해결하기 위해 MedOpenClaw는 VLM이 3D Slicer와 같은 표준 의료 도구 내에서 동적으로 작동하도록 하는 감사 가능한 런타임을 제안합니다. 또한, MedFlowBench는 다중 시퀀스 뇌 MRI 및 폐 CT/PET를 포함하는 전체 연구 의료 영상 벤치마크를 도입하여 VLM의 에이전트 역량을 평가합니다. 초기 결과에 따르면 최신 LLM/VLM은 기본 연구 수준 작업을 해결할 수 있지만, 정밀한 공간 기반 추론 능력 부족으로 인해 전문 지원 도구에 접근할 때 성능이 저하되는 것으로 나타났습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 6. [RealChart2Code: Advancing Chart-to-Code Generation with Real Data and Multi-Task Evaluation](https://huggingface.co/papers/2603.25804)

RealChart2Code 벤치마크는 실제 데이터를 기반으로 하는 복잡한 멀티 패널 차트 생성 및 대화형 코드 개선 능력을 평가하여 VLM의 한계를 밝힙니다. (영문 용어: Chart-to-Code, Multi-Task). 기존 Vision-Language Models(VLM)는 실제 데이터로부터 복잡한 멀티 패널 차트를 생성하는 능력이 제대로 평가되지 않았습니다. 이 연구는 2,800개 이상의 실제 데이터 기반 인스턴스를 포함하는 새로운 대규모 벤치마크인 RealChart2Code를 소개합니다. RealChart2Code는 대규모 원시 데이터로부터 차트 생성 및 다중 턴 대화 설정에서 반복적인 코드 개선을 체계적으로 평가하는 최초의 벤치마크입니다. 14개 VLM에 대한 종합적인 평가 결과, 복잡한 플롯 구조와 실제 데이터 처리에서 VLM의 성능 저하와 독점 모델과 오픈 소스 모델 간의 상당한 성능 격차를 확인했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 7. [LongTail Driving Scenarios with Reasoning Traces: The KITScenes LongTail Dataset](https://huggingface.co/papers/2603.23607)

KITScenes LongTail 데이터셋은 자율주행의 Long-Tail 시나리오에 대한 Few-Shot 일반화 및 멀티모달 모델의 Instruction-Following 능력을 향상시키기 위해 다중 뷰 비디오, 궤적, 다국어 추론 흔적을 제공합니다. 자율주행과 같은 실제 환경에서 드문 시나리오에 대한 일반화는 여전히 근본적인 문제입니다. 이 연구는 이러한 문제를 해결하기 위해 Long-Tail 주행 이벤트를 중심으로 설계된 새로운 데이터셋인 KITScenes LongTail을 소개합니다. 이 데이터셋은 다중 뷰 비디오 데이터, 궤적, 높은 수준의 지침 및 상세한 추론 흔적을 제공하여 In-Context Learning 및 Few-Shot 일반화를 용이하게 합니다. 이를 통해 모델의 출력과 계획된 궤적 간의 의미론적 일관성을 측정하고, 안전, 편안함, 지시 따르기를 평가하는 Multi-Maneuver Score (MMS)를 제안하여 기존의 안전 및 편안함 지표를 넘어섭니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 8. [Natural-Language Agent Harnesses](https://huggingface.co/papers/2603.25723)

Natural-Language Agent Harnesses(NLAHs)는 에이전트의 harness 디자인을 자연어로 명시하고 Intelligent Harness Runtime(IHR)을 통해 실행하여 이식성과 재사용성을 높이는 방법을 제안합니다. 기존 에이전트의 harness 디자인은 컨트롤러 코드에 내재되어 있어 전송, 비교 및 연구가 어려웠습니다. 이 연구는 harness의 고수준 제어 로직을 이식 가능한 실행 아티팩트로 외부화하는 것을 목표로 합니다. 이를 위해 편집 가능한 자연어로 harness 동작을 표현하는 Natural-Language Agent Harnesses(NLAHs)와 이를 실행하는 공유 런타임인 Intelligent Harness Runtime(IHR)을 도입했습니다. NLAHs와 IHR은 코딩 및 컴퓨터 사용 벤치마크에서 운영 가능성, 모듈 제거 및 코드-텍스트 harness 마이그레이션에 대한 평가를 통해 그 효과를 입증했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 9. [Know3D: Prompting 3D Generation with Knowledge from Vision-Language Models](https://huggingface.co/papers/2603.22782)

Know3D는 VLM의 지식을 3D 생성 모델에 주입하여 3D 객체의 보이지 않는 뒷면을 언어로 제어하며 생성하는 새로운 프레임워크를 제안합니다. 기존 3D 생성 모델은 단일 뷰 관찰의 모호성과 제한된 3D 훈련 데이터로 인해 보이지 않는 영역의 생성이 불확실하고 제어하기 어려웠습니다. Know3D는 VLM(Vision-Language Model)의 풍부한 지식을 잠재 은닉 상태 주입(latent hidden-state injection)을 통해 3D 생성 프로세스에 통합합니다. 이를 통해 추상적인 텍스트 지시를 관찰되지 않은 영역의 기하학적 재구성과 연결하여, 기존에는 무작위적이었던 뒷면 생성을 의미론적으로 제어 가능한 프로세스로 전환합니다. 이 방법은 3D 생성 모델의 미래 방향에 유망한 가능성을 제시합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 10. [Sommelier: Scalable Open Multi-turn Audio Pre-processing for Full-duplex Speech Language Models](https://huggingface.co/papers/2603.25750)

Sommelier는 Full-duplex Speech Language Models을 위한 고품질 멀티턴 오디오 데이터 전처리 파이프라인을 제안합니다. (영문 용어: Multi-turn, Pre-processing). 기존 Speech Language Models(SLMs)은 실시간 자연스러운 인간-컴퓨터 상호작용을 위한 Full-duplex 시스템 개발에 필요한 고품질 멀티스피커 대화 데이터가 부족하다는 문제에 직면해 있습니다. Sommelier는 이러한 데이터 부족 문제를 해결하고 자연스러운 대화 역학(오버랩, 백채널링 등)을 처리하기 위해 견고하고 확장 가능한 오픈소스 데이터 전처리 파이프라인을 제시합니다. 이 파이프라인은 diarization 오류 및 ASR 환각과 같은 표준 처리 파이프라인의 한계를 극복하여 Full-duplex 모델 개발을 지원합니다. 이를 통해 사용자가 언제든지 LLM을 중단하고 LLM이 자연스럽게 대화에 참여할 수 있는 시스템 구축을 목표로 합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.
