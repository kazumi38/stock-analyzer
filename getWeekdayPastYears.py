from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def get_same_weekday_past_years(years):
    today = datetime.now() - timedelta(1)
    dates = []
    for i in range(0, years ):
        same_weekday = today - relativedelta(years=i, weekday=today.weekday())
        dates.append(same_weekday.strftime('%Y-%m-%d'))
    print(dates)
    return dates