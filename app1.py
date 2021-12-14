# Streamlit 라이브러리를 사용하기 위해 불러오기
import streamlit as st

# Streamlit은 main함수가 반드시 있어야 하며, 
# main 함수를 정의해야 한다.
def main() :
    st.title ('title. 제목을 쓰기 좋은 큰 글씨')
    st.header ('header. 부제목으로 사용하기 좋은 큰 글씨')
    st.subheader ('subheader. 헤더보다 좀 더 작은 글씨')

    st.write ('write\n표준적으로 본문에 사용하기 좋은 글씨')
    st.text ('tex\nwrite보다 좀 더 작고 폰트의 본새가 별로 좋지 않다. 하지만 탈출문자가 잘 작동함.')
    st.caption ('caption\n글자가 더 작고 흐려서 주석이나 참조를 달기 좋은 글씨')

    st.info ('info 청색 박스로 가시성을 높인 텍스트')
    st.success ('success 녹색 박스로 가시성을 높인 텍스트')
    st.warning ('warning 황색 박스로 가시성을 높인 텍스트')
    st.error ('error 적색 박스로 가시성을 높인 텍스트')

if __name__ == '__main__' :
    main()


# st.text('Fixed width text')
# st.markdown('_Markdown_') # see *
# st.caption('Balloons. Hundreds of them...')
# st.latex(r''' e^{i\pi} + 1 = 0 ''')
# st.write('Most objects') # df, err, func, keras!
# st.write(['st', 'is <', 3]) # see *
# st.title('My title')
# st.header('My header')
# st.subheader('My sub')
# st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True