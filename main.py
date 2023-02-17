import pyautogui
import time
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

KeyboardInterrupt_Text=color.BOLD+color.RED+color.UNDERLINE+"Stopped Clicking!"+color.END
error_text=color.BOLD+color.RED+color.UNDERLINE+"An error occured"+color.END
welcome_input=color.CYAN+color.BOLD+"Press Enter to start the AutoClicker"+color.END
welcome_text=color.BOLD+color.GREEN+color.UNDERLINE+"Welcome to KAutoClicker!"+color.END
Started_Text=color.BOLD+color.GREEN+"Started clicking..."+color.END
close_text_windows=color.BOLD+color.RED+color.UNDERLINE+"Press Ctrl+C to stop"+color.END
close_text_macOS=color.BOLD+color.RED+color.UNDERLINE+"Press Cmd+C to stop"+color.END

def main():
    try:
        clear()
        print(Started_Text)
        print(close_text_windows if os.name == 'nt' else close_text_macOS)
        while True:
            pyautogui.click(button='left')
            time.sleep(0)
    except KeyboardInterrupt:
        clear()
        print(KeyboardInterrupt_Text)
        exit()
    except:
        print(error_text)


try:
    print(welcome_text)
    choice = input(welcome_input)
    if choice == '':
        time.sleep(5)
        main()
except KeyboardInterrupt:
    clear()
    print(KeyboardInterrupt_Text)
    exit()