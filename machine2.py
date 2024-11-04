import pandas as pd  # Importa a biblioteca pandas, usada para manipulação e análise de dados.

# Cria um dicionário onde cada chave é uma string e cada valor é uma Series do pandas.
dic = {
    'um': pd.Series([1, 2, 3], index=['a', 'b', 'c']),  # Série 'um' com valores 1, 2 e 3, indexada por 'a', 'b' e 'c'.
    'dois': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])  # Série 'dois' com valores 1, 2, 3 e 4, indexada por 'a', 'b', 'c' e 'd'.
}

# Cria um DataFrame a partir do dicionário 'dic'.
# As chaves do dicionário se tornam os nomes das colunas do DataFrame.
df = pd.DataFrame(dic)

# Imprime a coluna 'um' do DataFrame no console.
print(df['um'])
print(df['dois'])

# Adiciona uma nova coluna chamada 'três' ao DataFrame, passando uma Série como valor.
print("Adicionando uma nova coluna passando como Série: ")
df['três'] = pd.Series([10, 20, 3], index=['a', 'b', 'c'])  # Nova série com valores 10, 20 e 3, indexada por 'a', 'b' e 'c'.
print(df)  # Imprime o DataFrame atualizado.

# Cria uma nova coluna chamada 'quatro' no DataFrame, que é a soma das colunas 'um' e 'três'.
print("Usando as colunas existentes no DataFrame:")
df['quatro'] = df['um'] + df['três']  # Soma os valores da coluna 'um' e da nova coluna 'três'.
print(df)  # Imprime o DataFrame com a nova coluna 'quatro'.

# Usando a função del 
# print("Excluindo a primeira coluna usando a função DEL:")
# del df['um']
# print(df)

# Usando a função pop
print ("Excluindo outra coluna usando a função POP:")
df.pop('dois')
print(df)

print(df.loc['b'])

print(df.iloc[2])

print(df[2:4])