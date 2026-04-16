import random 
elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
alpaca = int(input("insira aqui a quantidade de caracteres para a sua senha"))
senha = ""
for i in range(alpaca):
    senha += random.choice(elements)
print(senha)
