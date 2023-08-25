usernames = input().split(", ")
is_valid = True

for name in usernames:
    is_valid = True

    if not 3 <= len(name) <= 16:
        continue

    for char in name:
        if not (char.isalnum() or char == "_" or char == "-"):
            is_valid = False
            break
    if not is_valid:
        continue

    if is_valid:
        print(name)

# sh, too_long_username, !lleg@l ch@rs, jeffbutt