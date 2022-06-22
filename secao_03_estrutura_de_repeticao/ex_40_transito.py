"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""


from statistics import mean


def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    siglas = []
    n_carros = []
    n_acidentes = []
    indice_acidentes = []
    acidentes_cidades_pequenas = []

    for each in cidades:
        siglas.append(each[0])
        n_carros.append(each[1])
        n_acidentes.append(each[2])
        indice_acidentes.append(each[2]/each[1]*1000)

        if each[1] <= 150_000:
            acidentes_cidades_pequenas.append(each[2])

    maior_indice = max(indice_acidentes)
    menor_indice = min(indice_acidentes)
    nome_maior_indice = siglas[indice_acidentes.index(maior_indice)]
    nome_menor_indice = siglas[indice_acidentes.index(menor_indice)]
    media_acidentes = sum(n_acidentes) / len(n_acidentes)
    media_acidentes_cidades_pequenas = sum(acidentes_cidades_pequenas) / len(acidentes_cidades_pequenas)

    print(f'O maior índice de acidentes é de {nome_maior_indice}, com {maior_indice:.1f} acidentes por mil carros.')
    print(f'O menor índice de acidentes é de {nome_menor_indice}, com {menor_indice:.1f} acidentes por mil carros.')
    print(f'O média de veículos por cidade é de {mean(n_carros)}.')
    print(f'A média de acidentes total nas cidades com menos de 150 mil carros é de {media_acidentes_cidades_pequenas:.1f} acidentes.')