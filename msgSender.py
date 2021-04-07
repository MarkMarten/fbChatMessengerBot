from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import time
from fbchat import Client, log
from fbchat.models import *
options = webdriver.ChromeOptions()
#options.add_argument('headless')
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(options=options)

client=Client("username","password")
users = client.fetchAllUsers()
threads = client.fetchThreadList()

driver.get("https://www.kv.ee/?act=search.simple&last_deal_type=1&orderby=cdwl&deal_type=1&search_type=old")
kirjeldus=""
i=0
while(i!=30):
    print(i)
    i+=1
    time.sleep(1)
    if(i==29):
        driver.refresh()
        refreshedKirjeldus=driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[2]/h2/a").text
        if(kirjeldus!=refreshedKirjeldus):
            try:
                aeg=driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[5]/p/span").text
            except:
                aeg=""
            hind=driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[6]/p[1]").text
            tube=driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]").text
            link=driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[2]/h2/a").get_attribute("href")
            recentHouse=aeg+"\n"+hind+"\n"+tube+" tuba"+"\n"+kirjeldus+"\n"+link
            for user in users:
                if(user.name=="Marten Mark"):
                    client.send(Message(recentHouse),user.uid, ThreadType.USER)
            
            kirjeldus=refreshedKirjeldus
        i=0
    