"""
Exercício 2: Criando uma Lista a partir de um Range e Fatiamento.

- Crie uma lista chamada numeros utilizando a função range() para gerar uma sequência de números de 1 a 10 (inclusivo).
- Exiba na tela os números pares da lista.
- Crie uma nova lista chamada pares que contenha apenas os números pares da lista numeros.
- Mostre na tela a lista pares.
- Insira o número 15 na lista pares na terceira posição.
"""

numeros = list(range(1, 11))
pares = numeros[1::2]
print(pares)
pares[2] = 15
