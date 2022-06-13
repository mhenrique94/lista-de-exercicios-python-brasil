"""
Exercício 06 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele
mostre os números um ao lado do outro.

    >>> escrever_numeros_de_1_a_20(formato = 'um_abaixo_do_outro')
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    >>> escrever_numeros_de_1_a_20(formato = 'um_ao_lado_do_outro')
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
"""


from dataclasses import replace
import re


def escrever_numeros_de_1_a_20(formato:str) -> str:
    """Escreva aqui em baixo a sua solução"""
    count = 1
    linha_unica= []
    if formato == 'um_abaixo_do_outro':
        while count <21 :
            print(count)
            count = count + 1
    else:
        while count < 21:
            linha_unica.append(count)
            count = count + 1
        linha_unica = str(linha_unica).replace(',', '').replace('[', '').replace(']', '')
        print(linha_unica)

