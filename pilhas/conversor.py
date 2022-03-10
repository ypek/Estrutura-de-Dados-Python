from pilhas import *
#conversor decimano pra binario
if __name__ == "__main__":
    p1 = Pilha()
    num = int(input("Digite um numero: "))
    while num > 0:
        resto = num % 2
        p1.push(resto)
        num = num // 2
    while len(p1) > 0:
        print(p1.pop(), end="")
    print("")
    

