import re

sentence = input()
pattern = r"\s([a-z0-9]+([\.\-\_]?[a-z0-9]+)*@[a-z]+(\-[a-z]+)?\.[a-z]+(\.[a-z]+)*)\b"
matches = re.findall(pattern, sentence)

# print("\n".join([group[0] for group in matches])) #  това е еднакво със следващите редове

# тъй като имаме групи в регекса, трябва да отбележим коя група искаме да принтираме
# цялата голяма група с нужното съдържание на целият имейл е [0] група

for email in matches:
    print(email[0])


# Just send email to s.miller@mit.edu and j.hopking@york.ac.uk for more information.