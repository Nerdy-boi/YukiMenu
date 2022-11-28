import os

first_run = True
menuv = {}
menuv['1']="Pogfetch" 
menuv['2']="Apt Update"
menuv['3']="Pihole Update"
menuv['4']="Chronometer"
menuv['5']="Exit"
options=menuv.keys()
while(True):
    if first_run ==True:
        first_run = False
        pass
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
    for entry in options: 
        print(entry, menuv[entry])
    selection=input("Please Select:") 
    if selection =='1': 
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system("neofetch --ascii ${HOME}/.config/neofetch/logo.txt")
        input()
    elif selection == '2': 
        os.system("sudo apt update && apt upgrade")
    elif selection == '3': 
        os.system("pihole -up")
    elif selection == '4':
        os.system("pihole -c")
    elif selection == '5':
        exit()

    else: 
        print("Unknown Option Selected!")  
