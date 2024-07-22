"""
Exercício 1: Verificação de Idade para Votação.

Dica:
funções int() e input()
instrução if…else
operador lógico >=

- Escreva um programa Python que peça ao usuário a sua idade
- Verifique se ele é elegível para votar. No Brasil, a idade mínima para votar é 16 anos
"""

var_voto = int(input("Qual a sua idade? "))
if var_voto >= 16:
    print("Você já tem idade para votar!!")
else: 
    print("Você ainda não pode votar.")