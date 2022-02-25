from atividades import *
import os
os.system('cls')
#os.system('clear') se for em Linux ou porwershell

while True:
    print("""    
███████╗░█████╗░██╗░░██╗░█████╗░██████╗░
██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗
█████╗░░███████║███████║███████║██║░░██║
██╔══╝░░██╔══██║██╔══██║██╔══██║██║░░██║
██║░░░░░██║░░██║██║░░██║██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░

░█████╗░████████╗██╗██╗░░░██╗██╗██████╗░░█████╗░██████╗░███████╗░██████╗
██╔══██╗╚══██╔══╝██║██║░░░██║██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
███████║░░░██║░░░██║╚██╗░██╔╝██║██║░░██║███████║██║░░██║█████╗░░╚█████╗░
██╔══██║░░░██║░░░██║░╚████╔╝░██║██║░░██║██╔══██║██║░░██║██╔══╝░░░╚═══██╗
██║░░██║░░░██║░░░██║░░╚██╔╝░░██║██████╔╝██║░░██║██████╔╝███████╗██████╔╝
╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═════╝░
    
    (1) - Função de Retorno Maior
    (2) - Função de Retorno Soma
    (3) - Função de Retorno Repetidos
    (4) - Função de Retorno Média
    (5) - Função de Retorno Soma Negativo
    ==========================================================
    (6) - Sair
    ==========================================================
    (7) - Função de Retorno Media de Altura
    (8) - Função Mensagem Secreta
    
    Digite a opção desejada: """)
    opcao = int(input())
    if opcao == 1:
        retornamaior()
    elif opcao == 2:
        retornaSoma()
    elif opcao == 3:
        retornaRepetidos()
    elif opcao == 4:
        retornaMedia()
    elif opcao == 5:
        retornaSomaNegativo()
    elif opcao == 7:
        retornaMediaAltura()
    elif opcao == 8:
        traduzir()
    elif opcao == 6:
        break
    else:
        print("Opção inválida!")
        continue 




        

        

