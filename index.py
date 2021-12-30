import requests as re
from bs4 import BeautifulSoup as soup
url=""

def scrappost(url,data):
     return soup(re.post(url,data=data).text,'html.parser')
def scrap(url):
     return soup(re.get(url).text(),'html.parser')
re.session()
data={"username":"19bd1a0573","password":"resetme@1"}
sc=scrappost("http://kmitonline.com/login/index.php",data=data)
n=sc.find_all("h2",class_="course-date")
m=sc.find_all("a",class_="btn btn-primary btn-lg pull-right")
for i in range(len(n)):
    print(i,n[i].text)
url=m[int(input())]['href']



try:
     # url="http://kmitonline.com/mod/vpl/forms/edit.php?id=27324&userid=814"
     from selenium import webdriver
     from webdriver_manager.chrome import ChromeDriverManager
     from selenium.webdriver.common.keys import Keys
     # from selenium.webdriver.chrome.options import Options
     from selenium.webdriver import ActionChains
     import time
     # chrome_options=Options()
     # chrome_options.add_extension('C:\\Users\\bhanu\\Documents\\projects\\scrapping test\\paste.crx')
     driver=webdriver.Chrome(ChromeDriverManager().install())
     def login():
          driver.get("http://kmitonline.com/login/index.php")
          driver.find_element_by_name("username").send_keys("19bd1a0573")
          driver.find_element_by_name("password").send_keys("resetme@1")
          driver.find_element_by_id("loginbtn").click()
     # def setext():
     #      driver.get("chrome://extensions/?options=nkgllhigpcljnhoakjkgaieabnkmgdkb")
     def testopen(url):
          driver.get(url)
          act=ActionChains(driver)
          act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
          file=open('ans.txt','r')
          for line in file.readlines():
               act.send_keys(line).perform()
          print("clicking")
          # act.key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
          driver.find_element_by_id("vpl_ide_save").click()
     login()
     testopen(url)
except:
     print("error")
     time.sleep(5)
     driver.close()
input()
time.sleep(10)
driver.close()