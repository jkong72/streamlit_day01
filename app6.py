import streamlit as st
from PIL import Image

img = Image.open('data/image_03.jpg')
# 페이지 레이아웃
st.set_page_config( 
    page_title="알도롱고",
    page_icon=img,
    layout='wide',
    initial_sidebar_state='collapsed')

def main():
    pass

if __name__ == '__main__':
    main()