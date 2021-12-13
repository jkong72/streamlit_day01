import streamlit as st
import pandas as pd

import streamlit as st
def main() :
    df = pd.read_csv('data/iris.csv')
    st.dataframe(df,800,100)

    species = df['species'].unique()
    st.write(species)
    st.text('아이리스 꽃은' +species + '으로 되어있다.')


    st.write (df.head())

if __name__ == '__main__' :
    main()