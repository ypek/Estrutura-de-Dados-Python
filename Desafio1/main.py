import csv

tabela_periodica = {}

arq = csv.reader(open('tabela.csv'), delimiter=';') #Ta Abrindo o arquivo tabela.csv e lendo-o com delimitador ';' que e o separador de campos

print("""
                        
▒█▀▀▀ █░░ █▀▀ █▀▄▀█ █▀▀ █▀▀▄ ▀▀█▀▀ █▀▀█ █▀▀    ▒█▀▀▄ ░▀░ █▀▀ █▀▀█ █▀▀█ █▀▀▄ ░▀░ ▀█░█▀ █▀▀ ░▀░ █▀▀ 
▒█▀▀▀ █░░ █▀▀ █░▀░█ █▀▀ █░░█ ░░█░░ █░░█ ▀▀█    ▒█░▒█ ▀█▀ ▀▀█ █░░█ █░░█ █░░█ ▀█▀ ░█▄█░ █▀▀ ▀█▀ ▀▀█ 
▒█▄▄▄ ▀▀▀ ▀▀▀ ▀░░░▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀▀ ▀▀▀    ▒█▄▄▀ ▀▀▀ ▀▀▀ █▀▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ▀▀▀ 

█▀▀█ █▀▀█ █▀▀█ █▀▀█    ▒█▀▀█ █░░█ █▀▀ █▀▀ █▀▀█ ▄ 
█░░█ █▄▄█ █▄▄▀ █▄▄█    ▒█▀▀▄ █░░█ ▀▀█ █░░ █▄▄█ ░    Cu, Hg, Cr, Nb, He
█▀▀▀ ▀░░▀ ▀░▀▀ ▀░░▀    ▒█▄▄█ ░▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ▀
                                                    
""")

inputDados = input("Digite o simbolo do elemento: ")

for i,dado_linha in enumerate(arq): #enumerate() retorna um objeto que é uma tupla com o indice e o valor
    if i == 0: 
        continue

    dados = {}
    dados['simbolo'] = dado_linha[0] 
    dados['nome'] = dado_linha[1] 
    dados['estado'] = dado_linha[5] 
    dados['numeroAtomico'] = dado_linha[2]
    dados['linha'] = dado_linha[3]
    dados['coluna'] = dado_linha[4] 



    # insere os dados na tabela periodica
    tabela_periodica[dados['simbolo']] = dados


elemento = tabela_periodica[inputDados]
print(f"{'='*60}\nSeu Símbolo é: {elemento['simbolo']}\nO Elemento tem o nome de {elemento['nome']}")

if elemento['estado'] == 'l':
    print('O Elemento é Líquido')
elif elemento['estado'] == 'g':
    print('O Elemento é Gasoso')
elif elemento['estado'] == 's':
    print('O Elemento é Solido')

print(f"""O número atomico do elemento é {elemento['numeroAtomico']}
O elemento está na linha {elemento['linha']}
O elemento está na coluna {elemento['coluna']}
""")










    
    
