import user_management

class json_commands:
    def __init__(self, command ,username):
        self.command = command
        self.username = username
        self.syntax_error = False
        self.command_found = True


        self.command = command.strip()
        self.command = command.split()

        if (self.command[0] == "hostname"):
            if (len(self.command) == 1):
                self.hostname()
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "passwd"):
            if (len(self.command) == 1):
                self.passwd()
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "groupadd"):
            if (len(self.command) == 2):
                self.groupadd(self.command[1])
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "useradd"):
            if (len(self.command) == 2):
                self.useradd(self.command[1])
                return
            else:
                self.syntax_error = True
        
        elif (self.command[0] == "userdel"):
            if (len(self.command) == 2):
                self.userdel(self.command[1])
                return
            else:
                self.syntax_error = True

        else:
            self.command_found = False


    def hostname(self):
        try:
            with open("hostname.json", "r") as file:
                hostname = file.read()
                print("your host name is " + hostname)
            return 
        except Exception as e:
            print(f"An error occurred: {e}")
    

    def passwd(self):       
        try:
            users = user_management.users()

            user_number = 0
            for i in range(0, len(users[0])):
                if users[0][i] == self.username:
                    current_pass = users[1][i]
                    user_number = i
                    break

            for i in range(0, 3):
                current_pass_check = input("enter your current password: ") 
                if current_pass == current_pass_check:
                    for j in range(0, 3):
                        new_pass = input("enter your new password: ")
                        new_pass_check = input("confirm your new password: ") 
                        if new_pass == new_pass_check:
                            users[1][user_number] = new_pass
                            with open("users.json", "w") as file:
                                for i in range(0, len(users[0])): 
                                    file.write(users[0][i])
                                    file.write("\n")
                            with open("passwords.json", "w") as file:
                                for i in range(0, len(users[0])): 
                                    file.write(users[1][i])
                                    file.write("\n")

                            print("password successfuly changed")
                            return
                        else:
                            print("passwords don't match. try again ...")
                    
                else:
                    print("password is wrong")
        except Exception as e:
            print(f"An error occurred: {e}")


    def groupadd(self, name: str):
        try:
            with open("groupname.json", "r") as file:
                groups = file.read().splitlines()
            
            if name in groups:
                print(f"group {name} already exists")
                return

            if (name.isdigit()) or (name[0] == "/") or (len(name) > 32):
                print("invalid group name")
                return
            
            for i in range(0, len(name)):
                if name[i].isdigit():
                    continue
                elif name[i].isalpha():
                    continue
                elif name[i] in ["_", "/"]:
                    continue
                if i == len(name):
                    if name[i]== "$":
                        continue
                
                print("invalid group name")
                return
            
            user_management.add_group(name)

            print(name + " was successfully created")

        except Exception as e:
            print(f"An error occurred: {e}")


    def useradd(self, name: str):
        try:
            users = user_management.users()
            for i in users[0]:
                if i == name:
                    print("user already exists")
                    return
                
            groups = user_management.groups()
            for i in groups:
                if i == name:
                    print("group already exists")
                    return
                
            user_management.add_user(name)
            user_management.add_group(name)

        except Exception as e:
            print(f"An error occurred: {e}")


    def userdel(self, name: str):
        try:
            if (self.username != "Sonia") or name == "Sonia":
                print("you don't have access")
                return
            users = user_management.users()
            for i in range(0, len(users[0])):
                if users[0][i] == name:
                    user_management.del_user(name, users, i)
                    return
            
            print("user doesn't exit")
            return
        
        except Exception as e:
            print(f"An error occurred: {e}")