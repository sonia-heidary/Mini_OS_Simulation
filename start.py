import os
import sys
import subprocess
import importlib.util
from default_commands import basic_command
from my_commands import json_commands
import user_management
import process_manegment 


def main():
    # installing the programs
    install_system_apps()

    # get the host name
    try:
        with open("hostname.json", "r") as file:
            hostname = file.read().splitlines()
            hostname = hostname[0]
    except Exception as e:
        print(f"An error occurred: {e}")
    

    title = "MINI OS SONIA"
    sys.stdout.write(f"\x1b]2;{title}\x07")
    sys.stdout.flush()
    
    os.system('clear')
    
    # Welcome Message
    print("Welcome to Sonia's mini os")
    print("-------------------------------------\n")

    username = login()
    
    while True:

        # Get current working directory
        wd = os.getcwd()
        
        # Construct the prompt: $username@hostname:$wd
        prompt = f"{username}@{hostname}:{wd}$ "
        
        try:
            # The place where you write commands
            cmd = input(prompt)
            # Command Handling
            if cmd == "exit":
                print("Shutting down SONIA...")
                break
            if cmd == "restart":
                print("restarting down SONIA...")
                return main()
            
            elif cmd.strip() == "":
                continue

            elif cmd == "snake":
                print("Launching Snake...")
                # 'freegames' uses a different execution style. 
                # Usually, it's called as a module directly:
                subprocess.run([sys.executable, "-m", "freegames", "play", "snake"])

            elif cmd == "pacman":
                print("Launching Pacman...")
                # For many pip minesweeper clones, the module is just 'minesweeper'
                # but ensure it was installed correctly in the previous step.
                subprocess.run([sys.executable, "-m", "freegames", "play", "pacman"])


            else:
                b_command  = basic_command(cmd)
                if b_command.command_found:
                    if b_command.syntax_error:
                        print(f"An error occurred: {e}")
                else:
                    j_command = json_commands(cmd, username)
                    if j_command.command_found:
                        if j_command.syntax_error:
                            print(f"An error occurred: {e}")
                    else:
                        process = process_manegment.process(cmd)
                        if process.command_found:
                            if process.syntax_error:
                                print(f"An error occurred: {e}")

                
        except Exception as e:
            print(f"An error occurred: {e}")

def login():
    try:
        
        users = user_management.users()

        # prints out all the usernames so the user can choose their acount
        for i in range(0, len(users[0])):
            print(f"{i+1}) {users[0][i]}")
        
        while True:
            acount = input("choose an acount to log in: ")

            # checks the validity of 
            while True:
                if acount.isnumeric():
                    acount = int(acount)
                    if acount > len(users[0]):
                        acount = input("choose a valid acount to log in: ")
                    else:
                        break
                else:
                    acount = input("choose a valid acount to log in: ")

            userpassword = input("enter your password: ")
            if userpassword == users[1][acount - 1]:
                return users[0][acount - 1]
            else:
                print("incorrect password")


    except Exception as e:
        print(f"An error occurred: {e}")     


def install_system_apps():
    # List of official SONIA OS apps
    apps = ["freegames", "minesweeper"]
    
    # This identifies the 'site-packages' folder inside os_env
    # It ensures we are installing exactly where the venv expects them
    venv_site_packages = next(p for p in sys.path if 'site-packages' in p)

    print(f"SONIA System: Internalizing environment at {sys.prefix}...")
    
    for app in apps:
        spec = importlib.util.find_spec(app)
        
        if spec is None:
            print(f"[INSTALLING] Adding {app} to OS Virtual Layers...")
            try:
                # We use --target to force it into the venv's specific folder
                subprocess.check_call([
                    sys.executable, "-m", "pip", 
                    "install", app, 
                    "--target", venv_site_packages,
                    "-q"
                ])
                
                # Refresh the path so the script 'sees' the new files immediately
                site.addsitedir(venv_site_packages)
                print(f"[OK] {app} is now part of the system.")
                
            except subprocess.CalledProcessError:
                print(f"[ERROR] Could not reach SONIA servers to install {app}.")
        else:
            print(f"[INFO] {app} verified in local storage.")


if __name__ == "__main__":
    main()