import random
charset = "abcdefghijklmnopqrstuvwxyz"
def genPass(length):
    password = ""
    for i in range(length):
        char = charset[random.randrange(0, len(charset))]
        password += char
    return password
for i in range(10):
    print(genPass(7))
