import tushare as ts
import sys

sys.path.append('/home/alzer/PycharmProjects/THShelper/utils')
from dateUtils import nDaysAgo
from dateUtils import today
from myTushare import getTuShareService
from myTushare import exCompletion


IApi = getTuShareService()

data = IApi.stock_basic(exchange_id='', is_hs='N', fields='symbol,name,list_date,list_status')

exchangeCodeList = []

for index,row in data.iterrows():
    # print(row["symbol"],row["name"])
    exchangeCodeList.append(row["symbol"])

for line in exchangeCodeList:
    exName = exCompletion(line)
    df = IApi.daily(ts_code=exName, start_date=nDaysAgo(10), end_date=today())
    print(df)
