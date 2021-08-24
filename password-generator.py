import random

literki = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&'

dlugosc = input('Jakby co te haslo ktore sie wygeneruje zapisze sie na pulpicie. Podaj tutaj jak dlugie ma byc haslo ')
dlugosc = int(dlugosc)

password = ''
for c in range(dlugosc):
    password += random.choice(literki)
print(password)

with open('haslo.txt', 'w') as f:
    f.write(password)