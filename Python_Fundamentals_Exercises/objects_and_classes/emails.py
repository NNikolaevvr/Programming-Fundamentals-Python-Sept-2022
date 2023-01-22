class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def sent(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'

emails = []

line = input()

while line != 'Stop':
    line = line.split(" ")
    sender = line[0]
    receiver = line[1]
    content = line[2]

    email = Email(sender,receiver,content)

    emails.append(email)
    line = input()

send_emails = [int(x) for x in input().split(", ")]

for x in send_emails:
    emails[x].sent()

for email in emails:
    print(email.get_info())




