import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

st.title("📈 IBKR Options Journal")

st.write("Upload your IBKR Flex Query CSV to get started.")

uploaded = st.file_uploader("Upload CSV", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df.head())

    # Example: simple chart if Symbol column exists
    if "UnderlyingSymbol" in df.columns:
        symbol = df["UnderlyingSymbol"].iloc[0]
        data = yf.download(symbol, period="1mo", interval="1d")
        fig, ax = plt.subplots()
        ax.plot(data.index, data["Close"], label=symbol)
        ax.set_title(f"{symbol} - Last 1 Month")
        st.pyplot(fig)
