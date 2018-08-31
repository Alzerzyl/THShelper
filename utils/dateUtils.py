import datetime
import time
#获取N天前的日期
def nDaysAgo(n):
    today = datetime.date.today()

    targetDate = today - datetime.timedelta(days=n)
    resutl = targetDate.strftime('%Y%m%d')

    return resutl

#今天
def today():
    today=time.strftime('%Y%m%d')
    return today