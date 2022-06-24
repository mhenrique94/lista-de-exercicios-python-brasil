"""
Exercício 45 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma com uma casa decimal.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

    >>> corrigir(('Renzo','A','B','C','D','E','E','D','C','B','A' ))
    Aluno                 Nota
    Renzo                 10
    ---------------------------
    Média geral: 10.0
    Maior nota: 10
    Menor nota: 10
    Total de Alunos: 1
    >>> corrigir(
    ... ('Renzo','A','B','C','D','E','E','D','C','B','A' ),
    ... ('Fulano','A','B','C','D','E','E','D','C','B','B' ),
    ... )
    Aluno                 Nota
    Renzo                 10
    Fulano                 9
    ---------------------------
    Média geral: 9.5
    Maior nota: 10
    Menor nota: 9
    Total de Alunos: 2
"""


from platform import mac_ver
from typing import Counter


def corrigir(*provas):
    """Escreva aqui em baixo a sua solução"""
    resultado = {}
    total = 0
    maxima = 0
    minima = 10
    gabarito = ['cidadao', 'A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

    for conjunto in provas:
        count = 0
        for cadaum in conjunto:
                if len(cadaum) > 1:
                    resultado[cadaum] = 0
                    count += 1
                else:
                    if cadaum == gabarito[count]:
                        resultado[conjunto[0]] += 1
                        count += 1
                        
    print('Aluno                 Nota')

    for nome, nota in resultado.items():
        total += nota
        if maxima < nota:
            maxima = nota
        if minima > nota:
            minima = nota

        print(f'{nome}                 {nota}')

    media = total / len(resultado)

    print('---------------------------')
    print(f'Média geral: {media}')
    print(f'Maior nota: {maxima}')
    print(f'Menor nota: {minima}')
    print(f'Total de Alunos: {len(resultado)}')

