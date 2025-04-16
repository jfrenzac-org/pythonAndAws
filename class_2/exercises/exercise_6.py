"""
Password Checker (While Loop + Input + Dictionary)

Task:
Create a dictionary with usernames as keys and passwords as values.
Ask the user to input their username and password.
Keep prompting until the user provides correct credentials.

"""

"""Goal: Use a while loop to keep checking user input
until the correct username and password are entered."""

# Your code here


def check_login(users: dict) -> str:
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if users.get(username) == password:
            break
        else:
            print("Either the username or the password are incorrect! Try again!")

    return "Login Successful!"


if __name__ == "__main__":
    users = {"alice": "1234", "bob": "qwerty", "carol": "pass"}
    print(check_login(users))
