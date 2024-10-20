import numpy as np
import pandas as pd

def createEarnings(financials, ticker):
    earnings = financials.T["Net Income"] # 当期純利益

    earnings = pd.DataFrame(earnings).T  # DataFrame化
    # earnings.columns = ticker            # カラム名の設定

def createEquity(balances, ticker):
    equity = balances.T["Stockholders Equity"] # 自己資本

    equity = pd.DataFrame(equity).T  # DataFrame化
    # equity.columns = ticker            # カラム名の設定

def createROE(financials, balances, ticker):
    roe = financials.T["Net Income"] / balances.T["Stockholders Equity"]
    roe = pd.Series(roe)  # DataFrame化

    return roe

def createEPS(financials, balances, ticker):
    eps = financials.T["Net Income"] / balances.T["Basic Shares Outstanding"]

    eps = pd.DataFrame(eps).T  # DataFrame化
    # eps.columns = ticker            # カラム名の設定
