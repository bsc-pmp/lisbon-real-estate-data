# import selenium since the website is in javascript
from selenium import webdriver
#to find element and click
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# webdriver to open in firefox, here we are using firefox
from webdriver_manager.firefox import GeckoDriverManager

# beautifulsoup to extract from html
from bs4 import BeautifulSoup
# import time to delay parts of the code
import time

# to create a csv file with data scraped
import csv

# to extract parts of string and numbers from data
import re

#create a pop up question input
import tkinter as tk
from tkinter import simpledialog

#create a folder
import os

# New directory
if not os.path.exists("C:\\LxReData"):
    new_dir = "LxReData"
    parent_dir = "C:\\"
    path = os.path.join(parent_dir, new_dir)
    os.mkdir(path)

#tkinter pop up questions
ROOT = tk.Tk()

ROOT.withdraw()

bairro_input = simpledialog.askstring(title="Test",
                                  prompt="Qual o Bairro?:")
bairro = bairro_input

time.sleep(5)

tipo_input = simpledialog.askstring(title="Test",
                                  prompt="Qual a tipologia? ex.: t1, t2, t3 ou t4:")
tipo = tipo_input

time.sleep(5)

#drivers for Firefox
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

i=1
def data(i):
    while (i<10):
        main_url = ("https://casa.sapo.pt/comprar-apartamentos/"+tipo+"/lisboa/?fs="+bairro+",%20lisboa&pn="+str(i))
        print (main_url)
        driver.get(main_url)
        time.sleep(5)

        src = driver.page_source
        soup = BeautifulSoup(src, 'lxml')

        url = soup.find ("a",{"class":"property-info"})
        print(url)
        if (url != None):
            # open a .csv file, write there and dont create newline
            with open( 'C:\\LxReData'+'\\csv'+bairro+tipo+str(i)+'.csv', 'w', newline="", encoding='UTF8') as f:
                writer = csv.writer(f)
                header = ['Property type', '\nLocation', '\nArea', '\nAsking price', '\nFeatures', '\nURL']
                writer.writerow(header)
                for items in soup.find_all(class_="property-info-content"):
                    # extract string from items in the class to variable
                    ptype = items.find('div', {'class': 'property-type'})
                    #convert to text
                    ptype = ptype.get_text().strip()
                    location = items.find('div', {'class': 'property-location'})
                    location = location.get_text().strip()
                    location = location.split(",")[0]
                    features = items.find('div', {'class': 'property-features'})
                    features = features.get_text().strip()
                    features = re.findall('[0-9]+', features)
                    features = ' '.join([str(elem) for elem in features])
                    # extract the price from items in the class
                    price = items.find('div', {'class': 'property-price'})
                    #convert to text
                    price = price.get_text().strip()
                    #extract only numbers of the price
                    price = re.findall('[0-9]+', price)
                    #List comprehension to convert list to string
                    price = ' '.join([str(elem) for elem in price])    
                    url = items.find ("a",{"class":"property-info"}).get("href")
                    #find tag inside especific div because span didn't had a class
                    g = items.find_all('div', {'class': 'property-features-tag'})
                    #if condition to confirm if I have data to insert in garagem variable
                    if (len(g) == 0):
                        garagem = "None"
                        data = [ptype, location, features, price, garagem, url]
                        writer.writerow(data)
                        continue
                    else:
                        for item in g:
                            garagem = item.find('span')
                            garagem = garagem.get_text().strip()

                            data = [ptype, location, features, price, garagem, url]
                            writer.writerow(data)
                            continue
                        continue
                    continue
                    f.close()

        else:
            print("it is the end")
            break

        #scroll down to end of page to go to next page
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        i=i+1

#calling the function
data (i)

driver.close()
driver.quit()
