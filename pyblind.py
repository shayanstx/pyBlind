# imports
from secrets import choice
import pyfiglet, time, os, sys
from colorama import Fore
from scripts import tabledatabase, tablelike, tablelist, dbversion
from scripts import pySource

# Logo
pySource.opacity(1)
pySource.logo()

# Get Arguments
user_choise = sys.argv

# Error Handle
def Handle_Error(a):
    try:
        a.start(user_choise[2])
    except:
        pySource.pyError()

# Check Arguments
if len(user_choise) == 1:
    pySource.pyhelp()

# [-u] (url)
elif (user_choise[1] == '-u') or (user_choise[1] == '--url'):
    # [-V] (version)
    if user_choise[3] == '-V':
        Handle_Error(dbversion)

    # [-T] (Table)
    elif user_choise[3] == '-T':
        # [--db] (Database Method)
        if user_choise[4] == '--db':
            Handle_Error(tabledatabase)

        # [--like] (Like Method)
        if user_choise[4] == '--like':
            Handle_Error(tablelike)

        # [--list] (List Method)
        if user_choise[4] == '--list':
            Handle_Error(tablelist)

# Developer
elif user_choise[1] == '--developer':
    pySource.Developers()

# help
elif (user_choise[1] == '-h') or (user_choise[1] == '--help'):
    pySource.pyhelp()

else:
    time.sleep(2)
    sys.exit()