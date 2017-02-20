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
    # cookiesLen = len(str(login.cookies))
    # print(len(str(login.cookies)))
    return session

def toupiao(toupiaoUrl, session, toupiaoData):
    login = session.post(toupiaoUrl, toupiaoData, headers = headers)
    # print(login.cookies)
    return login.cookies

def numberSaved(number):
    # with open('numbersaved.txt','w+') as numbers:
    #     numbers.write(number)
    file_number = open("numbersaved.txt", "w+")
    # file_number = open("numberSaved.txt", "w+")
    file_number.write(number)
    file_number.close()

if __name__ == '__main__':
    count = 0
    # getUrl = "http://njupt.pocketuni.net/index.php?app=event&mod=Front&act=playerDetails&id=212818&pid=98359"
    loginUrl = "http://pocketuni.net/index.php?app=home&mod=Public&act=doLogin&school=njupt"
    file_object = open('numbersaved.txt', 'rb')
    school = "南京邮电大学"
    sid = "592"
    # number = "B15041216"
    password = "111111"
    login = "登 录"
    # __hash__ = getHash()
    toupiaoUrl = "http://njupt.pocketuni.net/index.php?app=event&mod=Front&act=vote"
    pids = ["98359", "99982", "99957", "99420", "93253", "98681"]
    idd = 212818
    while True:

        try:
            number = file_object.read(9)
            __hash__ = getHash()
            loginData = {'school':school, 'sid':sid, 'number':number, 'password':password, 'login':login, '__hash__':__hash__[0]}
            session = create_session(loginUrl, loginData) 
            # pid = 97293  ,
            # if cookiesLen == 21:
                # numberSaved(number)
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
