def palindromes(word):
    palindrome_list = []
    for current_word in word:
        if current_word == current_word[::-1]:
            palindrome_list.append(current_word)

    return palindrome_list


words = input().split(" ")
palindrome_word = input()

print(palindromes(words))
palindrome_counter = palindromes(words).count(palindrome_word)
print(f'Found palindrome {palindrome_counter} times')
