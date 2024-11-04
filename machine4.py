import pandas as pd  # Importa a biblioteca pandas, utilizada para manipulação e análise de dados.

# Cria um DataFrame a partir de um dicionário, onde as chaves se tornam os nomes das colunas.
# A coluna 'a' contém os valores [1, 2, 3] e a coluna 'b' contém os valores [4, 5, 6].
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

# Exibe o DataFrame original no console.
print("DataFrame Original:")
print(df)

# Exclui a linha com índice 1 do DataFrame.
df = df.drop(1)

# Exibe o DataFrame após a exclusão da linha.
print("\nDataFrame após excluir a linha com índice 1:")
print(df)
