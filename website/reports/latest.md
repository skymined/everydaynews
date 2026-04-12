# IMDIGEST - 2026-04-13

2026-04-13 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-04-13 AI 브리핑입니다. 오늘은 TechCrunch AI, TechCrunch AI에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

### [HumanX 컨퍼런스에서 Anthropic의 Claude가 가장 많이 언급되며 OpenAI의 ChatGPT를 제치고 주목받았습니다.](https://techcrunch.com/2026/04/12/at-the-humanx-conference-everyone-was-talking-about-claude)

샌프란시스코에서 열린 HumanX AI 컨퍼런스에서 에이전트 AI가 비즈니스를 변화시키는 방식에 대한 논의가 활발했습니다. 참가자들 사이에서 가장 인기 있는 챗봇으로 Anthropic의 Claude가 일관되게 언급되었습니다. OpenAI의 ChatGPT는 컨퍼런스에서 거의 언급되지 않았으며, 일부 벤더들은 ChatGPT와 OpenAI가 하락세라고 평가했습니다. 에이전트 AI의 비즈니스 및 코딩 작업 자동화가 산업 전반에 걸쳐 확산되면서, 기업 및 소비자 중심 챗봇의 중요성이 커지고 있습니다. 출처는 TechCrunch AI입니다.

### [트럼프 행정부, 은행들에게 Anthropic의 Mythos 모델 테스트를 장려하며 사이버 보안 역량 강화 추진](https://techcrunch.com/2026/04/12/trump-officials-may-be-encouraging-banks-to-test-anthropics-mythos-model)

미 재무장관 Scott Bessent와 연준 의장 Jerome Powell은 은행 경영진들에게 Anthropic의 새로운 Mythos 모델을 활용하여 취약점을 탐지하도록 권고했습니다. JPMorgan Chase 외에도 Goldman Sachs, Citigroup, Bank of America, Morgan Stanley 등 주요 은행들이 Mythos 모델을 테스트 중인 것으로 알려졌습니다. Anthropic은 Mythos 모델이 사이버 보안에 특화되지 않았음에도 불구하고 보안 취약점 탐지에 매우 뛰어나다고 밝혔습니다. 미국 정부가 AI 기술을 활용하여 금융 시스템의 사이버 보안을 강화하려는 움직임을 보이며, AI 모델의 실제 적용 사례가 확대되고 있습니다. 출처는 TechCrunch AI입니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [LLM 및 Agentic 모델 벤치마킹의 비효율성과 자원 낭비 문제에 대한 비판이 제기되며, 베이지안 기법을 활용한 새로운 벤치마킹 프레임워크의 필요성이 강조되고 있습니다.](https://www.reddit.com/r/MachineLearning/comments/1sjnha5/frameworks_for_supporting_llmagentic_benchmarking)

기존 LLM 벤치마킹 방식은 새로운 모델을 만들고 방대한 벤치마킹 스위트를 실행하여 미미한 성능 향상을 입증하는 데 초점을 맞추고 있습니다. (영문 용어: LLM/Agentic). Google Gemini 벤치마킹 사례에서 30,000개의 프롬프트를 사용하는 등 막대한 자원 소모가 발생하며, 이는 모델 반복 시마다 반복되어 비효율적입니다. 현재 주로 사용되는 pass@k와 같은 지표는 모델의 실제 능력에 대한 신뢰를 주거나 개선 사항을 효과적으로 전달하지 못한다는 비판이 있습니다. LLM 개발 및 MLOps 과정에서 발생하는 막대한 컴퓨팅 자원 소모와 환경적 영향에 대한 우려가 커지면서, 보다 효율적이고 신뢰할 수 있는 벤치마킹 방법론에 대한 요구가 증가하고 있습니다. 출처는 Reddit r/MachineLearning입니다.

### [Pi와 Qwen3.5 모델이 llama-cpp 환경에서 프롬프트 재처리를 과도하게 수행하는 문제 발생](https://www.reddit.com/r/LocalLLaMA/comments/1sjsejm/pi_qwen35_with_llamacpp_doing_a_lot_of_prompt)

llama-cpp를 사용하여 Pi를 코딩 에이전트로 활용할 때, Qwen3.5 122b 모델에서 프롬프트 재처리 문제가 발생합니다. (영문 용어: re-processing). 에이전트가 여러 번의 편집 작업을 수행하며 'thinking' 및 'tool calls'를 인터리빙하는 과정은 정상적으로 작동합니다. 하지만 사용자의 다음 입력 시, Pi가 'thinking blocks'를 전송하지 않아 컨텍스트 캐시가 무효화되고 재연산이 발생합니다. 이는 LLM 에이전트의 효율적인 컨텍스트 관리 및 캐싱 전략에 대한 중요성을 부각시키며, 특히 복잡한 상호작용에서 성능 저하를 야기할 수 있습니다. 출처는 Reddit r/LocalLLaMA입니다.

### [동아프리카 공동체(EAC), 역내 AI 기술 펀드 조성으로 AI 주권 확보 및 경제 변혁 추진](https://www.reddit.com/r/artificial/comments/1sjln80/east_african_community_launches_regional_ai_fund)

동아프리카 공동체(EAC) 회원국들은 상업적으로 실현 가능한 AI 솔루션 연구 및 혁신 확대를 목표로 하는 역내 AI 기술 펀드 설립에 합의했습니다. 이 펀드는 혼합 금융을 동원하고 민간 부문 투자를 유치하여 현지 개발 AI 솔루션을 위한 지속 가능한 자금 파이프라인을 구축할 예정입니다. EAC는 동아프리카 데이터로 훈련되고 Kiswahili와 같은 현지 언어로 운영되며 역내 인프라에 호스팅되는 AI 시스템 개발을 통해 AI 주권을 확보하고자 합니다. 아프리카 개발은행에 따르면, 포괄적인 AI 배치는 2035년까지 아프리카 전역에서 최대 1조 달러의 추가 GDP를 창출하고 4천만 개의 디지털 일자리를 만들 수 있어, 이번 펀드 조성은 아프리카의 경제 변혁에 중요한 기여를 할 것으로 예상됩니다. 출처는 Reddit r/artificial입니다.

### [Bain & Company가 Agentic AI 플랫폼의 세 가지 핵심 레이어를 제시하며 AI 시스템 구축의 중요성을 강조합니다.](https://news.google.com/rss/articles/CBMifkFVX3lxTFBucGQzdjd6V0h0R0ZUcUdNU21GN3RESnFrVzF2MldTUW12Tkw4Tkw3RnhXTW9DSndHanEyZnhmTm1hX2JkYklrZi1oVVc3YWlGVDBGMWNBdHZyRVRqX0dXSTVKNmZ1ZUlHYjFnNExIcnlHckFNdlRId1lRaXJzUQ?oc=5)

Bain & Company는 Agentic AI 플랫폼을 구축하기 위한 세 가지 핵심 레이어인 'Foundation Models', 'Agentic Capabilities', 'Enterprise Integration'을 제시했습니다. 'Foundation Models'는 AI 시스템의 기반이 되는 대규모 언어 모델 등을 의미하며, 'Agentic Capabilities'는 AI가 자율적으로 목표를 설정하고 실행하는 능력을 말합니다. 'Enterprise Integration'은 이러한 AI 역량을 기업의 기존 시스템 및 워크플로우에 통합하는 과정을 포함합니다. Agentic AI는 단순한 도구를 넘어 자율적으로 의사결정하고 행동하는 AI 시스템으로 진화하고 있으며, 이는 기업의 운영 방식과 비즈니스 모델에 근본적인 변화를 가져올 잠재력을 가지고 있습니다. 출처는 Google News AI Search입니다.

### [Anthropic, 에이전트의 '두뇌'와 '손'을 분리하여 확장성 높은 Managed Agent 시스템 구축](https://news.google.com/rss/articles/CBMiYkFVX3lxTE5LY3VWakFxdE02bVBBdDNrSEJaY2NqV1ZkZ3hfNUxBeWFXZDdrU21vTTdnSFdNUGNPRVpSMWVyVGp6MWlQWTFYU2JIcVZDdDcwMXcwRlpYNExMeWZBMGxXOWJ3?oc=5)

Anthropic은 에이전트의 '두뇌'(추론 및 계획)와 '손'(도구 사용 및 환경 상호작용)을 분리하는 새로운 아키텍처를 제안했습니다. 이 분리된 접근 방식은 에이전트의 각 구성 요소를 독립적으로 확장하고 개선할 수 있게 합니다. 이를 통해 복잡한 작업을 수행하는 에이전트의 안정성과 효율성을 높이는 것을 목표로 합니다. AI 에이전트의 복잡성이 증가함에 따라, 모듈화된 설계는 확장성 및 관리 용이성 측면에서 중요한 트렌드로 부상하고 있습니다. 출처는 Google News AI Search입니다.

### [RTX 3060 12GB 환경에서 Claude 4.6 Sonnet에 준하는 성능을 내는 LLM 모델에 대한 관심이 증가하고 있습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1sjqq92/any_good_llm_near_claude_46sonnet_for_a_3060_12gb)

사용자가 RTX 3060 12GB GPU 환경에서 Claude 4.6 Sonnet과 유사한 성능을 내는 LLM을 찾고 있습니다. 현재 Gemma4를 사용해봤지만 코딩 및 실제 업무 호환성 문제로 다른 대안을 모색 중입니다. 주로 프로그래밍 어시스턴트 용도로 활용할 수 있는 LLM을 찾고 있습니다. 로컬 환경에서 고성능 LLM을 구동하려는 수요가 증가하며, 특정 하드웨어 제약 내에서 최적의 모델을 찾는 것이 중요해지고 있습니다. 출처는 Reddit r/LocalLLaMA입니다.

### [KIV 기술로 RTX 4070에서 1M 토큰 컨텍스트 윈도우를 구현, HuggingFace 모델에 재학습 없이 적용 가능합니다.](https://www.reddit.com/r/MachineLearning/comments/1sjkmwz/kiv_1m_token_context_window_on_a_rtx_4070_12gb)

KIV(K-Indexed V Materialization)는 HuggingFace 트랜스포머의 표준 KV 캐시를 계층형 검색 시스템으로 대체하는 미들웨어 레이어입니다. (영문 용어: drop-in). 이 기술은 최근 토큰을 VRAM에 유지하고, 오래된 K/V를 시스템 RAM으로 이동시키며, K 벡터를 검색 인덱스로 사용하여 디코딩 단계당 약 256개의 가장 관련성 높은 V 엔트리만 불러옵니다. RTX 4070 (12GB VRAM)에서 Gemma 4 E2B (4-bit) 모델로 1M 토큰 컨텍스트를 12MB의 KIV VRAM 오버헤드와 약 6.5GB의 총 GPU 사용량으로 처리할 수 있습니다. 이 기술은 제한된 GPU VRAM 환경에서도 대규모 언어 모델(LLM)의 컨텍스트 윈도우를 획기적으로 확장하여, 더 긴 문서나 대화를 처리할 수 있게 합니다. 출처는 Reddit r/MachineLearning입니다.

### [Palantir CEO, AI가 인문학 일자리를 파괴할 것이라고 경고](https://news.google.com/rss/articles/CBMilAFBVV95cUxPYUpnTUFwQWpmQURZdzYxblotNzJjMFZROU1TQ2hZdXp5bkFNdGdnYUh6TWk3M2FETUJmQVRWRG91MU9hRHpUNnJVYllybGt3NkZQWFExdjJZR0FlUC1fX0FjdVVXR1FQTXR2azNfY2NUcjR6WHVtNjM2eU5JUTVqWG44M2FQbkFOdUh0eEo3T0pIZ25h?oc=5)

Palantir의 CEO 알렉스 카프는 AI가 인문학 분야의 일자리를 파괴할 것이라고 예측했습니다. 그는 AI가 인간의 지능을 능가하는 능력을 가질 것이며, 이는 인문학 관련 직업에 큰 영향을 미칠 것이라고 언급했습니다. 카프 CEO는 이러한 변화가 사회 전반에 걸쳐 광범위한 영향을 미칠 것이라고 강조했습니다. AI 기술의 발전이 특정 산업 분야를 넘어 인문학 등 다양한 직업군에 미칠 파괴적인 영향에 대한 경고가 나오고 있습니다. 출처는 Google News AI Search입니다.

### [미국 전역의 AI 데이터센터 건설 붐이 지역사회 저항에 부딪히고 있습니다.](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOMnNsbXpFUkNFZGhfaHF4YVdEdTlWZGhKVFpPaEFZZDdUS19fUlo4Z1RJeWQ2SGhEWi1sQ0RhdzZmanlGNXJxM0ExRUJCRzZ5cGZlcVBDWHp0VzNNVGYwWFpDMU5WbGhaUW1sLTJtSGNjeElOdGQyb1hVajFqZGVuaDU5UTB2cURW0gGOAUFVX3lxTFBEM0lKZ3dncWN3eGZiTW1nMUQ1MkdJcktlSzBLdklZSXBXZUcxWHNDNExibFJQR3dtRTlNYjliU1RaaGF3eXlyaXpRUWJ3QjdmUFhKRm1PdkpiUVlRSjVlS29BV05NdWRlTWRYQ1lrd2Q4aktPQzFLek1pS2FSWWJyQi1kUm5GZHRKUFlueEE?oc=5)

AI 기술 발전과 함께 데이터센터 수요가 급증하며 미국 전역에 새로운 데이터센터 건설이 활발합니다. 이러한 데이터센터는 막대한 전력을 소비하고, 소음과 열을 발생시키며, 지역의 물 자원을 많이 사용합니다. 지역 주민들은 데이터센터 건설로 인한 환경 문제와 생활 불편을 우려하며 반대 운동을 벌이고 있습니다. AI 인프라 확장이 가속화되면서 전력, 용수 등 자원 소비 증가에 대한 사회적 논의와 갈등이 심화될 것입니다. 출처는 Google News AI Search입니다.

### [영국 규제 당국, Anthropic의 최신 AI 모델 위험성 평가에 착수](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNTE5WeEN6VnpyejdsUVA2OWlMNUZabmVPMGpLUkIzbDVMZXgyZ3JhWjBIU2dwODdZZzZpZThObkFQME9QMk8xX0Y2MXg3TVhBdzZsS3hPXzJJLVQ3aTY5SkxHTVBTWnBRRmVvbEhZcVBrVkswdWZLQlpYbWNZdFF1cW9PbzRRdHU0R3VmQ1NKRnZhSWZ3SGdCSThLdWdMZGNvNnRkQzJObUMtcTBUTWFXb3pNSkNfaE4yUmJrRkpUQWh1Zw?oc=5)

영국 규제 당국이 Anthropic의 새로운 AI 모델에 대한 위험성 평가를 서두르고 있습니다. 이번 평가는 AI 기술의 급속한 발전에 따른 잠재적 위험에 대한 우려가 커지고 있음을 반영합니다. AI 기술의 발전 속도가 빨라지면서 각국 정부와 규제 기관들이 AI 모델의 안전성과 윤리적 문제에 대한 감독을 강화하는 추세입니다. 출처는 Google News AI Search입니다.

### [Qwen 3.5 28B A3B REAP 모델이 코딩 작업에서 인상적인 성능을 보였습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1sjprna/qwen_35_28b_a3b_reap_for_coding_initial)

Qwen 3.5 모델은 코딩 작업에 최적화되어 있으며, 특히 Qwen-3.5-28B-A3B-REAP-GGUF 버전이 주목받고 있습니다. 이 모델은 llama.cpp 환경에서 관련 참조를 언급하고 상세한 '사고' 및 계획 단계를 거쳐 응답을 생성합니다. Qwen 3.5는 셸 스크립트 코드 분석 및 사용 문서화 작업에서 뛰어난 성능을 보여주며, 잘 포맷된 .md 파일을 생성합니다. Qwen 3.5는 코딩 및 문서화 작업에 특화된 LLM의 발전 가능성을 보여주며, 개발 생산성 향상에 기여할 수 있습니다. 출처는 Reddit r/LocalLLaMA입니다.

### [Canva 사용자가 AI 기능으로 인해 구독 취소를 고려하며, 이는 모든 B2B 벤더에게 경고가 되고 있습니다.](https://news.google.com/rss/articles/CBMiwAFBVV95cUxOMTVzRlB2bGpHa29vTG1WaklPd0pKS2F0a05QVTJyQzBaVGY2UUk1ckNNREJSX2RHMC1rekVETnYxRWM4VW9PS1VnUXg1V211LTN5bHpsYThNUTRyVXdUdlVPRHl4WDgzeHhTLWtUai1UMUNnd0hQVVptazJPcnRaejEwUjhFSlpsR2F1ZVdvMjlHRmtCSC1reDFKajRyaWFoejFrcGUtVFlZbkk1SGFOdzU4MGw3eTlMRHUtbFZ3YUM?oc=5)

Canva는 저렴한 가격과 편리한 기능으로 많은 사용자에게 사랑받고 있습니다. 최근 AI 기능 도입에도 불구하고, 일부 사용자는 AI 기능이 충분히 만족스럽지 않아 구독 취소를 고려하고 있습니다. 이는 AI 기능이 사용자 경험을 오히려 저해하거나 기대에 미치지 못할 경우, 기존 서비스의 장점마저 상쇄할 수 있음을 시사합니다. AI 기술 도입이 모든 서비스에 긍정적인 영향을 미치는 것은 아니며, 사용자 니즈와 기대치를 충족시키지 못하면 역효과를 낼 수 있습니다. 출처는 Google News AI Search입니다.

### [Palantir CEO, AI가 인문학 일자리를 파괴할 것이며 직업 훈련을 받은 사람들에게는 충분한 일자리가 있을 것이라고 언급](https://www.reddit.com/r/artificial/comments/1sjqjji/palantir_ceo_says_ai_will_destroy_humanities_jobs)

Palantir의 CEO Alex Karp는 AI가 인문학 분야의 일자리를 없앨 것이라고 주장했습니다. 그는 AI가 직업 훈련을 받은 사람들에게는 더 많은 일자리를 창출할 것이라고 예측했습니다. Karp는 AI가 사회에 미치는 영향에 대해 강한 의견을 표명했습니다. AI 기술 발전이 미래 노동 시장에 미칠 구조적 변화에 대한 논의가 활발해지고 있음을 보여줍니다. 출처는 Reddit r/artificial입니다.

### [ICML 논문 심사에서 극단적인 평가를 받은 연구자가 혼란을 겪고 있습니다.](https://www.reddit.com/r/MachineLearning/comments/1sjkfil/so_confused_about_polarizing_icml_reviews_d)

ICML 논문 심사에서 긍정적인 평가와 부정적인 평가가 극명하게 엇갈리는 상황이 발생했습니다. 한 논문이 초기 5, 4, 4, 2점에서 재심사 후 5, 5, 5, 2점으로 변경되었으며, 평균 점수는 4.25점, 신뢰도 평균은 4점입니다. 두 명의 심사위원은 재심사 후 점수를 4점에서 5점으로 상향 조정하며 긍정적인 피드백을 제공했습니다. ICML과 같은 주요 학회에서 논문 심사의 공정성과 일관성에 대한 의문이 제기되고 있습니다. 출처는 Reddit r/MachineLearning입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [Rethinking Generalization in Reasoning SFT: A Conditional Analysis on Optimization, Data, and Model Capability](https://huggingface.co/papers/2604.06628)

이 연구는 SFT(Supervised Finetuning)가 추론 작업에서 일반화되지 않는다는 통념을 재고하며, 최적화, 데이터, 모델 역량에 따라 조건부적인 교차 도메인 일반화가 가능함을 밝힙니다. 기존에는 SFT가 추론 작업에서 일반화되지 않고 암기만 한다고 여겨졌습니다. 본 연구는 긴 CoT(Chain-of-Thought) 감독을 통한 SFT가 최적화 역학, 훈련 데이터, 기본 모델 역량에 따라 조건부적인 교차 도메인 일반화를 보임을 발견했습니다. 특히, 충분한 훈련 시 성능 저하 후 회복 및 개선되는 'dip-and-recovery' 패턴을 보이며, 검증된 고품질의 긴 CoT 데이터가 일관된 교차 도메인 이득을 제공합니다. 또한, 강력한 모델은 전이 가능한 절차적 패턴을 내재화하지만, 이러한 일반화는 추론 능력 향상과 안전성 저하라는 비대칭적인 결과를 가져옵니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 2. [SkillClaw: Let Skills Evolve Collectively with Agentic Evolver](https://huggingface.co/papers/2604.08377)

SkillClaw는 다중 사용자 LLM 에이전트 시스템에서 사용자 상호작용을 집계하여 재사용 가능한 스킬을 자율적으로 업데이트하고 개선하는 집단 스킬 진화 프레임워크를 제안합니다. 기존 LLM 에이전트 시스템에서 스킬은 배포 후 정적 상태로 유지되어 사용자 간에 유사한 워크플로우와 실패 모드가 반복적으로 발생했습니다. SkillClaw는 이러한 문제를 해결하기 위해 다중 사용자 및 시간 경과에 따른 상호작용을 스킬 개선의 주요 신호로 활용합니다. 이 프레임워크는 사용 중 생성된 궤적을 지속적으로 집계하고, 자율적인 Evolver가 반복적인 행동 패턴을 식별하여 기존 스킬을 개선하거나 새로운 기능을 추가함으로써 스킬 세트를 업데이트합니다. 이를 통해 사용자 간 지식 전달과 누적 역량 개선이 가능하며, WildClawBench 실험에서 Qwen3-Max의 성능을 크게 향상시키는 것을 보여주었습니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 3. [ClawBench: Can AI Agents Complete Everyday Online Tasks?](https://huggingface.co/papers/2604.08523)

ClawBench는 AI 에이전트가 복잡한 온라인 작업을 수행할 수 있는지 평가하기 위해 153개의 실제 웹 작업을 포함하는 새로운 벤치마크를 제시합니다. 이 연구는 AI 에이전트가 이메일 자동화를 넘어 일상생활의 다양한 온라인 작업을 처리할 수 있는지 평가하는 문제를 제기합니다. 이를 위해 ClawBench는 구매, 예약, 구직 신청 등 144개 플랫폼에 걸쳐 153개의 실제 다단계 웹 작업을 포함하는 평가 프레임워크를 도입합니다. 이 벤치마크는 기존 벤치마크와 달리 실제 운영 웹사이트에서 동적인 상호작용과 복잡성을 유지하며 에이전트를 평가합니다. 평가 결과, 7개의 최신 모델(예: Claude Sonnet 4.6) 모두 이러한 작업의 극히 일부만 완료할 수 있었으며, 이는 AI 에이전트의 일반적인 보조 기능에 대한 상당한 개선이 필요함을 시사합니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 4. [HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents](https://huggingface.co/papers/2604.07430)

HY-Embodied-0.5는 Mixture-of-Transformers 아키텍처와 반복적인 후속 학습을 통해 실제 환경 에이전트의 시각 인지 및 추론 능력을 향상시킨 Embodied Foundation Model 제품군입니다. (영문 용어: Real-World). 이 연구는 일반 VLM과 Embodied Agent 간의 격차를 해소하기 위해 공간적, 시간적 시각 인지 및 예측, 상호작용, 계획을 위한 Embodied 추론 능력을 강화한 HY-Embodied-0.5 모델을 제안합니다. 모델은 모달리티별 컴퓨팅을 가능하게 하는 Mixture-of-Transformers(MoT) 아키텍처를 채택하여 미세한 시각 인지 능력을 향상시키고, 반복적인 자기 진화 후속 학습 패러다임을 도입하여 추론 능력을 개선합니다. 또한, 대규모 모델의 고급 기능을 소규모 모델로 전이시키는 on-policy distillation을 활용하여 효율적인 엣지 배포 모델과 복잡한 추론 모델 두 가지를 제공합니다. 22개 벤치마크에서 시각 인지, 공간 추론, Embodied 이해도에 걸쳐 광범위한 평가를 통해 접근 방식의 효과를 입증했습니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 5. [When Numbers Speak: Aligning Textual Numerals and Visual Instances in Text-to-Video Diffusion Models](https://huggingface.co/papers/2604.08546)

NUMINA는 텍스트-투-비디오 확산 모델에서 텍스트 프롬프트에 지정된 객체 수를 정확하게 생성하지 못하는 문제를 해결하기 위해 훈련 없이 레이아웃 불일치를 식별하고 어텐션 변조를 통해 재생성을 유도하는 프레임워크입니다. (영문 용어: Text-to-Video). 텍스트-투-비디오 확산 모델은 프롬프트에 명시된 객체 수를 정확하게 생성하는 데 어려움을 겪습니다. NUMINA는 이러한 수치적 불일치를 개선하기 위해 훈련이 필요 없는 '식별-안내' 프레임워크를 제안합니다. 이 프레임워크는 판별적인 self- 및 cross-attention 헤드를 선택하여 계산 가능한 잠재 레이아웃을 도출하고, 이를 보수적으로 개선한 다음 cross-attention을 변조하여 재생성을 안내합니다. CountBench에서 NUMINA는 기존 모델의 카운팅 정확도를 최대 7.4% 향상시키며, CLIP 정렬도 개선하고 시간적 일관성을 유지합니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 6. [MegaStyle: Constructing Diverse and Scalable Style Dataset via Consistent Text-to-Image Style Mapping](https://huggingface.co/papers/2604.08364)

MegaStyle은 대규모 생성 모델의 일관된 텍스트-이미지 스타일 매핑 능력을 활용하여 다양하고 확장 가능한 스타일 데이터셋을 구축하고, 이를 통해 효과적인 스타일 표현 추출을 위한 style-supervised contrastive learning을 제안합니다. (영문 용어: Text-to-Image). 기존 스타일 데이터셋의 일관성 부족과 다양성 한계를 해결하기 위해, MegaStyle은 대규모 생성 모델이 특정 스타일 설명에 따라 일관된 이미지를 생성할 수 있다는 점에 착안했습니다. 이 파이프라인은 170K 스타일 프롬프트와 400K 콘텐츠 프롬프트를 조합하여 대규모 스타일 데이터셋인 MegaStyle-1.4M을 구축합니다. 이 데이터셋을 기반으로 style-supervised contrastive learning을 통해 스타일 인코더 MegaStyle-Encoder를 학습시켜 표현력이 풍부한 스타일별 표현을 추출하고, FLUX 기반의 스타일 전이 모델 MegaStyle-FLUX를 훈련합니다. 결과적으로 MegaStyle-1.4M은 스타일 데이터셋의 일관성, 다양성 및 고품질의 중요성을 입증하며, MegaStyle-Encoder와 MegaStyle-FLUX는 신뢰할 수 있는 스타일 유사도 측정 및 일반화 가능한 스타일 전이를 제공합니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 7. [LPM 1.0: Video-based Character Performance Model](https://huggingface.co/papers/2604.07823)

LPM 1.0은 실시간 대화형 캐릭터 퍼포먼스 생성을 위해 정체성 일관성을 유지하며 상호작용적이고 무한 길이의 비디오 합성을 가능하게 하는 대규모 멀티모달 모델입니다. (영문 용어: Video-based). 기존 비디오 모델들은 높은 표현력, 실시간 추론, 장기적인 정체성 안정성을 동시에 달성하기 어려웠습니다. LPM 1.0은 이러한 '퍼포먼스 트릴레마'를 해결하기 위해 단일 인물 전이중 오디오-비주얼 대화 퍼포먼스에 중점을 둡니다. 엄격한 필터링과 멀티모달 데이터셋 구축을 통해 17B 파라미터 Diffusion Transformer (Base LPM)를 훈련하여 높은 제어력과 정체성 일관성을 가진 퍼포먼스를 생성합니다. 이를 인과적 스트리밍 생성기 (Online LPM)로 증류하여 낮은 지연 시간과 무한 길이의 상호작용을 가능하게 합니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 8. [OpenVLThinkerV2: A Generalist Multimodal Reasoning Model for Multi-domain Visual Tasks](https://huggingface.co/papers/2604.08539)

OpenVLThinkerV2는 Gaussian GRPO를 활용하여 다양한 시각 작업에서 안정적인 학습과 지각-추론 균형을 달성하는 범용 멀티모달 추론 모델입니다. (영문 용어: Multi-domain). 멀티모달 모델 학습의 주요 과제인 다양한 시각 작업 보상 토폴로지의 극심한 분산과 지각-추론 균형 문제를 해결하기 위해 Gaussian GRPO(G^2RPO)를 제안합니다. G^2RPO는 선형 스케일링 대신 비선형 분포 매칭을 사용하여 이점 분포를 표준 정규 분포로 수렴시켜 태스크 간 기울기 균등성을 보장하고 학습 안정성을 높입니다. 또한, 응답 길이 조절(response length shaping)과 엔트로피 조절(entropy shaping)을 통해 지각과 추론 능력의 균형을 맞추어 OpenVLThinkerV2의 성능을 향상시킵니다. 이 모델은 이러한 방법론을 통합하여 다양한 시각 작업에서 뛰어난 성능을 보입니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 9. [DMax: Aggressive Parallel Decoding for dLLMs](https://huggingface.co/papers/2604.08302)

DMax는 Diffusion Language Model(dLLM)의 병렬 디코딩 중 오류 축적을 줄이고 생성 품질을 유지하면서 효율성을 높이는 새로운 패러다임을 제시합니다. 기존의 마스크 기반 dLLM은 이진 마스크-토큰 전환을 통해 디코딩했지만, DMax는 마스크 임베딩에서 토큰 임베딩으로의 점진적인 자기 개선으로 디코딩을 재구성합니다. 이 접근 방식의 핵심은 마스크된 입력과 모델의 잘못된 예측 모두에서 깨끗한 토큰을 복구할 수 있도록 모델을 훈련하는 On-Policy Uniform Training이라는 새로운 훈련 전략입니다. 또한, Soft Parallel Decoding을 제안하여 각 중간 디코딩 상태를 예측된 토큰 임베딩과 마스크 임베딩 간의 보간으로 표현함으로써 임베딩 공간에서 반복적인 자기 수정이 가능하게 합니다. 결과적으로 DMax는 GSM8K 및 MBPP 벤치마크에서 정확도를 유지하면서 TPF(Tokens Per Forward)를 크게 향상시키는 효과를 보여주었습니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.

### 10. [KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation](https://huggingface.co/papers/2604.08455)

KnowU-Bench는 사용자 선호도 추론 및 능동적 지원 능력을 평가하는 개인화된 모바일 에이전트 벤치마크를 제시합니다. 기존 벤치마크는 사용자 선호도를 정적인 기록이나 고정된 컨텍스트에서 평가하여, 에이전트가 상호작용을 통해 누락된 선호도를 이끌어내거나 실시간 GUI 환경에서 언제 개입할지 결정하는 능력을 측정하지 못했습니다. KnowU-Bench는 재현 가능한 Android 에뮬레이션 환경에서 구축된 온라인 벤치마크로, 에이전트에게 사용자 프로필을 숨기고 행동 로그만 노출하여 진정한 선호도 추론을 강제합니다. 또한, LLM 기반 사용자 시뮬레이터를 통해 다중 턴 선호도 도출 및 능동적 동의 처리를 지원하며, GUI 실행, 동의 협상, 거부 후 제약 등 능동적 의사결정 체인 전반을 평가합니다. 이 벤치마크는 개인화된 모바일 에이전트의 실제 성능 저하를 드러냅니다. 이 항목은 Hugging Face Papers (Top today) (2026-04-10 기준)에서 확인했습니다.
