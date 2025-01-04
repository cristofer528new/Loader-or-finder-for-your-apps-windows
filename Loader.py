import os
import subprocess
import time

print("Loader of apps")
print("please select any app to run")
print("1. explorer.exe") #if you want, you can change the name of the app or add another app
print("2. notepad.exe")
print("3. cmd.exe")
print("4. Find you app.exe")
print("5. exit")
print("Enter your choice: ")
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
        app_name = input("Enter the name of the .exe file you want to find (e.g., app.exe): ")
        apps = find_apps(app_name)
elif choice == '5':
    print("Exiting...")
    time.sleep(1)
    exit()
else:
    print("Invalid choice")
    time.sleep(1)
    exit()

if apps:
    print("Multiple instances found. Please select one to run:")
    for idx, app in enumerate(apps):
        print(f"{idx + 1}. {app}")
    app_choice = int(input("Enter your choice: ")) - 1
    if 0 <= app_choice < len(apps):
        subprocess.run(apps[app_choice], shell=True)
    else:
        print("Invalid selection")
else:
    print("No app found")
