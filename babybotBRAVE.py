import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        [sg.FileBrowse(key="-INPUT3-"), sg.Text("Brave.exe Path: ", size=(45, 1))],
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
        print("-----------------------")
        baby_name = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]/section/div[4]/div/form/input')
        name = baby_name.get_attribute("value")
        print("Hi " + name)
        print("-----------------------")
        print("Your current skills are: ")
        
        dex = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[2]/ul/li[1]/h3').text
        app = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[2]/ul/li[2]/h3').text
        play = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[2]/ul/li[3]/h3').text
        kind = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[2]/ul/li[4]/h3').text
        pat = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[2]/ul/li[5]/h3').text
        pers = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[3]/ul/li[1]/h3').text
        intell = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[2]/ul/li[2]/h3').text
        obed = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[2]/ul/li[3]/h3').text
        sleep_skills = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[2]/ul/li[4]/h3').text
        ador = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[2]/ul/li[5]/h3').text
        print('Dexterity: ' + dex)
        print('Appetite: ' + app)
        print('Playfulness: ' + play)
        print('Kindness: ' + kind)
        print('Patience: ' + pat)
        print('Persuasion: ' + pers)
        print('Intelligence: ' + intell)
        print('Obedience: ' + obed)
        print('Sleep Skills: ' + sleep_skills)
        print('Adorability: ' + ador)
        
        babyScript()

def babyScript():
    while running:
        print("--Questing!--")
        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[2]/div[3]/button')).click()
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[2]/div[3]/button').click()
        sleep(3)
        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable(By.XPATH, '/html/body/div[12]/div/button[1]')).click()
        driver.find_element(By.XPATH, '/html/body/div[12]/div/button[1]').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[12]/div/button[1]').click()
        sleep(2)
        skill_gain = driver.find_element(By.XPATH, '/html/body/div[12]/div/div[6]/div/div/h2').text
        skill_tree = driver.find_element(By.XPATH, '/html/body/div[12]/div/div[6]/div/div/img').get_attribute('src')
        print(skill_tree + " gained ")
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[12]/div/button[1]').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[12]/div/button[1]').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[12]/div/button[1]').click()
        sleep(4)
        
        
        print("Gained: " + skill_gain)

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
        brave_path =values['-INPUT3-']
        option = webdriver.ChromeOptions()
        option.binary_location = brave_path
        service = Service(executable_path=user_path)
        driver = webdriver.Chrome(service=service, options=option)
        option.add_argument("--ignore-certificate-error")
        option.add_argument("--ignore-ssl-errors")
        option.add_argument("--ignore-certificate-errors-spki-list")
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        option.add_experimental_option('detach', True)
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
