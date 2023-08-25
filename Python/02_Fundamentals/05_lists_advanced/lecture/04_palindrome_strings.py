words = input().split()
palindrome = input()

palindrome_word_list = []
count_palindrome = 0

for palindrome_word in words:
    if palindrome_word[0::] == palindrome_word[::-1]:
        palindrome_word_list.append(palindrome_word)
    if palindrome_word == palindrome:
        count_palindrome += 1

print(palindrome_word_list)
print(f"Found palindrome {count_palindrome} times")