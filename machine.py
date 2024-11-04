import pandas as pd  # Importa a biblioteca pandas, que é utilizada para manipulação de dados.

# Cria uma lista de dicionários, onde cada dicionário representa uma linha de dados.
data = [
    {'a': 1, 'b': 2, 'c': 3},  # Primeiro dicionário com valores para as colunas 'a', 'b' e 'c'.
    {'a': 5, 'b': 10, 'c': 20}  # Segundo dicionário com valores para as mesmas colunas.
]

# Constrói um DataFrame a partir da lista de dicionários.
# Os índices das linhas são especificados como 'primeiro' e 'segundo'.
df = pd.DataFrame(data, index=['primeiro', 'segundo'])

# Imprime o DataFrame resultante, que exibe os dados organizados em uma tabela.
print(df)
