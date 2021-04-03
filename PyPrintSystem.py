from sys import stdout
from os import linesep
from time import sleep

def doHeart(message, iterations = 1, delayTime = 0.1):
    for i in range(0, iterations):
        for i in range(90, 97):
            stdout.write("\r\033[0m[\033[" + str(i) + ";1m<3\033[0m] \033[0m" + message)
            stdout.flush()
            sleep(delayTime)
    stdout.write(linesep)
    return

def i(message, mode = 'i', verbose = False):
    if mode == 'v' and verbose: #VERBOSE
        return input("\033[90;1m" + message + "\033[0m")
    elif mode == 'e': #ERROR
        return input("\033[91;1m" + message + "\033[0m")
    elif mode == 's': #SUCCESS
        return input("\033[92;1m" + message + "\033[0m")
    elif mode == 'w': #WARNING
        return input("\033[93;1m" + message + "\033[0m")
    elif mode == 'i': #INFORMATION
        return input("\033[94;1m" + message + "\033[0m")
    else:
        return

def p(message, mode = 'i', verbose = False, prefix = "", suffix = linesep):
    if mode == 'v' and verbose: #VERBOSE
        stdout.write(prefix + "\033[0m[\033[90;1m#\033[0m] \033[90;2m" + message + "\033[0m" + suffix)
    elif mode == 'e': #ERROR
        stdout.write(prefix + "\033[0m[\033[91;1m-\033[0m] \033[0m" + message + "\033[0m" + suffix)
    elif mode == 's': #SUCCESS
        stdout.write(prefix + "\033[0m[\033[92;1m+\033[0m] \033[0m" + message + "\033[0m" + suffix)
    elif mode == 'w': #WARNING
        stdout.write(prefix + "\033[0m[\033[93;1m*\033[0m] \033[0m" + message + "\033[0m" + suffix)
    elif mode == 'i': #INFORMATION
        stdout.write(prefix + "\033[0m[\033[94;1m!\033[0m] \033[0m" + message + "\033[0m" + suffix)
    else:
        return
