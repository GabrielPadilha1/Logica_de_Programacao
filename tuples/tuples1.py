"""
Exercício 1: Criando e Acessando Elementos de uma Tupla

Dicas:
Utilize a função print() para exibir os resultados na tela.
Para acessar um elemento específico da tupla, utilize o 
índice entre colchetes []. O primeiro índice é 0.
As tuplas são imutáveis, ou seja, seus valores não podem ser
modificados após a criação.
Para criar uma nova tupla a partir de outra, você pode 
utilizar o fatiamento ou a função tuple().


- Crie uma tupla chamada minha_tupla que armazene as cores 
do arco-íris: "vermelho", "laranja", "amarelo", "verde", 
"azul", "anil" e "violeta".
- Exiba na tela a cor que está na quarta posição da tupla.
- Tente modificar o valor da cor na quinta posição da tupla.
(Isso deve gerar um erro, pois tuplas são imutáveis).
- Crie uma nova tupla chamada cores_invertidas que seja a reversa da minha_tupla.
- Mostre na tela as cores_invertidas.
"""

minha_tupla = ("vermelho", "laranja", "amarelo", "verde", "azul", "anil", "violeta")
print(minha_tupla[3])
#minha_tupla.append[4] = "branco" #ERROR

cores_invertidas = minha_tupla[::-1]
print(cores_invertidas) 
