"""
Exercício 42 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.

    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[-1, 10, 15, 20, 50, 13, 78, 22, 14, 16]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    7 número(s) entre o intervalo de zero a 25
    1 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[14, -5, 10, 2, 80, 99]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    2 número(s) entre o intervalo de zero a 25
    2 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[-55, 144, 5, 32, 18, 43, 12, 26, 76]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    3 número(s) entre o intervalo de zero a 25
    3 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[3, 5, 100, -5, 70, 88, 28, 12]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    1 número(s) entre o intervalo de zero a 25
    1 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 51 a 75
    1 número(s) entre o intervalo de 76 a 100

"""


def listar_numeros_para_avaliacao():
    """Escreva aqui em baixo a sua solução"""

    ls25 = []
    ls50 = []
    ls75 = []
    ls100 =[]

    while True:
        n = int(input('Insira ai: '))

        if n < 0:
            break
        elif n < 26:
            ls25.append(n)
        elif n < 51:
            ls50.append(n)
        elif n < 76:
            ls75.append(n)
        elif n < 101:
            ls100.append(n)
        else:
            continue
    
    if len(ls25) > 0:
        print(f'{len(ls25)} número(s) entre o intervalo de zero a 25')
    if len(ls50) > 0:
        print(f'{len(ls50)} número(s) entre o intervalo de 26 a 50')
    if len(ls75) > 0:
        print(f'{len(ls75)} número(s) entre o intervalo de 51 a 75')
    if len(ls100) > 0:
        print(f'{len(ls100)} número(s) entre o intervalo de 76 a 100')
                