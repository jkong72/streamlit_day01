## 여러 파일을 업로드 하는 app

import streamlit as st
from PIL import Image
import pandas as pd
from datetime import datetime as dt
import os

# 파일 업로드 함수
def save_uploaded_file(directory, file) :
    # 디렉토리의 존재 여부를 확인
    if not os.path.exists(directory):
        # 디렉토리가 없다면 해당 위치를 생성
        os.makedirs(directory)
    # 디렉토리가 형성됐다고 보고 파일을 저장
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    return st.success (f'{file.name} 파일을 {directory} 경로에 저장하는데 성공했습니다.')


def main ():
    st.title('여러 파일을 업로드 하는 앱')

    # 사이드바 메뉴
    menu = ['Image', 'CSV', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)

    #시간 
    # datef = (dt.now().strftime('%y-%M-%D_%H-%M-%S'))
    #확장자 찾기
    # dotloc = file.name.find('.')

    # sidebar Image
    if choice == menu[0]:
        uploaded_files = st.file_uploader('이미지 파일 업로드',
                        type = ['png', 'jpg', 'jpeg'],
                        accept_multiple_files=True)
        print (uploaded_files)
        if uploaded_files is not None:
            for file in uploaded_files:
                current_time = dt.now()
                current_time = current_time.isoformat().replace(':', '-')
                dotloc = file.name.find('.')
                file.name = current_time + file.name[dotloc : ]
                save_uploaded_file('temp_all', file)

                img = Image.open(file)
                st.image(img)

    # sidebar CSV
    if choice == menu[1]:
        uploaded_csv_files = st.file_uploader('CSV 파일 업로드', type = ['csv'], accept_multiple_files = True)
        print (uploaded_csv_files)
        if uploaded_csv_files is not None:
            for file in uploaded_csv_files:
                current_time = dt.now()
                current_time = current_time.isoformat().replace(':', '-')
                dotloc = file.name.find('.')
                file.name = current_time + file.name[dotloc : ]

                save_uploaded_file('csv_all/', file)

                df = pd.read_csv(file)
                st.dataframe(df)
    


    # sidebar About
    if choice == menu[2]:
        st.header ('기능 소개')
        st.write ('여러개의 이미지 파일 (.png, .jpg, .jpeg)과 csv파일을 업로드/다운로드 할 수 있습니다.')
        pass


        pass
if __name__ == '__main__':
    main()