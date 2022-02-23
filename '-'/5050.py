import os
import random
from plyer import notification

def notifyMe(title, message, app_icon = r"ico.ico", timeout = 5): 
    notification.notify(title , message , app_icon = r"ico.ico", timeout = 5)
    
kek = random.randint(1, 100)
print(kek)
if kek > 49:
    print("Coroa")
    notifyMe("Coroa", "Coroa!")
if kek < 51:
    print("Cara")
    notifyMe("Cara", "Cara!")
os.system("pause")
