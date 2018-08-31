#update memo:时间需要自动更新到今天的日期，并且显示出来
#获取的数据是否是复权数据


import tushare as ts
from decimal import Decimal
import time
import sys
sys.path.append('/home/alzer/PycharmProjects/THShelper/utils')
from myTushare import getTuShareService

#input validation
def exCompletion(ex):

    if(len(ex) != 6 ):
        print('ex code %s error,not recognised.' %ex)
        return False

    #begin with
    #000 shenzhen 主板
    #002 shenzhen 中小板
    #600 shanghai 主板
    #3   shenzhen 创业板
    #shenzhen
    if ( ex.startswith('000') or ex.startswith('002') or ex.startswith('3') or ex.startswith('00')):
        exComplete = '%s.SZ' %ex
        return exComplete
    elif (ex.startswith('600') or ex.startswith('601') or ex.startswith('603')):
        exComplete = '%s.SH' %ex
        return exComplete
    else:
        print('The ex code %s not recognised.' %ex)
        return False


def scheme1(p):
    price = Decimal(p)

    factor = 99.00

    while factor >= 90.00:

        buyPrice = price * Decimal(factor/100)

        print('factor=%s%%,buyPrice=%f' %(factor,buyPrice))

        factor -= 1

def today():
    today=time.strftime('%Y%m%d')
    return today

#THS团队的冒险指数，如果<1表示谨慎，如果大于1表示想追涨

def calcRish(closePrice,expectPrice):
    # print('t1=%s' %type(closePrice))
    # print('t2=%s' %type(expectPrice))
    risk = Decimal(expectPrice)/Decimal(closePrice)
    return risk

print('Please input the exchanges , seperate by a space,end with an enter:')

#login on to the tushare
# ts.set_token('c43dab7d00de3db2a87947459b13da12bada68f6bd78019102ffa04e')
# IApi = ts.pro_api()
IApi = getTuShareService()

ExchangeList = input().split()
iStockCount = len(ExchangeList)

if(iStockCount%3 != 0):
    print('input error.')
    sys.exit(1)

#get close price of each stock.
for j in range(0,iStockCount,3):

    # print('j=%d' %j)
    # i+=1
    # ex=ExchangeList[j]
    # low=ExchangeList[j+1]
    # high=ExchangeList[j+2]
    # print('test=%s,low=%s,high=%s' %(ex,low,high))

    exComplete = exCompletion(ExchangeList[j])

    if(exComplete != False and exComplete != None):
        print('The %d stock info,code=%s:' %(j/3+1,exComplete))

    df = IApi.daily(ts_code=exComplete, start_date='20180830', end_date='20180830')
    # df = IApi.daily(ts_code=exComplete, start_date=today(), end_date=today())
    print(df)

    closePrice = df.iat[0,5]
    # print(closePrice)
    scheme1(closePrice)
    lowRish = (1 - calcRish(closePrice,ExchangeList[j+1])) * 100
    highRish =(1 - calcRish(closePrice,ExchangeList[j+2])) * 100

    if(lowRish >= 0):
        lowRishStr = '-%.5s' %lowRish
    else:
        lowRishStr = '%.5s' %-lowRish

    if(highRish >= 0):
        highRishStr = '-%.5s' %highRish
    else:
        highRishStr ='%.5s' %-highRish

    print('Risk=[%s,%s]' %(lowRishStr,highRishStr))

    if(lowRish *2 < 5):
        pioneerPrice = (100 - Decimal(lowRish)*2)/100 * Decimal(closePrice)
        print('pioneerPrice=%s' %pioneerPrice)
    else:
        print('No pioneerPrice')


    if(j < iStockCount):
        print('------------------------------------------')
