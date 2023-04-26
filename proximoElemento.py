def a(numero):
    while numero < 15:
        numero = numero + 2;
        print(numero)
def b(numero):
    while numero < 100:
        numero = numero * (2)
        print(numero)

def c():
    for num in range(10):
        print(num*num)
def d():
    for num in range(2, 10):
        print(num*num)
        num = num+2

def e(numero):
    a, b = 0, 1
    listaFib = [0, 1]
    while b <= numero:
        a, b = b, a + b
        listaFib.append(a and b)
    print(listaFib)
    if numero in listaFib:
        print("O número ", numero," está na sequência de Fibonacci")
    else:
        print("O número ", numero," não está na sequéncia de Fibonacci")

def f(numero):
    import random
    numeros = [numero, numero*10]
    for i in range(numero, numero*10):
        while len(numeros) < 10:
            a = random.randint(numero, numero*10)
            if a not in numeros:
                numeros.append(a)
        for i in range(1, len(numeros)):
            j = i
            while j > 0 and numeros[j-1] > numeros[j]:
                numeros[j], numeros[j-1] = numeros[j-1], numeros[j]
                j -= 1
    print(numeros)
    


def main():
    print(" a)\n b)\n c)\n d)\n e)\n f)\n")
    opcao = input("Escolha uma opção: ")

    if opcao.lower() == "a" or opcao.lower() == "a)":
        numero = int(input("Digite um número inteiro positivo: "))
        a(numero)
    elif opcao.lower() == "b" or opcao.lower() == "b)":
        numero = int(input("Digite um número inteiro positivo: "))
        b(numero)
    elif opcao.lower() == "c" or opcao.lower() == "c)":
        c()
    elif opcao.lower() == "d" or opcao.lower() == "d)":
        d()
    elif opcao.lower() == "e" or opcao.lower() == "e)":
        numero = int(input("Digite um número inteiro positivo: "))
        e(numero)
    elif opcao.lower() == "f" or opcao.lower() == "f)":
        print("Não consegui entender essa lógica... então criei algo aleatório");
        numero = int(input("Digite um número inteiro positivo: "))
        f(numero)
    else:
        print("Opção inválida")
        main()
main()