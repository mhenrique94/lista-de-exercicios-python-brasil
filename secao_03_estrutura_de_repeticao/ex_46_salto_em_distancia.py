"""
Exercício 46 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada
atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
informe a média dos saltos conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média).
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são
ordenados.

Mostre os valores com uma casa decimal sem arredondar.

    >>> calcular_estatiscas_do_salto('Rodrigo Curvêllo', 6.5, 6.1, 6.2, 5.4, 5.3)
    Atleta: Rodrigo Curvêllo
    ---------------------------------
    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m
    ---------------------------------
    Melhor salto:  6.5 m
    Pior salto: 5.3 m
    Média dos demais saltos: 5.8 m
    ---------------------------------
    Resultado final:
    Rodrigo Curvêllo: 5.8 m
    >>> calcular_estatiscas_do_salto('João do Pulo', 6.8, 6.5, 6.1, 6.2, 5.4)
    Atleta: João do Pulo
    ---------------------------------
    Primeiro Salto: 6.8 m
    Segundo Salto: 6.5 m
    Terceiro Salto: 6.1 m
    Quarto Salto: 6.2 m
    Quinto Salto: 5.4 m
    ---------------------------------
    Melhor salto:  6.8 m
    Pior salto: 5.4 m
    Média dos demais saltos: 6.2 m
    ---------------------------------
    Resultado final:
    João do Pulo: 6.2 m

"""


from operator import indexOf
from statistics import mean
import math

def calcular_estatiscas_do_salto(nome, *saltos):
    """Escreva aqui em baixo a sua solução"""
    
    prova = []
    for salto in saltos:
        prova.append(salto)
    number = sum(sorted(prova)) / 5
    resultado_final = round_decimals_down(number)

    print(f'Atleta: {nome}')
    print('---------------------------------')
    print(f'Primeiro Salto: {prova[0]} m')
    print(f'Segundo Salto: {prova[1]} m')
    print(f'Terceiro Salto: {prova[2]} m')
    print(f'Quarto Salto: {prova[3]} m')
    print(f'Quinto Salto: {prova[4]} m')

    melhor = prova.pop(indexOf(prova, max(prova)))
    pior = prova.pop(indexOf(prova, min(prova)))
    number = sum(sorted(prova)) / 3
    media = round_decimals_down(number)

    print('---------------------------------')
    print(f'Melhor salto:  {melhor:.1f} m')
    print(f'Pior salto: {pior:.1f} m')
    print(f'Média dos demais saltos: {media} m')
    print('---------------------------------')
    print('Resultado final:')
    print(f'{nome}: {resultado_final:.1f} m')

def round_decimals_down(number:float, decimals:int=1):
    """
    Returns a value rounded down to a specific number of decimal places. Afinal, StackOverflow também é ferramenta de trabalho rs
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.floor(number)

    factor = 10 ** decimals
    return math.floor(number * factor) / factor