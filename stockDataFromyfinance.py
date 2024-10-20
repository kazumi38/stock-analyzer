import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib import gridspec
import pandas as pd
import json
import csv
from pathlib import Path 
import pprint 
from createROE import *
from getWeekdayPastYears import get_same_weekday_past_years

# 銘柄情報取得
ticker = '9346.T'  # 株の銘柄コード

# 必要な情報を取得
weekday = get_same_weekday_past_years(5)
dateHistoryStr = '|'.join(weekday)

stock = yf.Ticker(ticker)
info = stock.info
financials = stock.financials
balances = stock.balance_sheet
history = stock.history(period="5y")
cashflow = stock.cashflow

output = Path('output/'+ticker)
output.mkdir(parents=True, exist_ok=True)

with output.joinpath('info.json').open('w') as f:
    json.dump(info, f, indent=2, separators=(',', ': '))
financials.sort_index(axis='index').to_csv('output/'+ticker+'/financials.csv')
balances.sort_index(axis='index').to_csv('output/'+ticker+'/balances.csv')
history.sort_index(axis='index').to_csv('output/'+ticker+'/history.csv')
cashflow.sort_index(axis='index').to_csv('output/'+ticker+'/cashflow.csv')

# 過去5年分の終値と日付
closing_prices = history['Close'].filter(regex=dateHistoryStr, axis=0)
# dates = closing_prices.index.strftime('%Y-%m-%d').tolist()

required_count = 5
# データが不足している場合に補完の処理を実行
if len(closing_prices) < required_count:
    # データが存在する場合は最も古い日付を基準に、存在しない場合は現在の日付を基準にする
    latest_date = history.index[-1] if not history.empty else pd.Timestamp.today()

    # 不足しているデータのための日付を作成
    missing_dates = pd.date_range(end=latest_date, periods=required_count - len(closing_prices), freq='D')
    
    # データに不足分の日付を追加し、ソートしてから線形補完を実施
    closing_prices = closing_prices.reindex(closing_prices.index.union(missing_dates)).sort_index()
    closing_prices = closing_prices.interpolate(method='linear')

# # 配当情報や財務指標
dividend_yield = info.get('dividendYield', '---')
payout_ratio = info.get('payoutRatio', '---')
pe_ratio = info.get('trailingPE', '---')
market_cap = info.get('marketCap', '---')

# # 決算データ
closing_dates = financials.head(0)
eps = financials.loc['Basic EPS']
net_income = financials.loc['Net Income']
sales = financials.loc['Total Revenue']

# 自己資本と総資産を取得
shareholder_equity = balances.loc['Stockholders Equity']
total_assets = balances.loc['Total Assets']

# # 財務データ
operating_cf = cashflow.loc['Operating Cash Flow']

# 自己資本比率の計算
equity_ratio = (shareholder_equity / total_assets) * 100
roe = net_income / shareholder_equity

# # 表のデータ作成
data = [
    ['銘柄コード', ticker, 'NASDAQ', 'IT・テクノロジー', 'テクノロジー'],
    weekday[::-1],
    ['終値'] + closing_prices.tolist(),
    ['配当金', dividend_yield, '配当利回り', payout_ratio, 'PER', pe_ratio, market_cap],
    ['決算日'] + closing_dates.columns.strftime('%Y-%m-%d').tolist(),
    ['EPS'] + eps.tolist(),
    ['自己資本比率 (%)'] + equity_ratio.tolist(),
    ['営業CF (百万)'] + operating_cf.tolist(),
    ['ROE (%)'] + roe.tolist(),
    ['純利益 (百万)'] + net_income.tolist(),
    ['売上高 (百万)'] + sales.tolist()
]

pprint.pprint(data)

data = [
    ['銘柄コード', ticker, 'NASDAQ', 'IT・テクノロジー', 'テクノロジー'],
    weekday[::-1],
    ['終値'] + closing_prices.tolist(),
    ['配当金', dividend_yield, '配当利回り', payout_ratio, 'PER', pe_ratio, market_cap],
    ['決算日'] + closing_dates.columns.strftime('%Y-%m-%d').tolist(),
    ['EPS'] + eps.tolist(),
    ['自己資本比率 (%)'] + equity_ratio.tolist(),
    ['営業CF (百万)'] + operating_cf.tolist(),
    ['ROE (%)'] + roe.tolist(),
    ['純利益 (百万)'] + net_income.tolist(),
    ['売上高 (百万)'] + sales.tolist()
]
