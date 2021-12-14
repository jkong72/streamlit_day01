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

# altair를 통한 차트
# https://altair-viz.github.io/gallery/index.html
import altair as alt

# plotly를 통한 차트
# https://plotly.com/python/getting-started/
import plotly.express as px



def main() :
    df1 = pd.read_csv('data/lang_data.csv')
    st.dataframe(df1)

    print (df1.columns[1:])
    langs = df1.columns[1:]

    choices = st.multiselect('언어를 선택할 수 있습니다.', langs)
    if len(choices) != 0:
        # 유저가 언어를 선택하면 차트를 그리려한다.
        df_selected = df1[choices]

        # 스트림릿의 라인차트
        st.line_chart(df_selected)

        # 스트림릿의 영역차트
        st.area_chart(df_selected)
    
    df2 = pd.read_csv('data/iris.csv')

    # 스트림릿의 바차트
    df2_selected = df2[['sepal_length', 'petal_length']]
    st.bar_chart(df2_selected)

# Altair
# x축과 y축과 더불어 색상이나 크기따위로 더 많은 정보를 표시할 수 있음.

    chart = alt.Chart(df2).mark_circle().encode(
        x = 'petal_length',
        y = 'petal_width',
        color = 'species'
    )

    st.altair_chart(chart)

    # 스트림릿의 맵차트
    df3 = pd.read_csv('data/location.csv')
    st.dataframe(df3)

    st.map(data=df3)

    # plotly를 이용한 차트 그리기
    df4 = pd.read_csv('data/prog_languages_data.csv', index_col=0)
    st.dataframe(df4)

    # plotly의 pie차트
    df_sorted = df4.sort_values('Sum', ascending=False)
    fig1 = px.pie(df_sorted, 'lang', 'Sum', title='프로그래밍 언어 점유율')
    st.plotly_chart(fig1)

    # plotly의 bar차트
    df_sorted = df4.sort_values('Sum', ascending=False)
    fig2 = px.bar(df_sorted, x='lang', y='Sum')
    st.plotly_chart(fig2)

if __name__ == '__main__':
    main()