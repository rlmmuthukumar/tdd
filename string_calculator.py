import re 
def add(numbers):
    if not numbers:
        return 0
    return None  # Placeholder for future steps

def add_number(numbers):
    if not numbers:
        return 0
    return int(numbers)

def add_comma_multiple(numbers):
    if not numbers:
        return 0
    num_list = map(int, numbers.split(","))
    return sum(num_list)

def add_newline(numbers):
    if not numbers:
        return 0
    numbers = numbers.replace("\n", ",")
    num_list = map(int, numbers.split(","))
    return sum(num_list)

def add_custom(numbers):
    if not numbers:
        return 0

    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split("\n", 1)
        numbers = numbers.replace(delimiter, ",")

    numbers = numbers.replace("\n", ",")
    num_list = map(int, numbers.split(","))
    return sum(num_list)

def add_negative(numbers):
    if not numbers:
        return 0

    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split("\n", 1)
        numbers = numbers.replace(delimiter, ",")

    numbers = numbers.replace("\n", ",")
    num_list = list(map(int, numbers.split(",")))

    negatives = [num for num in num_list if num < 0]
    if negatives:
        raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")

    return sum(num_list)
