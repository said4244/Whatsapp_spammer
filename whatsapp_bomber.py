from selenium import webdriver
import time


def whatsapp_bomber():
    driver = webdriver.Chrome(r'C:\Users\User\Desktop\chromedriver.exe') #locatie van chromedriver*******
    driver.get('https://web.whatsapp.com')
    name = input('Enter the name of user or group you want to send messages to : ')
    msg = input('Enter the message here : ')
    count = input('specify how many times you want to send the message : ')
    input('Enter anything after scanning the QR code')
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_class_name('_3uMse')
    count = int(count)
    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_1U1xa')
        button.click()
whatsapp_bomber()
time.sleep(3000)