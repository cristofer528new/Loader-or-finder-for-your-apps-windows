import os
import subprocess
import time
from colorama import init, Fore, Style

# Initialize colorama
init()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.CYAN + "Loader or finder of apps" + Style.RESET_ALL)
print(Fore.GREEN + "1. explorer.exe" + Style.RESET_ALL) #if you want, you can change the name of the app or add another app
print(Fore.GREEN + "2. notepad.exe" + Style.RESET_ALL)
print(Fore.GREEN + "3. cmd.exe" + Style.RESET_ALL)
print(Fore.GREEN + "4. Find your app.exe" + Style.RESET_ALL)
print(Fore.RED + "5. exit" + Style.RESET_ALL)
print(Fore.CYAN + "Enter your choice: " + Style.RESET_ALL)
choice = input()

def find_apps(app_name=None):
    found_apps = []
    for root, dirs, files in os.walk("C:\\"):
        for file in files:
            if file.endswith(".exe") and (app_name is None or app_name == file):
                app_path = os.path.join(root, file)
                found_apps.append(app_path)
    return found_apps

apps = []
if choice == '1':
    apps = find_apps("explorer.exe") #in this list, you can add the name of the app you want to run
elif choice == '2':
    apps = find_apps("notepad.exe")
elif choice == '3':
    apps = find_apps("cmd.exe")
elif choice == '4':
    app_name = input(Fore.CYAN + "Enter the name of the .exe file you want to find (e.g., app.exe): " + Style.RESET_ALL)
    apps = find_apps(app_name)
elif choice == '5':
    print(Fore.RED + "Exiting..." + Style.RESET_ALL)
    time.sleep(1)
    exit()
else:
    print(Fore.RED + "Invalid choice" + Style.RESET_ALL)
    time.sleep(1)
    exit()

clear_console()

if apps:
    print(Fore.YELLOW + "Multiple instances found. Please select one to run:" + Style.RESET_ALL)
    for idx, app in enumerate(apps):
        print(Fore.GREEN + f"{idx + 1}. {app}" + Style.RESET_ALL)
    app_choice = int(input(Fore.CYAN + "Enter your choice: " + Style.RESET_ALL)) - 1
    if 0 <= app_choice < len(apps):
        subprocess.run(apps[app_choice], shell=True)
    else:
        print(Fore.RED + "Invalid selection" + Style.RESET_ALL)
else:
    print(Fore.RED + "No app found" + Style.RESET_ALL)
#i really hate making this