from random import choice

choiceset = int(input("Password type:\n1. Full char set.\n2. Letters + Numbers.\n3. Letters only.\n\nYou choose: "))
if choiceset == 1:
    charset = "abcdefghijklmnopqrstuvwxyz1234567890!\"£$%^&*()[]{}-=_+./<>?;'#:@~"
elif choiceset == 2:
    charset = "abcdefghijklmnopqrstuvwxyz1234567890"
elif choiceset == 3:
    charset = "abcdefghijklmnopqrstuvwxyz"

length = int(input("Password Length: "))


password = ""

for i in range(length):
    password = password + choice(charset)

print("\nYour password is: ")
print(password)