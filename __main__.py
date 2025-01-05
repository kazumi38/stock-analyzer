import pandas as pd


def main():
    print('Hello World!')
    
    stockholders_equity = pd.Series([96995000000.0, 99803000000.0, None, 57411000000.0], index=['2023-09-30', '2022-09-30', '2021-09-30', '2020-09-30'])
    total_assets = pd.Series([383285000000.0, 0, 365817000000.0, 274515000000.0], index=['2023-09-30', '2022-09-30', '2021-09-30', '2020-09-30'])
    
    print(stockholders_equity/total_assets)
    
if __name__ == '__main__':
    main()