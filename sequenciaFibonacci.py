numero = int(input("Digite um número para verificar se pertence à sequência: "));

def fibonaci(numero):
    a, b = 0, 1
    listaFib = [0, 1]
    while b <= numero:
        a, b = b, a + b
        listaFib.append(a and b)
        print(listaFib)
    if numero in listaFib:
        print("O número ", numero," está na sequência de Fibonaci")
    else:
        print("O número ", numero," não está na sequéncia de Fibonaci")

fibonaci(numero)