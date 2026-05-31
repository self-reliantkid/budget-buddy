import os
import platform
import time
from datetime import datetime


def clear_screen(t=0.8):
    time.sleep(t)
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")



def get_current_date():
    date = datetime.now().strftime("%d-%m-%Y")
    return date



def num_count(info):
    new_num = 1

    if info:
        current_num = max(list(info))
        new_num = current_num + 1

    return new_num