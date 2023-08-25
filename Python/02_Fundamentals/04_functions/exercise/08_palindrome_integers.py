def palindrome_integers(list_nums):

    for current_number in list_nums:
        if current_number[0::] == current_number[::-1]:
            print("True")
        else:
            print("False")


list_of_numbers = input().split(", ")
palindrome_integers(list_of_numbers)


