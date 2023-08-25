# I
#
# def received_grade(grade):   # => "grade1" - променливата и "grade" във функцията са различни
#     if 2 <= grade < 3:
#         print("Fail")
#     elif 3 <= grade < 3.50:
#         print("Poor")
#     elif 3.50 <= grade < 4.50:
#         print("Good")
#     elif 4.50 <= grade < 5.50:
#         print("Very Good")
#     else:
#         print("Excellent")
#
#
# grade1 = float(input()) # => тъй като подаваме само едни данни, функцията взима тези данни, без значение от името им
# received_grade(grade1) # => трябва да извикаме функцията (все едно да използваме принт)
#
# II

grade_data = float(input())


def received_grade(grade):
    if 2 <= grade < 3:
        return"Fail"
    elif 3 <= grade < 3.50:
        return"Poor"
    elif 3.50 <= grade < 4.50:
        return"Good"
    elif 4.50 <= grade < 5.50:
        return"Very Good"
    else:
        return"Excellent"


print(received_grade(grade_data))
