from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()

nav = webdriver.Chrome(ChromeDriverManager().install(), options=options)

nav.get('https://prenotami.esteri.it/')
# Login
input_email = WebDriverWait(nav, 30).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="login-email"]')))
input_email.click()
input_email.send_keys('joaopedro2144123@proton.me')

input_senha = WebDriverWait(nav, 30).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="login-password"]')))
input_senha.click()
input_senha.send_keys('#Mv854877852')

button_login = WebDriverWait(nav, 30).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="login-form"]/button')))
button_login.click()

click_reservar = WebDriverWait(nav, 30).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="advanced"]')))
click_reservar.click()

                          #Pop UP
pop_up = '/html/body/div[2]/div[2]/div/div/div/div/div/div/div'

while True:
    button_cidadania = WebDriverWait(nav, 60).until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="dataTableServices"]/tbody/tr[2]/td[4]/a/button')))
    button_cidadania.click()
    if(pop_up): 
       pop = WebDriverWait(nav,60).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button')))
       pop.click()
    else:
       button_cidadania = WebDriverWait(nav, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dataTableServices"]/tbody/tr[2]/td[4]/a/button')))
       button_cidadania.click()
       break
input('Deu tudo certo')

