"""
Exercício 6: Calculadora de Média.

Dica:
funções int(), float() e str()
formatação de floats → f'{var:.#f}'
operador aritmético +


- Crie um programa que peça ao usuário três números (pode ser decimal ou inteiro)
- Calcule a média desses números. O programa deve exibir a média com duas casas decimais.
"""

var_numero1 = float(input("Digite um número: "))
var_numero2 = float(input("Digite um segundo número: "))
var_numero3 = float(input("Digite um terceiro número: "))
var_media = (var_numero1 + var_numero2 + var_numero3) / 3
print(f"A média é {var_media:.2f}")