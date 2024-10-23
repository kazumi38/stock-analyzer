import pandas as pd

def getFromDataFrame(df: pd.DataFrame, index: str):
    # print('\n\n',index, '\n\n')
    # print(df)
    data = pd.Series([None, None, None, None])
    max_length = len(data)
    update_length = min(len(df.loc[index]), max_length)
    data[:update_length] = df.loc[index][:update_length]
    return data

if __name__ == '__main__':
    date_labels = ['2023-09-30', '2022-09-30', '2021-09-30']
    f_index = ['Basic EPS', 'Net Income', 'Total Revenue']
    nan_financials = pd.DataFrame(
        [
            [6.16, 5.67, None], 
            [96995000000.0, None, 57411000000.0],
            [None, 365817000000.0, 274515000000.0]
        ],
        index=f_index,
        columns=date_labels
    )
    print(nan_financials)

    print('Basic EPS')
    print(getFromDataFrame(nan_financials, 'Basic EPS'))

    print('Net Income')
    print(getFromDataFrame(nan_financials, 'Net Income'))

    print('Total Revenue')
    print(getFromDataFrame(nan_financials, 'Total Revenue'))