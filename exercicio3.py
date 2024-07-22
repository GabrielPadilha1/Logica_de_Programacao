"""
Exercício 3: Conversão de Temperatura.

Dica:
função float()
formatação de floats → f'{var:.#f}'

- Desenvolva um programa python que converta a temperatura de Celsius para Fahrenheit. 
O usuário deve fornecer a temperatura em Celsius
e o programa deve calcular e exibir a temperatura em Fahrenheit.
A fórmula para conversão é  F = C * 9/5 + 32 .
"""

var_celsius = float(input("Digite uma temperatura em Celsius: "))
var_fahrenheit = var_celsius * 9 / 5 + 32 
print(f"A temperatura é {var_fahrenheit:.2f} °F" )