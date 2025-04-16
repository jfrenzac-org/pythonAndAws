"""Description:
You are given two lists: one with keys and the other with values.
Create a dictionary by pairing the elements of the two lists.

Concepts Covered: Lists, dictionaries, for loops, zip(), items()"""


def create_inventory(keys: list, values: list) -> dict:
    return dict(zip(keys, values))


if __name__ == "__main__":
    fruits = ["Apple", "Banana", "Kiwi"]
    quantity = [10, 5, 3]

    print(create_inventory(fruits, quantity))
