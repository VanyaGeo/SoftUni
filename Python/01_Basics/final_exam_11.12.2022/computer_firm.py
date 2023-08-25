number_computer = int(input())
final_sales = 0
real_sales = 0
final_rating = 0
average_rating = 0

for i in range (1, number_computer + 1):
    user_input = int(input())
    rating = user_input % 10
    possible_sales = user_input // 10
    if rating == 2:
        real_sales = possible_sales * 0
    if rating == 3:
        real_sales = possible_sales * 0.50
    if rating == 4:
        real_sales = possible_sales * 0.70
    if rating == 5:
        real_sales = possible_sales * 0.85
    if rating == 6:
        real_sales = possible_sales * 1
    final_sales = final_sales + real_sales
    final_rating = final_rating + rating
    average_rating = final_rating / number_computer

print(f"{final_sales:.2f}")
print(f"{average_rating:.2f}")
