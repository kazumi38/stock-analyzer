import numpy as np
from pprint import pprint

def formatter(datas: list[list]):
    formatter_datas = datas
    formatter_datas = formatter_None(formatter_datas)
    formatter_datas = formatter_nan(formatter_datas)
    formatter_datas = formatter_inf(formatter_datas)
    
    return formatter_datas

def formatter_None(datas: list[list]):
    return [['---' if type(data) is not str and data is None else data for data in data_row] for data_row in datas]

def formatter_nan(datas: list[list]):
    return [[ '---' if type(data) is not str and np.isnan(data)  else data for data in data_row] for data_row in datas]

def formatter_inf(datas: list[list]):
    return [[ '---' if type(data) is not str and np.isinf(data) else data for data in data_row] for data_row in datas]

if __name__ == '__main__':
    from pprint import pprint 
    datas = [
        ['銘柄コード', '9346.T', 'NASDAQ', 'IT・テクノロジー', 'テクノロジー'],
        ['2020-10-27', '2021-10-26', '2022-10-25', '2023-10-24', '2024-10-22'],
        ['終値', float('nan'), float('nan'), float('nan'), float('nan'), float('nan')],
        ['配当金', 0.056999996, '配当利回り', '---', 'PER', 10.834522, 5511098880],
        ['決算日', '2024-06-30', '2023-06-30', '2022-06-30', '2021-06-30'],
        ['EPS', float('inf'), None, 80.745838, 57.99505],
        ['自己資本比率 (%)',
        74.14713559745634,
        72.16433897894278,
        42.57139433693863,
        30.414557997291354],
        ['営業CF (百万)', 562618000.0, 421415000.0, 176197000.0, 141638000.0],
        ['ROE (%)',
        0.22368141621543866,
        0.2501893394304957,
        0.42340816523564767,
        0.5685755315646676],
        ['純利益 (百万)', 525584000.0, 452903000.0, 258746000.0, 200341000.0],
        ['売上高 (百万)', 5750811000.0, 5083804000.0, 4176184000.0, 3325346000.0]
    ]
    
    pprint(formatter(datas))