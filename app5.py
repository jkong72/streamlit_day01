import streamlit as st

def main() :
# 텍스트 입력받기
    name = st.text_input('이름을 입력하세요!')
    if name.isalpha() == True:
        name = name.upper()
    st.title (f'환영한다! {name}!!')

    name2 = st.text_input('글자제한', max_chars=4)
    st.title(f'글자제한! {name2}')

# 여러 행을 갖는 텍스트 입력받기
    message = st.text_area('메세지를 입력', height=3, )
    st.text(message)

# 숫자 입력받기
    num = st.number_input ('숫자를 입력', 1, 100)
    st.text(num)

    num2 = st.number_input('정수 입력', 0.0, 100.0)
    st.text(num2)

# 날짜 입력받기
    my_date = st.date_input('약속 날짜 입력')
    st.write(my_date)
    print(my_date)
# 시간 입력받기
    my_time = st.time_input('시간 선택', )

# 비밀번호 입력
    password = st.text_input('12자리 비밀번호', type='password')

# 색깔 입력
    col1, col2, col3 = st.columns(3)
    with col1:
        base_color = st.color_picker('기반 색상')
    with col2:
        main_color = st.color_picker('주 색상')
    with col3:
        accent_color = st.color_picker('강조 색상')

if __name__ == '__main__':
    main()