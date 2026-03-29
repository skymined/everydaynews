# IMDIGEST - 2026-03-30

2026-03-30 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-03-30 AI 브리핑입니다. 오늘은 TechCrunch AI에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

### [OpenAI, 출시 6개월 만에 Sora 앱 및 관련 비디오 모델 서비스 종료](https://techcrunch.com/2026/03/29/soras-shutdown-could-be-a-reality-check-moment-for-ai-video)

OpenAI가 Sora 앱과 관련 비디오 모델 서비스를 출시 6개월 만에 중단한다고 발표했습니다. 이번 결정은 OpenAI가 기업 및 생산성 도구에 집중하려는 전략의 일환으로 해석됩니다. Wall Street Journal에 따르면, OpenAI는 상장(IPO)을 앞두고 비즈니스 제품, 기업 제품, 프로그래밍 제품에 주력하고 있습니다. 이번 Sora 서비스 종료는 AI 비디오 도구 제작자와 AI 비디오가 할리우드를 대체할 것이라고 주장하는 사람들에게 현실 점검의 계기가 될 수 있습니다. 출처는 TechCrunch AI입니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [Andrej Karpathy의 AutoResearch에서 영감을 받아, 표 형식 데이터에 대한 ML 실험을 자율적으로 수행하는 에이전트가 개발되었습니다.](https://www.reddit.com/r/MachineLearning/comments/1s73gma/p_i_built_an_autonomous_ml_agent_that_runs)

Claude Code를 활용하여 이 에이전트는 이진 분류(churn, conversion 등) 작업을 위한 자율 ML 연구원 역할을 수행합니다. 데이터셋을 입력하면 데이터 분석, 가설 형성, 코드 편집, 실험 실행, 평가(확장 시간 윈도우 사용) 과정을 무한히 반복합니다. 에이전트는 feature engineering, model hyperparams, analysis code 세 가지 파일만 수정하며, 나머지는 잠겨 있습니다. 이는 ML 모델에 새로운 신호를 추가하는 문제를 해결하고, 제한된 데이터셋에 과적합하는 것을 방지하는 데 중점을 둡니다. 출처는 Reddit r/MachineLearning입니다.

### [Nicolas Carlini, 저명한 보안 연구원이 Claude가 자신보다 뛰어난 보안 연구 능력을 가졌다고 평가했습니다.](https://www.reddit.com/r/artificial/comments/1s738xf/nicolas_carlini_672k_citations_on_google_scholar)

Nicolas Carlini는 Claude가 스마트 컨트랙트 취약점 악용으로 370만 달러를 벌었으며, Linux와 Ghost에서 취약점을 발견했다고 밝혔습니다. Claude가 발견한 Linux 취약점은 2003년에 도입된 버퍼 오버플로우 오류로, 지금까지 발견되지 않았던 심각한 보안 문제입니다. Carlini는 LLM의 보안 연구 능력이 시간이 지남에 따라 더욱 향상될 것으로 예상하고 있습니다. AI, 특히 LLM이 복잡한 보안 취약점을 식별하고 악용하는 데 있어 인간 전문가를 능가하는 능력을 보여주며 사이버 보안 분야의 패러다임 변화를 예고합니다. 출처는 Reddit r/artificial입니다.

### [Anthropic의 Claude, 이제 Mac에서 사용자가 자리를 비워도 백그라운드에서 작업 지속 가능](https://news.google.com/rss/articles/CBMiXEFVX3lxTE5CM0dZcm9VT2U0Y0FYemhfNEh5bC04SkNEU01HRWJzUF9pQU93dkZBVURxbV95S2NwUkZpc1FOUV8yN3VpR0tVdXVFeE5Va1V3dHAxRlJab2VsUWRY?oc=5)

Anthropic의 AI 챗봇 Claude가 Mac에서 사용자가 자리를 비운 동안에도 작업을 계속할 수 있게 업데이트되었습니다. 이 기능은 사용자가 다른 작업을 하거나 잠시 자리를 비웠을 때도 Claude가 주어진 작업을 완료하도록 합니다. 이는 생산성 향상에 기여하며, 복잡하거나 시간이 오래 걸리는 작업에 특히 유용합니다. AI 챗봇의 백그라운드 작업 지원은 사용자 편의성과 AI 활용도를 크게 높이는 중요한 발전입니다. 출처는 Google News AI Search입니다.

### [Arm이 에이전트 AI 클라우드 시대를 위한 AGI CPU를 발표하며 AI 인프라 시장에 새로운 지평을 열었습니다.](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9ZZ0dXNEhjUjJYMVVDd2l3U1J6bUdRSmxubjBLcUpoM1lHYk8xU3FzSkN3dEZzSWVMM3dUb2Z3Nm9XZFNsNzF4aGc3WWZOLVhiRlBDcktqVmJEVzJDVkV0M2JyOA?oc=5)

Arm은 에이전트 AI 클라우드 시대를 위한 새로운 CPU인 Arm AGI CPU를 공개했습니다. 이 CPU는 AI 워크로드에 최적화된 실리콘 기반을 제공하여 차세대 AI 애플리케이션을 지원합니다. Arm은 AGI CPU를 통해 AI 인프라 시장에서의 입지를 강화하고 있습니다. AI 기술 발전과 함께 에이전트 AI의 중요성이 부각되면서, 이를 효율적으로 처리할 수 있는 하드웨어의 필요성이 커지고 있습니다. 출처는 Google News AI Search입니다.

### [Python 버그 해결 과정에서 Claude Opus가 다른 LLM보다 뛰어난 문제 해결 능력을 보였습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1s78bxj/i_had_a_persistent_python_bug_that_i_turned_into)

Reddit 사용자가 Python 버그를 해결하는 과정에서 여러 LLM의 성능을 비교하는 벤치마크를 진행했습니다. Claude Opus는 다른 LLM들이 실패한 버그 수정 및 코드 개선 제안에서 가장 정확하고 유용한 답변을 제공했습니다. 다른 LLM들은 버그를 제대로 진단하지 못하거나, 잘못된 해결책을 제시하는 경우가 많았습니다. 이번 사례는 LLM의 단순한 정보 검색이나 코드 생성 능력을 넘어선 복합적인 문제 해결 및 추론 능력이 실제 개발 환경에서 얼마나 중요한지 강조합니다. 출처는 Reddit r/LocalLLaMA입니다.

### [Agent 시스템에서 실제 실행을 막는 메커니즘에 대한 논의가 활발합니다.](https://www.reddit.com/r/artificial/comments/1s76o5b/what_actually_prevents_execution_in_agent_systems)

API 호출을 트리거하는 Agent를 구축하는 과정에서, 검증, 도구 제약, 재시도 등 안전장치에도 불구하고 오래된 상태(stale state)와 재시도(retry)로 인해 동일한 작업이 두 번 실행되는 문제가 발생했습니다. 이는 기존의 안전장치들이 실행 자체를 막기보다는 Agent의 행동을 형성하는 데 그쳤음을 시사합니다. 사용자들은 Agent 외부의 시스템, 결정론적 허용/거부, 거부 시 fail-closed 방식 등 실제 실행을 제어할 수 있는 구체적인 패턴이나 시스템에 대한 궁금증을 표하고 있습니다. Agent 시스템의 안정성과 신뢰성 확보를 위해 단순한 행동 제어를 넘어 실제 실행을 막는 강력한 메커니즘의 필요성이 부각되고 있습니다. 출처는 Reddit r/artificial입니다.

### [Python으로 구현된 TurboQuant, 캘리브레이션 없이 효율적인 온라인 벡터 양자화 가능성을 제시하다](https://www.reddit.com/r/MachineLearning/comments/1s73sbf/p_implemented_turboquant_in_python)

"TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate" 논문을 바탕으로 한 Python 구현체가 공개되었습니다. 이 구현체는 기존 양자화 방식과 달리 캘리브레이션 데이터나 데이터셋별 튜닝 없이 작동하며, 모든 곳에 동일한 양자화기를 적용할 수 있습니다. 핵심 아이디어는 벡터에 무작위 회전을 적용하여 좌표를 가우시안처럼 만들고, 각 차원별로 최적의 1D 양자화를 수행하는 것입니다. TurboQuant는 토큰이 스트리밍되는 Transformer의 KV cache나 독립적으로 벡터를 압축하는 벡터 DB/임베딩과 같이 온라인 처리가 필요한 분야에서 전처리 단계 없이 효율적인 양자화를 가능하게 하여 활용도가 높습니다. 출처는 Reddit r/MachineLearning입니다.

### [AI 모델의 유해 데이터 사전 제거를 통한 정렬 및 제어 가능성 연구의 필요성 제기](https://www.reddit.com/r/MachineLearning/comments/1s73jb1/d_data_curation_and_targeted_replacement_as_a)

Reddit r/MachineLearning에서 AI 모델 학습 전 유해 데이터(폭력, 거짓, 기만 등)를 제거하거나 대체하는 방법에 대한 논의가 시작되었습니다. (영문 용어: pre-training). 기존의 controllability 연구(RLHF, Constitutional AI 등)는 주로 학습 후(post-training)에 이루어졌습니다. 제안된 방법은 Mo Gawdat의 'AI를 아이처럼 키우기' 제안을 문자 그대로 적용하여, 유해한 자료로 모델을 학습시키지 않는 것입니다. AI 모델의 안전성과 윤리적 사용에 대한 중요성이 커지면서, 학습 데이터 단계부터 유해성을 제어하려는 'pre-training alignment' 접근 방식에 대한 관심이 증가하고 있습니다. 출처는 Reddit r/MachineLearning입니다.

### [AI 신약 개발사 Insilico Medicine, Lilly와 최대 27.5억 달러 규모의 상업화 계약 체결](https://news.google.com/rss/articles/CBMinAFBVV95cUxPYmNMZno2a2N4NmlSLVMyVDBrUGhzV25EVUVsUVVabGxRWlI3R0gwVjE2dXA2VVdJbmZhcFI3MkZpWE1NSWRpdFh2VUdQakdid3JyOFBuTV9WYjVrTTBHM2wxdE00ZFlBVEJZaFVTVU91VXFHVmVGV3l3cmhXb0JtRDVyelpub3lCd0kwYVg3LXNzdTl6YmgzdnVmeTI?oc=5)

AI 기반 신약 개발 기업 Insilico Medicine이 제약 대기업 Eli Lilly와 최대 27.5억 달러 규모의 상업화 계약을 맺었습니다. (영문 용어: statnews.com). 이번 계약은 Insilico Medicine이 발굴한 잠재적 신약 후보 물질에 대한 권리를 Lilly에 부여하는 내용입니다. Insilico Medicine은 계약금과 마일스톤 지급액을 통해 수익을 얻게 됩니다. 이번 계약은 AI 기반 신약 개발의 상업적 가치와 잠재력을 입증하는 중요한 사례입니다. 출처는 Google News AI Search입니다.

### [Llama.cpp 및 로컬 LLM 관리를 돕는 앱 개발 중, 사용자 피드백 요청](https://www.reddit.com/r/LocalLLaMA/comments/1s783dm/are_you_interested_in_trying_out_an_app_that)

한 개발자가 Llama.cpp 설치 및 로컬 모델 관리를 용이하게 하는 앱을 개발 중이며, 사용자 피드백을 구하고 있습니다. 이 앱은 모델 다운로드, 테스트, 다른 앱을 위한 모델 서빙 기능을 제공합니다. 현재 Windows에서 사용 가능하며, 필요시 Linux 또는 Mac 빌드도 제공할 예정인 휴대용(portable) 앱입니다. 로컬 LLM 사용이 증가함에 따라, Llama.cpp와 같은 도구의 복잡성을 줄이고 사용자 편의성을 높이는 솔루션에 대한 수요가 커지고 있습니다. 출처는 Reddit r/LocalLLaMA입니다.

### [VAE 재구성 정확도 향상을 위한 픽셀 시프트 활용 연구에 대한 문의](https://www.reddit.com/r/MachineLearning/comments/1s787p0/d_prior_work_using_pixel_shift_to_improve_vae)

사용자는 현재 &quot;f8ch32&quot; VAE를 훈련 중이며, 재구성 충실도(reconstruction fidelity) 개선에 어려움을 겪고 있습니다. 기존 LPIPS 및 GAN 기반 방법들이 과도한 스무딩이나 이미지 조작 문제를 일으킨다고 지적합니다. 사용자는 훈련 이미지 세트에 픽셀 시프트(pixel shift)를 적용하여 정확도를 높이는 방법을 시도하고 있으며, 초기 성공을 거두고 있습니다. VAE의 재구성 충실도 개선은 생성 모델의 실제 적용 가능성을 높이는 중요한 연구 분야입니다. 출처는 Reddit r/MachineLearning입니다.

### [과학 글쓰기에서 AI 활용 시 저작권과 보조 역할의 균형이 중요해지고 있습니다.](https://news.google.com/rss/articles/CBMimgFBVV95cUxPMjV3MEIzU2p6VnBCdndSN2xPU3lXTWxVX1VlRERJWkxiR0VILW84N2h4Tkl1WmpRaVZ5NU5rMU1udmQ4dlhZYm5JWTFPWkxYODVvMzJiZGxwME9DeE5WX2pMM2MyVEVmcHVfckFjclJwZzBFbXFEQXRXZVpobThzTV9tNXpQSjcwYkF1WnQxVGNXSUJyTHhjVFh3?oc=5)

AI는 과학 글쓰기 과정에서 초안 작성, 문법 및 스타일 교정, 데이터 분석 요약 등 다양한 보조 역할을 수행할 수 있습니다. (영문 용어: KevinMD.com). AI의 도움을 받아도 최종 저작권은 인간 저자에게 있으며, AI가 생성한 내용에 대한 책임도 저자에게 있습니다. AI 사용 시 투명성을 확보하고, AI가 생성한 내용의 정확성과 신뢰성을 검증하는 과정이 필수적입니다. 과학 연구 및 출판 분야에서 AI 도구의 활용이 증가하면서, AI의 역할과 인간 저자의 책임 범위에 대한 명확한 가이드라인과 윤리적 논의가 중요해지고 있습니다. 출처는 Google News AI Search입니다.

### [Meta의 뇌 반응 예측 모델이 실제 콘텐츠에서 높은 정확도를 보이며 잠재적 활용 가능성을 입증했습니다.](https://www.reddit.com/r/MachineLearning/comments/1s6ylp1/p_i_tested_metas_brainresponse_model_on_posts_it)

한 Reddit 사용자가 Meta의 오픈소스 뇌 반응 모델을 활용하여 실험적인 UI와 시각화 도구를 구축했습니다. (영문 용어: brain-response). 이 모델은 실제 콘텐츠(텍스트)만으로 게시물의 뇌 반응 패턴을 예측하며, 좋아요나 공유 같은 실제 인기도 데이터 없이도 Elon Musk 관련 게시물이 바이럴 콘텐츠와 유사하다고 거의 완벽하게 예측했습니다. 동일한 주제라도 'UFO'와 '천체물리학'처럼 다른 방식으로 표현된 콘텐츠에 대해 모델이 완전히 다른 예측 반응 패턴을 보였습니다. 이 모델은 콘텐츠의 잠재적 영향력을 사전에 예측하고 최적화하는 데 활용될 수 있어, 마케팅, 콘텐츠 제작 등 다양한 분야에 혁신적인 변화를 가져올 수 있습니다. 출처는 Reddit r/MachineLearning입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [PixelSmile: Toward Fine-Grained Facial Expression Editing](https://huggingface.co/papers/2603.25728)

PixelSmile은 대칭적 공동 학습과 대조 학습을 통해 얼굴 표정 의미를 분리하여 정밀하고 제어 가능한 미세한 표정 편집을 가능하게 하는 diffusion 프레임워크를 제안합니다. (영문 용어: Fine-Grained). 기존의 미세한 얼굴 표정 편집은 의미론적 중첩으로 인해 한계가 있었습니다. 이 연구는 이러한 문제를 해결하기 위해 연속적인 감정 주석이 있는 Flex Facial Expression (FFE) 데이터셋을 구축하고, FFE-Bench를 통해 편집 정확도와 신원 보존 간의 균형을 평가합니다. PixelSmile은 완전히 대칭적인 공동 학습과 강도 감독, 대조 학습을 결합하여 표정 의미를 분리하고, 텍스트 잠재 공간 보간을 통해 정밀하고 안정적인 선형 표정 제어를 달성합니다. 이를 통해 PixelSmile은 우수한 분리 능력과 강력한 신원 보존을 보여주며, 연속적이고 제어 가능한 미세한 표정 편집에 효과적임을 입증합니다. 이 항목은 Hugging Face Papers (Top today) (2026-03-27 기준)에서 확인했습니다.

### 2. [Intern-S1-Pro: Scientific Multimodal Foundation Model at Trillion Scale](https://huggingface.co/papers/2603.25040)

Intern-S1-Pro는 1조 개의 파라미터를 가진 과학 멀티모달 파운데이션 모델로, 일반 및 과학 분야의 에이전트 기능과 100개 이상의 전문 과학 태스크를 마스터하여 성능을 향상시켰습니다. 이 연구는 일반 및 과학적 역량을 강화하기 위해 Intern-S1-Pro라는 1조 파라미터 규모의 과학 멀티모달 파운데이션 모델을 소개합니다. 이 모델은 XTuner 및 LMDeploy의 인프라 지원을 통해 1조 파라미터 수준의 효율적인 RL 학습을 가능하게 합니다. 이를 통해 모델은 일반적인 추론 및 이미지-텍스트 이해 능력을 넘어 고급 에이전트 기능을 갖추고, 화학, 재료, 생명 과학, 지구 과학 등 100개 이상의 전문 과학 태스크를 마스터합니다. 결과적으로 Intern-S1-Pro는 오픈 소스 모델 중 일반 능력에서 최고 수준을 유지하면서 전문 과학 태스크에서는 독점 모델을 능가하는 성능을 보여줍니다. 이 항목은 Hugging Face Papers (Top today) (2026-03-27 기준)에서 확인했습니다.

### 3. [Calibri: Enhancing Diffusion Transformers via Parameter-Efficient Calibration](https://huggingface.co/papers/2603.24800)

Calibri는 단일 학습 스케일링 파라미터를 사용하여 Diffusion Transformers(DiTs)의 생성 품질을 향상시키고 추론 단계를 줄이는 파라미터 효율적인 캘리브레이션 접근 방식입니다. (영문 용어: Parameter-Efficient). 이 연구는 Diffusion Transformers(DiTs)의 잠재력을 최대한 활용하여 생성 작업을 개선하는 데 중점을 둡니다. DiT 블록의 디노이징 프로세스 분석을 통해 단일 학습 스케일링 파라미터 도입이 성능을 크게 향상시킬 수 있음을 발견했습니다. 이를 바탕으로 Calibri는 DiT 구성 요소를 최적으로 보정하여 생성 품질을 높이는 파라미터 효율적인 접근 방식을 제안합니다. Calibri는 캘리브레이션을 진화 알고리즘으로 효율적으로 해결되는 블랙박스 보상 최적화 문제로 정의하며, 약 100개의 파라미터만 수정하여 다양한 text-to-image 모델에서 성능을 일관되게 향상시키고 추론 단계를 줄입니다. 이 항목은 Hugging Face Papers (Top today) (2026-03-27 기준)에서 확인했습니다.

### 4. [RealRestorer: Towards Generalizable Real-World Image Restoration with Large-Scale Image Editing Models](https://huggingface.co/papers/2603.25502)

RealRestorer는 대규모 이미지 편집 모델을 활용하여 다양한 실제 환경 이미지 손상 복원 성능을 향상시키기 위한 대규모 데이터셋과 오픈소스 모델을 개발했습니다. (영문 용어: Real-World, Large-Scale). 기존 이미지 복원 모델은 훈련 데이터의 규모와 분포 한계로 인해 실제 환경 손상에 대한 일반화 능력이 부족했습니다. 이 연구는 9가지 일반적인 실제 손상 유형을 포함하는 대규모 데이터셋을 구축하고, 이를 기반으로 최첨단 오픈소스 모델을 훈련하여 폐쇄형 모델과의 성능 격차를 줄였습니다. 또한, 손상 제거 및 일관성 유지에 초점을 맞춘 RealIR-Bench라는 벤치마크를 도입하여 실제 환경 손상 복원 성능을 평가했습니다. 실험 결과, RealRestorer는 오픈소스 방법 중 최고 성능을 달성했습니다. 이 항목은 Hugging Face Papers (Top today) (2026-03-27 기준)에서 확인했습니다.

### 5. [Voxtral TTS](https://huggingface.co/papers/2603.25551)

Voxtral TTS는 의미론적 토큰 생성과 acoustic 토큰에 대한 flow-matching을 결합한 하이브리드 아키텍처를 사용하여 짧은 참조 오디오로부터 자연스러운 다국어 음성을 생성하는 Text-to-Speech 모델입니다. Voxtral TTS는 3초 정도의 짧은 참조 오디오만으로도 자연스러운 다국어 음성을 생성하는 표현력 있는 Text-to-Speech 모델입니다. 이 모델은 semantic speech 토큰의 auto-regressive 생성과 acoustic 토큰에 대한 flow-matching을 결합한 하이브리드 아키텍처를 채택합니다. Voxtral Codec이라는 새로운 speech tokenizer를 사용하여 토큰을 인코딩 및 디코딩하며, 이 tokenizer는 VQ-FSQ 양자화 방식을 사용합니다. 사람 평가에서 Voxtral TTS는 ElevenLabs Flash v2.5 대비 68.4%의 선호도를 보이며 다국어 음성 복제에서 자연스러움과 표현력으로 우수함을 입증했습니다. 이 항목은 Hugging Face Papers (Top today) (2026-03-27 기준)에서 확인했습니다.

### 6. [MSA: Memory Sparse Attention for Efficient End-to-End Memory Model Scaling to 100M Tokens](https://huggingface.co/papers/2603.23516)

MSA(Memory Sparse Attention)는 sparse attention과 document-wise RoPE를 통해 LLM이 최대 1억 토큰의 장문 컨텍스트를 선형 복잡도로 효율적으로 처리할 수 있도록 합니다. (영문 용어: End-to-End). 기존 LLM은 full-attention 아키텍처의 제약으로 인해 컨텍스트 길이가 1M 토큰으로 제한되며, 이를 확장하려는 시도는 정확도 저하나 지연 시간 증가 등의 문제를 겪었습니다. 이 연구는 Memory Sparse Attention(MSA)이라는 새로운 프레임워크를 제안하여 이러한 한계를 극복합니다. MSA는 scalable sparse attention과 document-wise RoPE를 핵심 혁신으로 사용하여 학습 및 추론에서 선형 복잡도를 달성하며, 16K에서 100M 토큰으로 확장 시에도 9% 미만의 정확도 저하를 보입니다. 또한, KV cache compression과 Memory Parallel을 통해 2xA800 GPU에서 100M 토큰 추론이 가능하며, Memory Interleaving을 통해 복잡한 multi-hop 추론을 지원합니다. 이 항목은 Hugging Face Papers (Top today) (2026-03-27 기준)에서 확인했습니다.

### 7. [MACRO: Advancing Multi-Reference Image Generation with Structured Long-Context Data](https://huggingface.co/papers/2603.25319)

MACRO는 다중 참조 이미지 생성의 한계를 극복하기 위해 구조화된 장문 컨텍스트 데이터와 표준화된 평가 프로토콜을 제공하는 대규모 데이터셋과 벤치마크를 소개합니다. (영문 용어: Multi-Reference, Long-Context). 기존 다중 참조 이미지 생성 모델들은 입력 참조의 수가 증가함에 따라 성능 저하를 겪는데, 이는 단일 또는 소수 참조 쌍 위주의 데이터셋과 참조 간의 밀접한 의존성을 학습하는 데 필요한 구조화된 장문 컨텍스트 감독의 부족 때문입니다. 이 문제를 해결하기 위해, 최대 10개의 참조 이미지를 포함하는 40만 개의 샘플로 구성된 대규모 데이터셋인 MacroData를 제안합니다. 또한, 생성적 일관성을 평가하기 위한 4천 개의 샘플로 구성된 표준화된 벤치마크인 MacroBench를 함께 제시합니다. MacroData로 파인튜닝한 결과 다중 참조 생성에서 상당한 개선을 보였으며, 교차 태스크 공동 훈련과 장문 컨텍스트 복잡성 처리 전략의 시너지 효과가 확인되었습니다. 이 항목은 Hugging Face Papers (Top today) (2026-03-27 기준)에서 확인했습니다.

### 8. [SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks](https://huggingface.co/papers/2603.24755)

SlopCodeBench는 코딩 에이전트가 장기적인 반복 작업에서 코드 품질이 저하되는 방식을 측정하는 새로운 벤치마크를 제시합니다. (영문 용어: Long-Horizon). 기존 코딩 에이전트 벤치마크는 단일 솔루션 평가에 집중하여 반복적인 소프트웨어 개발의 특성을 제대로 반영하지 못했습니다. SlopCodeBench는 에이전트가 진화하는 사양에 따라 이전 솔루션을 반복적으로 확장하도록 요구하는 20가지 문제와 93가지 체크포인트로 구성된 언어 독립적인 벤치마크를 도입합니다. 이 벤치마크는 코드의 중복성을 나타내는 verbosity와 복잡도가 높은 함수에 집중된 structural erosion을 추적하여 코드 품질 저하를 측정합니다. 실험 결과, 현재 에이전트들은 반복적인 소프트웨어 개발에 필요한 설계 규율이 부족하며, 시간이 지남에 따라 코드 품질이 지속적으로 저하됨을 보여줍니다. 이 항목은 Hugging Face Papers (Top today) (2026-03-27 기준)에서 확인했습니다.

### 9. [AVControl: Efficient Framework for Training Audio-Visual Controls](https://huggingface.co/papers/2603.24793)

AVControl은 LTX-2 기반의 효율적인 프레임워크로, LoRA 어댑터를 활용하여 다양한 오디오-비주얼 제어 모달리티를 개별적으로 학습시켜 뛰어난 성능을 달성합니다. (영문 용어: Audio-Visual). 기존 오디오-비주얼 생성 제어 방식은 단일 모델로 고정된 제어를 수행하거나 새로운 모달리티마다 아키텍처 변경이 필요했습니다. AVControl은 LTX-2라는 오디오-비주얼 파운데이션 모델 위에 구축된 경량 프레임워크로, 각 제어 모달리티를 별도의 LoRA 어댑터로 학습시킵니다. 이 LoRA 어댑터는 병렬 캔버스에서 참조 신호를 추가 토큰으로 제공하여 아키텍처 변경 없이 다양한 제어 작업을 효율적으로 수행합니다. VACE 벤치마크에서 depth 및 pose 기반 생성, 인페인팅, 아웃페인팅 등에서 기존 베이스라인을 능가하며, 카메라 제어 및 오디오-비주얼 벤치마크에서도 경쟁력 있는 결과를 보여줍니다. 이 항목은 Hugging Face Papers (Top today) (2026-03-27 기준)에서 확인했습니다.

### 10. [VFIG: Vectorizing Complex Figures in SVG with Vision-Language Models](https://huggingface.co/papers/2603.24575)

VFIG는 Vision-Language 모델을 활용하여 복잡한 래스터 이미지를 SVG 형식의 벡터 그래픽으로 변환하는 새로운 모델 패밀리입니다. 이 연구는 래스터 이미지(PNG, JPEG)를 해상도 독립적이고 편집 가능한 SVG 벡터 그래픽으로 변환하는 문제를 해결합니다. VFIG는 대규모 데이터셋인 VFIG-DATA와 계층적 훈련 접근 방식을 사용하여 이 변환을 수행합니다. 모델은 원자적 프리미티브 학습을 위한 SFT(Supervised Fine-Tuning)와 전역적 다이어그램 충실도 최적화를 위한 RL(Reinforcement Learning)을 포함하는 coarse-to-fine 훈련 커리큘럼을 따릅니다. VFIG는 독점 모델에 필적하는 성능을 달성하며, 복잡한 그림의 구조적 무결성을 측정하는 새로운 평가 도구인 VFIG-BENCH를 도입했습니다. 이 항목은 Hugging Face Papers (Top today) (2026-03-27 기준)에서 확인했습니다.
