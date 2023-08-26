import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

sg.theme('BrightColors')
header_font = ('Arial Bold', 20)

layout = [
    [sg.Text("Welcome to the BabyBot", size=(20, 1),
             key='-TEXT-', font=header_font)],
    [sg.Text("Enter email:", size=(12, 1)), sg.InputText(key='-INPUT-')],
    [sg.Text("Enter password:", size=(12, 1)), sg.InputText(
        key='-PASSWORD-', password_char='●')],
    [sg.Button("Run BabyScript", pad=(0, 15), font=header_font)], [
        sg.Button("Exit BabyBot", pad=(0, 0))],
    [sg.Image('babyimage.png', expand_x=True,
              expand_y=True, pad=(0, 15))],
    [sg.Text("made by: eir", pad=(0, 0))]
]

window = sg.Window("B-BabyBot", layout, margins=(200, 100),
                   element_justification='c')

service = Service(executable_path='D:\\B-BabyBot\\path\\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.blockbabies.world/play/login.php'
driver.get(url)

print("  ____        _           ____        _   ")
print(" |  _ \      | |         |  _ \      | |  ")
print(" | |_) | __ _| |__  _   _| |_) | ___ | |_ ")
print(" |  _ < / _` | '_ \| | | |  _ < / _ \| __|")
print(" | |_) | (_| | |_) | |_| | |_) | (_) | |_ ")
print(" |____/ \__,_|_.__/ \__, |____/ \___/ \__|")
print("                     __/ |                ")
print("                    |___/                 ")

def sleep(num):
    for i in range(num):
        print("\r: {} seconds.".format(num - i), end='')
        time.sleep(1)


def login():
    bbaby_email = user_email
    bbaby_pass = user_pass

    driver.find_element('name', 'email').send_keys(bbaby_email)
    driver.find_element('name', 'password').send_keys(bbaby_pass)
    driver.find_element(By.CLASS_NAME, 'button').click()

    print("--Login successful!--")

    sleep(10)
    babyClicker()


def babyClicker():
    while running:
        print("--Questing!--")
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[2]/div[3]/button').click()
        sleep(3)
        driver.find_element(By.XPATH, '/html/body/div[12]/div/button[1]').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[12]/div/button[1]').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[12]/div/button[1]').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[12]/div/button[1]').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[12]/div/button[1]').click()
        sleep(4)

        print("New quest in 1 hour. Counting down... Will refresh every 400 seconds to stay online")
        sleep(400)
        driver.refresh()
        sleep(400)
        driver.refresh()
        sleep(400)
        driver.refresh()
        sleep(400)
        driver.refresh()
        sleep(400)
        driver.refresh()
        sleep(400)
        driver.refresh()
        sleep(400)
        driver.refresh()
        sleep(400)
        driver.refresh()
        sleep(400)
        driver.refresh()
        sleep(400)
        driver.refresh()
        sleep(5)


    # try:
    #     element = driver.find_element(
    #         By.NAME, 'email')
    #     babyClicker()
    # except NoSuchElementException:
    #     time.sleep(5)
    #     login()
    #     time.sleep(5)


while True:
    event, values = window.read()

    if event == "Run BabyScript":
        user_email = values['-INPUT-']
        user_pass = values['-PASSWORD-']
        sg.popup(f'... Initiating babyscript')
        print("Logging in with e-mail: " + user_email)
        running = True
        login()
    if event == "Exit BabyBot":
        running = False
        break
