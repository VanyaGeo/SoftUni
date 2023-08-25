class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

command = input()

while command != "Stop":
    commands = command.split()
    sender = commands[0]
    receiver = commands[1]
    content = commands[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()

sent_email = [int(x) for x in input().split(", ")]
for number in sent_email:
    emails[number].send()

for mail in emails:
    print(mail.get_info())


