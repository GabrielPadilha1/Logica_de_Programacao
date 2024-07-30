"""
Exercício 6: Trabalhando com Dicionários Aninhados e Funções

Dicas:
Funções permitem organizar o código em blocos reutilizáveis.
Dicionários aninhados são úteis para representar estruturas hierárquicas de dados.
A função sum() pode ser utilizada para calcular a soma de valores em um dicionário ou lista.
A divisão por len() fornece a média.
Exemplo de função `calcula_media()`	

def calcula_media(notas):
    soma = sum(notas.values())
    media = soma / len(notas)
    return media

- Crie uma função chamada calcula_media() que recebe um dicionário de notas 
como argumento e retorna a média das notas.
- Crie um dicionário chamado alunos
que armazene as notas de 3 alunos em 3 disciplinas: matemática, português e história.
- Utilize dicionários aninhados para armazenar as notas de cada aluno em cada disciplina.
- Utilize a função calcula_media() para calcular a média das notas 
de cada aluno em todas as disciplinas.
- Exiba na tela o nome de cada aluno e sua média final.
"""

def calcula_media(notas_alunos):
    soma = sum(notas.values())
    quantidade = len(notas)
    media = soma / quantidade
    return media

alunos = {
    'Pedro': {
        'matematica': 9.0,
        'portugues': 8.0,
        'historia': 10
    },
    'Thiago': {
        'matematica': 9.5,
        'portugues': 7.0,
        'historia': 6.0
    },
    "João": {
        'matematica': 8.0,
        'portugues': 5.0,
        'historia': 7.0
    } 
}
for aluno, notas in alunos.items():
    media = calcula_media(notas)
    print(f'{aluno}, sua média final é: {media:.2f}')