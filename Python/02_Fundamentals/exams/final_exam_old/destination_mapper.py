import re

text = input()
pattern = r"(=|/)([A-Z][A-Za-z]{2,})(\1)"
matches = re.findall(pattern, text)

valid_points = 0
destinations = []

for match in matches:
    valid_points += len(match[1])
    destinations.append(match[1])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {valid_points}")

# =Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=