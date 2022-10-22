first_string = input()
second_string = input()

for i in range(len(first_string)):
    left_part = second_string[:i+1]
    right_part = first_string[i+1:]

    mutated_string = left_part + right_part
    if mutated_string == first_string:
        continue
    print(mutated_string)
    first_string = mutated_string