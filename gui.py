import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

sg.theme('DarkBrown4')
header_font = ('Arial Bold', 20)

layout = [
    [sg.Text("Welcome to the BabyBot", size=(20, 1),
             key='-TEXT-', font=header_font)],
    [sg.Text("Enter email", size=(12, 1)), sg.InputText(key='-INPUT-')],
    [sg.Text("Enter password", size=(12, 1)), sg.InputText(
        key='-PASSWORD-', password_char='●')],
    [sg.Button("Run BabyScript", pad=(0, 15), font=header_font)], [
        sg.Button("Exit B-BabyBot", pad=(0, 0))],
    [sg.Image('babyimage.png', expand_x=True,
              expand_y=True, pad=(0, 15))],
    [sg.Text("made by: eir", pad=(0, 0))]
]

window = sg.Window("B-BabyBot", layout, margins=(200, 100),
                   element_justification='c')


def babyScript():
    bbaby_email = user_email
    bbaby_pass = user_pass

    service = Service(executable_path='D:\\B-BabyBot\\path\\chromedriver.exe')
    options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=service, options=options)

    url = 'https://www.blockbabies.world/play/login.php'
    driver.get(url)

    driver.find_element('name', 'email').send_keys(bbaby_email)
    driver.find_element('name', 'password').send_keys(bbaby_pass)
    driver.find_element(By.CLASS_NAME, 'button').click()

    time.sleep(5)
    driver.find_element(By.ID, 'sa-basic').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[12]/div/button[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body')
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[12]/div/button[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[12]/div/button[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[12]/div/button[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[12]/div/button[1]').click()

    time.sleep(20)


while True:
    event, values = window.read()

    if event == "Run BabyScript":
        user_email = values['-INPUT-']
        user_pass = values['-PASSWORD-']
        sg.popup(f'... Initiating babyscript')
        print(user_email, user_pass)
        babyScript()
    else:
        break
