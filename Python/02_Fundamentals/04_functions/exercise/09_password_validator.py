def valid_password(string):
    password_is_valid = True
    if len(string) < 6 or len(string) > 10:
        print("Password must be between 6 and 10 characters")
        password_is_valid = False
    if not string.isalnum():
        password_is_valid = False
        print("Password must consist only of letters and digits")
    counter = 0
    for index in string:
        if index.isdigit():
            counter += 1
    if counter < 2:
        print("Password must have at least 2 digits")
        password_is_valid = False

    return password_is_valid


password = input()
password_validation = valid_password(password)
if password_validation is True:
    print("Password is valid")
