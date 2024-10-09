# Imports
import os
import requests

# Functions

# main handler (command prompts)
def subMain():
    startServer()
    main()

def main():
    prompt = str(input())
    if prompt == "start":
        startServer()
        main()
    elif prompt == "stop":
        closeServer()
        main()
    elif prompt == "restart" or prompt == "res":
        closeServer()
        startServer()
        main()
    elif prompt == "exit":
        closeServer()
        exit(1)
    elif prompt == "help" or prompt == "list":
        print("start -- start server\nstop -- stop server\nrestart/res -- restart server\nexit -- exit the program")
        main()
    else:
        print("type help for commands list.")
        main()


def startServer():
    os.system("start C:\PythonServer-Fozik.ru\PythonServer.bat")  # open file in directory with serverHandler.py
    main()


# close in system
def closeServer():
    os.system("taskkill /f /im Python.exe")

if __name__ == '__main__':
    subMain()