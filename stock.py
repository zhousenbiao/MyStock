# -*- coding:utf-8 -*-

import urllib.request

# 调试
debug=False

# 工具类
class Utility:
  def ToGB(str):
    if(debug): print(str)
    return str.decode('gb2312')

# 股票信息类
class StockInfo:

  #返回的字串： v_s_sz002070="51~众和股份~002070~19.15~0.92~5.05~429162~81069~~121.65";
  #通过股票代码查询
  def GetStockStrByCode(code):
    f= urllib.request.urlopen('http://qt.gtimg.cn/q=s_'+ str(code))
    if(debug): print(f.geturl())
    if(debug): print(f.info())
    return f.readline()
    f.close()

  def ParseResultStr(resultstr,displayColor =0):#显示方式：0 -－黑体字  1 －－彩色字
    if(debug): print(resultstr)
    slist=resultstr[14:-3]
    if(debug): print(slist)
    slist=slist.split('~')
    if(debug) : print(slist)
    code = "%-8s" % slist[2]
    name = "%-8s" % slist[1]
    current_price = "%-8s" % slist[3]
    change_price = "%-8s" % slist[4]
    change_percent ="%-6s"% slist[5]
    volume="%-10s" % slist[6]
    turnover="%-8s"% slist[7]

    # 彩色显示方式
    if(displayColor==1):
        # 涨的红色显示
        if(float(slist[4])>0.0):
            print('\033[1;31m')
            print("{0} {1} {2}  {3}   {4}%    {5}    {6}".format(code,name,current_price,change_price,change_percent,volume,turnover) )
            print('\033[0m')
        # 跌的绿色显示
        elif(float(slist[4])<0.0):
            print('\033[1;32m')
            print("{0} {1} {2}  {3}   {4}%    {5}    {6}".format(code,name,current_price,change_price,change_percent,volume,turnover) )
            print('\033[0m')
        else:
            print("{0} {1} {2}  {3}   {4}%    {5}    {6}".format(code,name,current_price,change_price,change_percent,volume,turnover) )
    # 黑白显示方式
    else:
        print("{0} {1} {2}  {3}   {4}%    {5}    {6}".format(code,name,current_price,change_price,change_percent,volume,turnover) )

  def GetStockInfo(code,colorDefault):
    str=StockInfo.GetStockStrByCode(code)
    strGB=Utility.ToGB(str)
    StockInfo.ParseResultStr(strGB,colorDefault)

  def getInfo(stocks,colorDefault):
      print("--代码-----名称---------价格------涨跌-------幅度-------成交量(手)-----成交额(万)-- ")
      for stock in stocks:
        StockInfo.GetStockInfo(stock,colorDefault)
      print("--code-----name------price----amount------range------Volume-------Turnover---- ")


if __name__ == '__main__':
  # 'sh600888','sz300104','sz300027','sz000919','sz000858','sz300219'
  StockInfo.getInfo(['sh000001','sh601005','sh600546','sh600022','sh600795','sh600500'],1)