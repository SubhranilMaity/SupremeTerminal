import os
from rich import print



def ls():
    list = os.listdir(".")
    for i in list:
        if os.path.isdir(i):
            print("[green]"+ i, end = ' ')
        else:
            print(i)
    print("\n")
