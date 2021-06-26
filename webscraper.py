from selenium import webdriver
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 
import nltk
import random
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


data=[]
final =[]

fileObj = open("negative-words.txt", "r") #opens the file in read mode
negative = fileObj.read().splitlines() #puts the file into an array
fileObj.close()

with Chrome(executable_path=r"/usr/local/bin/chromedriver") as driver:
    wait = WebDriverWait(driver,5)
    driver.get("https://youtu.be/TMrtLsQbaok")

    for item in range(3): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(5)

        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
            data.append(comment.text)

with open('comments.txt', 'w') as f:
    for x in data:
        f.write(x)
        f.write('\n')

for comment in data:

    counter = 0
    # array to store key words
    found = []
    for word in negative:

        # incrementer counter by 1 if key word found in comment
        if word in comment:
            counter += 1
            found.append(word)

            # append domain and key words to result if 2 or more key words found
    if counter >= 10:
        final.append((comment))

for x in final:
    print( x + '\n')
