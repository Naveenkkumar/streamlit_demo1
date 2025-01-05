import yfinance as yf
import streamlit as st
import pandas as pd

st.title("Stock Market App by Naveen")

st.write("I will be making this website more advance!!")

user_input_symbol = st.text_input("Enter the stock symbol", "AAPL")
user_input_start_date = st.date_input("Enter the start date", value=pd.to_datetime("2024-12-01"))
user_input_end_date = st.date_input("Enter the end date")

ticker_data = yf.Ticker(user_input_symbol)
df = ticker_data.history(period="1d", start="2021-5-1", end="2021-5-10")
st.write("Stock Market Data of Apple", df)




col1, col2 = st.columns(2)

with col1:
    st.write("This is volume chart")
    st.line_chart(df.Volume)

with col2:
    st.write("This is closing price chart")
    st.line_chart(df.Close)

