def loading_bar(num1):
    if num1 == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    return f"{number}% [{'%' * (num1 // 10)}{'.' * (10 - (num1 // 10))}]\nStill loading..."


number = int(input())

print(loading_bar(number))
