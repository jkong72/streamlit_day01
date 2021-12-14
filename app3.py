from typing import Sequence
import streamlit as st
import pandas as pd

def main() :
    st.title ('아이리스 연구')
    df = pd.read_csv('data/iris.csv')

#버튼
    # if st.button('데이터 보기'): # 버튼이 눌린 순간에만 True
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

    if st.checkbox("show / hide"): #체크가 되어있을 때가 True
        st.dataframe(df.head())
    else :
        st.write('데이터가 없습니다.')


# 셀렉트 박스
    language = ['Python', 'C', 'Java', 'Go']
    my_choice = st.selectbox ('목록에서 하나를 선택할 수 있습니다.', language)
    if my_choice == 'C' :
        st.write('C언어는 역사와 전통이 있는 언어')

# 멀티 셀렉트 박스
    choice_list = st.multiselect('여러개를 선택할 수 있습니다(태깅)', language)
    st. write(choice_list)

# 멀티 셀렉트 박스 데이터프레임 예제
    choice_list = st.multiselect('컬럼을 선택하세요', df.columns)
    st.dataframe(df[choice_list])

# 슬라이더 
    age = st.slider('나이', 1, 100, value=30, step=10)
    st.write(f'선택한 나이는 {age}살 입니다.')

# 익스팬더
    sentence = '아무런 텍스트를 통해 긴 텍스트를 어떻게 표현하는지, 혹은 어디까지 표현하는지를 알 수 있습니다. 더 많은 양의 텍스트가 주어졌을 때의 상황을 시험하기 위해 더 많은 양의 텍스트를 삽입해 보겠습니다.'
    with st.expander('hello') :
        st.text(sentence)

if __name__ == '__main__':
    main()