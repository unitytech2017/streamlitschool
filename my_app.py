import streamlit as st

# 제목 설정
st.title("오류중학교 3학년 2반 홈페이지")

# 학급 소개
st.header("😃학급 소개")
st.write("안녕하세요! 오류중학교 3학년 2반 홈페이지 입니다. 이 홈페이지를 통해 학급 정보와 공지사항을 확인할 수 있습니다.")

# 이미지 URL 사용
image_url = "https://cdn.pixabay.com/photo/2017/08/06/22/01/books-2596809_1280.jpg"  # 이미지 URL을 여기에 입력하세요.
st.image(image_url, caption="이미지 캡션", use_column_width=True)

# 배경 색상 설정
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("school_background.jpg");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 헤더 색상 설정
st.markdown(
    """
    <style>
    .css-1v3fvcr {
        color: #007ACC;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# 학급 일정
st.header("😃학급 일정")
st.write("이번 달의 학급 일정은 다음과 같습니다:")
st.write("- 기말고사: 9월 20일")
st.write("- 체육 대회: 9월 25일")

# # 학급 사진
# st.header("학급 사진")
# st.image("classroom.jpg", caption="우리 학급 사진", use_column_width=True)

# 공지사항
st.header("😃학급 공지사항")
st.write("중요한 공지사항이나 소식은 여기에 게시됩니다.")

# # 학급 회원 명단
# st.header("학급 회원 명단")
# st.write("우리 학급의 회원 명단은 다음과 같습니다:")
# st.write("- 홍길동")
# st.write("- 김철수")
# st.write("- 이영희")
# st.write("- 박지영")

# 연락처 정보
st.header("연락처 정보")
st.write("학급 담임 선생님의 연락처는 다음과 같습니다:")
st.write("- 이름: 김가현")
st.write("- 이메일: ka2017t@oryu.sen.ms.kr")
st.write("- 전화번호: 010-2220-8370")