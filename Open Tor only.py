#coding:utf-8

import time
import os
import webbrowser
import platform
from selenium import webdriver
import rand2
import pyautogui




user_OS = platform.system()
#firefox_path any os
firefox_path_windows = 'C:/Users/Ali/Desktop/Tor Browser/Browser/firefox.exe %s'  
firefox_path_linux = '/usr/bin/Tor Browser/Browser/firefox %s'                    
firefox_path_mac = 'open -a /Applications/Google\ Chrome.app %s'                  

#chrome_path any os
chrome_path_windows = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
chrome_path_linux = '/usr/bin/google-chrome %s'
chrome_path_mac = 'open -a /Applications/Google\ Chrome.app %s'

#tor_path_windows any os
#G:\OneDrive\Documents\Tor Browser
tor_path_windows = 'C:/Users/Othman/Desktop/Tor Browser/Browser/firefox.exe %s'
tor_path_linux = '/usr/bin/Tor Browser/Browser/firefox %s'
tor_path_mac = 'open -a /Applications/Google\ Chrome.app %s'
tor_path = ''


game_site_link = 'http://www.fb.com'


if user_OS == 'Windows':
    browser_path = tor_path_windows
elif user_OS == 'Linux':
    browser_path = tor_path_linux
elif user_OS == 'Darwin':
    browser_path = tor_path_mac
elif user_OS == 'Java':
    browser_path = tor_path_mac
else:
    webbrowser.open_new_tab(game_site_link)
    

webbrowser.get(browser_path).open_new_tab(game_site_link)
time.sleep(35)  # الانتظار لين تحميل الصفحه 

# pyautogui.hotkey('Ctrl', 't')               # فتح تاب جديد
# pyautogui.hotkey('Ctrl', 'W')               # Close Tab	
# pyautogui.hotkey('Ctrl', 'F4')              # Close Tab	
# pyautogui.hotkey('Ctrl', 'N')               # New Window
# pyautogui.hotkey('Backspace')               # Backspace
# pyautogui.hotkey('F5')                      #Reload
# pyautogui.hotkey('Ctrl', 'F5')              #Reload (override cache)
# pyautogui.hotkey('Esc')                     #Esc
# pyautogui.hotkey('Ctrl', 'F5')              #Reload (override cache)
#webbrowser.quit()   # اغلاق المتصفح 


os.system("TASKKILL /F /IM firefox.exe") #ايقاف متصفح فير فوكس  
print ("#" * 50)
