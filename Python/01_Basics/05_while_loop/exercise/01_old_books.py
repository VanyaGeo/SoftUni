wanted_book = input()
book_name = input()
count_books = 0
is_found = False

while book_name != "No More Books":
    if book_name == wanted_book:
        is_found = True
        break
    count_books = count_books + 1
    book_name = input()

if is_found:
    print(f"You checked {count_books} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {count_books} books.")
