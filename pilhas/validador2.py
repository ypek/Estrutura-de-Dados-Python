from pilhas import *

if __name__ == "__main__":
    p1 = Pilha()
    expressao = (input('Digite a expresão matematica: '))
    exprAbrir = ['{','[','(']
    exprFechar= ['}',']',')']
    for i in range(len(expressao)):
        if expressao[i] in exprAbrir:
            p1.push(expressao[i])
        elif expressao[i] in exprFechar:
            if len(p1) == 0:
                print('Expressão inválida')
                break
            elif p1.peek() == '{' and expressao[i] == '}':
                p1.pop()
            elif p1.peek() == '[' and expressao[i] == ']':
                p1.pop()
            elif p1.peek() == '(' and expressao[i] == ')':
                p1.pop()
            else:
                print('Expressão inválida')
                break
        else:
            continue
    if len(p1) == 0:
        print('Expressão válida')