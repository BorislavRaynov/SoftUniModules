class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []
some_info = input()
while some_info != "Stop":
    some_info = some_info.split()
    sender = some_info[0]
    receiver = some_info[1]
    content = some_info[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    some_info = input()

indices = list(map(int, input().split(", ")))
for index in indices:
    emails[index].send()
for email in emails:
    print(email.get_info())
