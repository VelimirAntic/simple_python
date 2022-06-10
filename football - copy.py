# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 06:45:55 2022

@author: Luciano
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

USERNAME = 'username' # Your username lubovespa@gmail.com
PASSWORD = 'password' # Your password @lex3256
CHROMEDRIVER_PATH = 'C:\\Users\\Luciano\\chromedriver' # Insert the path of chromedriver (to be downloaded from "https://sites.google.com/a/chromium.org/chromedriver/downloads")

s = Service('C:/Users/.../chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())
 
driver.get('https://footystats.org/login');


time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('username')
search_box.send_keys(USERNAME)
search_box = driver.find_element_by_name('password')
search_box.send_keys(PASSWORD)

PATH = './chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com")

driver.find_element_by_id('register_account').submit()

time.sleep(5) # Let the user actually see something!

#2022
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6135');  # premier league - inglaterra
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6089');  # championship - inglaterra
driver.get('https://footystats.org/c-dl.php?type=matches&comp=7097'); # série a - brasil
driver.get('https://footystats.org/c-dl.php?type=matches&comp=7107'); # série b - brasil
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6211'); # la liga - espanha
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6120'); # la liga 2 - espanha
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6192'); # bundesliga - alemanha
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6020'); # bundesliga2 - alemanha
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6019'); # ligue 1 -frança
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6198'); # série a - itália
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6205'); # série b - itália
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6117'); # liga NOS - portugal
driver.get('https://footystats.org/c-dl.php?type=matches&comp=5951'); # eredivisie - holanda
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6969'); # MLS - estados unidos
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6079'); # pro league - bélgica
driver.get('https://footystats.org/c-dl.php?type=matches&comp=5992'); # premiership - escócia
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6008'); # bundesliga - áustria
driver.get('https://footystats.org/c-dl.php?type=matches&comp=5956'); # prva hnl - croácia
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6639'); # a league - austrália
driver.get('https://footystats.org/c-dl.php?type=matches&comp=7172'); # primera division - argentina
driver.get('https://footystats.org/c-dl.php?type=matches&comp=5977'); # champions league - europa
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6218'); # europa league - europa
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6050'); # conference league - europa
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6957'); # copa libertadores - américa do sul
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6958'); # copa sulamericana - américa do sul
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6905'); # categoria primera a - colômbia
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6038'); # liga mx - méxico
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6044'); # superleague - suiça
driver.get('https://footystats.org/c-dl.php?type=matches&comp=7166'); # primera division - venezuela
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6966'); # primera division - peru
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6960'); # primera division - paraguai
#-----------------------------------------------------------------------------------------------------------
#2021
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4759');  # premier league - inglaterra
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4912');  # championship - inglaterra
driver.get('https://footystats.org/c-dl.php?type=matches&comp=5713'); # série a - brasil
driver.get('https://footystats.org/c-dl.php?type=matches&comp=5721'); # série b - brasil
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4944'); # la liga - espanha
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4842'); # la liga 2 - espanha
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4673'); # bundesliga - alemanha
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4676'); # bundesliga2 - alemanha
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4505'); # ligue 1 -frança
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4889'); # série a - itália
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4972'); # série b - itália
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4885'); # liga NOS - portugal
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4746'); # eredivisie - holanda
driver.get('https://footystats.org/c-dl.php?type=matches&comp=5674'); # MLS - estados unidos
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4567'); # pro league - bélgica
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4478'); # premiership - escócia
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4861'); # bundesliga - áustria
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4660'); # prva hnl - croácia
driver.get('https://footystats.org/c-dl.php?type=matches&comp=5361'); # a league - austrália
driver.get('https://footystats.org/c-dl.php?type=matches&comp=5586'); # primera division - argentina
driver.get('https://footystats.org/c-dl.php?type=matches&comp=5220'); # primera division - argentina
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4655'); # champions league - europa
driver.get('https://footystats.org/c-dl.php?type=matches&comp=5640'); # copa libertadores - américa do sul
driver.get('https://footystats.org/c-dl.php?type=matches&comp=5639'); # copa sulamericana - américa do sul
driver.get('https://footystats.org/c-dl.php?type=matches&comp=5421'); # categoria primera a - colômbia
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4507'); # liga mx - méxico
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4906'); # superleague - suiça
driver.get('https://footystats.org/c-dl.php?type=matches&comp=5631'); # primera division - venezuela
driver.get('https://footystats.org/c-dl.php?type=matches&comp=5627'); # primera division - peru
driver.get('https://footystats.org/c-dl.php?type=matches&comp=5503'); # primera division - paraguai
#---------------------------------------------------------------------------------------------------------
#2020
driver.get('https://footystats.org/c-dl.php?type=matches&comp=3817'); # série a - brasil
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4565'); # série b - brasil
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4473'); # MLS - estados unidos
driver.get('https://footystats.org/c-dl.php?type=matches&comp=2366'); # primera division - argentina
driver.get('https://footystats.org/c-dl.php?type=matches&comp=3852'); # copa libertadores - américa do sul
driver.get('https://footystats.org/c-dl.php?type=matches&comp=3707'); # copa sulamericana - américa do sul
driver.get('https://footystats.org/c-dl.php?type=matches&comp=3638'); # categoria primera a - colômbia

time.sleep(5)


driver.quit()