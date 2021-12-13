import streamlit as st
import pandas as pd

def main() :
    st.title ('아이리스 연구')
    df = pd.read_csv('data/iris.csv')

#버튼
    # if st.button('데이터 보기'):
    #     st.dataframe(df)

    # name = 'Mike'
    # if st.button ('대문자로'):
    #     st.write(name.upper() )
    # if st. button ('소문자로'):
    #     st.write(name.lower() ) 

#라디오 버튼
    st.dataframe(df)
    status = st.radio('정렬 기준 (petal length)', ['오름차순', '내림차순'])
    if status == '오름차순' :
        st.dataframe(df.sort_values('petal_length'))
    elif status == '내림차순':
        st.dataframe(df.sort_values('petal_length', ascending=False))


if __name__ == '__main__':
    main()