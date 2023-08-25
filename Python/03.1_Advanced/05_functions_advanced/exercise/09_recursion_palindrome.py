def palindrome(word, index=0):
    result = ""
    if word == word[::-1]:
        result = f"{word} is a palindrome"
    else:
        result = f"{word} is not a palindrome"

    return result


# II
# def palindrome(word, index):
# 
#     if index == len(word) // 2:
#         return f"{word} is a palindrome"
#     if word[index] != word[-index-1]:
#         return f"{word} is not a palindrome"
#
#     return palindrome(word, index+1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))