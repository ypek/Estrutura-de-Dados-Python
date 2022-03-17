from filas import *
import os
#Painel de atendimento
os.system('cls')
if __name__ == "__main__":
    f = Fila()
    counter = 0

    while True:

        #printar a ultima senha
        print("""
        
                                            MENU
                                        

        (1) - Gerar Proximo Senha    (2) - Chamar proxima senha    (3) - Mostrar senhas chamadas
        """)
        op = input("Digite a opcao desejada: ")
        if op == "1":
            f.enqueue(counter)
            counter += 1
            print('Senhas geradas:',f)
        elif op == "2":
            if f.is_empty():
                print("Fila vazia!")
            else:
                print("Senha: ", f.dequeue())
        elif op == "3":
            print("Senhas chamadas: ", f)
        else:
            print("Opcao invalida!")