"""
Exercício 2: Par ou Ímpar

Dica: 
operador aritmético % (módulo)
operador lógico ==
interpolação f'{var}'

- Crie um programa Python que peça ao usuário um número inteiro 
- Determine se ele é par ou ímpar.
"""

var_numero = int(input("Digite um número: "))
if var_numero % 2 == 0:
    print(f"{var_numero} é par. ")
else:
    print(f"{var_numero} é ímpar. ")