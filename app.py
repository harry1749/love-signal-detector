import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# 1. 환경 변수 로드 (.env 파일이 같은 폴더에 있다면 읽어옵니다)
load_dotenv()

# Streamlit 페이지 설정
st.set_page_config(page_title="그린라이트 감지기", page_icon="💚")

st.title("💚 그린라이트 감지기")
st.subheader("그 사람의 카톡, 헷갈린다면 AI 연애 코치에게 물어보세요!")

# 2. API 키 처리 로직
# .env에서 가져오거나, 없으면 사이드바에서 입력받음
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    api_key = st.sidebar.text_input("OpenAI API Key를 입력하세요", type="password")
else:
    # .env에서 키를 찾았을 경우 사이드바에 안내 문구 표시 (선택 사항)
    st.sidebar.success("API Key가 로드되었습니다.")

# 사용자 입력
chat_log = st.text_area("상대방과 주고받은 카톡 대화 내용을 복사해서 붙여넣으세요.", height=200)

if st.button("분석 시작하기"):
    if not api_key:
        st.error("API Key가 없습니다. .env 파일을 확인하거나 사이드바에 키를 입력해주세요!")
    elif not chat_log:
        st.warning("대화 내용을 입력해주세요!")
    else:
        with st.spinner("대화를 분석 중입니다... 🕵️"):
            try:
                client = OpenAI(api_key=api_key)
                
                # 최종 프롬프트 (V2 - 하령쌤 페르소나 적용)
                system_prompt = """
                너는 20대 연애 상담 분야 1위 유튜버이자, MBTI 과몰입러야.
                사용자의 카톡 대화를 보고, 친구처럼 솔직하고 시원하게 조언해줘야 해.

                [필수 분석 항목]
                1. 🚦 **그린라이트 지수**: 0~100% (이유를 팩트 폭격으로 설명)
                2. 🧠 **상대방 예상 심리**: (MBTI 관점에서 추측, 예: T라서 그런지, F라서 그런지 등)
                3. 🚀 **추천 답장**: 상대방의 호기심을 유발할 수 있는 센스 있는 답장 2개 추천.

                [제약 조건]
                - 말투는 "야," "솔직히 말해서," "~인 듯" 같은 구어체를 사용해.
                - 상대방이 어장관리 중이라면 따끔하게 정신 차리라고 말해줘.
                """
                
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": chat_log}
                    ],
                    temperature=0.8
                )
                
                result = response.choices[0].message.content
                st.success("분석 완료!")
                st.markdown(result)
                
            except Exception as e:
                st.error(f"에러가 발생했습니다: {e}")