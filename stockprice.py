import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# simple stock price App

Show are the stock closing price and volume of Google

""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id', start='2010-5-31', end='2020-5-310')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.volume)


C:\Users\GOD\anaconda3\Lib\site-packages\anaconda_project\internal\__pycache__
