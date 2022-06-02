"""
Exercício 15 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

    >>> classificar_trinagulo(2, 3, 4)
    'Triângulo Escaleno'
    >>> classificar_trinagulo(2, 2, 3)
    'Triângulo Isósceles'
    >>> classificar_trinagulo(2, 2, 2)
    'Triângulo Equilátero'
    >>> classificar_trinagulo(2, 2, 5)
    'Não é um triângulo'
    >>> classificar_trinagulo(5, 2, 2)
    'Não é um triângulo'
    >>> classificar_trinagulo(2, 5, 2)
    'Não é um triângulo'

"""


def classificar_trinagulo(lado_a: float, lado_b: float, lado_c: float):
    """Escreva aqui em baixo a sua solução"""
    lados = [lado_a, lado_b, lado_c]
    lados = sorted(lados, reverse=True)

    if lado_a == lado_b == lado_c:
        print("'Triângulo Equilátero'")
    elif lado_a > lado_c or lado_b > lado_c:
        print("'Não é um triângulo'")
    elif lados[0] < (lados[1] + lados[2]):
        if lado_a != lado_b != lado_c:
            print("'Triângulo Escaleno'")
        elif lados[1] == lados[2]:
            print("'Triângulo Isósceles'")
        else:
            return
    else:
        print("'Não é um triângulo'")