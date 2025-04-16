"""Write a program that asks the user for a username and password.
Check if they match a predefined username and password,
then display whether the login was successful or not.
"""


def validate_login(username: str, password: str) -> str:
    valid_username = "user01"
    valid_password = "qwerty01"

    if username == valid_username and password == valid_password:
        return "Login Successful!"
    else:
        return "Either username or password are incorrect!"


if __name__ == "__main__":
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    print(validate_login(username, password))
