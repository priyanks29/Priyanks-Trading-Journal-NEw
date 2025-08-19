# IBKR Options Journal

A private trading journal app (similar to TradeZella) built with Streamlit.

## Features
- Import IBKR Flex Query CSVs for options
- Track trades, P&L, and commissions
- Overlay entries & exits on underlying charts (TradingView or Yahoo)
- KPIs: win rate, expectancy, profit factor, equity curve

## How to run locally
```bash
python3 -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run app.py
```

## Deployment on Streamlit Cloud
1. Push this repo to GitHub (public)
2. Go to https://streamlit.io/cloud → Sign in with GitHub
3. Deploy `app.py` as the main file
