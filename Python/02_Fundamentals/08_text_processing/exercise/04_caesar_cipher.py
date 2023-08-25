message = input()

encrypted_message = ""

for index in message:
    encrypted_message += chr(ord(index) + 3)

print(encrypted_message)

# One year has 365 days.