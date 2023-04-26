#inverter = input("Digite uma palavra para inverter: ")
#print(inverter[::-1])

#outra forma de fazer:
palavra = input("Digite uma palavra para inverter: ")
palavraInvertida = ""
for letra in palavra:
    palavraInvertida = letra + palavraInvertida
print(palavraInvertida)