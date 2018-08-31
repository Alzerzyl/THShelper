import tushare as ts

#login to tushare and get pro api
def getTuShareService():
    ts.set_token('c43dab7d00de3db2a87947459b13da12bada68f6bd78019102ffa04e')
    IApi = ts.pro_api()
    return IApi


#add exchange suffix
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
