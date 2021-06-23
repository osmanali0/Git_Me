import time
import webbrowser
import pyautogui as pg

myFile= open("list_site_link.txt", "r")
list_site_link = list( myFile )
myFile.close()


tor_path_windows = 'C:/Users/Othman/Desktop/Tor Browser/Browser/firefox.exe'

for website in list_site_link:
  Duplicate = 0
  while Duplicate < 1 :
         time.sleep(5)
         webbrowser.tor_path_windows(website)
         #time.sleep(8)
         #pg.moveTo(907,35,)
         #pg.click()
         time.sleep(12)
         Duplicate = Duplicate +1
