import pandas as pd  # Importa a biblioteca pandas, utilizada para manipulação e análise de dados.

# Cria uma lista de dicionários, onde cada dicionário representa uma linha de dados.
data = [
    {'a': 1, 'b': 2},  # Primeiro dicionário com valores para as colunas 'a' e 'b'.
    {'a': 5, 'b': 10, 'c': 20}  # Segundo dicionário com valores para as colunas 'a', 'b' e 'c'.
]

# Cria o primeiro DataFrame (df1) a partir da lista de dicionários.
# Os índices das linhas são especificados como 'primeiro' e 'segundo'.
# As colunas que serão incluídas no DataFrame são 'a' e 'b'.
df1 = pd.DataFrame(data, index=['primeiro', 'segundo'], columns=['a', 'b'])

# Cria o segundo DataFrame (df2) a partir da mesma lista de dicionários.
# Os índices das linhas são os mesmos, mas as colunas incluídas são 'a' e 'b1'.
df2 = pd.DataFrame(data, index=['primeiro', 'segundo'], columns=['a', 'b1'])

# Imprime o primeiro DataFrame (df1) no console, mostrando os dados organizados nas colunas 'a' e 'b'.
print(df1)

# Imprime o segundo DataFrame (df2) no console, que terá a coluna 'b1' como ausente e preencherá com NaN.
print(df2)
