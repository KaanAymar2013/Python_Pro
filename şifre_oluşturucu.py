import random


def şifre_oluştur(pass_length):
    elements = "+-/*!&$#?=@<>1234567890/"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

print(şifre_oluştur(10))   