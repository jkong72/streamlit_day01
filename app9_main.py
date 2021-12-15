import streamlit as st
from app9_EDA import run_eda_app
from app9_ML import run_ml_app

# 하나의 앱을 여러 파일로 구성하는 법
def main():
    st.title('파일 분리 앱')

    menu = ['Home', 'EDA', 'ML', 'About']

    choice = st.sidebar.selectbox ('메뉴', menu)

    # menu Home
    if choice == menu[0] :
        st.subheader ('메인 화면')

    # menu EDA
    elif choice == menu[1] :
        run_eda_app()

    # menu ML
    elif choice == menu[2] :
        run_ml_app()

    # menu About
    elif choice == menu[3] :
        st.write('EDA는 탐색적 자료분석, ML은 머신러닝의 약자입니다.')



if __name__ == '__main__':
    main() 