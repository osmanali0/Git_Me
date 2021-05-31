import time
import os
import webbrowser
import platform
import random

myFilelist= open("list_site_link.txt", "r")
site_link = list( myFilelist )
myFilelist.close()
# user_OS = platform.system()
#tor_path_windows = 'C:/Users/Othman/Desktop/Tor Browser/Browser/firefox.exe %s'
tor_path_linux = '/usr/bin/Tor Browser/Browser/firefox %s'
browser_path = tor_path_linux
for website in site_link:
  Duplicate = 0
  while Duplicate < 1 :
        time.sleep(13)
        webbrowser.get(browser_path).open_new_tab(website)
        time.sleep(25)
        #os.system("TASKKILL /F /IM firefox.exe")
        #webbrowser.open_new_tab(website)
        #time.sleep(12)
        Duplicate = Duplicate +1
        

# firefox_path any os
# firefox_path_windows = 'C:/Users/Ali/Desktop/Tor Browser/Browser/firefox.exe %s'  
# firefox_path_linux = '/usr/bin/Tor Browser/Browser/firefox %s'                    
# firefox_path_mac = 'open -a /Applications/Google\ Chrome.app %s'                  
# chrome_path any os
# chrome_path_windows = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# chrome_path_linux = '/usr/bin/google-chrome %s'
# chrome_path_mac = 'open -a /Applications/Google\ Chrome.app %s'
#tor_path_windows any os
# user_OS = platform.system()
#tor_path_windows = 'C:/Users/Ali/Desktop/Tor Browser/Browser/firefox.exe %s'
#tor_path_linux = '/usr/bin/Tor Browser/Browser/firefox %s'
#tor_path_mac = 'open -a /Applications/Google\ Chrome.app %s'
#tor_path = ''
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
# time.sleep(15)
# os.system("TASKKILL /F /IM firefox.exe")



#send_keys(Keys.ALT, Keys.TAB)

#.......................
#
#
#
#
#
#......................


