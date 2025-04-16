"""Number List Builder (While Loop + List)
Task:
Ask the user to input numbers (as integers).
Add each number to a list.
Stop asking when the user types "done".
Then, print the list of numbers and their total sum."""

"""Goal: Use a while loop to collect input and store it in a list."""

# Your code here


def list_builder():
    numbers = []
    while True:
        number = input("Ingrese un número entero: ")
        if number == "done":
            break
        numbers.append(int(number))

    return f"The sum of all the given numbers is: {sum(numbers)}"


if __name__ == "__main__":
    print(list_builder())
