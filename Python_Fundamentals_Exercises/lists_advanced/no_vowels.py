word = input()
vowels = ['a', 'o', 'u', 'e', 'i']

result = [x for x in word if x.lower() not in vowels]

print(*result, sep="")
