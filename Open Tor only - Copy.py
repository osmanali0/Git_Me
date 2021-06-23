import time   
import os                      
import webbrowser           
import platform                    
import rand2                        
import random                      
import selenium
from selenium import webdriver    


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os


  


#from webdriver_manager.firefox import GeckoDriverManager
#driver = webdriver.Firefox(executable_path='C:/Users/Ali/Downloads/Compressed/geckodriver.exe')

  
exitlist2=[30,33,45,54,45,42,40,51,39,42]
random.shuffle(exitlist2)
exit_time = (exitlist2[1])

#print (Watching_time)  المسؤله عن توقيت مشاهدة الموقع
Watching_time_list=[6,7,8,9,10,11,12,13,14,15] 
random.shuffle(Watching_time_list) 
Watching_time = (Watching_time_list[1])
# print (Watching_time)


# convert url from text file to list
myFilelist= open("list_site_link.txt", "r") # فتح ملف الروابط 
site_link = list( myFilelist )  # قراءه ملف الروابط وتحويل الملف الي قايمه 
myFilelist.close() # اغلاق الملف الروابط 


# user_OS = platform.system()

tor_path_windows = 'C:/Users/Ali/Desktop/Tor Browser/Browser/firefox.exe %s'
browser_path = tor_path_windows
#webbrowser.get(browser_path).open("")
webbrowser.get(browser_path).open_new(website) 
#for website in site_link:
  #Duplicate = 0
  #while Duplicate < 1 :
         #time.sleep(9)
         #webbrowser.get(browser_path).open_new_tab(website) 
         ##webbrowser.open_new_tab(website)
         #time.sleep(7)
         #Duplicate = Duplicate +1




#تحديد مكان برنامج الفيرفوكس في كل الانظمه
#firefox_path any os

#  firefox_path_windows = 'C:/Users/Ali/Desktop/Tor Browser/Browser/firefox.exe %s'  
#  firefox_path_linux = '/usr/bin/Tor Browser/Browser/firefox %s'                    
#  firefox_path_mac = 'open -a /Applications/Google\ Chrome.app %s'  

#تحديد مكان برنامج كروم في كل الانظمه            
# chrome_path any os
  
  # chrome_path_windows = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
  # chrome_path_linux = '/usr/bin/google-chrome %s'
  # chrome_path_mac = 'open -a /Applications/Google\ Chrome.app %s'

#تحديد مكان برنامج تور في كل الانظمه
#tor_path_windows any os

#  user_OS = platform.system()
#  tor_path_windows = 'C:/Users/Ali/Desktop/Tor Browser/Browser/firefox.exe %s'
#  tor_path_linux = '/usr/bin/Tor Browser/Browser/firefox %s'
#  tor_path_mac = 'open -a /Applications/Google\ Chrome.app %s'
#  tor_path = ''




#site_link = 'https://www.fb.com'
#if user_OS == 'Windows':
    #browser_path = tor_path_windows
# elif user_OS == 'Linux':
#     browser_path = tor_path_linux
# elif user_OS == 'Darwin':
#     browser_path = tor_path_mac
# elif user_OS == 'Java':
#     browser_path = tor_path_mac
# else:
#     webbrowser.open_new_tab(game_site_link)
# webbrowser.get(browser_path).open_new_tab(site_link)
time.sleep(15)

# اغلاق متصفح firefox
os.system("TASKKILL /F /IM firefox.exe")

#send_keys(Keys.ALT, Keys.TAB)