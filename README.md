# 💚 그린라이트 감지기 (Love Signal Detector)

> **"그 사람의 카톡, 헷갈린다면 AI 연애 코치에게 물어보세요!"** >
> 
> 썸 타는 상대방과의 대화를 분석하여 호감도를 판별하고, 센스 있는 답장을 추천해 주는 AI 서비스입니다.

<br>

## 🛠 사용 기술 (Tech Stack)

| 구분 | 기술 스택 |
| :--- | :--- |
| **Language** | Python 3.9+ |
| **AI Model** | OpenAI GPT-4o |
| **Framework** | Streamlit (Web UI) |
| **Library** | LangChain, OpenAI API |

<br>

## ✨ 주요 기능 (Features)

1.  **호감도 분석 (Greenlight Score):** 대화 내용을 바탕으로 0~100% 사이의 호감 확률을 계산합니다.
2.  **심리 분석:** 상대방의 말투, 답장 속도, 질문 빈도를 분석해 MBTI 관점의 심리를 추측합니다.
3.  **답장 추천:** 호감도를 높일 수 있는 '필살기 답장' 3가지를 제안합니다.

<br>

## 📂 폴더 구조 (Project Structure)

```bash
love-signal-detector/
├── 📄 app.py                     # Streamlit 웹 애플리케이션 메인 코드
├── 📄 love_signal_analysis.ipynb # 프롬프트 엔지니어링 실험 및 기획 과정 (Notebook)
├── 📄 requirements.txt           # 프로젝트 실행에 필요한 라이브러리 목록
└── 📄 README.md                  # 프로젝트 설명서
```
<br>

## 🚀 실행 방법 (Getting Started)

이 프로젝트를 내 컴퓨터에서 실행하려면 아래 단계를 따라주세요.

1. 프로젝트 복제 (Clone)
```bash
git clone [https://github.com/본인아이디/love-signal-detector.git](https://github.com/본인아이디/love-signal-detector.git)
cd love-signal-detector
```

2. 라이브러리 설치
```bash
pip install -r requirements.txt
```

3. 환경 변수 설정 (중요!)

프로젝트 폴더 최상단에 .env 파일을 생성하고, 본인의 OpenAI API Key를 입력하세요. (주의: .env 파일은 깃허브에 올라가지 않도록 주의하세요.)

```plaintext
# .env 파일 내용 예시
OPENAI_API_KEY=sk-your-api-key-here
```

4. 앱 실행
```bash
streamlit run app.py
```

실행 후 브라우저가 자동으로 열립니다. (주소: http://localhost:8501)

## 📊 프롬프트 전략 (Prompt Engineering)

이 프로젝트는 최적의 답변을 얻기 위해 Iterative Prompting(반복적 개선) 방식을 사용했습니다.

상세 과정은 love_signal_analysis.ipynb에서 확인할 수 있습니다.

**Role (페르소나)**: "20대 연애 상담 1위 유튜버이자 MBTI 과몰입러

**Context**: 썸남/썸녀와의 미묘한 기류를 파악해야 하는 상황

**Constraints**:

뻔한 위로보다는 냉철한 팩트 폭격

구어체 사용 ("~인 듯", "솔직히 말해서")

명확한 섹션 구분 (점수, 이유, 추천 답장)
