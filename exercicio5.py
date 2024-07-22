"""
Exercício 5: Conversão de Tipos.

Dica: 
funções int(), float() e str()

- Escreva um programa que peça ao usuário três informações: um número inteiro,
um número decimal e uma palavra. O programa deve converter essas entradas
para os tipos corretos e exibir as informações formatadas em uma frase.
"""

var_numinteiro = int(input("Digite um número inteiro: "))
var_numdecimal = float(input('Digite um número decimal usando ".": '))
var_palavra = str(input("Digite uma palavra: "))
print(f"Você digitou o inteiro {var_numinteiro}, o decimal {var_numdecimal}, e a palavra {var_palavra}")
