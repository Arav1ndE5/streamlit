import yfinance as yf
import streamlit as st
import numpy as np


st.write("""Hello goois ee data nokkk\n
this is stock price of google""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerGP = tickerData.history(period='1d',start='2020-5-31', end='2023-7-01')

st.line_chart(tickerGP.Close)
st.line_chart(tickerGP.Volume)


