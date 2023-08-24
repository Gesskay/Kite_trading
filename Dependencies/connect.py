from kiteconnect import KiteConnect

from selenium import webdriver
import time
import os 

# cwd = os.chdir("/home/gesskay/Documents/trading/selenium")

def autologin():
    token_path="kite.txt"
    key_secret = open(token_path,'r').read().split()
    kite=KiteConnect(api_key=key_secret[0])
    
    service = webdriver.chrome.service.Service('/home/gesskay/Documents/trading/Dependencies/chromedriver')
    service.start()
    options = webdriver.ChromeOptions()
    # options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    # chrome_driver_binary = "/usr/local/bin/chromedriver"
    
    # options=options.to_capabilities()
    driver = webdriver.Remote(command_executor=service.service_url,options=options)
    driver.get(kite.login_url())
    driver.implicitly_wait(5)
    
    username = driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[1]/input')
    password = driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/input')
    
    username.send_keys(key_secret[2])
    password.send_keys(key_secret[3])
    
    driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[4]/button').click()
    
    pin = driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/div/input')
    pin.send_keys(key_secret[4])
    driver.find_element_by_xpath('xpath','/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[3]/button').click()
    
    time.sleep(15)
    
    request_token=driver.current_url.split('request_token=')[1].split('&action')[0]
    with open('request_token.txt', 'w') as the_file:
        the_file.write(request_token)
        
autologin()

#generating and storing access token - valid till 6 am the next day
request_token = open("request_token.txt",'r').read()
key_secret = open("kite.txt",'r').read().split()
kite = KiteConnect(api_key=key_secret[0])
data = kite.generate_session(request_token, api_secret=key_secret[1])
with open('access_token.txt', 'w') as file:
        file.write(data["access_token"])
