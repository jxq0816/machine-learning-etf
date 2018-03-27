# coding=utf-8
# Created on 2018年3月26日
# author: jiangxingqi

import xlrd
#代码 名称 日期 开盘 收盘	最高价 最低价	前收盘 成交量	流通盘 对数收益 成交额	日振幅	RSI(24)	3日动量	MA(20)	标准差（20）	复权收盘价	Bollup	Bolllo	K（9）	D(5)	J(5)	Madif10:60	EMA(12)	EMA(26)	DIF	MACD	MV(14)	MV(28)	VA	VROC(25)	ATR7	10:100ATR	Delta ATR Ratio	价速10	初始买卖点	ADX(14,6)	%W（10）	Bias（24）	OBV	趋势点	开盘收益

# 打开文件
try:
    data = xlrd.open_workbook('etf_data/510050.xls')
except:
    print("fail to open file")
else:
    file = open("etf_data/data_extract.txt", "a")  # 文件读写方式是追加
    # 第一个sheet
    table = data.sheets()[0]
    # 第一列
    table.col_values(0)
    # 多少行
    n = table.nrows

    file.writelines("3日动量,Madif10:60,ATR7,10:100ATR,价速10,开盘收益,label\r")  # 将字符串写入新文件

    for i in range(n):
        # 今收盘4
        today_close = table.cell(i, 4).value
        # 前收盘7
        pre_close = table.cell(i, 7).value

        dis=today_close-pre_close

        if dis > 0 :
            label = 1
        elif dis == 0:
            label = 0
        else:
            label = -1

        momentum = table.cell(i, 14).value
        madif1060 = table.cell(i, 23).value
        atr7 = table.cell(i, 32).value

        atr10100 = table.cell(i, 33).value
        price_speed = table.cell(i, 35).value
        open_close = table.cell(i, 42).value

        values = str(momentum) + "," + str(madif1060) + "," + str(atr7) + "," + str(atr10100) + "," + str(price_speed) + "," + str(open_close)+","+str(label);
        file.writelines(values + "\r")  # 将字符串写入新文件
    file.close()  # 关闭写入的文件
print("end")
