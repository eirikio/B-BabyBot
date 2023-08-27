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
    [sg.Text("Enter email:", size=(12, 1)), sg.InputText(key='-INPUT2-')],
    [sg.Text("Enter password:", size=(12, 1)), sg.InputText(
        key='-PASSWORD-', password_char='●')],
        [sg.FileBrowse(key="-INPUT1-"), sg.Text("Driver Path: ", size=(45, 1))],
    [sg.Button("Run BabyScript", pad=(0, 15), font=header_font)], [
        sg.Button("Exit BabyBot", pad=(0, 0))],
    [sg.Image('images/babyimage.png', expand_x=True,
              expand_y=True, pad=(0, 15))],
    [sg.Text("made by: 3ir", pad=(0, 0))]
]

window = sg.Window("B-BabyBot v2.0", icon="images/happybaby.ico", margins=(200, 100),
                   element_justification='c').Layout(layout)




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

        print("--Attempting to log in!--")

        sleep(10)
        
        print("--Login successful!")
        
        babyScript()

def babyScript():
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

        print("New quest in 1 hour! (⌐ ͡■ ͜ʖ ͡■)")
        sleep(800)
        driver.refresh()
        sleep(800)
        driver.refresh()
        sleep(800)
        driver.refresh()
        sleep(800)
        driver.refresh()
        sleep(800)
        driver.refresh()
        sleep(5)
        


while True:
    event, values = window.read()

    if event == "Run BabyScript":
        user_path = values['-INPUT1-']
        options = webdriver.ChromeOptions()
        service = Service(executable_path=user_path)
        driver = webdriver.Chrome(service=service, options=options)
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--ignore-certificate-errors-spki-list")
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('detach', True)
        url = 'https://www.blockbabies.world/play/login.php'
        driver.get(url)
        print(user_path)
        
        user_email = values['-INPUT2-']
        user_pass = values['-PASSWORD-']
        sg.popup(f'Prepare your setup before clicking Ok. Move the windows somewhere where they wont be in the way etc.... Initialize babyscript?')
        print("Logging in with e-mail: " + user_email)
        running = True
        login()
    if event == "Exit BabyBot":
        running = False
        break
