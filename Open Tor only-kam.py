#coding:utf-8
import time
import os
import webbrowser
import platform
import rand2
user_OS = platform.system()

# firefox_path any os
# firefox_path_windows = 'C:/Users/Ali/Desktop/Tor Browser/Browser/firefox.exe %s'  
# firefox_path_linux = '/usr/bin/Tor Browser/Browser/firefox %s'                    
# firefox_path_mac = 'open -a /Applications/Google/ Chrome.app %s'                  
# chrome_path any os
# chrome_path_windows = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# chrome_path_linux = '/usr/bin/google-chrome %s'
# chrome_path_mac = 'open -a /Applications/Google/ Chrome.app %s'
#tor_path_windows any os
tor_path_windows = 'G:/OneDrive/Documents/Tor Browser/Browser/firefox.exe %s'
#tor_path_linux = '/usr/bin/Tor Browser/Browser/firefox %s'
#tor_path_mac = 'open -a /Applications/Google/ Chrome.app %s'
#tor_path = ''
game_site_link = 'https://www.fb.com'
if user_OS == 'Windows':
    browser_path = tor_path_windows
# elif user_OS == 'Linux':
#     browser_path = tor_path_linux
# elif user_OS == 'Darwin':
#     browser_path = tor_path_mac
# elif user_OS == 'Java':
#     browser_path = tor_path_mac
# else:
#     webbrowser.open_new_tab(game_site_link)
webbrowser.get(browser_path).open_new_tab(game_site_link)
webbrowser.get('https://www.quora.com/How-do-I-open-a-URL-in-Google-Chrome-in-new-tab-using-Python')
webbrowser.get('https://www.quora.com/')
time.sleep(40)
os.system("TASKKILL /F /IM firefox.exe")



#send_keys(Keys.ALT, Keys.TAB)

#.......................
#
#
#
#
#
#......................

