
from selenium import webdriver
import os
#import pyautogui

PATH="C:\Program Files (x86)\chromedriver.exe" # Define the path of the Chrome driver
driver=webdriver.Chrome(PATH) # Select the webDriver
url=driver.get("https://www.nytimes.com/search?dropmab=false&query=shcool%20shooting&sort=best") #Enter the site Nytimes
string1 = "Shooting" #The word that i want to find 
num = 0 # Number of line in arcticle
index = 0 #Index of the line exsample: line 1 == [0]
Shoot=driver.find_element_by_class_name("css-46b038") # The class name of the arcticles

os.system('cls') #Clear the console
file=open('Information.txt', 'w+') # open/create the file and write to the file
file.write(Shoot.text) #Write the arcticles to the file
file.close() #Close the file
file1 = open('Information.txt', 'r') #Open the file again 
input('press any key to continue: ') # To make sure that it won't read the lines if there is no lines
for word in file1: #loop of all the lines in the file
    index += 1 #increase the index of the line
    num += 1 #Count the number of the line
    if string1 in word:
        print("I Found the word",string1, "In line",num) #prints
        
file1.close() #close the file
input()
