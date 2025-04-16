"""Description:
Write a program that takes a dictionary with numerical values and calculates
the average of those values. The dictionary keys are student names, and the values
 are their respective scores.

Concepts Covered: Dictionaries, for loops, values(), sum(), len(), print"""


def calculate_average(scores: dict) -> str:

    return f"The average score in the class is: {round(sum(scores.values()) / len(scores), 2)}"


if __name__ == "__main__":
    class_scores = {
        "Matthew": 30,
        "Jhon": 85,
        "Carl": 75,
        "Stephen": 100,
        "Sofia": 85,
        "Robert": 100,
        "Angela": 100,
    }

    print(calculate_average(class_scores))
