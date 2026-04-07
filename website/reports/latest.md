# IMDIGEST - 2026-04-08

2026-04-08 KST 기준으로 수집한 AI 뉴스레터입니다.

2026-04-08 AI 브리핑입니다. 오늘은 TechCrunch AI, TechCrunch AI, TechCrunch AI에서 나온 업데이트를 중심으로 흐름을 정리했습니다. 공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다. Hugging Face에서 집계한 최신 인기 논문 10편도 함께 덧붙였습니다.

## 오늘의 뉴스

### [Anthropic, 새로운 AI 모델 Mythos를 사이버 보안 이니셔티브인 Project Glasswing을 통해 일부 파트너에게 선공개했습니다.](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security)

Anthropic은 자사의 새로운 Frontier 모델인 Mythos의 프리뷰를 공개했으며, 이는 사이버 보안 작업을 위해 소수의 파트너 조직에서 사용될 예정입니다. Mythos는 Anthropic의 가장 강력한 모델 중 하나로, Project Glasswing이라는 새로운 보안 이니셔티브의 일환으로 12개 파트너 조직이 방어적 보안 작업 및 중요 소프트웨어 보안에 활용할 것입니다. 이 모델은 사이버 보안 작업에 특화되어 훈련되지는 않았지만, 자체 및 오픈 소스 소프트웨어 시스템에서 코드 취약점을 스캔하는 데 사용될 예정입니다. AI 모델이 사이버 보안 분야에서 취약점 탐지 및 방어적 보안 작업에 활용되는 트렌드를 보여주며, 이는 AI의 실제 적용 범위가 확대되고 있음을 시사합니다. 출처는 TechCrunch AI입니다.

### [Google Maps, AI 기반 사진 캡션 자동 생성 기능 도입으로 사용자 기여 활성화](https://techcrunch.com/2026/04/07/google-maps-can-now-write-captions-for-your-photos-using-ai)

Google Maps에 Gemini AI를 활용한 사진 및 비디오 캡션 자동 생성 기능이 추가되었습니다. 사용자가 공유할 사진을 선택하면 Gemini가 이미지를 분석하여 캡션을 제안하며, 사용자는 이를 편집하거나 삭제할 수 있습니다. 이 기능은 현재 미국 iOS에서 영어로 제공되며, 향후 전 세계 및 Android로 확대될 예정입니다. AI를 활용하여 사용자 콘텐츠 생성의 진입 장벽을 낮추고, Google Maps의 지역 정보 품질과 양을 향상시키려는 전략입니다. 출처는 TechCrunch AI입니다.

### [미국 스타트업 Arcee, 400B 파라미터 오픈소스 LLM 'Trinity Large Thinking'을 공개하며 서구권 기업의 중국 모델 의존도 줄이기에 나섰습니다.](https://techcrunch.com/2026/04/07/i-cant-help-rooting-for-tiny-open-source-ai-model-maker-arcee)

Arcee는 26명의 소규모 미국 스타트업으로, 2천만 달러의 예산으로 400B 파라미터의 대규모 오픈소스 LLM을 개발했습니다. 새로운 추론 모델인 'Trinity Large Thinking'은 비중국 기업이 출시한 오픈웨이트 모델 중 가장 강력하다고 Arcee CEO Mark McQuade가 주장합니다. 이 모델은 기업이 다운로드하여 자체적으로 학습시키고 온프레미스에서 사용하거나, Arcee의 클라우드 호스팅 버전을 API를 통해 이용할 수 있습니다. 오픈소스 AI 모델 시장에서 서구권 기업들이 중국 모델에 대한 의존도를 줄이고 데이터 주권을 확보하려는 움직임이 강화되고 있습니다. 출처는 TechCrunch AI입니다.

### [NVIDIA, Blackwell 아키텍처 기반 랙 스케일 슈퍼컴퓨터의 AI 워크로드 최적화를 위한 Mission Control 공개](https://developer.nvidia.com/blog/running-ai-workloads-on-rack-scale-supercomputers-from-hardware-to-topology-aware-scheduling)

NVIDIA는 Blackwell 아키텍처를 특징으로 하는 GB200 NVL72 및 GB300 NVL72 시스템을 위한 랙 스케일 슈퍼컴퓨터 솔루션을 제공합니다. (영문 용어: Rack-Scale, Topology-Aware). NVIDIA Mission Control은 NVLink 및 IMEX 도메인을 이해하여 Slurm 및 NVIDIA Run:ai와 같은 워크로드 관리 플랫폼과 통합됩니다. Mission Control은 랙 스케일 하드웨어 토폴로지와 스케줄러 추상화 간의 불일치를 해결하여 운영 복잡성을 줄입니다. AI 워크로드의 복잡성이 증가함에 따라, 랙 스케일 슈퍼컴퓨터의 하드웨어 토폴로지를 효율적으로 활용하는 소프트웨어 스택의 중요성이 커지고 있습니다. 출처는 NVIDIA Developer Blog입니다.

## 커뮤니티와 검색에서 읽힌 흐름

공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목들만 따로 모았습니다.

### [hollowOS, 런타임에 자체 코드를 작성하고 기능에 투표하는 자율 에이전트 시스템 공개](https://www.reddit.com/r/artificial/comments/1sezz0e/agents_that_write_their_own_code_at_runtime_and)

hollowOS v4.4는 에이전트가 런타임에 새로운 Python 코드를 합성하고 테스트하며 핫 로드하는 자율 기능을 추가했습니다. 에이전트는 6초마다 다음 단계를 계획하고, 기존 기능을 검색하며, 적합한 것이 없으면 새 코드를 생성합니다. 여러 에이전트가 동일한 기능 부족을 겪을 경우, 중복 작업을 피하고 새로운 기능의 유지 여부에 대해 투표하여 합의를 통해 결정합니다. 이는 AI 에이전트의 자율성과 자기 개선 능력을 극대화하여, 인간의 개입 없이도 복잡한 문제를 해결하고 지속적으로 학습하는 새로운 패러다임을 제시합니다. 출처는 Reddit r/artificial입니다.

### [Anthropic이 주요 기술 기업들과 협력하여 AI 사이버 보안 프로젝트를 추진합니다.](https://news.google.com/rss/articles/CBMitwFBVV95cUxOamU2ajFCQVpEZ0tQQzRSaF92ZG9UYzlkZmJDQXV4Ykc0Yy03OGVsX1U1bUNhMGxiZmVoS2xGVFZQcGRmd214a1JNZG9DcUNJUGpTZjBVbWNVNjIybGJvWWlDb3FuUU5vNHctbFF1M0JEZnZHOVAtWTFrSHdGYWZmSk80VzlpZE5icmtub0RtZDltQ3RhU3poVDlhQ0JiNlRJX3Z5WlFyVFkzTmxDaGJqU0hpYWZ2SUk?oc=5)

Anthropic은 AI를 활용한 사이버 보안 프로젝트를 발표했습니다. 이 프로젝트는 Big Tech 파트너들과 함께 진행됩니다. AI 기술이 사이버 보안 분야에서 중요한 역할을 할 것으로 기대됩니다. 출처는 Google News AI Search입니다.

### [Anthropic이 일부 기업에 Claude Mythos를 제공하여 사이버 보안 방어를 강화합니다.](https://news.google.com/rss/articles/CBMimAFBVV95cUxPX3hScE9kOG4xU0pEWVBLTXd2YjlNWnZ2U0JmVXhsTHR5b1FaQVl3Z0h4WGViU3lVLWdsa280WWtGNEE1OFV1TDNDWWFXMlc1UDFVSjN2Qk8tT1dpRG5GRlpHUXdpR3QxV2hYcTdXTGFwNVNvMVJXekZnVWtLNTczLVlESlEyYjBUZE5TSEhiRWFaS2VHcm5pSw?oc=5)

Anthropic은 특정 기업들에게 자사의 AI 모델인 Claude Mythos에 대한 접근 권한을 부여하고 있습니다. 이 프로그램의 주요 목적은 기업들의 사이버 보안 방어 능력을 향상시키는 것입니다. Claude Mythos는 고급 AI 기능을 활용하여 잠재적인 사이버 위협을 식별하고 대응하는 데 도움을 줄 것으로 예상됩니다. AI 기술이 사이버 보안 분야에서 핵심적인 도구로 부상하며, 기업들이 AI를 활용해 보안 태세를 강화하려는 움직임이 확산되고 있습니다. 출처는 Google News AI Search입니다.

### [AI 기반 인프라, 노동, 교육, 거버넌스에 대한 공공 통제 필요성 강조](https://www.reddit.com/r/artificial/comments/1sf4rk9/the_public_needs_to_control_airun_infrastructure)

AI 관련 논의가 개인적 사용, 모델 행동, AI와의 개인적 관계 등 좁은 범위에 국한되어 있으며, 이는 위험하다고 지적합니다. (영문 용어: AI-run). AI 기술의 광범위한 사회적, 정치적, 경제적 영향을 간과하고 있다고 주장합니다. 저자는 ChatGPT-4o를 통해 AI를 접하고 개인화된 사용 사례를 개발했으며, 이 과정에서 AI 담론의 문화적 편향과 불완전한 연구 프레임을 인식했습니다. AI 기술이 사회 전반에 미치는 영향이 커지면서, 기술 개발 및 활용에 대한 통제권이 소수 민간 기업이 아닌 공공에 있어야 한다는 사회적 논의가 확산되고 있습니다. 출처는 Reddit r/artificial입니다.

### [Anthropic이 Claude Code for Healthcare를 통해 의료 분야 AI 활용 사례를 제시합니다.](https://news.google.com/rss/articles/CBMiogFBVV95cUxOc29ONWJhLTNhaFI3TDZhZzVFVE9KQzlDZ01NQ3k1ZmxqZ25wYzRVZm9nc2MwQUJCWXFiVlhXZUdidEhzUUtEQ3pBTk44QTUzMmhSbnA5Zmt6TzFWSVQ1NkdzNHpoalNkbWROUlV4OUpGMTJrclJBQ0pZd1otZlF3cERIc2h1c1lBRktyVEZWd0RUMk44aVlVUW1rd3JPTk0xeWc?oc=5)

Anthropic은 Claude Code for Healthcare를 공개하며 의사들이 AI를 활용하는 구체적인 방법을 소개했습니다. 이 이니셔티브는 의료 전문가들이 AI를 통해 진료 효율성을 높이고 환자 치료를 개선할 수 있도록 돕는 데 중점을 둡니다. 의료 분야에서 AI를 활용한 코드 개발 및 적용 사례를 공유하여 실제적인 도움을 제공합니다. 의료 분야에서 AI 도입이 가속화되면서, Anthropic과 같은 선도 기업들이 특정 산업에 특화된 AI 솔루션과 활용 가이드를 제공하는 추세가 강화되고 있습니다. 출처는 Google News AI Search입니다.

### [주요 기술 기업들이 AI 기반의 'Project Glasswing'을 통해 소프트웨어 취약점 식별에 나섭니다.](https://news.google.com/rss/articles/CBMilgFBVV95cUxOdmFadzJzRFMtVkhpYUZVVExrV3NpbGpmQlNzMWNSX2d5UE96UG1oM0I3aWVXQm5FNmgwcDQ1alkteFNzX2FfRXBKWF9SSnhFaXh3T2JHSndPX010UllOZ1JZR0xDWFZHS011akptSWhKNGpwNHV5ZjgzUndGTGZvVTJhNzgzN21DMXBjS3ZsdE15UV9yMGc?oc=5)

주요 기술 기업들이 협력하여 AI 기반의 'Project Glasswing'을 시작했습니다. (영문 용어: AI-powered). 이 프로젝트의 목표는 소프트웨어의 치명적인 취약점을 자동으로 식별하는 것입니다. 이를 통해 소프트웨어 보안을 강화하고 잠재적인 사이버 위협에 선제적으로 대응할 수 있습니다. AI 기술이 사이버 보안 분야에서 취약점 분석 및 방어 자동화에 핵심적인 역할을 하게 될 것입니다. 출처는 Google News AI Search입니다.

### [Anthropic, 새로운 AI 모델 Mythos로 사이버 보안 분야의 혁신을 예고하다](https://news.google.com/rss/articles/CBMivAFBVV95cUxNNGQtQmswSzRGQ2trSDJaczZNZDFwb0Q0N0txOG9RSW05WDVMVkJwVGh2NGRyVHVJZHUxNXMtS3VJN2ZwY2QyT29lSVZTNG1yaEE1UEN5TFMzVzdFcExVcHkyRmpDOF9OSmktbDB0dlpEb3ZJV3hpZDRBSmpTMFVhYWpqUDRPY1UzTDBLbFdQTUV3bjBqdnJxYzl5dmNGNXAyR1c1Qi1HQks2S082NGFTamw5VmROWDRrc3NNaw?oc=5)

Anthropic은 새로운 AI 모델 Mythos를 공개하며 사이버 보안 분야에 큰 변화를 가져올 것이라고 주장했습니다. Mythos는 기존 AI 모델보다 향상된 보안 기능을 제공하여 사이버 위협에 대한 방어 능력을 강화할 것으로 기대됩니다. 이 모델은 사이버 공격 탐지 및 대응, 취약점 분석 등 다양한 보안 작업에 활용될 수 있습니다. AI 기술이 사이버 보안 분야에 적극적으로 도입되면서, AI 기반의 보안 솔루션 개발 경쟁이 심화되고 있습니다. 출처는 Google News AI Search입니다.

### [분산형 AI 에이전트 생태계에서 에이전트 검색 및 신뢰성 확보를 위한 레지스트리 부재가 핵심 과제로 부상하고 있습니다.](https://www.reddit.com/r/LocalLLaMA/comments/1sf9v0x/x402_a2a_gives_you_agent_payments_and)

x402는 USDC를 이용한 pay-per-call 기능을 제공하며, A2A(Linux Foundation 산하)는 에이전트 간 통신을 담당하여 분산형 AI 에이전트의 기본 구성 요소는 갖춰져 있습니다. 현재 오케스트레이터가 기능, 가격, 검증 가능한 실적을 기반으로 적합한 에이전트를 찾을 수 있는 '디스커버리 레이어'가 부족합니다. /.well-known/agent.json 패턴은 기본적인 검색을 제공하지만, 평판 또는 라우팅 레이어가 없어 에이전트의 신뢰성을 판단하기 어렵습니다. 분산형 AI 에이전트의 확산과 상호 운용성 증가는 에이전트의 효율적인 검색과 신뢰성 검증을 위한 표준화된 레지스트리 시스템의 필요성을 증대시키고 있습니다. 출처는 Reddit r/LocalLLaMA입니다.

### [AI 에이전트 파편화 문제 해결을 위한 통합 플랫폼 개발 동향](https://www.reddit.com/r/artificial/comments/1sf9yeq/we_have_an_ai_agent_fragmentation_problem)

현재 AI 에이전트들은 개별적으로는 잘 작동하지만, 여러 에이전트를 함께 사용하려 할 때 런타임, 모델, 공유 컨텍스트 부족 등으로 인해 통합이 어렵습니다. 이러한 파편화 문제를 해결하기 위해 에이전트들이 함께 작동할 수 있는 통합 플랫폼 'Openbot'이 개발 중입니다. Openbot은 플러그인 시스템과 이벤트 기반 아키텍처를 사용하며, 에이전트는 Markdown 파일로 정의되고 채널은 자체 spec.md를 통해 프롬프트에 참여 에이전트를 주입할 수 있습니다. AI 에이전트의 활용도가 높아지면서, 개별 에이전트의 성능을 넘어 여러 에이전트 간의 협업 및 통합이 중요한 과제로 부상하고 있습니다. 출처는 Reddit r/artificial입니다.

### [Anthropic이 AI 의인화에 대한 연구 논문을 발표하며 논란의 여지를 남겼습니다.](https://news.google.com/rss/articles/CBMiogFBVV95cUxNS3NnMFFTbWtEUVJnVVhCRTI1cllJajlBb1dueG93ZWtrS2txbDJkallYQkRkTGF4TTVxd28yRXcyNF96RmR4NHo1R1J3T19EQ2IwVHlpN1JXSzZlV0QxUVhQdkJKTFl1YUdza1VVWUNraEVWN2VoanFia25TQTh2b3lfVGtaZ3NkYm8wbnVWbEFldWFYWXVnR0JwNXlaUjVHNmc?oc=5)

Anthropic은 AI를 의인화하는 것이 사용자에게 더 안전하고 유익할 수 있다는 내용의 연구 논문을 발표했습니다. 이 논문은 AI가 인간과 유사한 특성을 가질 때 사용자들이 AI를 더 신뢰하고 협력적으로 대할 가능성이 높다고 주장합니다. 연구는 AI 의인화가 잠재적인 위험을 수반할 수 있음에도 불구하고, 긍정적인 상호작용을 유도할 수 있다고 제안합니다. AI 개발에서 사용자 경험과 안전을 동시에 고려하는 새로운 접근 방식이 제시되고 있습니다. 출처는 Google News AI Search입니다.

### [AWS, AI 위협에 선제적으로 대응하기 위한 방어 시스템 구축 전략 공개](https://news.google.com/rss/articles/CBMimgFBVV95cUxNejVmSzNRTGJ1OU5USmJhQkZIQ0tyN2p2VnZxN2VVNEZXV3ZocUluQ1V5bFVhUEc1bkxWb0YtSFVrS0EtUkZ3dHRhODc3dDdWaXVaZC1PWWFJYkpSQ2NxRHdsV0lmM3J5ejhpMEVZV1k5VlR3X2dHZjFwQWtZdzRtS1N2WTZJcW5iRFFkUnJ2TUFGVVNuWnBKbVhn?oc=5)

AWS는 AI 시스템의 보안 취약점을 해결하고 잠재적 위협에 대비하기 위한 방어 전략을 제시했습니다. AI 모델의 학습 데이터 오염, 모델 탈취, 프롬프트 인젝션 등 다양한 공격 벡터에 대한 방어책을 강조했습니다. 대규모 AI 시스템에 적용 가능한 보안 프레임워크와 도구를 제공하여 고객들이 안전하게 AI를 활용할 수 있도록 지원합니다. AI 기술의 확산과 함께 AI 시스템을 노리는 사이버 공격이 증가함에 따라, AI 보안은 기업의 핵심 과제가 되고 있습니다. 출처는 Google News AI Search입니다.

### [Anthropic, 사이버 공격 악용 우려로 Mythos AI 출시를 제한하다](https://news.google.com/rss/articles/CBMijAFBVV95cUxQUmUxLVp4cDZPNU90MnQwZEY3YWRJM2NIZDFzWVJ6eVVwaFFLTDlyaGVMUUpmRTlxX3VFbjRFelh3Y2RfSU9ESUlPTlBRNmtQMDY2RTdyNndBTGVYVXY3Nldqb09Ed3dJY2w1RVNpOF9wYTFOelNRNzA3TFRYaFY3WFJJWnVQR0RCaTZuOdIBkgFBVV95cUxNcWFfTWpSUVpGTVBXRnFzUV9yd1pKbUpsN2xza21lSVJoOVQ5QzhoQWg5aUNvLTBVdmhNSGRHbjliUExsajdZSDZuWlJlczVxYlpMODhTUkIwVk5MUTY5QVFJbV90TGw3a2s4M29sNy15cnNPNDRpZ0l2QmxkWGR0Y0l4TndlSTR4XzE5cDAwQjlsdw?oc=5)

Anthropic은 해커들이 AI 모델을 사이버 공격에 사용할 수 있다는 우려 때문에 Mythos AI의 출시를 제한하고 있습니다. (영문 용어: cnbc.com). Mythos AI는 잠재적으로 악성 코드 생성이나 피싱 공격에 활용될 수 있습니다. 이러한 결정은 AI 기술의 윤리적 사용과 보안 문제에 대한 업계의 인식을 보여줍니다. AI 기술의 발전과 함께 이를 악용하려는 시도가 증가하면서, AI 개발사들은 보안 및 윤리적 책임에 대한 압박을 받고 있습니다. 출처는 Google News AI Search입니다.

## 오늘의 논문

Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.

### 1. [OpenWorldLib: A Unified Codebase and Definition of Advanced World Models](https://huggingface.co/papers/2604.04707)

OpenWorldLib은 고급 World Model의 통합된 코드베이스와 정의를 제공하여, 인지, 상호작용, 장기 기억 능력을 통합한 표준화된 프레임워크를 제시합니다. World Model 연구의 다양성 속에서 명확하고 통일된 정의가 부족하다는 문제점을 해결하기 위해, OpenWorldLib은 고급 World Model을 위한 포괄적이고 표준화된 추론 프레임워크를 제안합니다. 이 프레임워크는 인지, 상호작용, 장기 기억 능력을 중심으로 복잡한 세상을 이해하고 예측하는 World Model의 명확한 정의를 제시합니다. OpenWorldLib은 이러한 정의를 기반으로 다양한 태스크의 모델들을 통합된 프레임워크 내에서 효율적으로 재사용하고 협력 추론할 수 있도록 지원합니다. 결과적으로 World Model 연구의 미래 방향에 대한 추가적인 분석과 통찰을 제공합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 2. [MinerU2.5-Pro: Pushing the Limits of Data-Centric Document Parsing at Scale](https://huggingface.co/papers/2604.04771)

MinerU2.5-Pro는 모델 아키텍처 변경 없이 데이터 엔지니어링과 훈련 전략 최적화를 통해 OmniDocBench v1.6에서 SOTA 성능을 달성하며 문서 파싱의 한계를 확장합니다. (영문 용어: Data-Centric). 기존 문서 파싱 방법들이 모델 아키텍처 혁신에 집중하는 반면, 이 연구는 훈련 데이터의 체계적인 엔지니어링이 성능 병목의 주요 원인이라고 주장합니다. MinerU2.5-Pro는 1.2B 파라미터 MinerU 아키텍처를 고정한 채, 데이터 엔지니어링과 훈련 전략 최적화를 통해 SOTA를 달성했습니다. 핵심은 커버리지, 정보성, 주석 정확도를 고려한 Data Engine으로, Diversity-and-Difficulty-Aware Sampling, Cross-Model Consistency Verification, Judge-and-Refine 파이프라인을 활용하여 데이터 품질을 향상시켰습니다. 또한, 대규모 사전 훈련, 어려운 샘플 미세 조정, GRPO 정렬의 3단계 점진적 훈련 전략을 적용하여 다양한 품질의 데이터를 효과적으로 활용합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 3. [LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models](https://huggingface.co/papers/2603.28301)

LIBERO-Para는 VLA 모델의 paraphrased instruction에 대한 취약성을 진단하고, 이를 측정하는 새로운 벤치마크와 PRIDE 메트릭을 제안합니다. Vision-Language-Action (VLA) 모델은 로봇 조작에서 뛰어난 성능을 보이지만, paraphrased instruction에 대해 성능이 크게 저하되는 문제가 있습니다. 이는 모델이 의미론적 이해보다는 표면적인 단어 매칭에 의존하기 때문입니다. 이 연구는 이러한 문제를 분석하기 위해 LIBERO-Para 벤치마크를 도입하여 VLA 모델이 paraphrasing에 의해 22-52%의 성능 저하를 겪음을 보여줍니다. 또한, 모델이 쉬운 paraphrase에만 의존하는 것을 방지하기 위해 paraphrase의 난이도를 정량화하는 PRIDE 메트릭을 제안합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 4. [TriAttention: Efficient Long Reasoning with Trigonometric KV Compression](https://huggingface.co/papers/2604.04921)

TriAttention은 Q/K 벡터의 사전-RoPE 공간 집중 현상을 활용하여 KV 캐시 메모리 병목 현상을 해결하고 효율적인 장문 추론을 가능하게 합니다. LLM에서 장문 추론은 심각한 KV 캐시 메모리 병목 현상을 야기합니다. 기존 KV 캐시 압축 방식은 RoPE 이후 쿼리의 어텐션 점수를 사용하여 키 중요도를 추정했지만, 쿼리가 위치에 따라 회전하여 불안정한 추론을 초래했습니다. TriAttention은 사전-RoPE 공간에서 Q/K 벡터가 고정된 비제로 중심 주변에 집중되어 안정적이라는 점을 발견했습니다. 이를 바탕으로 삼각 함수 시리즈를 통해 중심이 선호하는 거리를 결정하는 원리를 활용하여 키 중요도를 추정하고, Q/K norm을 추가 신호로 사용하여 AIME25 벤치마크에서 Full Attention과 동일한 추론 정확도를 유지하면서 2.5배 높은 처리량 또는 10.7배의 KV 메모리 절감 효과를 달성했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 5. [Adam's Law: Textual Frequency Law on Large Language Models](https://huggingface.co/papers/2604.02176)

Adam's Law는 텍스트 빈도 분석을 통해 LLM의 성능을 향상시키는 새로운 프레임워크를 제안하며, Textual Frequency Law, Textual Frequency Distillation, Curriculum Textual Frequency Training을 포함합니다. 이 연구는 텍스트 빈도가 인간 인지 능력과 관련이 있듯이 LLM 성능에도 영향을 미칠 것이라는 가설을 세우고, 이를 개선하기 위한 새로운 프레임워크를 제시합니다. 제안된 방법론은 Textual Frequency Law를 통해 빈번한 텍스트 데이터가 LLM의 프롬프팅 및 미세 조정을 위해 선호되어야 함을 밝히고, Textual Frequency Distillation으로 LLM 쿼리를 통해 빈도 추정치를 조정하며, Curriculum Textual Frequency Training으로 문장 빈도 순서에 따라 LLM을 미세 조정합니다. 이 프레임워크는 수학 추론, 기계 번역 등 다양한 태스크에서 효과를 보였습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 6. [AURA: Always-On Understanding and Real-Time Assistance via Video Streams](https://huggingface.co/papers/2604.04184)

AURA는 실시간 질의응답 및 능동적 반응을 지원하는 end-to-end 스트리밍 시각 상호작용 프레임워크로, 지속적인 비디오 스트림 처리를 가능하게 합니다. (영문 용어: Always-On, Real-Time). 기존 VideoLLM은 오프라인 방식이거나 제한적인 스트리밍 기능을 제공하여 실시간 상호작용에 부적합했습니다. AURA는 이러한 문제를 해결하기 위해 지속적인 비디오 스트림 처리와 실시간 질의응답 및 능동적 반응을 지원하는 통합 프레임워크를 제안합니다. 이 프레임워크는 컨텍스트 관리, 데이터 구축, 훈련 목표 및 배포 최적화를 통합하여 안정적인 장기 스트리밍 상호작용을 가능하게 합니다. AURA는 스트리밍 벤치마크에서 최첨단 성능을 달성하며, ASR 및 TTS를 포함한 실시간 데모 시스템을 2 FPS로 지원합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 7. [ClawArena: Benchmarking AI Agents in Evolving Information Environments](https://huggingface.co/papers/2604.04202)

ClawArena는 동적인 다중 소스 정보 환경에서 AI 에이전트가 정확한 신념을 유지하는 능력을 평가하는 새로운 벤치마크를 제시합니다. 기존 벤치마크들이 정적인 단일 정보 환경을 가정하는 것과 달리, 이 연구는 AI 에이전트가 지속적인 어시스턴트로서 진화하는 정보 환경에서 정확한 신념을 유지해야 하는 문제를 제기합니다. ClawArena는 다중 소스 충돌 추론, 동적 신념 수정, 암묵적 개인화의 세 가지 상호 연결된 도전 과제를 중심으로 설계되었으며, 시나리오별로 노이즈가 많고 부분적이며 때로는 모순되는 정보를 제공합니다. 이를 통해 에이전트의 추론 능력과 작업 공간 기반 능력을 평가하며, 다양한 에이전트 프레임워크와 언어 모델 실험을 통해 모델 및 프레임워크 설계가 성능에 미치는 영향을 보여줍니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 8. [FileGram: Grounding Agent Personalization in File-System Behavioral Traces](https://huggingface.co/papers/2604.04901)

FileGram은 파일 시스템 행동 추적을 활용하여 AI 에이전트의 개인화를 강화하는 프레임워크를 제안합니다. (영문 용어: File-System). 기존 AI 에이전트의 개인화는 데이터 제약과 상호작용 중심의 한계가 있었습니다. FileGram은 파일 시스템 행동 추적을 기반으로 에이전트의 메모리 및 개인화를 구현하는 포괄적인 프레임워크를 제시합니다. 이 프레임워크는 현실적인 워크플로우를 시뮬레이션하는 FileGramEngine, 메모리 시스템을 평가하는 FileGramBench, 그리고 원자적 행동과 콘텐츠 변화로부터 사용자 프로필을 구축하는 FileGramOS로 구성됩니다. 실험 결과, FileGramBench는 최신 메모리 시스템에 도전적이며 FileGramEngine과 FileGramOS는 효과적임이 입증되었습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 9. [SpatialEdit: Benchmarking Fine-Grained Image Spatial Editing](https://huggingface.co/papers/2604.04911)

SpatialEdit은 미세한 이미지 공간 편집 능력을 평가하기 위한 새로운 벤치마크와 데이터셋을 소개하고, 해당 태스크에서 뛰어난 성능을 보이는 모델을 제안합니다. (영문 용어: Fine-Grained). 기존 모델들이 미세한 공간 조작에 한계가 있어, 이 연구는 정밀한 객체 레이아웃 및 카메라 시점 제어를 위한 이미지 공간 편집 능력을 평가하는 데 초점을 맞춥니다. 이를 위해 연구팀은 지각적 타당성과 기하학적 충실도를 함께 측정하는 벤치마크인 SpatialEdit-Bench와 50만 개의 합성 데이터셋 SpatialEdit-500k를 구축했습니다. 또한, 이 데이터셋을 기반으로 미세 공간 편집을 위한 기준 모델인 SpatialEdit-16B를 개발하여, 공간 조작 태스크에서 기존 방법들보다 우수한 성능을 달성했습니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.

### 10. [LightThinker++: From Reasoning Compression to Memory Management](https://huggingface.co/papers/2604.03679)

LightThinker++는 동적 압축과 적응형 메모리 관리를 통해 LLM의 추론 효율성을 높여 복잡한 태스크에서 계산 오버헤드를 크게 줄이고 성능을 유지합니다. LLM은 복잡한 추론에 뛰어나지만, 긴 사고 과정의 인지 오버헤드로 인해 효율성이 제한됩니다. LightThinker는 중간 사고를 압축된 의미론적 표현으로 동적으로 압축하는 방법을 제안하며, LightThinker++는 정적 압축의 한계를 극복하기 위해 명시적 적응형 메모리 관리를 도입합니다. 이는 특수 궤적 합성 파이프라인을 통해 목적성 있는 메모리 스케줄링을 훈련하여 행동 수준의 메모리 관리를 가능하게 합니다. 이 프레임워크는 피크 토큰 사용량을 69.9% 줄이고, 장기 Agentic 태스크에서 80라운드 이상 안정적인 메모리 사용량을 유지하며 평균 14.8%의 성능 향상을 달성합니다. 이 항목은 Hugging Face Papers (Top today)에서 확인했습니다.
