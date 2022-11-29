import os


clear_command = "cls" if os.name == "nt" else "clear"

#my custom neofetch config.
def pogfetch():
    os.system(clear_command)
    os.system("neofetch --ascii ${HOME}/.config/neofetch/logo.txt")
    input()


# Construct menu
menu = {
    "1": {
        "name": "Pogfetch",
        "func": pogfetch
    },
    "2": {
        "name": "Update packages",
        "func": lambda: os.system("sudo apt-get update && sudo apt-get upgrade")
    },
    "3": {
        "name": "Update Pihole",
        "func": lambda: os.system("pihole -up")
    },
    "4": {
        "name": "Chronometer",
        "func": lambda: os.system("pihole -c")
    },
    "5": {
        "name": "Bash",
        "func": lambda: (exit())
    },
}


# This can be folded into the body of the if below the function
def main():
    keep_running = True
    first_run = True
    while keep_running:
        # Clear the screen on first iteration
        if first_run:
            first_run = False

        else:
            os.system(clear_command)

        # Display menu
        for num, entry in menu.items():
            print(num, entry["name"])

        # Prompt user
        selection = input("Please select:")

        # Execute selection
        if menu_entry := menu.get(selection, None):
            menu_entry["func"]()

        else:
            print("Unknown option selected")

    # When the loop is done
    print("Exiting")


# Realistically optional, but good practice
if __name__ == "__main__":
    main()