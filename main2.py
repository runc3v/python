emails = []
amount = int(input('Enter the amount emails:'))
for i in range(amount):
    email = input('Enter emails with " @example.com ": ')
    emails.append(email)
for i in emails:
    if i.endswith('@example.com'):
        print(i)

