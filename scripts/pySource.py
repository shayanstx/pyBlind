from colorama import Fore
import os, pyautogui

# Logo & Clear
def logo():
    os.system('cls')
    print(Fore.RED+"""
 ██████╗ ██╗   ██╗██████╗ ██╗     ██╗███╗   ██╗██████╗ 
 ██╔══██╗╚██╗ ██╔╝██╔══██╗██║     ██║████╗  ██║██╔══██╗
 ██████╔╝ ╚████╔╝ ██████╔╝██║     ██║██╔██╗ ██║██║  ██║
 ██╔═══╝   ╚██╔╝  ██╔══██╗██║     ██║██║╚██╗██║██║  ██║
 ██║        ██║   ██████╔╝███████╗██║██║ ╚████║██████╔╝
 ╚═╝        ╚═╝   ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝ \n"""+Fore.RESET)


# Error
def pyError():
   print(Fore.YELLOW+"\n [ Wrning ] "+Fore.RESET+"Check the URL parameter :)")
   print(Fore.RED+"\n [ Error ]  "+Fore.RESET+"Check Your Internet Connection or Enter A Valid Tagret :)")


# Help Menue
def pyhelp():
    print(Fore.YELLOW+"\n [Usage] ",end=''+Fore.RESET)
    print("""pyblind.py -u target.com -levels --methods
    
 [Levels]

    Version -> [-V] : Find the site database version
    Tables -> [-T] : Find the site Tables
    Columns -> [-C] : Find the site Columns
    Password -> [-P] : Find the Users Passwords

 [Methods]

    Database -> [--db] : By testing the characters one by one
    Like -> [--like] : Using the similarity method
    List -> [--list] : By testing the members of the table list one by one

 Example:

     [$] pyblind.py -u target.com -T --db 

 [Developer Info] pyblind.py --developer
"""+Fore.RESET)

# Developers
def Developers():
   print(Fore.RED+" (pyBlind # Developer)\n"+Fore.RESET)

   print(Fore.LIGHTBLACK_EX+' [Developer]'+Fore.RESET+' SHAYAN STX')
   print(Fore.LIGHTBLACK_EX+' -----------')
   print(Fore.LIGHTBLACK_EX+' [Instagram]'+Fore.RESET+' SHAAYAAN.io')
   print(Fore.LIGHTBLACK_EX+' -----------')
   print(Fore.LIGHTBLACK_EX+' [ TWITTER ]'+Fore.RESET+' SHAAYAAN_io')
   print(Fore.LIGHTBLACK_EX+' -----------')
   print(Fore.LIGHTBLACK_EX+' [ Academy ]'+Fore.RESET+' SHEKARCHI.io\n')


# opacity
def opacity(opacity):
   for _ in range(15):
      pyautogui.hotkey("ctrl", "shift", "+")

   for _ in range(opacity):
      pyautogui.hotkey("ctrl", "shift", "-")