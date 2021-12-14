import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')



def main() :
    st.title('st.pyplot()을 통한 차트와 그래프')
    
    df = pd.read_csv('data/iris.csv')
    st.dataframe(df)

#차트 그리기
    # 산점분포를 통한 예시
    fig = plt.figure(figsize=([5,5])) # 차트 영역 설정
    plt.scatter(data=df,x='sepal_length',y='sepal_width') # 차트 그리기
    plt.title ('꽃밭임 길이와 너비의 상관관계')
    plt.xlabel('꽃밭임 길이')
    plt.ylabel('꽃밭임 너비')

    st.pyplot(fig) # 구성된 차트 영역을 화면에 표시

    # seaborn의 regression
    fig2 = plt.figure()
    sns.regplot(data=df, x='sepal_length', y='sepal_width')
    st.pyplot(fig2)

    # sepal_length로 히스토그램
    fig3 = plt.figure(figsize=(10,5))
    plt.subplot (1,2,1)
    plt.hist(data=df, x='sepal_length', bins=10, rwidth=0.8)

    plt.subplot (1,2,2)
    plt.hist(data=df, x='sepal_length', bins=20, rwidth=0.8)
    st.pyplot(fig3)

    # species 컬럼에는 종 정보가 기록되어 있다.
    # 각 종별 갯수를 바탕으로 차트로 표시
    fig4 = plt.figure()
    sns.countplot(data=df, x='species')
    st.pyplot(fig4)

    # 데이터프레임의 차트 코드도 실행 가능
    fig5 = plt.figure()
    df['species'].value_counts().plot(kind = 'bar')
    st.pyplot(fig5)

    fig6 = plt.figure()
    df['sepal_length'].hist()
    st.pyplot(fig6)

if __name__ == '__main__':
    main()