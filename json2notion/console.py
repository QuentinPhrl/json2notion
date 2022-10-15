import os

os.system("")

class Style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def _formatted_print(left,right,error=False):
    color = Style.RED if error else Style.GREEN
    print(f"{color}{Style.BOLD}{left+' ':>12}{Style.RESET}{right}")
    

def print_error(message):
    print()
    _formatted_print("ERROR",message,error=True)
    print()

def print_status(status,message):
    print()
    _formatted_print(status,message)
    print()