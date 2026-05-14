def users():
    try:
        users = [[], []]
        with open("users.json", "r") as file:
            users[0] = file.read().splitlines()
        with open("passwords.json", "r") as file:
            users[1] = file.read().splitlines()

        return users
    
    except Exception as e:
            print(f"An error occurred: {e}")


def add_user(name):
    try:
        with open("users.json", "a") as file:
            file.write(name)
            file.write("\n")
        with open("passwords.json", "a") as file:
            file.write("0000")
            file.write("\n")

        return 
    
    except Exception as e:
            print(f"An error occurred: {e}")


def del_user(name: str, users: list, user_number: int):
    try:
        users[0].pop(user_number)
        users[1].pop(user_number)
        with open("users.json", "w") as file:
            for i in users[0]:
                 file.write(i)
                 file.write("\n")
        with open("passwords.json", "w") as file:
            for i in users[1]:
                 file.write(i)
                 file.write("\n")
        return 
    
    except Exception as e:
            print(f"An error occurred: {e}")


def groups():
    try:
        with open("groupname.json", "r") as file:
            groups = file.read().splitlines()
        return groups
    
    except Exception as e:
            print(f"An error occurred: {e}")


def add_group(name):
    try:
        with open("groupname.json", "a") as file:
            file.write(name)
            file.write("\n")

    except Exception as e:
            print(f"An error occurred: {e}")    