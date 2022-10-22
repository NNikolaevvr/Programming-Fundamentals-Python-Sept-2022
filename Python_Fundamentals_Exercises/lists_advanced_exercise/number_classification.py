def positive_numbers(numbers):
    return [x for x in numbers if (int(x)) >= 0]


def negative_numbers(numbers):
    return [x for x in numbers if (int(x)) < 0]


def even_numbers(numbers):
    return [x for x in numbers if (int(x)) % 2 == 0]


def odd_numbers(numbers):
    return [x for x in numbers if (int(x)) % 2 != 0]


list_of_numbers = input().split(", ")

print(f"Positive: {', '.join(positive_numbers(list_of_numbers))}")
print(f"Negative: {', '.join(negative_numbers(list_of_numbers))}")
print(f"Even: {', '.join(even_numbers(list_of_numbers))}")
print(f"Odd: {', '.join(odd_numbers(list_of_numbers))}")
