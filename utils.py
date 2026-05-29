import os
import platform
import time
import sys


def clear_screen(t=0.8):
    time.sleep(t)
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")



def exit(n=6):
    clear_screen(0.5)
    print("Quitting program", end="", flush=True)

    for _ in range(n):
        time.sleep(0.3)
        print(".", end="", flush=True)

    clear_screen()
    print("Program quit successful!")
    sys.exit()