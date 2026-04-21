# IMDIGEST - 2026-04-22

2026-04-22 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-04-22 AI 브리핑입니다. 오늘은 Google Research Blog, TechCrunch AI, TechCrunch AI에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

### [Google Research, 성공 및 실패 경험을 통해 추론 전략을 학습하는 새로운 에이전트 메모리 프레임워크 ReasoningBank를 공개했습니다.](https://research.google/blog/reasoningbank-enabling-agents-to-learn-from-experience)

ReasoningBank는 에이전트가 배포 후에도 경험을 통해 지속적으로 학습할 수 있도록 성공 및 실패 경험을 활용하여 일반화 가능한 추론 전략을 추출하는 새로운 에이전트 메모리 프레임워크입니다. 기존 에이전트 메모리 방식은 모든 행동을 기록하거나 성공적인 시도만 요약하여 저장하는 방식이었지만, ReasoningBank는 고수준의 추론 패턴을 추출하고 실패 경험에서도 학습합니다. 이 프레임워크는 ICLR 논문 "ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory"에서 소개되었으며, GitHub에서 관련 자료를 확인할 수 있습니다. 에이전트가 실제 환경에서 장기적인 역할을 수행함에 따라, 성공과 실패 경험을 분석하고 학습하는 능력이 중요해지고 있으며, ReasoningBank는 이러한 요구를 충족하는 핵심적인 기술입니다. 출처는 Google Research Blog입니다.

### [AI 연구소 NeoCognition, 인간처럼 학습하는 AI 에이전트 개발을 위해 4천만 달러 시드 펀딩 유치](https://techcrunch.com/2026/04/21/ai-research-lab-neocognition-lands-40m-seed-to-build-agents-that-learn-like-humans)

Ohio State 교수가 설립한 NeoCognition은 인간처럼 스스로 학습하여 특정 도메인의 전문가가 될 수 있는 AI 에이전트 시스템을 개발합니다. 이 스타트업은 Cambium Capital과 Walden Catalyst Ventures가 공동 주도하고 Vista Equity Partners 등이 참여한 4천만 달러 규모의 시드 펀딩을 유치했습니다. 현재 AI 에이전트들은 작업 성공률이 약 50%에 불과하여 신뢰할 수 없는 수준이며, NeoCognition은 이러한 한계를 극복하고자 합니다. 현재 AI 에이전트의 낮은 신뢰성과 일관성 부족 문제를 해결하려는 시도로, AI 에이전트 기술의 상용화 및 실제 적용 가능성을 높이는 데 기여할 것입니다. 출처는 TechCrunch AI입니다.

### [ChatGPT의 새로운 Images 2.0 모델이 텍스트 생성 능력을 크게 향상시켜 AI 이미지와 인간 제작 이미지의 구분이 어려워지고 있습니다.](https://techcrunch.com/2026/04/21/chatgpts-new-images-2-0-model-is-surprisingly-good-at-generating-text)

ChatGPT Images 2.0 모델은 멕시칸 레스토랑 메뉴와 같이 이미지 내 텍스트를 정확하게 생성할 수 있게 되었습니다. 과거 AI 이미지 생성기는 'enchuita', 'churiros'와 같은 오타를 자주 만들어냈으나, 이제는 실제 사용 가능한 수준의 텍스트를 생성합니다. 기존 DALL-E 3와 같은 확산 모델(diffusion models)은 이미지 내 텍스트 처리에서 한계가 있었습니다. AI 이미지 생성 기술이 텍스트 처리 능력을 강화하면서, AI가 생성한 콘텐츠의 현실성이 더욱 높아져 인간과 AI의 경계가 모호해지고 있습니다. 출처는 TechCrunch AI입니다.

### [Sam Altman이 Anthropic의 사이버 보안 AI 모델 Mythos에 대해 "공포 마케팅"이라고 비판했습니다.](https://techcrunch.com/2026/04/21/sam-altman-throws-shade-at-anthropics-cyber-model-mythos-fear-based-marketing)

OpenAI CEO Sam Altman은 팟캐스트 Core Memory에 출연하여 Anthropic의 새로운 사이버 보안 모델 Mythos를 비판했습니다. (영문 용어: fear-based). Altman은 Anthropic이 Mythos를 사이버 범죄자들이 악용할 수 있을 만큼 강력하다고 주장하며 대중에게 공개하지 않는 것이 "공포 기반 마케팅"이라고 지적했습니다. Anthropic은 이달 초 Mythos를 소수의 기업 고객에게만 공개했으며, 모델의 강력함 때문에 대중 공개를 우려하고 있다고 밝혔습니다. AI 안전 및 윤리적 배포에 대한 논의가 계속되는 가운데, AI 기업 간의 경쟁 심화와 마케팅 전략에 대한 비판적 시각을 보여줍니다. 출처는 TechCrunch AI입니다.

### [Amazon Bedrock에서 Claude Cowork를 실행하여 조직 전체의 AI 도입을 확대합니다.](https://aws.amazon.com/blogs/machine-learning/from-developer-desks-to-the-whole-organization-running-claude-cowork-in-amazon-bedrock)

Amazon Bedrock에서 Claude Cowork 및 Claude Code Desktop을 직접 또는 LLM 게이트웨이를 통해 실행할 수 있습니다. Claude Cowork는 문서 읽기, 다단계 연구 실행, 파일 처리 및 작업 완료를 지원하는 데스크톱 애플리케이션으로, 조직 내 모든 지식 근로자에게 AI를 확장할 수 있습니다. Amazon Bedrock은 기존 AWS 환경 내에서 구축, 엔터프라이즈 보안 및 지역 데이터 상주 유지, 추론 확장을 가능하게 합니다. 기업들은 Amazon Bedrock을 통해 Claude Code를 사용하여 개발자 생산성을 높이고 배포를 가속화하고 있습니다. 출처는 AWS Machine Learning Blog입니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [제프 베이조스의 "Project Prometheus"가 "Physical AI" 개발을 위해 380억 달러 가치로 100억 달러 투자를 유치하고 있습니다.](https://www.reddit.com/r/artificial/comments/1srwofc/jeff_bezoss_project_prometheus_is_raising_10b_at)

제프 베이조스가 아마존을 떠난 후 첫 운영 역할로 공동 CEO Vik Bajaj와 함께 "Project Prometheus"를 설립했습니다. 이 스타트업은 물리 법칙을 이해하는 "Physical AI"를 개발하여 항공우주, 자동차, 로봇 공학 등 물리적 제품 분야에 혁신을 가져오는 것을 목표로 합니다. JPMorgan 및 BlackRock과 같은 월스트리트 거대 기업의 지원을 받아 100억 달러 규모의 자금 조달 라운드를 진행 중이며, 기업 가치는 380억 달러로 평가됩니다. 이는 AI 기술이 소프트웨어 영역을 넘어 물리적 세계와 상호작용하고 혁신하는 "Physical AI" 분야로 확장되고 있음을 보여줍니다. 출처는 Reddit r/artificial입니다.

### [이미지 조작에 특화된 LLM 에이전트 PixelClaw가 오픈소스로 공개되었습니다.](https://www.reddit.com/r/artificial/comments/1srsod4/pixelclaw_an_llm_agent_for_image_manipulation)

PixelClaw는 대화, 계획, 도구 사용을 위한 LLM과 이미지 생성/AI 기반 편집 기능을 결합합니다. gpt-image를 통한 이미지 생성 및 편집, rembg를 통한 배경 제거, pyxelate를 이용한 픽셀화 등 다양한 이미지 처리 기능을 제공합니다. Whisper를 이용한 STT와 Kokoro 및 HALO를 이용한 TTS 기능을 포함하며, Raylib 기반의 UI를 제공합니다. LLM을 활용하여 복잡한 이미지 처리 작업을 자동화하고 사용자 접근성을 높이는 AI 에이전트 개발 트렌드를 보여줍니다. 출처는 Reddit r/artificial입니다.

### [Physical AI가 로봇 공학의 산업 전반에 걸쳐 혁신을 주도하고 있습니다.](https://news.google.com/rss/articles/CBMidkFVX3lxTFA1ZVM2Tlc1V0ZHZm5xSDkzdnJkd1RXZ2RNM2o2Z0wtWEIzOTNtWGxOekxHamhZY0pENTVZQXBJTlRPVGMzcGdRTWtxS2tpU0RhTDhrOHpPcjJJb2JYc1VFVzB4V0kwWXpEU3Q5MVM2U3c0RWF5Unc?oc=5)

Physical AI는 로봇이 물리적 세계와 상호 작용하고 학습하는 방식을 변화시키는 기술입니다. 기존 로봇이 프로그래밍된 작업을 수행하는 반면, Physical AI 로봇은 예측 불가능한 환경에 적응하고 새로운 작업을 학습할 수 있습니다. 이는 제조, 물류, 헬스케어 등 다양한 산업에서 로봇의 활용 범위를 확장하고 있습니다. Physical AI는 로봇이 더욱 자율적이고 유연하게 작동하도록 하여 생산성 향상과 비용 절감에 기여합니다. 출처는 Google News AI Search입니다.

### [사용자가 직접 운영하는 로컬 LLM인 Gemma 4 31B가 번역 품질에서 최신 Chat GPT 및 Gemini Chat을 능가하며 모델 성능 저하 및 검열 문제를 부각시켰습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1ss2lib/an_actual_example_of_if_you_dont_run_it_you_dont)

사용자는 중국 소설 번역을 위해 다양한 AI 모델을 사용했으며, 초기에는 GPT 4o가 가장 우수한 성능을 보였습니다. GPT 4o는 5.2 및 5.3 업데이트를 거치면서 번역 품질이 저하되고 검열 필터링이 발생하기 시작했습니다. 최근 테스트에서 로컬에서 실행되는 Gemma 4 31B 모델이 번역 품질 면에서 GPT 4o의 전성기 수준과 유사하며, Chat GPT 및 Gemini Chat보다 우수한 성능을 보였습니다. 클라우드 기반 LLM의 성능 저하 및 검열 문제가 사용자들 사이에서 직접 모델을 운영하는 "If you don't run it, you don't own it" 철학을 강화하고 있습니다. 출처는 Reddit r/LocalLLaMA입니다.

### [Qwen 3.6 35B-A3B 모델의 이미지 처리 속도 저하에 대한 사용자 문의가 제기되었습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1ss1mco/qwen_36_35ba3b_takes_a_long_time_at_image)

한 Reddit 사용자가 Qwen 3.6 35B-A3B 모델을 사용하여 이미지 처리 시 추론 시작까지 1분 35초가 소요된다고 보고했습니다. 동일한 시스템에서 Gemma4 모델은 이미지 처리에 10초밖에 걸리지 않아 Qwen 모델과의 성능 차이가 두드러집니다. 사용자는 RTX 4080 GPU와 96GB RAM을 포함한 고사양 시스템을 사용하고 있으며, 텍스트 채팅에서는 두 모델 모두 65 t/s의 유사한 속도를 보였습니다. 대규모 언어 모델(LLM)의 멀티모달 기능이 중요해지면서, 이미지 처리와 같은 비텍스트 데이터 처리 성능이 사용자 경험에 큰 영향을 미치고 있습니다. 출처는 Reddit r/LocalLLaMA입니다.

### [OpenAI, ChatGPT가 연루된 총격 사건으로 형사 조사를 받게 되었습니다.](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBtQzhxOThXRDlYNWI4TFJ2TFlsQlNhdG5kVm5Ta0M1YkxzLTdyNWcyeHB4aHlsWkF5TkliRXY2eDVWZ2NaeTQteGhzaUFBVzNLN1NNYzE4Y2FwUQ?oc=5)

BBC에 따르면 OpenAI는 ChatGPT가 총격 사건에 연루된 혐의로 형사 조사를 받고 있습니다. 이번 조사는 ChatGPT의 콘텐츠가 실제 범죄 행위에 영향을 미쳤는지 여부를 밝히는 데 중점을 둘 것입니다. AI 기술의 윤리적 책임과 실제 사회에 미치는 영향에 대한 논의가 심화될 것으로 예상됩니다. 출처는 Google News AI Search입니다.

### [Amazon Bedrock에서 Claude Cowork를 조직 전체로 확장하여 AI 도입 가속화](https://news.google.com/rss/articles/CBMizgFBVV95cUxPQ2l1RXZHUktYTExISnBTenFYZm5uclBmWnhMSGF1UmtaVXFDSlN4ZG9UR0VNVUptMF9yR3poYnZIYW1od1h3M3NWbUpFZHVTMUR2ak0wNTVUWVRQam9BRkV4MEhOSExncjZKcUJEOU0wN0tTWFk3XzVuMGtUa2pfMzVXWXdlRlM1WGZlLV9nMzQxNEg4Y1NSTVdYbU5TSjVUMGxRaWc3MUJaaHBaSExHTW1mcEVkdWtZbHBncWNWSVVfcTV2MVVnZzFpY3lYdw?oc=5)

Amazon Bedrock을 통해 개발자 수준에서 조직 전체로 Claude Cowork 사용을 확대합니다. Claude Cowork는 Amazon Bedrock에서 실행되어 기업의 AI 도입을 가속화하는 데 기여합니다. 이 확장은 기업이 AI 모델을 더 쉽게 통합하고 활용할 수 있도록 지원합니다. 기업들이 생성형 AI 모델을 개발자 수준을 넘어 전사적으로 활용하려는 트렌드를 반영합니다. 출처는 Google News AI Search입니다.

### [Claude Pro 플랜에서 코드 기능이 제거되면서 로컬 모델로의 전환이 주목받고 있습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1ss23b8/claude_code_removed_from_claude_pro_plan_better)

Claude Pro 플랜에서 코드 기능이 사라졌습니다. 사용자들은 Kimi K2.6과 같은 모델을 제공하는 OpenCode Go 코딩 플랜으로 전환을 고려하고 있습니다. OpenCode Go는 월 $20로 Claude Pro $100 플랜과 유사한 토큰 양을 제공합니다. 클라우드 기반 AI 서비스의 기능 변경이 사용자들의 로컬 AI 모델 사용으로의 전환을 가속화하고 있습니다. 출처는 Reddit r/LocalLLaMA입니다.

### [llama.cpp 사용자가 단일 3090 GPU에서 Qwen3.6 모델 실행 시 성능 최적화에 대한 도움을 요청했습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1ss1rbx/need_help_with_llamacpp_qwen36_configuration_on_a)

Reddit r/LocalLLaMA의 한 사용자가 단일 3090 GPU(48GB RAM) 환경에서 Qwen3.6 35B A3B 모델을 llama.cpp로 실행할 때 발생하는 성능 저하(stuttering) 문제에 대한 도움을 요청했습니다. 사용자는 llama-server router 기능을 config.ini 파일과 함께 사용하고 있으며, VRAM이 완전히 채워져 성능 문제가 발생한다고 설명했습니다. 제공된 설정 파일에는 'general tasks' 및 'precise coding'을 위한 두 가지 Qwen3.6 35B A3B 모델 구성이 포함되어 있습니다. 이는 로컬 환경에서 대규모 언어 모델(LLM)을 효율적으로 실행하기 위한 llama.cpp와 같은 도구의 중요성을 보여줍니다. 출처는 Reddit r/LocalLLaMA입니다.

### [Google Gemini 앱이 이제 Mac에서도 사용 가능해지며 AI 접근성을 확장합니다.](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPeXdQVmxFWlVnUWE3WWpZZVZ3UURhZUFMalhyOGF5UGYyeVJEQ09ITlVHblh4d0VINjdLb1FLbVRxaXZOOFhhdWlDZGlmOUxlLVBSNEpBbjJyd0NCRFQwVHh6YU5WVU9zWWF0bGMtREdyZXZMSVZkcUozWGFoZWVnNFU3Rmp4XzhpRmk0?oc=5)

Google의 AI 어시스턴트 Gemini 앱이 Mac 기기에서도 공식적으로 출시되었습니다. (영문 용어: blog.google). 사용자들은 이제 Mac에서 Gemini를 통해 텍스트 생성, 정보 요약, 아이디어 구상 등 다양한 AI 기능을 활용할 수 있습니다. Gemini는 Google Workspace 앱과 연동되어 Gmail, Docs 등에서 AI 기능을 직접 사용할 수 있습니다. Google이 Gemini 앱을 Mac으로 확장함으로써, AI 어시스턴트의 접근성을 높이고 더 많은 사용자가 다양한 기기에서 AI를 활용할 수 있도록 지원합니다. 출처는 Google News AI Search입니다.

### [개인이 M2 MacBook Air에서 Diffusion Language Model을 직접 구현하고 학습시켜 화제입니다.](https://www.reddit.com/r/MachineLearning/comments/1srufft/bulding_my_own_diffusion_language_model_from)

한 Reddit 사용자가 AI 코드 생성 도구 없이 Diffusion Language Model을 처음부터 직접 구현했습니다. 해당 모델은 약 750만 개의 파라미터를 가지며, Karpathy의 tiny Shakespeare 데이터셋으로 M2 MacBook Air에서 학습되었습니다. 짧은 학습 시간에도 불구하고 "to be, " 프롬프트에 대해 의미 있는 텍스트를 생성했습니다. AI 코드 생성 의존도를 줄이고자 하는 개발자들에게 직접 구현의 가능성과 교육적 가치를 보여주는 사례입니다. 출처는 Reddit r/MachineLearning입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [Extending One-Step Image Generation from Class Labels to Text via Discriminative Text Representation](https://huggingface.co/papers/2604.18168)

MeanFlow의 이미지 생성 기능을 클래스 레이블에서 텍스트 입력으로 확장하기 위해 LLM 기반 텍스트 인코더를 통합하고, 텍스트 특징 표현의 판별력을 높여 효율적인 텍스트 조건부 합성을 가능하게 했습니다. (영문 용어: One-Step). 기존 MeanFlow는 주로 클래스-이미지 생성에 초점을 맞췄으나, 본 연구는 이를 유연한 텍스트 입력으로 확장하는 것을 목표로 합니다. 강력한 LLM 기반 텍스트 인코더를 통합하려 했으나, MeanFlow의 제한된 정제 단계(예: 1단계)로 인해 텍스트 특징 표현의 판별력이 충분히 높아야 한다는 문제에 직면했습니다. 연구팀은 이러한 통찰력을 바탕으로 필요한 의미론적 속성을 가진 LLM 기반 텍스트 인코더를 활용하고 MeanFlow 생성 프로세스를 조정하여, 텍스트 조건부 합성을 효율적으로 구현했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 2. [OneVL: One-Step Latent Reasoning and Planning with Vision-Language Explanation](https://huggingface.co/papers/2604.18486)

OneVL은 자율주행을 위한 통합 VLA 및 World Model 프레임워크로, 시각-언어 설명을 통해 잠재 추론 및 계획을 한 단계로 수행하여 빠르고 정확한 궤적 예측을 가능하게 합니다. (영문 용어: One-Step, Vision-Language). 기존 Chain-of-Thought (CoT) 추론 방식은 자율주행 궤적 예측에 효과적이지만, 순차적인 특성으로 인해 실시간 배포에 제약이 있었습니다. OneVL은 이러한 문제를 해결하기 위해 언어 및 시각적 World Model 감독을 통합하여 잠재 CoT 추론의 정확도와 속도를 향상시킵니다. 특히, 미래 프레임 토큰을 예측하는 시각적 World Model 디코더를 도입하여 잠재 공간이 도로 기하학, 에이전트 움직임, 환경 변화의 인과적 역학을 내면화하도록 강제합니다. 이를 통해 OneVL은 명시적 CoT를 능가하는 최초의 잠재 CoT 방법이 되었으며, 4가지 벤치마크에서 최첨단 성능을 달성했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 3. [Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence](https://huggingface.co/papers/2604.18292)

Agent-World는 자율적인 환경 발견과 지속적인 학습을 통해 일반 에이전트 지능을 발전시키는 자기 진화 훈련 프레임워크를 제안합니다. (영문 용어: Real-World). 기존 에이전트 훈련은 현실적인 환경 부족과 평생 학습 메커니즘의 한계로 인해 강력한 에이전트 개발에 어려움을 겪었습니다. Agent-World는 Agentic Environment-Task Discovery를 통해 수천 개의 실제 환경 테마에서 실행 가능한 도구 생태계를 탐색하고 검증 가능한 작업을 합성하며, Continuous Self-Evolving Agent Training을 통해 다중 환경 강화 학습과 자기 진화 에이전트 아레나를 결합합니다. 이를 통해 에이전트 정책과 환경의 공동 진화를 가능하게 하여 23개의 벤치마크에서 기존 모델들을 능가하는 성능을 보여줍니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 4. [OpenGame: Open Agentic Coding for Games](https://huggingface.co/papers/2604.18394)

OpenGame는 웹 게임 생성을 위한 오픈소스 에이전트 프레임워크로, GameCoder-27B라는 특화된 코드 LLM과 OpenGame-Bench 평가 파이프라인을 활용하여 엔드투엔드 게임 개발을 가능하게 합니다. 기존 LLM과 코드 에이전트는 고수준 디자인에서 완전한 플레이 가능한 게임을 생성하는 데 어려움을 겪었으며, 파일 간 불일치나 논리적 비일관성 문제에 직면했습니다. OpenGame는 Game Skill이라는 재사용 가능한 기능을 통해 안정적인 아키텍처를 구축하고 통합 오류를 체계적으로 수정하며, 게임 엔진에 특화된 GameCoder-27B LLM을 활용합니다. 또한, 빌드 상태, 시각적 유용성, 의도 정렬을 평가하는 OpenGame-Bench를 도입하여 인터랙티브 플레이 가능성을 검증합니다. 이를 통해 150가지 다양한 게임 프롬프트에서 효과적인 게임 생성을 입증했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 5. [MultiWorld: Scalable Multi-Agent Multi-View Video World Models](https://huggingface.co/papers/2604.18564)

MultiWorld는 Multi-Agent Condition Module과 Global State Encoder를 통해 다중 에이전트 제어와 다중 시점 일관성을 유지하는 확장 가능한 Multi-Agent Multi-View Video World Model을 제안합니다. 기존 비디오 월드 모델은 단일 에이전트 시나리오에 국한되어 복잡한 다중 에이전트 시스템의 상호작용을 포착하는 데 한계가 있었습니다. MultiWorld는 Multi-Agent Condition Module을 도입하여 정밀한 다중 에이전트 제어 가능성을 확보하고, Global State Encoder를 통해 다양한 시점 간의 일관된 관찰을 보장합니다. 이 프레임워크는 에이전트 및 시점 수의 유연한 확장을 지원하며, 다중 플레이어 게임 환경 및 다중 로봇 조작 작업에서 비디오 충실도, 행동 추종 능력 및 다중 시점 일관성 측면에서 기존 모델보다 우수한 성능을 보였습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 6. [EasyVideoR1: Easier RL for Video Understanding](https://huggingface.co/papers/2604.16893)

EasyVideoR1은 비디오 이해를 위한 효율적인 강화 학습 프레임워크로, 훈련 처리량을 개선하고 다양한 비디오 작업을 지원하며 이미지-비디오 공동 훈련을 가능하게 합니다. 기존 RL 훈련 프레임워크는 텍스트 및 이미지 시나리오에 적합했지만, 비디오 모달리티에 특화된 최적화가 부족했습니다. EasyVideoR1은 이러한 문제를 해결하기 위해 비디오 디코딩 중복을 제거하는 오프라인 전처리 및 텐서 캐싱을 통해 훈련 처리량을 1.47배 향상시켰습니다. 또한, 11가지 비디오 및 이미지 문제 유형을 포괄하는 포괄적인 보상 시스템과 큐레이션된 고품질 궤적과 온-폴리시 탐색을 결합한 혼합 오프라인-온라인 데이터 훈련 패러다임을 제공합니다. 이를 통해 대규모 비전-언어 모델의 비디오 이해 작업 훈련을 위한 완전하고 효율적인 강화 학습 프레임워크를 제공합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 7. [GFT: From Imitation to Reward Fine-Tuning with Unbiased Group Advantages and Dynamic Coefficient Rectification](https://huggingface.co/papers/2604.14258)

GFT는 SFT의 한계를 극복하기 위해 Group Advantage Learning과 Dynamic Coefficient Rectification을 통해 LLM의 후속 학습을 개선하는 통합 프레임워크를 제안합니다. (영문 용어: Fine-Tuning). 대규모 언어 모델(LLM)의 후속 학습은 SFT와 RL에 의존하지만, 효율적인 지식 주입과 강력한 일반화의 통합은 여전히 어렵습니다. 이 연구는 SFT가 희소한 암묵적 보상과 불안정한 역확률 가중치를 가진 정책 그라디언트 최적화의 특수한 경우임을 분석하여, 단일 경로 의존성, 엔트로피 붕괴, 그라디언트 폭발과 같은 문제를 야기함을 진단합니다. 이를 해결하기 위해 GFT는 다양한 응답 그룹을 구성하고 보상 희소성을 완화하는 Group Advantage Learning과 역확률 가중치를 적응적으로 제한하여 최적화를 안정화하는 Dynamic Coefficient Rectification을 제안합니다. 실험 결과 GFT는 SFT 기반 방법들을 지속적으로 능가하며, 후속 RL 훈련과 더 원활하게 통합되는 정책을 생성합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 8. [When Can LLMs Learn to Reason with Weak Supervision?](https://huggingface.co/papers/2604.18574)

LLM이 약한 감독(weak supervision) 하에서도 추론을 학습할 수 있는 조건을 탐구하며, 보상 포화 역학(reward saturation dynamics)과 추론 충실도(reasoning faithfulness)가 중요하고 명시적 추론 흔적에 대한 SFT가 필수적임을 밝힙니다. 이 연구는 LLM이 약한 감독 하에서 추론 작업을 일반화하는 조건을 체계적으로 탐구합니다. 희소 데이터, 노이즈가 있는 보상, 자기 지도 프록시 보상이라는 세 가지 약한 감독 설정에서 실험한 결과, 일반화는 훈련 보상 포화 역학에 의해 결정되며, 모델이 빠르게 포화되면 암기하는 경향이 있음을 발견했습니다. 또한, 중간 단계가 최종 답변을 논리적으로 얼마나 잘 뒷받침하는지를 나타내는 추론 충실도가 모델의 학습 방식을 예측하는 중요한 요소임을 확인했습니다. 이러한 발견을 바탕으로, 약한 감독 하에서 일반화를 위해서는 명시적 추론 흔적(explicit reasoning traces)에 대한 SFT(Supervised Fine-Tuning)가 필수적이며, 도메인 데이터에 대한 지속적인 사전 학습(continual pre-training)이 그 효과를 증폭시킨다고 주장합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 9. [WebCompass: Towards Multimodal Web Coding Evaluation for Code Language Models](https://huggingface.co/papers/2604.18224)

WebCompass는 코드 언어 모델의 웹 개발 능력을 평가하기 위해 텍스트, 이미지, 비디오 등 다양한 입력 양식과 생성, 편집, 복구의 세 가지 작업 유형을 포괄하는 새로운 멀티모달 벤치마크입니다. 기존 벤치마크는 코드 언어 모델의 웹 코딩 능력을 텍스트 기반 생성과 정적 정확도 측정에만 집중하여 시각적 충실도, 상호작용 품질, 코드베이스 수준 추론을 제대로 측정하지 못했습니다. WebCompass는 실제 웹 코딩 워크플로우를 반영하여 텍스트, 이미지, 비디오 세 가지 입력 양식과 생성, 편집, 복구 세 가지 작업 유형을 포함하는 7가지 작업 카테고리를 제공합니다. 이 벤치마크는 LLM-as-a-Judge 프로토콜과 Agent-as-a-Judge 패러다임을 통해 생성된 웹사이트를 실제 브라우저에서 실행하고 상호작용을 탐색하여 모델의 웹 엔지니어링 능력을 종합적으로 평가합니다. 평가 결과, 클로즈드 소스 모델이 오픈 소스 모델보다 훨씬 강력하고 균형 잡힌 성능을 보였습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 10. [ClawEnvKit: Automatic Environment Generation for Claw-Like Agents](https://huggingface.co/papers/2604.18543)

ClawEnvKit은 자연어 설명을 통해 claw-like 에이전트의 훈련 및 평가 환경을 자동으로 생성하는 파이프라인을 제안합니다. 기존 claw-like 에이전트 환경 구축은 수동적이고 비효율적이었습니다. ClawEnvKit은 자연어 설명을 파싱하여 작업 사양, 도구 인터페이스, 점수 구성을 생성하고, 유효성 검사를 통해 다양하고 일관된 환경을 자동으로 만듭니다. 이를 통해 Auto-ClawEval이라는 대규모 벤치마크를 구축했으며, 이는 수동 환경보다 비용 효율적이고 성능 평가에 효과적임을 입증했습니다. 또한, 이 파이프라인은 정적 벤치마킹을 넘어 실시간 평가도 가능하게 합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.
