from rich import print
from _subprocess import system
import os
import re

_currentDir = "C:/"

while True:
    # take inpute
    inpute = input( _currentDir + ">")
    # tokenize the inpute
    command = re.findall("[\w']+", inpute)
    # print(command)

    if "exit" in inpute:
        print("Exited with code 0")
        break
    elif "ls" in inpute:
        system.ls()


    # print(output)
    # clear the inpute
    inpute = ""
