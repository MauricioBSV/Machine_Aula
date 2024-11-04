import pandas as pd  # Importa a biblioteca pandas, que é utilizada para manipulação e análise de dados.

# Cria o primeiro DataFrame (df) a partir de uma lista de listas.
# Cada lista interna representa uma linha e as colunas são nomeadas como 'a' e 'b'.
df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])

# Cria o segundo DataFrame (df2) de forma semelhante ao primeiro.
# Este DataFrame também tem duas colunas: 'a' e 'b'.
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])

# Concatena os dois DataFrames (df e df2) ao longo do eixo das linhas (0).
# O parâmetro ignore_index=True faz com que os índices sejam renumerados, criando um índice contínuo.
df = pd.concat([df, df2], ignore_index=True)

# Imprime o DataFrame resultante no console.
print(df)
