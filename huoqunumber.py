# huoqunumber.py 用于创建number初始列表 
# 保存在startnumber.txt里面

import os

fileObject = open("B140413.txt", "a")
numberIn = [15040100, 15040200, 15040500, 15040700, 15040900, 15040300, 15040400, 15040600, 15040800]
numberIn1 = [15050100, 15050200, 15050500, 15050700, 15050900, 15050300, 15050400, 15050600, 15050800]
numberIn2 = [15060100, 15060200, 15060500, 15060700, 15060900, 15060300, 15060400, 15060600, 15060800]
number3 = [15030100, 15030200, 15030500, 15030700, 15030900, 15030300, 15030400, 15030600, 15030800]
numberIn4 = [14041300]
for i in range(0, 1):
	for x in range(1,39):
		numberIn4[i] = numberIn4[i] + 1
		# print(numberIn)
		numberOut = "B" + str(numberIn4[i])
		fileObject.write(numberOut)
		# fileObject.write("\n")

fileObject.close()
