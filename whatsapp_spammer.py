from selenium import webdriver
import time


def whatsapp_bomber():
    driver = webdriver.Chrome(r'C:\Users\User\Desktop\chromedriver.exe') #locatie van chromedriver*******
    driver.get('https://web.whatsapp.com')
    name = input('Naar wie wil je het bericht sturen? : ')
    msg = input('Evul hier je bericht in : ')
    count = input('hoevaak moet het bericht gestuurd worden? : ')
    input('klik op een willekeurige toets, na het scannen van de QR code :')
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
