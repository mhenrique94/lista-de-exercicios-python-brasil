"""
Exercício 05 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Altere o programa anterior (ex_04_crescimento_populacional) permitindo ao usuário informar as populações e as taxas de
crescimento iniciais. Valide a entrada (crescimento do país A precisa ser maior que a do país B. Pense na razão dessa
restrição).

    >>> calcular_ano_ultrapassagem_populacional(80_000, 0.03, 200_000, 0.015)
    'População de A, depois de 63 ano(s) será de 515033 pessoas, superando a de B, que será de 510964 pessoas'
    >>> calcular_ano_ultrapassagem_populacional(80_000, 0.03, 200_000, 0.04)
    'A taxa de crescimento do país B (4.0%) deve ser menor do que a do país A (3.0%)'
    >>> calcular_ano_ultrapassagem_populacional(80_000, 0.05, 200_000, 0.015)
    'População de A, depois de 28 ano(s) será de 313610 pessoas, superando a de B, que será de 303444 pessoas'
    >>> calcular_ano_ultrapassagem_populacional(800_000, 0.05, 200_000, 0.015)
    'População de A, depois de 0 ano(s) será de 800000 pessoas, superando a de B, que será de 200000 pessoas'


"""


def calcular_ano_ultrapassagem_populacional(
        populacao_menor: int, taxa_crescimento_populacao_menor: float, populacao_maior,
        taxa_crescimento_populacao_maior:float ) -> str:
    """Escreva aqui em baixo a sua solução"""

    ano = 0
    pais_A = populacao_menor
    pais_B = populacao_maior

    if taxa_crescimento_populacao_maior > taxa_crescimento_populacao_menor:
        return(f'A taxa de crescimento do país B ({100*taxa_crescimento_populacao_maior:.1f}%) deve ser menor do que a do país A ({100*taxa_crescimento_populacao_menor:.1f}%)')

    while pais_A < pais_B:
        pais_A = pais_A + (pais_A * taxa_crescimento_populacao_menor)
        pais_B = pais_B + (pais_B * taxa_crescimento_populacao_maior)
        ano = ano + 1
    print(f"'População de A, depois de {ano} ano(s) será de {round(pais_A)} pessoas, superando a de B, que será de {round(pais_B)} pessoas'")
