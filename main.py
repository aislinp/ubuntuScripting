import random
import string
import os


def passwordgen():
    password_length = 20

    characters = string.ascii_letters + string.digits

    password = ""

    for index in range(password_length):
        password = password + random.choice(characters)

    return password

def paswdenforcer():
    os.system("sudo apt-get install libpam-cracklib")
    os.system("sudo gedit /etc/login.defs")
    os.system("sudo gedit /etc/pam.d/common-password")


if __name__ == '__main__':
    filepath = "users.txt"
    with open(filepath) as fp:
        lines = fp.read().splitlines()
    with open(filepath, "w") as fp:
        for line in lines:
            if '#' not in line:
                print(line + ":" + passwordgen(), file=fp)

    print("open up the users.txt file, are you ready to change their passwords? Y/N:")
    run = input()
    if run.lower() == 'y':
        os.system("sudo chpasswd < users.txt")
    else:
        exit()
