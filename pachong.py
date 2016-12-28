# pachong.py

import requests
import urllib.request
import re
import configparser
from pprint import pprint
from bs4 import BeautifulSoup
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'}
headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/535.11 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/535.11'}

def getHash():
    firstURL = "http://pocketuni.net/njupt/login/"
    request = urllib.request.Request(firstURL, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read()
    # print(type(content))
    # print(str(content, encoding = "utf-8"))
    # suop = BeautifulSoup(response.content)  str(b, encoding = "utf-8")cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)
    pattern = re.compile(r'name=\"__hash__\" value=\"(.*?)\"', re.S)
    __hash__ = pattern.findall(str(content, encoding = "utf-8"))
    print(__hash__[0])
    return __hash__[0]

def create_session(loginURL, postUrl, data):
    # email = "903430068@qq.com"
    # password = "meng19960815"

    session = requests.session()
    login = session.post(loginURL, loginData, headers=headers)
    # print(login.cookies)
    # r = session.get(postUrl, cookies=login.cookies, headers=headers) # 实现验证码登陆
    # html = str(r.content, encoding = "utf-8")
    print(login.headers)
    print(login.cookies)
    # print(str(r.content, encoding = "utf-8"))
    # print(r)
    # print(r.text)
    return str(login.headers),str(login.cookies)

def function():
    pass

def htmlSaved(html):
    with open('texthearders1.txt','w') as htmlw:
        for htmls in html:
            htmlw.writelines(htmls)

def htmlSave1d(html):
    with open('texcoocies1.txt','w') as htmlw:
        for htmls in html:
            htmlw.writelines(htmls)

if __name__ == '__main__':
    # getHash()
    # loginURL = "http://pocketuni.net/njupt/login/"
    # postUrl = "http://njupt.pocketuni.net/index.php?app=home&mod=space&act=index&uid=1642252"
    # postUrl = 'http://pocketuni.net/index.php?app=home&mod=Public&act=doLogin&school=njupt'
    # postUrl = "http://njupt.pocketuni.net/"
    # postUrl = "http://njupt.pocketuni.net/index.php?app=home&mod=User&act=countNew"
    # getUrl = "http://njupt.pocketuni.net/index.php?app=home&mod=space&act=index&uid=1642252"
    getUrl = "http://njupt.pocketuni.net/index.php?app=event&mod=Front&act=playerDetails&id=212818&pid=98359"
    loginUrl = "http://pocketuni.net/index.php?app=home&mod=Public&act=doLogin&school=njupt"
    # file_object = open('number.txt', 'rb')
    school = "南京邮电大学"
    sid = "592"
    number = "B14041305"
    password = "111111"
    login = "登 录"
    # __hash__ = "4c35cd4100e3c428946244cbc4c1423f"

    # login_data = {'email': email, 'password': password}  
    # try:
    # while True:
    #     number = file_object.read(9)
    __hash__ = getHash()
    #     if not number:
    #         break
    loginData = {'school':school, 'sid':sid, 'number':number, 'password':password, 'login':login, '__hash__':__hash__[0]}
    headers,cookies = create_session(loginUrl, getUrl, loginData)
        # print(session)
        # do_something_with(chunk)
    # finally:
    print(len(cookies))
    htmlSaved(headers)
    htmlSave1d(cookies)
    # file_object.close()

#driver.find_element_by_id("submit").click()
# driver.find_element_by_xpath("//div[@class='person_list_vote']")
# element = driver.find_element_by_id("passwd-id")  
#element = driver.find_element_by_name("passwd")  
#element = driver.find_element_by_xpath("//input[@id='passwd-id']")
#http://njupt.pocketuni.net/index.php?app=event&mod=Front&act=index&id=212818 活力团支部
# http://njupt.pocketuni.net/index.php?app=event&mod=Front&act=index&id=212818
# http://njupt.pocketuni.net/index.php?app=event&mod=Front&act=index&id=212818
# http://njupt.pocketuni.net/index.php?app=event&mod=Front&act=vote