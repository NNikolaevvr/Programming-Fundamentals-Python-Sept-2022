def palindrome(num1):
    for i in num1:
        if i == i[::-1]:
            print(True)
        else:
            print(False)


numbers = input().split(", ")

palindrome(numbers)
