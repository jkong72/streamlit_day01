## 파일 업로드하는 방법 ##

import streamlit as st
from PIL import Image
import pandas as pd
from datetime import datetime as dt
import os

# 디렉토리 정보와 파일을 건네주면
# 해당 디렉토리에 파일을 저장하는 함수 작성
def save_uploaded_file(directory, file) :
    # 디렉토리의 존재 여부를 확인
    if not os.path.exists(directory):
        # 디렉토리가 없다면 해당 위치를 생성
        os.makedirs(directory)
    # 디렉토리가 형성됐다고 보고 파일을 저장
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    return st.success (f'{file.name} 파일을 {directory} 경로에 저장하는데 성공했습니다.')


def main() :
    st.title('파일 업로드 프로젝트')
    menu = ['Image', 'CSV', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0]: # Image
        st.subheader('이미지 파일 업로드')
        image_file = st.file_uploader('이미지를 업로드 하세요', type = ['png', 'jpg', 'jpeg'])
        if image_file is not None :
            # 파일의 속성을 터미널에 띄울 수 있다.
            # print(type(image_file))
            # print(image_file.name)
            # print(image_file.size)
            # print(image_file.type)


            # 파일 이름을 유니크하게 만들기 위해 현재 시간을 파일이름에 합성
            # str이나 isoformat 등을 통해서 문자열로 바꿔줌.
            # datetime이나 timestamp는 파일명으로 사용할 수 없는 부호(:)가 포함되어 있으므로
            # replace나 strftime 등을 통해 형식을 바꿔줄 것.
            current_time = dt.now()
            current_time = current_time.isoformat().replace(':', '-')
            dotloc = image_file.name.find('.')
            image_file.name = current_time + image_file.name[dotloc : ]

            # 함수를 호출해 파일을 새로 저장
            save_uploaded_file('temp/', image_file)
        

            # 동시에 해당 파일을 표시
            img = Image.open(image_file)
            st.image(img, width= 400)


            
            


    elif choice == menu[1]: # CSV
        st.subheader('CSV 파일 업로드')

        data_file = st.file_uploader('CSV 파일 업로드', type=['csv'])
        if data_file is not None :
            # print(type(data_file))
            # print(data_file.name)
            # print(data_file.size)
            # print(data_file.type)
            save_uploaded_file('csv_files/', data_file)
            df = pd.read_csv(data_file)
            st.dataframe(df)
            

    elif choice == menu[2]: # About
        st.subheader('기능 소개')
        st.write('이미지 파일이나 CSV파일을 업로드 할 수 있습니다.')
        

if __name__ == '__main__':
    main()