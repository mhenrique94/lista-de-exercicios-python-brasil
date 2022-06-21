"""
Exercício 37 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> from secao_03_estrutura_de_repeticao import ex_37_senso_de_academia
    >>> entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 162.0 centímetros
    Media de peso dos clientes: 81.0 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 177.0 centímetros
    Media de peso dos clientes: 80.5 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.0 centímetros
    Media de peso dos clientes: 90.2 kilos

"""


from operator import indexOf
from statistics import mean


def rodar_senso():
    """Escreva aqui em baixo a sua solução"""
    
    nomes =[]
    alturas = []
    pesos = []
    count = 0
    lista = []

    while True:
        nome = input('Nome')

        if nome == '0':
            break
        
        else:
            nomes.append(nome)
            alturas.append(int(input('Altura')))
            pesos.append(int(input('Peso')))
        
    gordo_kg = max(pesos)
    alto_cm = max(alturas)
    magro_kg = min(pesos)
    baixo_cm = min(alturas)

    gordo_nome = nomes[indexOf(pesos, gordo_kg)]
    magro_nome = nomes[indexOf(pesos, magro_kg)]
    alto_nome = nomes[indexOf(alturas, alto_cm)]
    baixo_nome = nomes[indexOf(alturas, baixo_cm)]

    media_peso = mean(pesos)
    media_altura = mean(alturas)

    print(f'Cliente mais alto: {alto_nome}, com {alto_cm} centímetros')
    print(f'Cliente mais baixo: {baixo_nome}, com {baixo_cm} centímetros')
    print(f'Cliente mais magro: {magro_nome}, com {magro_kg} kilos')
    print(f'Cliente mais gordo: {gordo_nome}, com {gordo_kg} kilos')
    print('--------------------------------------------------')
    print(f'Media de altura dos clientes: {media_altura:.1f} centímetros')
    print(f'Media de peso dos clientes: {media_peso:.1f} kilos')



        