# IMDIGEST - 2026-04-05

2026-04-05 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-04-05 AI 브리핑입니다. 오늘은 TechCrunch AI에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

### [Anthropic, Claude Code 구독자에게 OpenClaw 등 서드파티 툴 사용에 대한 추가 요금 부과](https://techcrunch.com/2026/04/04/anthropic-says-claude-code-subscribers-will-need-to-pay-extra-for-openclaw-support)

Anthropic은 4월 4일부터 Claude Code 구독자가 OpenClaw를 포함한 서드파티 툴 사용 시 구독 한도를 사용할 수 없게 되며, 별도의 종량제(pay-as-you-go) 옵션으로 추가 비용을 지불해야 한다고 발표했습니다. 이 정책은 OpenClaw를 시작으로 모든 서드파티 하네스에 적용될 예정입니다. Anthropic은 이러한 서드파티 툴의 사용 패턴에 맞게 구독 서비스가 설계되지 않았으며, 장기적으로 고객에게 지속 가능한 서비스를 제공하기 위해 성장을 관리하려는 의도라고 밝혔습니다. AI 서비스 제공업체들이 서드파티 툴과의 통합 및 사용에 대한 수익 모델을 재정의하고 있으며, 이는 AI 생태계 내에서 파트너십과 경쟁 구도에 영향을 미칠 수 있습니다. 출처는 TechCrunch AI입니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [사용자 피드백을 통해 LLM 에이전트의 반복적인 실수를 방지하는 시스템 구축에 대한 논의가 활발합니다.](https://www.reddit.com/r/LocalLLaMA/comments/1scm6om/has_anyone_built_a_feedback_loop_where_thumbsdown)

Reddit 사용자 eazyigz123는 LLM 에이전트가 코딩 작업에서 반복적으로 실수를 저지르는 문제에 직면했습니다. 그는 'thumbs-down' 피드백을 단순한 신호가 아닌, 에이전트의 특정 실수를 방지하는 'prevention rule'로 전환하는 시스템을 제안했습니다. 이 시스템은 에이전트의 툴 호출 실행 전에 규칙을 적용하여 실수를 물리적으로 차단하고, 'thumbs-up'은 좋은 행동을 강화합니다. 이는 LLM 에이전트의 신뢰성과 효율성을 높이는 중요한 방법론으로, 사용자 피드백을 직접적인 행동 제약으로 연결하여 에이전트의 학습 및 개선 과정을 혁신할 수 있습니다. 출처는 Reddit r/LocalLLaMA입니다.

### [Anthropic, Claude Code 구독자에게 OpenClaw 사용료 추가 부과 예정](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQakxlX1lJUklzd3JYNkp4Q2NGZlFPZ3NhcmVKYUJYcGprR3dxWWtYMUFrV0VXc1Yta1BNSUR5ZVEtZjdWY2hGeFRQZVNWeVhCX2RHeGtIY2k0ZVVRM1VmMlh2bFZjOWgwTTY2OXlSNTRGOHVNMGhiUkhoUnVHdGx3SHRlQ0Z1aWoyOUNDLXl2VXdMTXdldTVrZzFKSFhnMXJHTXZGXzItU1NnMnZ0aVl3UWp4eWxWRmdL?oc=5)

Anthropic은 Claude Code 구독자들이 OpenClaw를 사용하려면 추가 비용을 지불해야 한다고 밝혔습니다. (영문 용어: techcrunch.com). OpenClaw는 Anthropic의 AI 모델인 Claude를 활용하는 새로운 기능 또는 서비스로 보입니다. 이번 정책 변경은 Claude Code 구독 서비스의 약관 변경을 의미합니다. AI 서비스 제공업체들이 특정 고급 기능이나 새로운 서비스에 대해 추가적인 수익 모델을 모색하는 추세를 보여줍니다. 출처는 Google News AI Search입니다.

### [Cadenza, Weights & Biases(Wandb) 로그를 AI 에이전트에 쉽게 연결하여 자율 연구를 지원하는 CLI 도구 및 Python SDK 공개](https://www.reddit.com/r/MachineLearning/comments/1scm9do/p_cadenza_connect_wandb_logs_to_agents_easily_for)

Cadenza는 Wandb 프로젝트 및 실행 데이터를 AI 에이전트와 연동하는 CLI 도구 및 Python SDK입니다. 기존 Wandb CLI 및 MCP의 느리고 비효율적인 문제를 해결하여 자율 연구 루프에서의 사용성을 개선합니다. 프로젝트 임포트 시, Wandb 실행의 configs와 metrics만 분석하여 인덱싱하고 저장합니다. AI 에이전트를 활용한 자율 연구(autonomous research)의 효율성을 크게 향상시켜, 연구 개발 속도를 가속화할 수 있습니다. 출처는 Reddit r/MachineLearning입니다.

### [Anthropic의 Claude API가 타사 도구를 통한 무료 사용을 중단하고 유료 정책으로 전환됩니다.](https://news.google.com/rss/articles/CBMitgFBVV95cUxNRzFqY2FoRkRPMHRheTJyUEViSnpaOEY0enZSN3ZaOGI2cnZoVE95UVlDMWRjNlFMVkNwVmJPcGlndmZQV3VkRDJ2YjA2U2lhUkhLOFZZSGRkQUV0SVBGWXlhUzNCeUdyNm9NTHpaM3dMbUpXV2UwQXBsSEpFWXJJOUxrYXFhbU5DQUc0d0hNWDlMZ3dzZU1ueFFGY25ueE42NnNyNGhtMVpBQVVpOE50el9SS0FrUQ?oc=5)

Anthropic은 Claude API의 무료 사용을 중단하고 유료 정책으로 전환한다고 발표했습니다. (영문 용어: third-party). 이제 OpenClaw와 같은 타사 도구를 통해 Claude를 무료로 사용할 수 없게 됩니다. 이번 변경은 Claude 3 Opus, Sonnet, Haiku 모델에 모두 적용됩니다. 이는 AI 모델 개발사들이 서비스 수익화를 강화하고, API 사용에 대한 명확한 가치 책정을 통해 지속 가능한 비즈니스 모델을 구축하려는 움직임으로 해석됩니다. 출처는 Google News AI Search입니다.

### [Cadenza, W&B 로그를 AI 에이전트에 쉽게 연결하여 자율 연구를 지원하는 CLI 도구 및 Python SDK 공개](https://www.reddit.com/r/artificial/comments/1scmaxt/p_cadenza_connect_wandb_logs_to_agents_easily_for)

Cadenza는 Weights & Biases (W&B) 프로젝트 및 실행 로그를 AI 에이전트에 쉽게 연결하도록 설계된 CLI 도구 및 Python SDK입니다. 기존 W&B CLI 및 MCP 사용 시 발생하는 느리고 번거로운 문제, 그리고 Context Rot 현상을 해결하는 것을 목표로 합니다. 프로젝트 임포트 시, 설정(configs)과 지표(metrics)만 분석하여 실행(runs)을 인덱싱하고 저장하며, 에이전트가 이 인덱스에서 샘플링할 때 고성능 실험만 반환하여 Context Rot을 줄입니다. AI 에이전트를 활용한 자율 연구(autonomous research)의 효율성을 크게 향상시켜, 연구 개발 속도를 가속화할 수 있습니다. 출처는 Reddit r/artificial입니다.

### [KDD 2026 2월 사이클 논문 리뷰 결과가 발표되며, 연구자들이 리뷰 경험을 공유하고 있습니다.](https://www.reddit.com/r/MachineLearning/comments/1sci9nh/d_kdd_review_discussion)

KDD 2026 2월 사이클 논문 리뷰 결과가 4월 4일(AoE)에 공개되었습니다. Reddit의 r/MachineLearning 스레드에서 연구자들이 리뷰 결과에 대한 토론을 진행하고 있습니다. 참가자들은 성공적인 리뷰를 축하하고, 리뷰 시스템의 불확실성에 대한 공감대를 형성하며, 논문 개선에 도움이 되는 리뷰를 우선시할 것을 독려하고 있습니다. KDD와 같은 주요 학회 논문 리뷰 결과 발표는 머신러닝 연구 동향과 학계의 관심사를 파악할 수 있는 중요한 지표입니다. 출처는 Reddit r/MachineLearning입니다.

### [Nvidia의 새로운 AI 기술이 게임 GPU 메모리 사용량을 최대 85%까지 절감하면서도 시각적 품질 손실이 없다고 발표했습니다.](https://news.google.com/rss/articles/CBMixgJBVV95cUxOZkNBdU9sS2dRN01KQmhiRzhkeThLeUdadEI3cENDWmVrajVPTW5CeFE5TmVrZFprQmtETllDTHhodmh3NkUwSXlnMGQtZlVvQTJUMnljeFZyR2UxZ1ktUXNRY0pWWkI4WHp6X2FJX281T2dseVZkWEJEOTN2YTNZN1NJZHMyM0dKNEM5aGZ0TkQzTHFvZXE3Q2dvYXBjbTFIUzk1akhDVkFqNHdNcVdJUmZMVUNEbkxPc0o5ZU1TWnAycm04YmFYUzF6eHBwanoyM1Jub0RXeUNSaEFlTmVJNU44M2pIbWxaRktRU09HSjF2YzJ5UWxPTy1NdHlFZnBacW1NN084OU1tTUR5d1hNdnpVSXIyeVAyMzNKTzgySVlfLXZ4TDNpOVhGaF8tclVDWFdyWlRZYzNBNF9IN2FtR1dFM0xnUQ?oc=5)

Nvidia는 Neural Texture Compression 기술을 통해 게임 GPU의 VRAM 사용량을 6.5GB에서 970MB로 85% 절감하는 데 성공했습니다. 이 기술은 AI를 활용하여 텍스처 데이터를 압축하며, 시각적 품질 저하 없이 원본과 거의 동일한 수준의 그래픽을 제공합니다. 이번 데모는 게임 개발자들이 더 적은 메모리로 고품질 그래픽을 구현할 수 있는 가능성을 보여주었습니다. 이 기술은 게임 개발 비용을 절감하고, 더 많은 게임이 고품질 그래픽을 제공할 수 있도록 지원하여 게임 산업에 큰 영향을 미칠 것입니다. 출처는 Google News AI Search입니다.

### [Meta, 머신러닝 모델의 서브그룹 캘리브레이션을 개선하는 오픈소스 Python 패키지 MCGrad 공개](https://www.reddit.com/r/MachineLearning/comments/1scjzer/p_mcgrad_fix_calibration_of_your_ml_model_in)

Meta는 머신러닝 모델의 서브그룹 캘리브레이션 문제를 해결하기 위한 오픈소스 Python 패키지 MCGrad를 공개했습니다. MCGrad는 gradient boosted decision trees를 사용하여 multicalibration을 재구성하며, 각 단계에서 경량 부스터가 베이스 모델의 잔여 miscalibration을 예측하고 수정합니다. 이 방법은 대규모 데이터셋에 적용 가능하며, 예측 성능 유지를 위해 early stopping을 사용합니다. 머신러닝 모델이 전체적으로는 잘 보정되어 있어도 특정 서브그룹(예: '모바일 기기를 사용하는 X 지역 사용자')에서는 오작동할 수 있는 문제를 해결하여 모델의 신뢰성을 높이는 데 기여합니다. 출처는 Reddit r/MachineLearning입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [DataFlex: A Unified Framework for Data-Centric Dynamic Training of Large Language Models](https://huggingface.co/papers/2603.26164)

DataFlex는 LLM의 동적 데이터 중심 학습을 위한 통합 프레임워크로, 샘플 선택, 도메인 혼합 조정, 샘플 재가중을 지원하며 기존 학습 워크플로우와 호환됩니다. (영문 용어: Data-Centric). 기존 LLM 데이터 중심 학습 방식들은 개별적으로 개발되어 재현성 및 통합에 어려움이 있었습니다. DataFlex는 LLaMA-Factory 기반의 통합 프레임워크로, 샘플 선택, 도메인 혼합 조정, 샘플 재가중이라는 세 가지 주요 동적 데이터 최적화 패러다임을 지원합니다. 이 프레임워크는 표준 LLM 학습의 드롭인 대체가 가능하며, DeepSpeed ZeRO-3와 같은 대규모 설정도 지원합니다. 실험 결과, 동적 데이터 선택은 Mistral-7B 및 Llama-3.2-3B 모델에서 MMLU 성능을 향상시키고, DoReMi 및 ODM과 같은 데이터 혼합 방식은 MMLU 정확도와 perplexity를 개선했습니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-03 기준)에서 확인했습니다.

### 2. [The Latent Space: Foundation, Evolution, Mechanism, Ability, and Outlook](https://huggingface.co/papers/2604.02029)

이 서베이 논문은 언어 기반 모델에서 Latent Space의 기초, 진화, 메커니즘, 능력 및 미래 전망에 대한 포괄적인 분석을 제공합니다. Latent Space는 언어 기반 모델에서 토큰 수준의 명시적 접근 방식보다 연속적인 표현을 통해 언어적 중복성과 순차적 비효율성을 완화하는 이점을 제공하며 핵심적인 계산 기반으로 부상하고 있습니다. 이 서베이는 Latent Space의 범위와 명시적 공간과의 차이를 명확히 하고, 초기 탐색부터 현재의 대규모 확장까지 분야의 진화를 추적합니다. 메커니즘(Architecture, Representation, Computation, Optimization)과 능력(Reasoning, Planning, Modeling, Perception, Memory, Collaboration, Embodiment)이라는 두 가지 관점에서 기존 연구를 분석하여 기술적 지형을 정리합니다. 이를 통해 Latent Space가 언어 모델의 다양한 핵심 내부 프로세스를 지원하는 방식을 보여줍니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-03 기준)에서 확인했습니다.

### 3. [Generative World Renderer](https://huggingface.co/papers/2604.02329)

Generative World Renderer는 AAA 게임에서 추출한 대규모 동적 데이터셋을 활용하여 생성형 역 렌더링 및 순방향 렌더링의 사실성과 시간적 일관성을 개선합니다. 기존 합성 데이터셋의 제한된 사실성과 시간적 일관성으로 인해 생성형 역 렌더링 및 순방향 렌더링을 실제 시나리오에 적용하는 데 어려움이 있었습니다. 이 연구는 AAA 게임에서 추출한 4백만 프레임의 동적 데이터셋과 새로운 듀얼 스크린 캡처 방식을 도입하여 이 문제를 해결합니다. 이를 통해 인버스 렌더러는 실제 환경에서의 기하학 및 재료 분해를 가능하게 하고, G-buffer 기반의 고품질 비디오 생성을 촉진합니다. 또한, VLM 기반의 새로운 평가 프로토콜을 제안하여 역 렌더링 성능을 인간의 판단과 유사하게 측정합니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-03 기준)에서 확인했습니다.

### 4. [SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization](https://huggingface.co/papers/2604.02268)

SKILL0는 LLM 에이전트가 훈련 중에 스킬을 내재화하여, 동적 커리큘럼을 통해 컨텍스트 오버헤드를 줄이면서 제로샷 자율 행동을 가능하게 하는 인컨텍스트 에이전트 강화 학습 프레임워크입니다. (영문 용어: In-Context). 기존 LLM 에이전트의 스킬 증강 방식은 검색 노이즈, 토큰 오버헤드, 그리고 모델이 지식을 진정으로 습득하지 못한다는 한계가 있었습니다. SKILL0는 이러한 문제를 해결하기 위해 훈련 시점에 스킬을 모델 파라미터에 내재화하는 인컨텍스트 강화 학습 프레임워크를 제안합니다. 이 프레임워크는 전체 스킬 컨텍스트로 시작하여 점진적으로 컨텍스트를 줄여나가는 동적 커리큘럼을 사용합니다. 이를 통해 SKILL0는 ALFWorld 및 Search-QA와 같은 에이전트 환경에서 기존 RL baseline 대비 상당한 성능 향상을 달성하며, 동시에 효율적인 컨텍스트 사용을 유지합니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-03 기준)에서 확인했습니다.

### 5. [Steerable Visual Representations](https://huggingface.co/papers/2604.02327)

Steerable Visual Representations는 텍스트와 시각적 특징의 early fusion을 통해 언어로 이미지 요소에 대한 시각적 표현의 초점을 유도하면서도 표현 품질을 유지하는 새로운 시각적 표현 방식을 제안합니다. 기존 Vision Transformers(ViTs)는 일반적인 시각적 특징을 제공하지만 특정 관심 개념으로 초점을 유도하기 어렵고, Multimodal LLM은 언어 중심적이라 일반 시각 작업에 비효율적이라는 문제가 있었습니다. 이 연구는 텍스트를 시각 인코더 레이어에 직접 주입하는 early fusion 방식을 사용하여, 자연어로 전역 및 지역 시각적 특징을 조종할 수 있는 Steerable Visual Representations를 제안합니다. 이를 통해 이미지 내 원하는 객체에 초점을 맞추면서도 표현 품질을 유지하며, anomaly detection 및 personalized object discrimination과 같은 작업에서 뛰어난 성능과 zero-shot 일반화 능력을 보여줍니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-03 기준)에서 확인했습니다.

### 6. [CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery](https://huggingface.co/papers/2604.01658)

CORAL은 지속적인 메모리, 비동기 실행, 협업 문제 해결을 통해 자율적인 다중 에이전트 진화를 가능하게 하여 Open-Ended Discovery에서 뛰어난 성능을 달성합니다. (영문 용어: Multi-Agent). 기존 LLM 기반 Open-Ended Discovery 방법론은 고정된 휴리스틱과 하드코딩된 탐색 규칙에 의존하여 LLM 에이전트의 자율성을 제한했습니다. CORAL은 이러한 한계를 극복하기 위해 지속적인 메모리, 비동기 다중 에이전트 실행, 하트비트 기반 개입을 통해 탐색, 반영, 협업하는 장기 실행 에이전트를 도입했습니다. 이 프레임워크는 수학, 알고리즘, 시스템 최적화 등 다양한 Open-Ended 문제에서 기존 SOTA를 뛰어넘는 성능을 보여주며, 특히 Anthropic의 커널 엔지니어링 태스크에서 획기적인 개선을 이루었습니다. CORAL은 지식 재사용과 다중 에이전트 탐색 및 통신을 통해 이러한 성능 향상을 달성했습니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-03 기준)에서 확인했습니다.

### 7. [EgoSim: Egocentric World Simulator for Embodied Interaction Generation](https://huggingface.co/papers/2604.01001)

EgoSim은 3D 장면 상태를 지속적으로 업데이트하며 공간적으로 일관된 egocentric 상호작용 비디오를 생성하는 폐쇄 루프 시뮬레이터입니다. 기존 egocentric 시뮬레이터들은 3D grounding이 부족하여 시점 변화 시 구조적 불일치가 발생하거나, 장면을 정적으로 취급하여 다단계 상호작용에서 세계 상태를 업데이트하지 못하는 한계가 있었습니다. EgoSim은 3D 장면을 업데이트 가능한 세계 상태로 모델링하여 이러한 문제들을 해결합니다. Geometry-action-aware Observation Simulation 모델과 Interaction-aware State Updating 모듈을 통해 공간 일관성을 유지하며 상호작용을 생성합니다. EgoSim은 시각적 품질, 공간 일관성, 복잡한 장면 및 실제와 같은 능숙한 상호작용에 대한 일반화에서 기존 방법들을 능가하며, 로봇 조작으로의 cross-embodiment transfer도 지원합니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-03 기준)에서 확인했습니다.

### 8. [NearID: Identity Representation Learning via Near-identity Distractors](https://huggingface.co/papers/2604.01973)

NearID는 Near-identity distractors를 활용하여 배경 맥락과 분리된 신원 표현 학습을 개선하고, 개인화된 생성 및 이미지 편집과 같은 신원 중심 비전 작업의 신뢰도를 높입니다. 기존 비전 인코더는 개인화된 생성 및 이미지 편집과 같은 신원 중심 작업에서 객체 신원과 배경 맥락을 얽히게 하여 신뢰할 수 없는 표현을 생성하는 문제가 있었습니다. NearID는 Near-identity (NearID) distractors를 사용하여 이 취약점을 해결하는 프레임워크를 제안합니다. 이는 의미론적으로 유사하지만 다른 인스턴스를 참조 이미지와 동일한 배경에 배치하여 배경 맥락을 제거하고 신원만을 식별 신호로 분리합니다. 이 원칙에 기반하여 NearID 데이터셋과 엄격한 마진 기반 평가 프로토콜을 제시하며, 이를 통해 사전 학습된 인코더의 성능이 저조함을 보였습니다. 연구팀은 두 계층의 대조 목표를 사용하여 신원 인식 표현을 학습함으로써 Sample Success Rates (SSR)를 99.2%로 향상시키고, DreamBench++에서 인간 판단과의 정렬을 강화했습니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-03 기준)에서 확인했습니다.

### 9. [LatentUM: Unleashing the Potential of Interleaved Cross-Modal Reasoning via a Latent-Space Unified Model](https://huggingface.co/papers/2604.02097)

LatentUM은 모든 모달리티를 공유된 시맨틱 잠재 공간에 표현하여 픽셀 공간 매개 없이 효율적인 교차 모달 추론 및 생성을 가능하게 하는 통합 모델입니다. (영문 용어: Cross-Modal, Latent-Space). 기존 통합 모델(UM)은 시각적 이해와 생성을 위해 분리된 시각적 표현을 사용하며 픽셀 디코딩을 필요로 하여 비효율적이었습니다. LatentUM은 모든 모달리티를 공유된 시맨틱 잠재 공간에 통합하여 픽셀 공간 매개 없이 유연한 교차 모달 추론 및 생성을 가능하게 합니다. 이 설계는 계산 효율성을 향상시키고 코덱 편향을 완화하며 교차 모달 정렬을 강화합니다. 결과적으로 LatentUM은 Visual Spatial Planning 벤치마크에서 최첨단 성능을 달성하고, 자기 성찰을 통한 시각적 생성 한계를 확장하며, 공유된 시맨틱 잠재 공간 내에서 미래 시각 상태를 예측하여 월드 모델링을 지원합니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-03 기준)에서 확인했습니다.

### 10. [VOID: Video Object and Interaction Deletion](https://huggingface.co/papers/2604.02296)

VOID는 비전-언어 모델과 비디오 확산 모델을 활용하여 물리적으로 그럴듯한 비디오 객체 및 상호작용 삭제를 수행하는 프레임워크입니다. 기존 비디오 객체 제거 방법은 객체 뒤의 내용을 채우거나 그림자, 반사 같은 외형적 아티팩트를 수정하는 데는 능숙했지만, 다른 객체와의 충돌과 같은 중요한 상호작용이 있을 때는 물리적으로 그럴듯하지 않은 결과를 생성했습니다. VOID는 이러한 복잡한 시나리오에서 물리적으로 타당한 인페인팅을 수행하도록 설계된 비디오 객체 제거 프레임워크입니다. 이 모델은 Kubric과 HUMOTO를 사용하여 객체 제거 시 물리적 상호작용 변경이 필요한 새로운 카운터팩추얼 객체 제거 데이터셋으로 훈련되었습니다. 추론 시, 비전-언어 모델이 제거된 객체에 의해 영향을 받는 장면 영역을 식별하고, 이 영역은 물리적으로 일관된 카운터팩추얼 결과를 생성하는 비디오 확산 모델을 안내하는 데 사용됩니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-03 기준)에서 확인했습니다.
