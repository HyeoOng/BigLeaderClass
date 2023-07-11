import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt

# 삼성전자 주식 데이터를 가져옵니다.
data = yf.download('005930.KS')

# Streamlit 앱을 시작합니다.
st.title('삼성전자 주식 가격')
st.line_chart(data['Close'])

# 종료가, 시가, 고가, 저가 정보를 보여줍니다.
st.subheader('주식 가격 정보')
st.write(data)

# 8501포트에서 열림