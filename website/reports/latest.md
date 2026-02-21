# IMDIGEST - 2026-02-21

- 기준일(KST): 2026-02-20 00:00:00 ~ 23:59:59

## AI News

### OpenAI의 첫 번째 증명 시도 공개
  - 내용 요약
    - OpenAI는 첫 번째 증명 문제 챌린지에 참가하여 AI 모델을 사용해 연구 수준의 논리적 사고를 테스트한 결과를 공윈습니다.
    - 공유된 내용은 전문가 수준의 문제들을 해결하는 데 대한 AI 모델의 연구급 논리적 사고 능력을 시험한 것입니다.
  - 링크: https://openai.com/index/first-proof-submissions

### Hugging Face는 GGML과 llama.cpp을 합류시켜 Local AI의 장기적 발전을 보장한다
  - 내용 요약
    - GGML과 llama.cpp의 개발자인 Georgi Gerganov와 팀이 Hugging Face에 합류하여 Local AI의 커뮤니티를 지원할 예정이다. (원문 용어: long-term)
    - Hugging Face는 ggml과 llama.cpp 프로젝트에 장기적인 자금 지원을 제공하며, 이는 프로젝트의 성장과 번영 확률을 높인다.
  - 링크: https://huggingface.co/blog/ggml-joins-hf

### Hugging Face와 Unsloth를 활용한 AI 모델 무료 훈련
  - 내용 요약
    - Unsloth과 Hugging Face Jobs를 사용하여 LiquidAI/LFM2.5-1.2B-Instruct 모델을 빠르게 훈련할 수 있습니다.
    - Unsloth은 표준 방법보다 약 2배 더 빠른 훈련 속도와 VRAM 사용량 감소를 제공합니다.
    - 무료 크레딧과 한 달간 Pro 구독을 받을 수 있는 Unsloth Jobs Explorers 조직에 가입할 수 있습니다.
  - 링크: https://huggingface.co/blog/unsloth-jobs

### Google Gemini 3.1 Pro가 복잡한 문제 해결 능력을 강화
  - 내용 요약
    - Gemini 3.1 Pro는 기존의 Gemini 3 Deep Think 모델을 업데이트하여, 과학, 연구 및 공학 분야에서 현대적인 도전 사항을 해결할 수 있는 더 뛰어난 인공지능을 제공합니다.
    - 3.1 Pro는 ARC-AGI-2 벤치마크에서 77.1%의 점수를 얻음으로써, 이전 모델 대비 두 배 이상의 논리적 추론 능력을 보여줍니다.
    - 새로운 기능으로 코드 기반 애니메이션 생성이 가능해지며, 텍스트 프롬프트만으로 웹사이트에 바로 사용할 수 있는 SVG 파일을 생성할 수 있습니다.
  - 링크: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro

### 일본 AI 개발 가속화를 위한 합성 페르소나 데이터 활용
  - 내용 요약
    - NTT DATA는 Nemotron-Personas-Japan이라는 합성 데이터셋을 통해 일본의 문화와 지리에 기반한 600만 명의 페르소나를 생성하여 AI 모델 개발을 지원함
    - NVIDIA의 NeMo Data Designer를 사용해 합성 데이터로 모델 정확도를 대폭 향상시켰음
    - NTT DATA는 합성 데이터를 활용한 기업 환경에서의 AI 모델 성능 향상을 실험적으로 검증함
  - 링크: https://huggingface.co/blog/nvidia/nemotron-personas-japan-nttdata-ja

### 미디어 진위 기술의 발전과 중요성에 대한 Microsoft 연구 보고서 발표
  - 내용 요약
    - Microsoft는 미디어 진위와 인증(MIA) 방법에 대해 연구보고서를 발표하였으며, 이를 통해 AI 시스템이 대규모로 생성하거나 수정한 이미지, 동영상 및 오디오의 구별이 점점 어려워짐을 설명하였다.
    - C2PA(콘텐츠 진위와 인증 연합)가 주도하는 표준화 기술과 함께 물음표와 속성치 등 보완적인 방법들이 미디어 진위를 증진시키고 있다.
    - 미래 법안 시행에 따른 인증 신호의 명확성과 유용성이 높아질 것으로 예상되며, 이를 방지하기 위한 적대적 공격 대응이 요구되고 있다.
  - 링크: https://www.microsoft.com/en-us/research/blog/media-authenticity-methods-in-practice-capabilities-limitations-and-directions

### NVIDIA GPU NUMA 노드 위치 최적화로 데이터 처리 속도 향상
  - 내용 요약
    - NVIDIA의 Ampere, Hopper 및 Blackwell GPU 시리즈는 NUMA 행동을 특징으로 하지만 단일 메모리 공간을 노출한다. (원문 용어: Multi-Instance)
    - MIG 모드를 활용하여 NUMA 노드 간 데이터 위치 최적화를 통해 성능과 전력 효율성을 향상시킨다.
    - Wilson-Dslash 스텐셜 연산자 사용 사례에서 MIG 모드와 UNLOCALIZED 상태의 성능을 비교한다.
  - 링크: https://developer.nvidia.com/blog/accelerating-data-processing-with-nvidia-multi-instance-gpu-and-numa-node-localization

### Union.ai와 Flyte를 사용하여 Amazon EKS에서 AI 워크플로 구축
  - 내용 요약
    - Flyte Python SDK를 활용해 AI/ML 워크플로를 오케스트레이션하고 확장할 수 있게 됨
    - Union.ai 2.0 시스템을 통해 Flyte를 Amazon EKS에 배포하여 AWS 서비스와 통합됨
  - 링크: https://aws.amazon.com/blogs/machine-learning/build-ai-workflows-on-amazon-eks-with-union-ai-and-flyte

### Amazon Quick가 Snowflake 데이터 소스에 대해 키 쌍 인증을 지원함
  - 내용 요약
    - Amazon Quick Sight은 이제 Snowflake 데이터 소스와의 연결을 위해 키 쌍 인증을 지원합니다.
    - RSA 키 쌍이 전통적인 비밀번호를 대체하여 보안성을 높입니다.
  - 링크: https://aws.amazon.com/blogs/machine-learning/amazon-quick-suite-now-supports-key-pair-authentication-to-snowflake-data-source

## Papers (Hugging Face Top 10)

### SpargeAttention2: Trainable Sparse Attention via Hybrid Top-k+Top-p Masking and Distillation Fine-Tuning
- 한 줄 요약: SpargeAttention2는 하이브리드 Top-k+Top-p 마스킹과 교육 영감을 받은 디스티루션 정교화 목표를 통해 고도의 스파르시티를 달성하면서 생성 품질을 유지하는 학습 가능한 스파르시티 어텐션 방법입니다. (원문 용어: Fine-Tuning)
- 핵심 아이디어: SpargeAttention2는 Top-k와 Top-p 마스킹 규칙의 결함을 피하기 위해 하이브리드 마스킹 규칙을 도입하고, 효율적인 학습 가능한 스파르시티 어텐션 구현과 교육 영감을 받은 정교화 목표를 통해 고도의 스파르시티와 생성 품질 간 균형을 맞추는 방법입니다. 이 연구는 다양한 실험에서 전반적으로 기존의 스파르시티 어텐션 방법보다 뛰어난 성능을 보여주며, 비학습 가능한 스파르시티 방법에 비해 95%의 어텐션 스파르시티와 16.2배의 속도 향상을 달성했습니다.
- 키워드: #spargeattention2 #hybrid-top-k+top-p-masking #distillation-fine-tuning #sparse-attention #video-diffusion-models #generation-quality
- 링크: https://huggingface.co/papers/2602.13515

### Mobile-Agent-v3.5: Multi-platform Fundamental GUI Agents
- 한 줄 요약: GUI-Owl-1.5는 다양한 플랫폼에서 GUI 자동화와 관련된 여러 작업에 최고 성능을 보이는 모델로, 하이브리드 데이터 파이프라인과 통합된 능력 강화 알고리즘을 통해 개발되었습니다. (원문 용어: Mobile-Agent-v3.5, Multi-platform)
- 핵심 아이디어: GUI-Owl-1.5는 다양한 플랫폼에서 GUI 자동화와 관련된 작업을 수행하기 위해 설계되었으며, 하이브리드 데이터 파이프라인과 통합된 능력 강화 알고리즘을 통해 모델의 효율성과 성능을 향상시킵니다. 이 모델은 UI 이해 및 경로 생성에 대한 데이터 수집 효율성을 높이는 하이브리드 데이터 플라이휠과, 도구 사용, 메모리 및 다중 에이전트 적응 능력을 강화하는 통합 사고 합성 파이프라인을 포함합니다.
- 키워드: #gui-owl-1.5 #하이브리드-데이터-플라이휠 #통합-사고-합성-파이프라인 #다중-플랫폼 #gui-자동화
- 링크: https://huggingface.co/papers/2602.16855

### Unified Latents (UL): How to train your latents
- 한 줄 요약: Unified Latents(UL)은 디퓨전 프라이어 정규화와 디퓨전 모델 디코딩을 통해 공동 잠재 표현을 학습하여, Stabl Diffusion 잠재 변수에서 fewer training FLOPs를 필요로하면서도 ImageNet-512에서 경쟁력을 갖는 FID 점수를 달성한다.
- 핵심 아이디어: Unified Latents(UL)은 디퓨전 프라이어와 디퓨전 모델을 통해 잠재 표현을 공동으로 정규화하고 디코딩하는 프레임워크로, 인코더의 출력 노이즈를 최소 노이즈 레벨과 연결하여 간단한 훈련 목표를 제공하며, 이는 잠재 비트레이트에 대한 tight upper bound을 제공한다. ImageNet-512와 Kinetics-600에서 경쟁력 있는 성능을 달성하면서도 fewer training FLOPs를 필요로 한다.
- 키워드: #unified-latents #디퓨전-프라이어 #잠재-표현 #fid-점수 #imagenet #kinetics
- 링크: https://huggingface.co/papers/2602.17270

### Frontier AI Risk Management Framework in Practice: A Risk Analysis Technical Report v1.5
- 한 줄 요약: Frontier AI Risk Management Framework는 대형 언어 모델의 새로운 위험 요인을 평가하고, 보안 배포를 위한 강력한 차단 전략을 제시한다.
- 핵심 아이디어: 이 연구에서는 빠르게 발전하는 AI 모델들이 새로운 위협을 초래할 수 있는 다섯 가지 중요한 차원을 평가하며, 이에 대한 보안 배포를 위한 구체적인 차단 전략을 제시한다. 특히, 사이버 공격, 설득 및 조작, 전략적 속임수, 비제어 가능한 AI 연구 개발, 그리고 자율적으로 능력 확장하는 에이전트의 자기 복제 등에 대한 위험 요인들을 구체화하고, 이를 근거로 한 강력한 차단 전략을 제안한다.
- 키워드: #frontier-ai-risk-management-framework #large-language-models #cyber-offense #persuasion-and-manipulation #uncontrolled-ai-r&d
- 링크: https://huggingface.co/papers/2602.14457

### "What Are You Doing?": Effects of Intermediate Feedback from Agentic LLM In-Car Assistants During Multi-Step Processing
- 한 줄 요약: "What Are You Doing?": 연구는 LLM 기반의 차량 내 AI 어시스턴트에서 중간 피드백이 사용자 경험에 미치는 영향을 조사한다. (원문 용어: In-Car, Multi-Step)
- 핵심 아이디어: 연구는 차량 내 AI 어시스턴트가 복잡한 작업 수행 시 중간 결과와 진행 상황 피드백이 사용자의 신뢰감, 효율성 및 작업 부담 감소에 미치는 효과를 분석하였다. 실험 결과, 중간 피드백은 특히 주의 집중이 필요한 운전 상황에서도 사용자 경험을 크게 향상시켰으며, 이는 다양한 작업 복잡성과 상호작용 맥락에서 일관되게 나타났다.
- 키워드: #llm #차량-내-ai-어시스턴트 #중간-피드백 #사용자-경험 #신뢰감 #효율성
- 링크: https://huggingface.co/papers/2602.15569

### Arcee Trinity Large Technical Report
- 한 줄 요약: Arcee Trinity Large는 400B 파라미터를 가지며, 각 토큰당 13B 파라미터가 활성화된 스 Mixture-of-Experts 모델입니다.
- 핵심 아이디어: Arcee Trinity Large는 다양한 파라미터 수와 활성화 패턴을 가진 스 Mixture-of-Experts 아키텍처를 사용하며, 현대적인 어텐션 메커니즘과 트레이닝 최적화 기법을 포함합니다. SMEBU라는 새로운 MoE 로드 밸런싱 전략이 Trinity Large에서 도입되었으며, Muon 옵티마이저를 사용하여 모델은 모든 경우에 걸쳐 0의 손실 스플라이크 없이 훈련되었습니다.
- 키워드: #arcee-trinity #mixture-of-experts #smebu #muon-optimizer #attention-mechanisms #pre-training
- 링크: https://huggingface.co/papers/2602.17004

### Calibrate-Then-Act: Cost-Aware Exploration in LLM Agents
- 한 줄 요약: Calibrate-Then-Act(CTA) 프레임워크는 대형 언어 모델이 비용에 대한 불확실성과 이를 균형 잡는 데 도움을 주며, 정보 검색 문제와 간단한 코딩 작업에서 더 효율적인 의사 결정 전략을 발견하는 데 도움이 됨. (원문 용어: Cost-Aware)
- 핵심 아이디어: Calibrate-Then-Act(CTA) 프레임워크는 대형 언어 모델이 복잡한 문제 해결 과정에서 비용과 불확실성 사이의 균형을 고려하도록 설계되었습니다. 이 방법은 정보 검색 문제와 코딩 작업 등 순차적인 의사 결정 문제를 처리할 때, LLM들이 더 효율적으로 환경과 상호작용하며, 비용-불확실성 트레이드오프를 명시적으로 고려하도록 합니다. 이를 통해 CTA는 기본 모델보다 더 우수한 성능을 보이는 것으로 나타났습니다.
- 키워드: #calibrate-then-act #cost-aware-exploration #llm-agents #sequential-decision-making #information-retrieval #coding
- 링크: https://huggingface.co/papers/2602.16699

### DDiT: Dynamic Patch Scheduling for Efficient Diffusion Transformers
- 한 줄 요약: DDiT는 동적 패치 스케줄링 기법을 사용하여 디퓨전 트랜스포머의 효율성을 향상시킵니다.
- 핵심 아이디어: DDiT는 이미지와 비디오 생성에서 고정 패치 크기 대신 동적 패치 크기를 사용하여 디퓨전 트랜스포머의 성능을 개선합니다. 이 방법은 내용 복잡성과 노이즈 제거 시간 단계에 따라 패치 크기를 조절하여 전반적인 구조 모델링에는 더 큰 패치가 필요하고, 세부 사항을 정교화할 때는 더 작은 패치가 필요한 점을 활용합니다. 이를 통해 추론 시점에서 비용이 크게 줄어들면서 동시에 생성 품질은 손실되지 않습니다.
- 키워드: #ddit #dynamic-patch-scheduling #diffusion-transformers #efficiency #image-generation #video-generation
- 링크: https://huggingface.co/papers/2602.16968

### TactAlign: Human-to-Robot Policy Transfer via Tactile Alignment
- 한 줄 요약: TactAlign은earable 장치를 통해 수집된 인간의 감각적 시나리오를 다른 체제의 로봇으로 전달하는 방법을 제시한다. (원문 용어: Human-to-Robot)
- 핵심 아이디어: 인간과 로봇 간의 체감 정보 전달에 있어 TactAlign는 페어데이터 없이 공유된 잠재 표현으로 인간과 로봇의 체감 관찰 값을 변환하여 감각적 시나리오를 다른 체제로 이식하는 방법을 제안한다. 이를 통해 다양한 접촉 기반 작업에서 인간 데이터를 이용한 로봇 학습이 가능해진다.
- 키워드: #tactalign #human-to-robot #tactile-alignment #latent-representation #cross-embodiment #policy-transfer
- 링크: https://huggingface.co/papers/2602.13579

### Computer-Using World Model
- 한 줄 요약: CUWM은 컴퓨터 사용 시나리오에서의 UI 상태 변화를 예측하기 위해 텍스트 설명과 시각 합성 두 단계로 분해된 방식으로 작동하는 월드 모델입니다. (원문 용어: Computer-Using)
- 핵심 아이디어: 복잡한 소프트웨어 환경에서 작업을 수행하는 에이전트들은 자신의 행동의 결과를 추론할 수 있어야 합니다. 컴퓨터 사용 시나리오에서는 실제 실행이 카운터팩트적 탐색을 지원하지 않기 때문에 대규모 도전과 오류 실험 학습 및 계획은 불가능합니다. 이 연구에서는 CUWM이라는 두 단계로 분해된 UI 동역학 모델을 제시하여 이러한 문제를 해결하고, 텍스트 설명과 시각 합성의 두 단계를 통해 다음 UI 상태를 예측합니다.
- 키워드: #computer-using-world-model #ui-dynamics #textual-description #visual-synthesis #reinforcement-learning #action-search
- 링크: https://huggingface.co/papers/2602.17365
