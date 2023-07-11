import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("간단한 대시보드 예제")

    # 데이터 로드
    df = load_data()

    # 데이터 테이블 출력
    st.subheader("데이터 테이블")
    st.dataframe(df)

    # 데이터 요약 정보 출력
    st.subheader("데이터 요약 정보")
    st.write(df.describe())

    # 데이터 시각화
    st.subheader("데이터 시각화")

    # 히스토그램
    st.subheader("히스토그램")
    selected_column = st.selectbox("히스토그램을 그릴 열 선택", df.columns)
    if selected_column:
        plt.hist(df[selected_column])
        st.pyplot()

    # 산점도
    st.subheader("산점도")
    selected_x = st.selectbox("X 축 선택", df.columns)
    selected_y = st.selectbox("Y 축 선택", df.columns)
    if selected_x and selected_y:
        plt.scatter(df[selected_x], df[selected_y])
        st.pyplot()

    # 상관 히트맵
    st.subheader("상관 히트맵")
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True)
    st.pyplot()

def load_data():
    # 임의의 데이터 생성
    data = {
        'A': np.random.randn(100),
        'B': np.random.randn(100),
        'C': np.random.randn(100),
        'D': np.random.randn(100)
    }
    df = pd.DataFrame(data)
    return df

if __name__ == '__main__':
    main()

# 실행은 streamlit run 파일명