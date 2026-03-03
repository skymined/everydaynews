# IMDIGEST - 2026-03-03

- 기준일(KST): 2026-03-02 00:00:00 ~ 23:59:59

## AI News

- 어제자 기준으로 트렌드 포함 뉴스가 없습니다.

## Papers (Hugging Face Top 10)

### OmniLottie: Generating Vector Animations via Parameterized Lottie Tokens
- 한 줄 요약: OmniLottie는 전문적인 벡터 애니메이션 생성을 위해 Lottie 토큰화기와 사전 학습된 비주얼-언어 모델을 사용하여 다중 모드 지시사항을 따르고 고급 벡터 애니메이션을 생성한다.
- 핵심 아이디어: OmniLottie 프레임워크는 Lottie 토큰화기를 통해 JSON 파일을 구조화된 명령과 매개변수로 변환하여 사전 학습된 비주얼-언어 모델을 활용해 다중 모드 지시사항을 따르며 고급 벡터 애니메이션을 생성한다. 이를 통해 프로페셔널한 벡터 애니메이션을 쉽게 만들 수 있으며, MMLottie-2M 데이터셋으로부터 얻은 실험 결과는 다중 모드 지시사항에 따른 생동감 넘치고 의미적으로 일관된 벡터 애니메이션 생성 가능성을 입증한다.
- 키워드: #omnilottie #lottie-tokenizer #vision-language-model #vector-animation #mmlottie-2m #multimodal-instruction
- 링크: https://huggingface.co/papers/2603.02138

### VGGT-Det: Mining VGGT Internal Priors for Sensor-Geometry-Free Multi-View Indoor 3D Object Detection
- 한 줄 요약: VGGT-Det는 Visual Geometry Grounded Transformer와 어텐션 가이드 쿼리 생성 및 쿼리 드라이브 피처 앙상블을 통합하여 센서-지오메트리-Free의 실내 다중 뷰 3D 물체 탐지를 가능하게 합니다. (원문 용어: Sensor-Geometry-Free, Multi-View)
- 핵심 아이디어: 현재의 다중 뷰 실내 3D 물체 탐지는 정확한 카메라 포즈를 필요로 하며, 이는 비용이 많이 듭니다. VGGT-Det는 이러한 문제를 해결하기 위해 Visual Geometry Grounded Transformer와 어텐션 가이드 쿼리 생성 및 쿼리 드라이브 피처 앙상블을 통합하여 센서-지오메트리-Free의 실내 다중 뷰 3D 물체 탐지를 수행합니다. 이를 통해 VGGT 내부에서 추출된 의미적이고 지오메트릭한 사전 지식을 효과적으로 활용할 수 있습니다.
- 키워드: #vggt-det #visual-geometry-grounded-transformer #어텐션-가이드-쿼리-생성 #쿼리-드라이브-피처-앙상블 #실내-3d-물체-탐지 #센서-지오메트리-free
- 링크: https://huggingface.co/papers/2603.00912

### RubricBench: Aligning Model-Generated Rubrics with Human Standards
- 한 줄 요약: RubricBench은 모델 생성 러브릭과 인간 표준을 일치시키는 새로운 벤치마크로, 기존 벤치마크의 단점을 보완한다. (원문 용어: Model-Generated)
- 핵심 아이디어: RubricBench은 대형 언어 모델(Large Language Model)의 라벨링 방향성을 정확히 평가하기 위해 설계된 새로운 벤치마크로, 기존 벤치마크들이 부족한 복잡성과 참조 표준이 부족하다는 문제를 해결한다. 이 연구는 모델 생성 러브릭과 인간 생성 러브릭 간의 성능 차이를 분석하여, 현재까지 가장 우수한 모델들도 인간에 비해 러브릭 기반 평가에서 큰 허위편향을 보이는 것으로 나타났다.
- 키워드: #rubricbench #대형-언어-모델 #러브릭 #평가 #표준화
- 링크: https://huggingface.co/papers/2603.01562

### Spectral Condition for μP under Width-Depth Scaling
- 한 줄 요약: 이 연구는 가중치와 그 업데이트의 넓이-깊이 스케일링에 따른 규모 변화를 정확히 설명하는 스펙트럼 μP 조건을 개발하여, 기존의 다양한 μP 공식을 통합하고, 광범위한 최적화 알고리즘에서 μP 구현 방법을 제시한다. (원문 용어: Width-Depth)
- 핵심 아이디어: 가중치 학습과 그 업데이트에 대한 스펙트럼 μP 조건을 개발하여, 가중치와 업데이트의 규모가 넓이-깊이 스케일링에 따라 어떻게 변화해야 하는지 정확히 설명한다. 이를 바탕으로 다양한 최적화 알고리즘에서도 μP를 구현하는 일반적인 레시피를 도출하여, 기존의 SGD와 AdamW 등과 같은 μP 공식을 포함하면서도 더 넓은 범위의 최적화 알고리즘에 자연스럽게 확장 가능하다. 이를 통해 GPT-2 스타일 언어 모델에서 안정적인 특징 학습과 뛰어난 하이퍼파라미터 전달을 보여준다.
- 키워드: #μp #spectral-condition #width-depth-scaling #stable-feature-learning #hyperparameter-transfer #optimization
- 링크: https://huggingface.co/papers/2603.00541

### LLaDA-o: An Effective and Length-Adaptive Omni Diffusion Model
- 한 줄 요약: LLaDA-o는 Mixture of Diffusion(MoD) 프레임워크를 사용하여 텍스트 이해와 시각 생성을 분리하고 공유된 어텐션 백본을 통해 결합하는 오미니 디퓨전 모델입니다. (원문 용어: Length-Adaptive)
- 핵심 아이디어: LLaDA-o는 Mixture of Diffusion(MoD) 프레임워크를 기반으로 텍스트 이해와 시각 생성을 분리하고 공유된 어텐션 백본을 통해 결합하여, 고정 조건에 대한 중복 계산을 줄이는 효과적인 오미니 디퓨전 모델입니다. 또한, 데이터 중심적 길이 적응 전략을 도입하여 다모달 설정에서 유동적인 길이 디코딩을 가능하게 하여 성능을 향상시킵니다.
- 키워드: #llada-o #mixture-of-diffusion-(mod) #오미니-디퓨전-모델 #공유-어텐션-백본 #데이터-중심적-길이-적응
- 링크: https://huggingface.co/papers/2603.01068

### Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data
- 한 줄 요약: Tool-R0는 초기 데이터 없이 대형 언어 모델을 기반으로 한 도구 사용 능력을 학습하는 자가 진화하는 LLM 에이전트 프레임워크입니다. (원문 용어: Self-Evolving, Tool-Learning)
- 핵심 아이디어: Tool-R0는 대형 언어 모델에서 시작하여 자기 플레이 강화학습을 통해 도구 사용 능력을 배우는 일반적인 도구 호출 에이전트를 학습하는 방법을 제시합니다. 이 프레임워크는 초기 데이터 없이 가정하더라도, 생성기와 해결기가 서로의 기술 경계에서 도전적인 작업을 제안하고 이를 해결하면서 자가 진화하는 루프를 형성합니다. 이를 통해 Tool-R0은 기본 모델보다 92.5% 성능 향상을 달성하며 완전히 감독하된 도구 호출 기반 모델들을 초과했습니다.
- 키워드: #tool-r0 #자기-플레이-강화학습 #대형-언어-모델 #도구-사용 #자가-진화
- 링크: https://huggingface.co/papers/2602.21320

### Legal RAG Bench: an end-to-end benchmark for legal RAG
- 한 줄 요약: Legal RAG Bench은 법적 정보 검색과 생성 시스템의 종합적인 평가를 위한 벤치마크로, 정보 검색이 성능에 더 큰 영향을 미친다는 것을 보여줍니다. (원문 용어: end-to-end)
- 핵심 아이디어: 법적 정보 검색-증강 생성(RAG) 시스템의 종합적인 평가를 위해 Legal RAG Bench이 제안되었습니다. 이 벤치마크는 복잡한 질문에 대한 정답과 지원 문서를 제공하는 4,876개의 판문서로 구성되어 있으며, 정보 검색 모델과 추론 모델의 기여도를 분석하기 위한 고급 요인 설계와 계층적 오류 분해 프레임워크를 사용합니다. 연구 결과, 정보 검색이 RAG 시스템 성능에 가장 큰 영향을 미치며, 언어 모델은 더 적은 영향력을 가졌습니다.
- 키워드: #legal-rag-bench #information-retrieval #rag-system #factorial-design #error-decomposition
- 링크: https://huggingface.co/papers/2603.01710

### When Does RL Help Medical VLMs? Disentangling Vision, SFT, and RL Gains
- 한 줄 요약: 이 연구는 의료 분야의 시각-언어 모델에서 강화학습(RL)이 주로 출력 분포를 둔화시키며, 이전에 확장된 초기 능력을 보완하는 역할을 한다.
- 핵심 아이디어: 연구는 의료 VLMs에서 RL과 SFT의 효과를 분리하여, 모델이 이미 충분한 논리적 지원을 받고 있을 때 RL은 주로 출력 분포를 둔화시키며, 이전에 확장된 초기 능력을 보완한다고 밝힌다. 이를 위해 MedMNIST와 같은 다중모달 테스트베드에서 시각 인식과 논리적 지원 및 샘플링 효율성을 평가하였으며, 이러한 결과를 바탕으로 모델의 경계에 맞춘 레시피를 제안하였다.
- 키워드: #reinforcement-learning #medical-vlms #supervised-fine-tuning #pass@k #medmnist #visual-perception
- 링크: https://huggingface.co/papers/2603.01301

### CC-VQA: Conflict- and Correlation-Aware Method for Mitigating Knowledge Conflict in Knowledge-Based Visual Question Answering
- 한 줄 요약: CC-VQA는 시각적 상관성과 갈등에 대한 인식을 통한 지식 기반 비주얼 질문 응답에서의 지식 갈등 해소 방법을 제시한다. (원문 용어: Correlation-Aware, Knowledge-Based)
- 핵심 아이디어: CC-VQA는 시각 정보와 언어 정보 간의 갈등을 분석하고, 관련성에 따라 인코딩과 디코딩을 조정하여 이러한 갈등을 해결하는 방법을 도입합니다. 이를 위해 두 가지 핵심 구성 요소가 있습니다: 첫째, 내부 및 외부 지식 컨텍스트에서 시각적-언어 간의 갈등 분석을 수행하는 시각 중심 컨텍스트 갈등 논리; 둘째, 관련성에 따라 위치 인코딩 압축과 상관성 가중 갈등 점수를 사용한 적응 디코딩을 특징으로 하는 관련성 지도 인코딩 및 디코딩입니다. 이러한 방법은 E-VQA, InfoSeek, OK-VQA 등 다양한 벤치마크에서 우수한 성능을 보여줍니다.
- 키워드: #cc-vqa #knowledge-based-visual-question-answering #conflict-reasoning #correlation-guided-encoding #visual-semantic-conflict
- 링크: https://huggingface.co/papers/2602.23952

### Half-Truths Break Similarity-Based Retrieval
- 한 줄 요약: CS-CLIP은 CLIP 모델의 반 진실 문제를 해결하기 위해 컴포넌트 감독 하에 미세 조정을 수행하여 콘 포지셔널 이해를 향상시킵니다. (원문 용어: Half-Truths, Similarity-Based)
- 핵심 아이디어: CLIP 스타일의 모델은 잘못된 세부 정보가 유사성 점수를 높이는 반 진실 문제에 취약하며, 이는 컴포넌트 감독 하에 미세 조정을 통해 해결됩니다. CS-CLIP은 캡션을 개체와 관계 단위로 분해하고, 각 단위에 대해 최소 편집된 대안을 생성하여 모델을 정확한 단위보다는 그의 대안을 더 낮게 평가하도록 미세 조정합니다. 이를 통해 반 진실 문제 해결률이 69.3%로 높아지고, 콘 포지셔널 벤치마크 성능도 향상됩니다.
- 키워드: #cs-clip #clip #반-진실 #컴포넌트-감독 #미세-조정 #콘-포지셔널-이해
- 링크: https://huggingface.co/papers/2602.23906
