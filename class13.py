
import streamlit as st

import datetime as dt
import pandas_datareader as pdr

today = dt.date.today()
start_date = today - dt.timedelta(days=365)

st.sidebar.header("User Inputs")


def user_inputs():
    ticker = st.sidebar.text_input('Ticker', 'AAPL')
    start = st.sidebar.text_input('Start Date', f'{start_date}')
    end = st.sidebar.text_input('End Date', f'{today}')
    button = st.sidebar.button('Get Chart')
    return ticker, start, end, button


ticker, start, end, button = user_inputs()


def get_symbol(ticker, start=start, end=end):
    symbol = ticker.upper()
    data = pdr.get_data_yahoo(ticker, start, end)
    return data

st.write(f'# {ticker.upper()}')

if button:
    data = get_symbol(ticker)
    st.line_chart(data.Close)

