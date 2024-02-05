import pandas as pd
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

option = webdriver.ChromeOptions()
option.add_argument('start-maximized')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

dictionar = {'Nr. crt.': [],
            'Judet': []}

for i in range(10, 15):
    driver.get(f'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{str(i)}-decembrie-ora-13-00-2/')
    dictionar[f'1{str(i)}.12'] = []

    #First Page
    if i == 10:
