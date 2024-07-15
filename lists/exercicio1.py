"""
Exercício 1: Criando e Acessando Elementos de uma Lista.

- Crie uma lista chamada `minha_lista` que armazene os nomes de 4 frutas diferentes.
- Exiba na tela o nome da fruta que está na segunda posição da lista.
- Adicione um novo item à lista, inserindo o nome de outra fruta no final.
- Mostre na tela a quantidade de frutas na lista.
- Remova a última fruta da lista.
"""

minha_lista = ["Manga", "Maçã", "Laranja", "Abacaxi",]
print(minha_lista[1])
minha_lista.append("Abacate")
print(len(minha_lista))
minha_lista.pop()
print(minha_lista)
