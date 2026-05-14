import subprocess
import os
import sys


class basic_command:
    def __init__(self, command: str): 

        self.command = command
        self.syntax_error = False
        self.command_found = True


        self.command = command.strip()
        self.command = command.split()


        if (self.command[0] == "rm"):
            if (len(self.command) == 2):
                self.rm(self.command[1])
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "mv"):
            if (len(self.command) == 3):
                self.mv(self.command[1], self.command[2])
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "mkdir"):
            if (len(self.command) == 2):
                self.mkdir(self.command[1])
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "echo"):
            if (len(self.command) == 2):
                self.echo(self.command[1])
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "cat"):
            if (len(self.command) == 2):
                self.cat(self.command[1])
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "cd"):
            if (len(self.command) == 2):
                self.cd(self.command[1])
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "tar"):
            if (len(self.command) == 4):
                self.tar(self.command[1], self.command[2], self.command[3])
                return
            if (len(self.command) == 3):
                self.tar(self.command[1], self.command[2])
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "find"):
            if (len(self.command) == 3):
                self.find(self.command[1], self.command[2])
                return
            if (len(self.command) == 2):
                self.find(self.command[1])
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "grep"):
            if (len(self.command) == 3):
                self.grep(self.command[1], self.command[2])
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "ls"):
            if (len(self.command) == 2):
                self.ls(self.command[1])
                return
            if (len(self.command) == 1):
                self.ls()
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "chmod"):
            if (len(self.command) == 3):
                self.chmod(self.command[1], self.command[2])
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "wc"):
            if (len(self.command) == 3):
                self.wc(self.command[1], self.command[2])
                return
            if (len(self.command) == 2):
                self.wc(self.command[1])
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "pip"):
            if (len(self.command) == 3):
                self.pip(self.command[1], self.command[2])
                return
            if (len(self.command) == 2):
                self.pip(self.command[1])
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "apt-get"):
            if (len(self.command) == 3):
                self.apt(self.command[1], self.command[2])
                return
            if (len(self.command) == 2):
                self.apt(self.command[1])
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "dpkg"):
            if (len(self.command) == 3):
                self.dpkg(self.command[1], self.command[2])
                return
            if (len(self.command) == 2):
                self.dpkg(self.command[1])
                return
            else:
                self.syntax_error = True

        else:
            self.command_found = False


    def rm(self, target_path):
        try:
            # you should give the compelete path
            # ['rm', 'path/to/file']
            result = subprocess.run(
                ['rm', target_path], 
                check=True, 
                capture_output=True, 
                text=True
            )
            print(f"Successfully removed: {target_path}")
        
        except Exception as e:
            print(f"An error occurred: {e}")


    def mv(self, source, destination):
        try:
            # ['mv', 'source_path', 'dest_path']
            result = subprocess.run(
                ['mv', source, destination], 
                check=True, 
                capture_output=True, 
                text=True
            )
            print(f"Successfully moved {source} to {destination}")
        
        except Exception as e:
            print(f"An error occurred: {e}")


    def mkdir(self, dir_name):
        try:
            # ['mkdir', 'folder_name']
            result = subprocess.run(
                ['mkdir', dir_name], 
                check=True, 
                capture_output=True, 
                text=True
            )
            print(f"Directory '{dir_name}' created successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")


    def echo(self, text_to_print):
        try:
            # ['echo', 'Hello World']
            result = subprocess.run(
                ['echo', text_to_print],
                check=True,
                capture_output=True,
                text=True
            )
            # result.stdout will contain the text plus a newline character
            print(result.stdout.strip())

        except Exception as e:
            print(f"An error occurred: {e}")


    def cat(self, file_path):
        try:
            # ['cat', 'filename.txt']
            result = subprocess.run(
                ['cat', file_path],
                check=True,
                capture_output=True,
                text=True
            )
            # The content of the file is stored in result.stdout
            print(result.stdout)

        except Exception as e:
            print(f"An error occurred: {e}")


    def cd(self, path):
        try:
            # We don't use subprocess here!
            # os.chdir stands for "change directory"
            os.chdir(path)
            
            # Print the new location to confirm it worked
            print(f"Moved to: {os.getcwd()}")
            
        except Exception as e:
            print(f"An error occurred: {e}")


    def tar(self, action, archive_name, target=None):
        try:
            # Construct the command based on the action
            # c = create, x = extract, t = list (table of contents)
            # f = file (specifies the archive name)
            # v = verbose (optional: shows progress)
            
            if action == "create":
                # Command: tar -cvf archive.tar file_or_folder
                cmd = ['tar', '-cvf', archive_name, target]
            elif action == "extract":
                # Command: tar -xvf archive.tar
                cmd = ['tar', '-xvf', archive_name]
            elif action == "list":
                # Command: tar -tvf archive.tar
                cmd = ['tar', '-tvf', archive_name]
            else:
                print("Unknown tar action")
                return

            result = subprocess.run(
                cmd,
                check=True,
                capture_output=True,
                text=True
            )
            print(result.stdout)

        except Exception as e:
            print(f"An error occurred: {e}")


    def find(self, search_path, filename=None):
        try:
            # -name: looks for a specific filename
            # search_path: where to start (e.g., "." for current folder)
            if not filename:
                filename = search_path
                search_path = "."

            result = subprocess.run(
                ['find', search_path, '-name', filename],
                check=True,
                capture_output=True,
                text=True
            )
            
            output = result.stdout.strip()
            
            if output:
                print(f"Results found:\n{output}")
            else:
                print("No matches found.")

        except Exception as e:
            print(f"An error occurred: {e}")


    def grep(self, pattern, file_path):
        try:
            # -n: Show line numbers
            # -i: Case-insensitive search
            # pattern: The text you are looking for
            # file_path: The file to search in
            result = subprocess.run(
                ['grep', '-ni', pattern, file_path],
                check=True,
                capture_output=True,
                text=True
            )
            
            if result.stdout:
                print(f"Matches in {file_path}:\n{result.stdout.strip()}")
            
        except Exception as e:
            print(f"An error occurred: {e}")


    def ls(self, path="."):
        try:
            # -l: long format (permissions, size, etc.)
            # -a: show hidden files (those starting with .)
            # -h: human-readable file sizes
            result = subprocess.run(
                ['ls', '-lah', path],
                check=True,
                capture_output=True,
                text=True
            )
            print(result.stdout)

        except Exception as e:
            print(f"An error occurred: {e}")


    def chmod(self, mode, path):
        try:
            # Command: chmod 755 myfile.py
            # or: chmod +x myscript.sh
            result = subprocess.run(
                ['chmod', mode, path],
                check=True,
                capture_output=True,
                text=True
            )
            print(f"Permissions for '{path}' changed to {mode}.")

        except Exception as e:
            print(f"An error occurred: {e}")


    def wc(self, file_path, option=None):
        try:
            # Build the command. 
            # Options: -l (lines), -w (words), -c (bytes/chars)
            cmd = ['wc']
            if option:
                cmd.append(option)
            cmd.append(file_path)

            result = subprocess.run(
                cmd,
                check=True,
                capture_output=True,
                text=True
            )
            
            # Output usually looks like: " 10  50 300 filename.txt"
            print(result.stdout.strip())

        except Exception as e:
            print(f"An error occurred: {e}")


    def pip(self, action, package_name=None):
        try:
            # sys.executable points to the current python path
            # Command: python -m pip install requests
            cmd = [sys.executable, '-m', 'pip', action]
            
            if package_name:
                cmd.append(package_name)

            result = subprocess.run(
                cmd,
                check=True,
                capture_output=True,
                text=True
            )
            print(result.stdout)

        except Exception as e:
            print(f"An error occurred: {e}")


    def apt(self, action, package_name=None):
        try:
            # 'sudo': Run with admin privileges
            # '-y': Auto-confirm prompts
            cmd = ['sudo', 'apt-get', action, '-y']
            
            if package_name:
                cmd.append(package_name)

            print(f"Executing: {' '.join(cmd)}...")
            
            result = subprocess.run(
                cmd,
                check=True,
                capture_output=True,
                text=True
            )
            print(result.stdout)

        except Exception as e:
            print(f"An error occurred: {e}")


    def dpkg(self, action, target=None):
        try:
            # Action mappings: 
            # "install" -> -i, "remove" -> -r, "list" -> -l, "status" -> -s
            action_map = {
                "install": "-i",
                "remove": "-r",
                "list": "-l",
                "status": "-s"
            }
            
            flag = action_map.get(action)
            if not flag:
                print(f"Unknown dpkg action: {action}")
                return

            # Build the command: sudo dpkg -i package.deb
            cmd = ['sudo', 'dpkg', flag]
            if target:
                cmd.append(target)

            result = subprocess.run(
                cmd,
                check=True,
                capture_output=True,
                text=True
            )
            print(result.stdout)

        except Exception as e:
            print(f"An error occurred: {e}")
