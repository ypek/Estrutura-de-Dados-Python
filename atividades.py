def retornamaior():  #Usando o método max() para retornar o maior número da lista e append para adicionar elementos a lista
    number = []
    for i in range(0, 5):
        number.append(int(input("Digite um número: ")))
        max_value = max(number)
    print("O maior número da lista é: ", max_value)

    

def retornaSoma(): #Usando o método sum() para retornar a soma dos números da lista
    number = []
    for i in range(0, 5):
        number.append(int(input("Digite um número: ")))
        sum_value = sum(number)
    print("A soma dos números da lista é: ", sum_value)



def retornaRepetidos(): #Usando o método count() para retornar a quantidade de vezes que um elemento se repete na lista
    number = []
    for i in range(0, 5):
        number.append(int(input("Digite um número: ")))
        number.count(number[i])
    print("O número ", number[i], " apareceu ", number.count(number[i]), " vezes.")
        



def retornaMedia(): #Usando o método sum() para retornar a soma dos números da lista e dividir pelo número de elementos da lista len(number)
    number = []
    for i in range(0, 5):
        number.append(int(input("Digite um número: ")))
        sum_value = sum(number)
        media = sum_value / len(number)
    print("A média dos números da lista é: ", media)



def retornaSomaNegativo(): #Usando o método sum() para retornar a soma dos números da lista e usando if para verificar se o número é negativo
    number = []
    for i in range(0, 5):
        number.append(int(input("Digite um número: ")))
        sum_value = sum(number)
    if sum_value < 0:
        print("A soma dos números negativos da lista é: ", sum_value)



def RecebeECompara(): #Usando append para adicionar os elementos as 2 listas e verificar se o primeiro elemento é igual ao segundo elemento
    list1 = []
    list2 = []
    for i in range(0, 5):
        list1.append(int(input("Digite um número para a 1° lista: ")))
    print("==========================================================")    
    for i in range(0, 5):
        list2.append(int(input("Digite um número para a 2° lista: ")))
        
    if list1 == list2:
        print("True") 
    else:
        print("False")



def retornaMaiorCaracter(): #Aqui foi pura Gambiarra dsclp mas nem eu sei ao certo como isso ta funcionando 
    lista = []
    for i in range(0,5):
        lista.append(input("Digite uma palavra: "))
    maior = 0
    for i in range(0,5):
        if len(lista[i]) > maior:
            maior = len(lista[i])
            palavra = lista[i]
    print("A palavra mais longa é: ", palavra)
    print("A palavra ", palavra, " Repetiu ", lista.count(palavra), " vezes.")
    print("o Numero de ocorrencias de palavras compostas são ", lista.count(palavra))


def retornaMediaAltura():
    idade = []
    altura = []
    for i in range(0,5):
        idade.append(int(input("Digite a idade: ")))
    print("==========================================================") 
    for i in range(0,5):
        altura.append(float(input("Digite a altura: ")))
    media_altura = sum(altura) / len(altura)
    print("A média das alturas é: ", media_altura)

def traduzir():
    palavraSecreta = [2,15,13,0,4,9,1]
    letras = ["''","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    palavra = []
    for i in range(0,7):
        palavra.append(letras[palavraSecreta[i]])
    print("A palavra traduzida é: ", palavra)

    
















