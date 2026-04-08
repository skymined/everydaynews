# IMDIGEST - 2026-04-09

2026-04-09 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-04-09 AI 브리핑입니다. 오늘은 Google Research Blog, TechCrunch AI, TechCrunch AI에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

### [Google Research, 학술 연구 워크플로우 개선을 위한 두 가지 AI 에이전트 공개](https://research.google/blog/improving-the-academic-workflow-introducing-two-ai-agents-for-better-figures-and-peer-review)

Google Research는 학술 연구 과정을 효율화하기 위해 PaperVizAgent와 ScholarPeer 두 가지 AI 에이전트를 도입했습니다. PaperVizAgent는 복잡한 방법론 다이어그램과 통계 플롯 등 학술 논문에 필요한 시각 자료 생성을 돕는 시각화 에이전트입니다. ScholarPeer는 제출된 학술 논문을 자동으로 엄격하게 평가하는 리뷰어 에이전트입니다. AI 기술의 발전이 학술 연구 속도를 가속화함에 따라, AI가 연구 과정의 능동적인 참여자로 활용되는 트렌드를 보여줍니다. 출처는 Google Research Blog입니다.

### [Tubi, ChatGPT 내에 자체 앱을 출시한 최초의 스트리밍 서비스가 되며 AI 기반 콘텐츠 탐색의 새로운 장을 열었습니다.](https://techcrunch.com/2026/04/08/tubi-is-the-first-streamer-to-launch-a-native-app-within-chatgpt)

Fox 소유의 스트리밍 서비스 Tubi가 ChatGPT 앱 스토어에 자체 앱을 출시했습니다. 사용자는 ChatGPT에서 "@Tubi"를 입력한 후 자연어로 영화나 TV 프로그램 추천을 요청할 수 있습니다. Tubi는 30만 개 이상의 영화 및 TV 에피소드 라이브러리를 보유하고 있으며, ChatGPT를 통해 개인화된 추천을 제공합니다. 스트리밍 서비스 간 경쟁이 심화되는 가운데, Tubi는 사용자들이 이미 정보를 찾는 ChatGPT 플랫폼으로 이동하여 콘텐츠 발견(Discovery)의 어려움을 해결하려는 전략적 전환을 보여줍니다. 출처는 TechCrunch AI입니다.

### [Poke, 문자 메시지를 통해 AI 에이전트 기능을 제공하며 일상 업무 자동화를 지원합니다.](https://techcrunch.com/2026/04/08/poke-makes-ai-agents-as-easy-as-sending-a-text)

Poke는 iMessage, SMS, Telegram, WhatsApp 등 친숙한 메시징 인터페이스를 통해 접근 가능한 AI 에이전트 서비스를 제공합니다. 사용자는 Poke를 통해 일상 계획, 캘린더 관리, 건강 및 피트니스 추적, 스마트 홈 제어, 사진 편집 등 다양한 작업을 문자 메시지로 수행할 수 있습니다. Poke는 사용자가 직접 자동화 스크립트를 작성하고 친구들과 공유할 수 있는 기능을 제공하여 개인화된 자동화 경험을 가능하게 합니다. agentic AI 시스템에 대한 수요가 급증하는 가운데, Poke는 비기술적인 사용자들도 쉽게 AI 에이전트를 활용할 수 있는 대중적인 접근 방식을 제시합니다. 출처는 TechCrunch AI입니다.

### [AWS, 헬스케어 및 생명 과학 분야의 AI 에이전트 워크플로우에 Human-in-the-loop (HITL) 통합 방안 제시](https://aws.amazon.com/blogs/machine-learning/human-in-the-loop-constructs-for-agentic-workflows-in-healthcare-and-life-sciences)

AWS는 헬스케어 및 생명 과학 분야에서 AI 에이전트가 임상 데이터 처리, 규제 서류 제출, 의료 코딩 자동화, 신약 개발 가속화 등을 돕는다고 설명합니다. 민감한 헬스케어 데이터와 GxP(Good Practice)와 같은 규제 요건 때문에 주요 의사 결정 지점에서 인간의 감독이 필수적이며, 이를 위해 HITL(Human-in-the-loop)이 중요하다고 강조합니다. AWS는 Strands Agents 프레임워크, Amazon Bedrock AgentCore Runtime 등을 활용하여 HITL을 구현하는 네 가지 실용적인 접근 방식을 제시합니다. 헬스케어 및 생명 과학 분야에서 AI 에이전트의 활용이 증가함에 따라, 규제 준수와 안전을 보장하기 위한 인간 개입의 중요성이 부각되고 있습니다. 출처는 AWS Machine Learning Blog입니다.

### [Amazon Bedrock에서 Reinforcement Fine-Tuning(RFT)을 활용한 모델 최적화 모범 사례가 공개되었습니다.](https://aws.amazon.com/blogs/machine-learning/reinforcement-fine-tuning-on-amazon-bedrock-best-practices)

Amazon Bedrock에서 Reinforcement Fine-Tuning(RFT)을 사용하여 Amazon Nova 및 지원되는 오픈 소스 모델을 맞춤 설정할 수 있습니다. RFT는 대규모 레이블링된 데이터셋 없이 보상 신호(reward signals)를 통해 학습하여 기본 모델 대비 최대 66%의 정확도 향상을 제공하며, 맞춤 설정 비용과 복잡성을 줄여줍니다. 이 게시물은 코드 생성, 구조화된 정보 추출, 콘텐츠 조정과 같은 사용 사례를 위한 데이터셋 설계, 보상 함수 전략, 하이퍼파라미터 튜닝 등 RFT 모범 사례를 다룹니다. RFT는 대규모 레이블링 데이터셋 없이도 모델 성능을 크게 향상시킬 수 있어, 데이터 준비 부담을 줄이고 다양한 산업 분야에서 AI 모델의 적용 가능성을 확대합니다. 출처는 AWS Machine Learning Blog입니다.

### [NVIDIA, Omniverse 라이브러리를 통해 기존 애플리케이션에 Physical AI 기능 통합 지원](https://developer.nvidia.com/blog/integrate-physical-ai-capabilities-into-existing-apps-with-nvidia-omniverse-libraries)

NVIDIA는 GTC 2026에서 로봇 및 디지털 트윈의 핵심 방향으로 Physical AI를 강조했습니다. 기존 Omniverse 플랫폼 외에 모듈형 라이브러리 기반 아키텍처를 추가하여 통합을 용이하게 합니다. RTX 렌더링, PhysX 기반 시뮬레이션, 데이터 스토리지 파이프라인 등 핵심 Omniverse 구성 요소가 ovrtx, ovphysx, ovstorage와 같은 독립형 C API로 제공됩니다. 이는 대규모 로봇 및 산업 배포에서 시뮬레이션 확장, Headless 배포, 기존 CI/CD 시스템과의 통합 문제를 해결하여 산업 소프트웨어 개발의 효율성을 높입니다. 출처는 NVIDIA Developer Blog입니다.

### [Astropad, AI 에이전트 관리에 최적화된 원격 데스크톱 솔루션 Workbench 출시](https://techcrunch.com/2026/04/08/astropads-workbench-reimagines-remote-desktop-for-ai-agents-not-it-support)

Astropad가 AI 에이전트 운영 및 모니터링을 위한 원격 데스크톱 솔루션인 Workbench를 선보였습니다. Workbench는 고품질 스트리밍, 음성 프롬프트 및 명령 지원, 키보드, Apple Pencil, 터치 등 다양한 입력 방식을 제공합니다. iPad 및 iPhone 클라이언트를 통해 모바일 환경에서도 AI 에이전트 관리가 가능하며, 여러 Mac에서 실행되는 에이전트 간 전환 기능을 제공합니다. 기존 원격 데스크톱 도구들이 IT 지원에 중점을 둔 반면, Workbench는 AI 에이전트의 모니터링, 로그 확인, 작업 재시작 등 AI 시대의 새로운 요구사항을 충족시킵니다. 출처는 TechCrunch AI입니다.

### [OpenAI가 AI를 활용한 아동 성 착취 문제에 대응하기 위한 Child Safety Blueprint를 발표했습니다.](https://techcrunch.com/2026/04/08/openai-releases-a-new-safety-blueprint-to-address-the-rise-in-child-sexual-exploitation)

OpenAI는 AI 기술 발전과 함께 증가하는 아동 성 착취 문제에 대응하기 위해 Child Safety Blueprint를 공개했습니다. 이 청사진은 AI 기반 아동 착취 사례의 더 빠른 탐지, 개선된 보고, 효율적인 조사를 목표로 합니다. Internet Watch Foundation(IWF)에 따르면 2025년 상반기에 8,000건 이상의 AI 생성 아동 성 학대 콘텐츠가 탐지되었으며, 이는 전년 대비 14% 증가한 수치입니다. AI 기술의 발전이 아동 성 착취와 같은 심각한 사회적 문제를 야기함에 따라, AI 기업들이 기술적, 정책적 안전 장치를 마련하는 것이 중요해지고 있습니다. 출처는 TechCrunch AI입니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [Anthropic, 새로운 AI 모델 Claude Mythos를 대중에 공개하지 않는 이유 설명](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNdDVzYzIyd1lfM2tpX0RqUDZiMGgwWjZ6UXU0VkswX3Y3bTk5RGM2ZmY4VGZBYlV2QmxfZ2l6RGtWZmxLMS1KSmZic2t1Qm94aHpsU3JMZHNsWm5QRDFzMnNGVTlLQXB0bVFjbHdyS3JkZGJYZEdMaDh3RG9aR1VmTVNLVXZhNGxpY1ZwSXFOMGNpOXBpMUpDd2VId3JPRWs5OW9OQ0RNMkxtZDZLLVNBY3dnVzhrSHZkUE1Z?oc=5)

Anthropic은 최근 개발한 AI 모델 Claude Mythos를 일반 대중에게 공개하지 않기로 결정했습니다. 이 결정은 AI 안전 및 책임 있는 배포에 대한 Anthropic의 신념과 관련이 있습니다. Claude Mythos는 이전 모델보다 향상된 기능을 가지고 있지만, 잠재적 위험에 대한 우려로 인해 신중한 접근을 택했습니다. AI 기술의 발전 속도가 빨라지면서, 개발사들은 모델 배포 시 안전성과 윤리적 문제를 더욱 중요하게 고려하는 추세입니다. 출처는 Google News AI Search입니다.

### [Gemma4가 Gemma3보다 번역 성능이 떨어지며, 챗봇에 특화된 훈련이 문제점으로 지적되었습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1sg7j8m/gemma327b_vs_gemma426b_and_gemma27b_rimworld)

Rimworld Autonomous Translator 벤치마크에서 Gemma3:27b가 Gemma4:26b 및 Gemma4:31b보다 우수한 번역 성능을 보였습니다. Gemma4는 챗봇으로 훈련되어 자연스러운 표현을 선호하지만, 실제로는 존재하지 않는 단어를 추가하고 용어집 제약을 무시하는 경향이 있습니다. Gemma4는 Gemma3에 비해 번역 속도가 2.6배에서 4.3배 느리며, 더 많은 토큰과 시간을 소모합니다. LLM의 특정 목적(예: 챗봇)을 위한 훈련이 다른 중요한 애플리케이션(예: 번역)에서는 오히려 성능 저하를 초래할 수 있음을 보여줍니다. 출처는 Reddit r/LocalLLaMA입니다.

### [Raspberry Pi 5에서 Gemma 4 E2B가 Qwen 3.5 2B를 텍스트 추론 성능에서 앞섰습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1sg621w/benchmarked_gemma_4_e2b_vs_qwen_35_2b_on_a)

Reddit 사용자가 Raspberry Pi 5 (8GB)에서 Ollama를 사용하여 Gemma 4 E2B와 Qwen 3.5 2B 모델의 벤치마크를 수행했습니다. 텍스트 추론 테스트에서 Gemma 4 E2B는 'thinking mode'에서 4/4 정답을 기록하며 Qwen 3.5 2B의 2/4 정답보다 우수한 성능을 보였습니다. 멀티모달 테스트에서는 Qwen 3.5 2B가 'black_hole' 이미지 설명에서 HIT를 기록하며 Gemma 4 E2B보다 나은 결과를 보였습니다. 저전력, 저비용 하드웨어인 Raspberry Pi 5에서 LLM을 구동하는 벤치마크는 엣지 디바이스에서의 AI 활용 가능성을 보여줍니다. 출처는 Reddit r/LocalLLaMA입니다.

### [NVIDIA, National Robotics Week 맞아 Physical AI 연구 성과 및 리소스 공개](https://news.google.com/rss/articles/CBMiakFVX3lxTE96SXR2cGI3dHBReDYxbUw5bWZlUnhSTHY0Z3ZoYXlYVGRId0ZUQ0hrdWtNQlRtQTVEVlNmME1CZ0QtNWN5SHNqb0F4eHUtbVExcG5wNWZoaUdDcUNsRlFWeklSREFDNEl0UGc?oc=5)

NVIDIA는 National Robotics Week를 기념하여 Physical AI 분야의 최신 연구 성과와 리소스를 발표했습니다. 여기에는 로봇이 물리적 세계에서 상호작용하고 학습하는 능력을 향상시키는 기술들이 포함됩니다. NVIDIA는 로봇 개발자들이 AI 기반 로봇을 구축하고 훈련할 수 있도록 다양한 도구와 플랫폼을 제공하고 있습니다. Physical AI는 로봇이 실제 환경에서 더 복잡하고 지능적인 작업을 수행할 수 있도록 하는 핵심 기술로 부상하고 있습니다. 출처는 Google News AI Search입니다.

### [Anthropic, 에이전트의 '두뇌'와 '손'을 분리하여 확장성 높은 Managed Agent 시스템 구축](https://news.google.com/rss/articles/CBMiYkFVX3lxTE5LY3VWakFxdE02bVBBdDNrSEJaY2NqV1ZkZ3hfNUxBeWFXZDdrU21vTTdnSFdNUGNPRVpSMWVyVGp6MWlQWTFYU2JIcVZDdDcwMXcwRlpYNExMeWZBMGxXOWJ3?oc=5)

Anthropic은 에이전트의 '두뇌'(추론 및 계획)와 '손'(도구 사용 및 환경 상호작용)을 분리하는 새로운 아키텍처를 제안했습니다. 이 분리된 접근 방식은 에이전트의 각 구성 요소를 독립적으로 확장하고 개선할 수 있게 합니다. 이를 통해 복잡한 작업을 수행하는 에이전트의 안정성과 효율성을 높이는 것을 목표로 합니다. AI 에이전트의 복잡성이 증가함에 따라, 모듈화된 설계는 확장성 및 관리 용이성 측면에서 중요한 트렌드로 부상하고 있습니다. 출처는 Google News AI Search입니다.

### [AI 에이전트의 파일 시스템 접근 방식에 대한 논의가 활발합니다.](https://www.reddit.com/r/artificial/comments/1sg4mmk/agents_isolated_vrs_working_on_same_file_system)

Reddit r/artificial 커뮤니티에서 AI 에이전트의 파일 시스템 접근 방식에 대한 토론이 진행되고 있습니다. 대부분의 플랫폼은 에이전트를 격리된(isolated) 샌드박스 환경에서 실행하는 방식을 채택하고 있습니다. 사용자들은 신뢰할 수 있는 시스템 내에서 여러 에이전트가 동일한 파일 시스템을 공유하며 작업할 수 있는지에 대한 의견을 나누고 있습니다. AI 에이전트의 협업 및 자원 공유 효율성을 높이는 동시에 보안 및 안정성을 확보하는 방안에 대한 관심이 증가하고 있습니다. 출처는 Reddit r/artificial입니다.

### [Meta가 비용이 많이 드는 슈퍼인텔리전스 팀에서 개발한 첫 AI 모델을 공개했습니다.](https://news.google.com/rss/articles/CBMiywFBVV95cUxPMGlQRHNjbkNMampHRlJWOVkxUTlLdmlUMWZoZTJOa05TZFgtNWppRVpBYk5XT0xVdVRBbHFqSlE2NDRQdHBEcGVaZ2p2dnFrZFhjZThBYjV4SlZFekNkdERsWHhhck1HU0NHUjdRNTY3OTg3TExWNXd2cVd4aldaV2tOVWVGZW5BYzRJYTNkWHJlcklfc3FkTmpOOWl3S3MzZTlOSktEVkFUXzZiU21SUUdXZ3J1UDNZaHIxR3RHQnNzR2VfYTZxRVVaQQ?oc=5)

Meta는 슈퍼인텔리전스 팀이 개발한 첫 AI 모델을 공개했습니다. 이 팀은 Meta의 AI 연구 및 개발을 담당하며, 장기적으로는 인간 수준의 지능을 뛰어넘는 AI를 목표로 합니다. Meta의 이번 AI 모델 공개는 AI 분야에서 선두를 유지하려는 Meta의 전략적 움직임을 보여줍니다. 출처는 Google News AI Search입니다.

### [Anthropic의 새로운 AI 모델 "Mythos"의 위험성에 대한 논의가 시작되었습니다.](https://news.google.com/rss/articles/CBMimAFBVV95cUxObWVrZ1djYW11TWVoSzdTQWJwdEZTdldDQktTSnBCcEFJQzBjcTJpUVlYSFRFcEE3TlB3eDFrQUxUcGRhNE1SUFBkU2lORXpjaDdDQnJsTkgwQ1hfaHg1RW1qSElKMjg5T0NBM0U0aFNYeE94U203N1BVeFB0ZFNqMVh4SjNZbWNBdEJla1otc19tQThDcURDTQ?oc=5)

Anthropic은 새로운 AI 모델인 "Mythos"를 공개했습니다. 이코노미스트는 "Mythos"의 잠재적 위험성에 대해 분석했습니다. "Mythos"는 Anthropic의 최신 AI 기술을 집약한 모델입니다. AI 기술 발전과 함께 모델의 안전성 및 윤리적 문제에 대한 사회적 관심이 증대되고 있습니다. 출처는 Google News AI Search입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [Video-MME-v2: Towards the Next Stage in Benchmarks for Comprehensive Video Understanding](https://huggingface.co/papers/2604.05015)

Video-MME-v2는 기존 벤치마크의 한계를 극복하고 비디오 이해 모델의 견고성과 충실도를 종합적으로 평가하기 위한 새로운 벤치마크를 제시합니다. 기존 비디오 이해 벤치마크는 모델의 실제 능력과 리더보드 점수 간의 불일치가 커지고 있어, 이를 해결하기 위해 Video-MME-v2가 개발되었습니다. 이 벤치마크는 시각 정보 집계부터 시간 역학 모델링, 복잡한 멀티모달 추론에 이르는 점진적인 3단계 계층 구조를 통해 비디오 이해의 복잡성을 체계적으로 평가합니다. 또한, 기존의 질문별 정확도 대신 관련 쿼리 간의 일관성과 다단계 추론의 일관성을 강화하는 그룹 기반 비선형 평가 전략을 제안하여, 파편화되거나 추측 기반의 정확성을 페널티하고 유효한 추론에 의해 뒷받침되는 답변에만 점수를 부여합니다. 엄격한 인간 주석 파이프라인을 통해 데이터 품질을 보장하며, 현재 최고 모델인 Gemini-3-Pro와 인간 전문가 사이에 상당한 격차가 있음을 보여줍니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 2. [Claw-Eval: Toward Trustworthy Evaluation of Autonomous Agents](https://huggingface.co/papers/2604.06132)

Claw-Eval은 자율 에이전트 벤치마크의 한계를 극복하기 위해 다중 모달리티, 궤적 인식 채점 및 안전성 평가를 포함하는 포괄적인 평가 스위트를 제안합니다. 기존 에이전트 벤치마크는 최종 결과만 확인하는 궤적 불투명 채점, 불충분한 안전성 및 견고성 평가, 그리고 좁은 모달리티 커버리지라는 세 가지 주요 한계를 가지고 있습니다. Claw-Eval은 이러한 문제들을 해결하기 위해 9개 카테고리에 걸쳐 300개의 인간 검증 태스크로 구성된 엔드투엔드 평가 스위트를 도입합니다. 이 스위트는 에이전트의 모든 행동을 세 가지 독립적인 증거 채널을 통해 기록하여 궤적 인식 채점을 가능하게 하며, Completion, Safety, Robustness를 평가하여 에이전트의 진정한 능력을 측정합니다. 실험 결과, 궤적 불투명 평가는 안전 위반 및 견고성 실패를 놓치는 등 신뢰할 수 없으며, Claw-Eval이 이러한 문제들을 효과적으로 포착함을 보여줍니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 3. [Learning to Retrieve from Agent Trajectories](https://huggingface.co/papers/2604.04949)

LRAT는 LLM 기반 검색 에이전트의 다단계 상호작용 데이터에서 검색 모델을 직접 학습시키는 새로운 패러다임을 제안합니다. 기존 정보 검색(IR) 시스템은 사람 사용자에 맞춰 학습되었지만, LLM 기반 검색 에이전트의 등장으로 에이전트가 검색 결과를 소비하는 방식과 기존 모델 간에 불일치가 발생합니다. 이 연구는 에이전트의 다단계 상호작용 데이터에서 직접 감독을 추출하여 검색 모델을 학습하는 'Learning to Retrieve from Agent Trajectories' (LRAT)라는 새로운 훈련 패러다임을 소개합니다. LRAT는 에이전트 궤적에서 문서 유용성을 나타내는 행동 신호를 식별하고, 가중치 최적화를 통해 관련성 강도를 통합하여 고품질 검색 감독을 추출합니다. 이를 통해 LRAT로 훈련된 검색기는 증거 회수율, 엔드투엔드 작업 성공률 및 실행 가능성을 일관되게 향상시킵니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 4. [ACES: Who Tests the Tests? Leave-One-Out AUC Consistency for Code Generation](https://huggingface.co/papers/2604.03922)

ACES는 LLM이 생성한 코드 후보 중 올바른 코드를 선별하기 위해, Leave-One-Out AUC Consistency를 활용하여 테스트의 신뢰도를 평가하고 순위를 매기는 새로운 방법을 제안합니다. LLM이 생성한 코드 후보를 LLM이 생성한 테스트로 검증하는 과정에서 테스트 자체의 신뢰성 문제가 발생합니다. 기존 방법들은 모든 테스트를 동등하게 취급하거나 임시방편적인 휴리스틱에 의존했지만, ACES는 테스트의 정확성을 직접 판단하는 대신, 테스트가 올바른 코드와 잘못된 코드를 얼마나 잘 구별하는지에 집중합니다. Leave-One-Out 평가와 LOO-AUC(Leave-One-Out AUC)를 통해 각 테스트의 분별력을 측정하고, 이를 기반으로 ACES-C와 ACES-O 두 가지 변형을 제안하여 코드 생성 벤치마크에서 SOTA Pass@k 성능을 달성합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 5. [GBQA: A Game Benchmark for Evaluating LLMs as Quality Assurance Engineers](https://huggingface.co/papers/2604.02648)

GBQA는 LLM이 QA 엔지니어로서 게임 환경에서 버그를 자율적으로 발견하는 능력을 평가하기 위한 새로운 벤치마크를 제시합니다. 최신 소프트웨어 개발에서 버그를 자율적으로 발견하는 것은 LLM에게 여전히 어려운 과제입니다. 이 연구는 게임 개발을 대표적인 도메인으로 삼아, 30개의 게임과 124개의 사람이 검증한 버그를 포함하는 GBQA 벤치마크를 도입했습니다. 이 벤치마크는 멀티 에이전트 시스템을 사용하여 게임을 개발하고 버그를 주입하며, ReAct 루프와 메모리 메커니즘을 갖춘 인터랙티브 에이전트를 제공하여 LLM의 버그 탐지 능력을 평가합니다. 실험 결과, 최신 LLM들도 자율적인 버그 발견에 큰 어려움을 겪으며, 가장 성능이 좋은 Claude-4.6-Opus 모델조차 검증된 버그의 48.39%만을 식별했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 6. [ThinkTwice: Jointly Optimizing Large Language Models for Reasoning and Self-Refinement](https://huggingface.co/papers/2604.01591)

ThinkTwice는 Group Relative Policy Optimization을 기반으로 LLM의 추론 및 자체 개선 능력을 동시에 최적화하는 2단계 프레임워크를 제안하여 수학적 추론 벤치마크에서 성능 향상을 입증했습니다. (영문 용어: Self-Refinement). 이 연구는 LLM이 추론 문제를 해결하고 자신의 답변을 개선하는 능력을 동시에 향상시키는 문제를 다룹니다. ThinkTwice는 Group Relative Policy Optimization(GRPO)을 활용하여, 첫 번째 단계에서는 추론 문제 해결에 모델을 최적화하고, 두 번째 단계에서는 동일한 문제에 대한 자신의 솔루션을 개선하는 데 최적화하는 2단계 프레임워크를 사용합니다. 이 방법은 Qwen3-4B 및 Olmo3-7B를 포함한 여러 수학적 추론 벤치마크에서 기존 온라인 정책 최적화 기준선보다 추론 및 개선 성능을 크게 향상시켰습니다. 특히, 훈련 역학 분석을 통해 초기에는 오류를 수정하고 점차적으로 올바른 솔루션을 보존하는 'rectify-then-fortify' 커리큘럼이 자연스럽게 형성됨을 발견했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 7. [Beyond Accuracy: Unveiling Inefficiency Patterns in Tool-Integrated Reasoning](https://huggingface.co/papers/2604.05404)

이 연구는 Tool-Integrated Reasoning 시나리오에서 KV-Cache 비효율성과 긴 도구 응답을 고려하여 실제 추론 지연 시간과 더 잘 상관관계가 있는 하드웨어 인식 효율성 지표인 PTE(Prefill Token Equivalents)를 제안합니다. LLM이 외부 도구 호출과 추론을 번갈아 수행하는 Tool-Integrated Reasoning(TIR) 시나리오에서 기존의 토큰 수나 도구 호출 수와 같은 효율성 지표는 실제 모델 추론 지연 시간을 정확히 반영하지 못합니다. 연구진은 KV-Cache 비효율성과 긴 도구 응답 시나리오를 명시적으로 고려하여 내부 추론 및 외부 도구 사용 비용을 통합하는 하드웨어 인식 TIR 효율성 지표인 PTE(Prefill Token Equivalents)를 도입했습니다. 고동시성 산업 환경에서의 검증 결과, PTE는 표준 토큰 수보다 실제 지연 시간과 훨씬 더 잘 일치하며 다양한 하드웨어 프로필에서 일관된 효율성 순위를 유지했습니다. 또한, TIR 벤치마크 실험을 통해 네 가지 비효율성 패턴을 식별하고, PTE 비용이 높은 경로가 추론 정확도가 낮아 단순히 더 많은 도구를 사용하는 것이 답변의 품질을 향상시키지 않음을 발견했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 8. [Vanast: Virtual Try-On with Human Image Animation via Synthetic Triplet Supervision](https://huggingface.co/papers/2604.04934)

Vanast는 단일 프레임워크에서 이미지 기반 가상 시착과 포즈 기반 애니메이션을 결합하여 의류가 전이된 사람 애니메이션 비디오를 생성하며, Triplet Supervision과 Dual Module 아키텍처를 통해 신원 이탈 및 의류 왜곡 문제를 해결합니다. (영문 용어: Try-On). 기존의 가상 시착 및 포즈 기반 애니메이션 파이프라인은 두 단계를 분리하여 신원 이탈, 의류 왜곡, 앞뒤 불일치 등의 문제를 야기했습니다. Vanast는 이 문제를 해결하기 위해 전체 과정을 단일 통합 단계로 수행하여 일관된 합성을 달성합니다. 이를 위해 대규모 Triplet Supervision을 구축하고, Dual Module 아키텍처를 도입하여 훈련을 안정화하고 의류 정확도, 포즈 준수 및 신원 보존을 개선합니다. 결과적으로 Vanast는 다양한 의류 유형에 걸쳐 고품질의 신원 일관된 애니메이션을 생성합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 9. [Watch Before You Answer: Learning from Visually Grounded Post-Training](https://huggingface.co/papers/2604.05117)

VidGround는 시각적으로 근거한 질문만을 사용하여 Vision-Language 모델의 비디오 이해 성능을 향상시키는 새로운 사후 훈련(post-training) 방법을 제안합니다. Vision-Language 모델(VLM)은 비디오 이해에서 텍스트 기반 편향으로 인해 어려움을 겪으며, 기존 벤치마크 및 데이터셋의 상당수 질문이 시각적 정보 없이 텍스트만으로 답변 가능했습니다. 이 연구는 이러한 문제를 해결하기 위해 VidGround를 도입합니다. VidGround는 언어적 편향이 없는 시각적으로 근거한 질문만을 사후 훈련에 사용하여 VLM의 비디오 이해 능력을 개선합니다. 이 간단한 기술은 기존 데이터셋의 69.1%만 사용하면서도 성능을 최대 6.2점 향상시키며, 데이터 품질이 VLM 비디오 이해 개선의 주요 병목임을 강조합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 10. [How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings](https://huggingface.co/papers/2604.04323)

LLM 에이전트의 Agentic Skills 활용 능력을 현실적인 조건에서 벤치마킹하고, 성능 저하를 완화하기 위한 skill refinement 전략을 연구했습니다. 기존 LLM 에이전트의 스킬 벤치마킹은 이상적인 조건에 초점을 맞췄지만, 본 연구는 34,000개의 실제 스킬 컬렉션에서 에이전트가 직접 스킬을 검색하고 선택해야 하는 현실적인 시나리오에서 스킬 활용도를 평가했습니다. 연구 결과, 현실적인 조건에서 스킬의 이점이 크게 감소하며, 가장 어려운 시나리오에서는 스킬이 없는 베이스라인과 유사한 성능을 보였습니다. 이러한 성능 저하를 개선하기 위해 query-specific 및 query-agnostic refinement 전략을 탐구했으며, query-specific refinement가 초기 스킬의 관련성과 품질이 적절할 때 성능을 크게 회복시킬 수 있음을 입증했습니다. 또한 Terminal-Bench 2.0에서 검색 및 refinement 전략의 일반성을 보여주며 Claude의 pass rate를 향상시켰습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.
