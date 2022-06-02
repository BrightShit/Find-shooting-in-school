
from selenium import webdriver
import os
#import pyautogui
Found = False
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
url=driver.get("https://www.nytimes.com/search?dropmab=false&query=shcool%20shooting&sort=best")
string1 = "Shooting"
num = 0
index = 0
Shoot=driver.find_element_by_class_name("css-46b038")

os.system('cls')
string1 = "Shooting"
index = 0
num = 0
file=open('Information.txt', 'w+')
file.write(Shoot.text)
for word in file:
    index += 1
    num += 1
    if string1 in word:
        print("I Found the word",string1, "In line",num)
        
file.close() #close the file
