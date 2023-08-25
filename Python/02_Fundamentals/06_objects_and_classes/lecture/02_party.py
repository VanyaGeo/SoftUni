# class Party:
#     people = []
#
#     def __init__(self):
#         pass

# и двата варианта са възможни

class Party:
    def __init__(self):
        self.people = []


party = Party()

command = input()
while command != "End":
    party.people.append(command)
    command = input()

going = ", ".join(party.people)
total = len(party.people)

print(f"Going: {going}")
print(f"Total: {total}")


