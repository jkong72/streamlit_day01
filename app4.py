import streamlit as st
import numpy as np
import pandas as pd

# 이미지 처리를 위한 라이브러리 PIL
from PIL import Image

def main():
# 이미지 파일 표시
    st.image('data/image_03.jpg')
    img = Image.open('data/image_03.jpg')
    print(img)
    st.image(img)
    st.image(img, use_column_width=True)
    # 이미지의 url을 통해서 표시할 수 있다.
    st.image('https://t1.daumcdn.net/cfile/blog/272B044654D1AE0B2C')

# 비디오 파일 표시
    st.video('data/bike.mp4')
    # 비디오의 url을 통해서 표시할 수 있다. 플레이어는 원본 사이트를 따른다.
    st.video('https://www.youtube.com/watch?v=aircAruvnKk')
    
    video_file = open('data/bike.mp4', 'rb')
    st.video(video_file)

# 오디오 파일 실행
    audio_file = open('data/sample_music.mp3', 'rb')
    st.audio(audio_file.read(), format='audio/mp3')
    st.audio('data/sample_music.mp3')


    print(np.array(img))

    pass
if __name__ == '__main__' :
    main()