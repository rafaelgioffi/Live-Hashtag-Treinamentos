import displayfunction
import pandas

tabela = pandas.read_csv('telecom_users.csv')

#imprime os dados com maiores informações
# print(tabela.info())

# Excluir coluna inútil...
# Método 1
#     Definindo a coluna que será excluída manualmente
#       1 coluna só = tabela.drop('nome da coluna')
#       2 colunas = tabela.drop(['lista'])
#           axis=0 = linha
#           axis=1 = coluna

tabela = tabela.drop(['Unnamed: 0','Codigo'], axis=1)

# Método 2
# Excluir todas as colunas vazias
#   dropna() = exclusão inteligente
#       how='all' = toda coluna vazia
#       how='any' = algum valor vazio
tabela = tabela.dropna(how='all', axis=1)

# Excluir linhas com valores vazios...
tabela = tabela.dropna(how='any', axis=0)

#transformar a coluna total de gasto para números...
## errors="coerce" = ignorar os erros se for transformar algum texto em número, palavra como número
tabela['TotalGasto'] = pandas.to_numeric(tabela['TotalGasto'], errors='coerce')

# Analise dos dados
churns = tabela['Churn'].value_counts()
porcentagem = tabela['Churn'].value_counts(normalize=True)
porcentagem_format = tabela['Churn'].value_counts(normalize=True).map("{:.1%}".format)

print(churns)
print(porcentagem_format)

# Analise detalhada dos dados...
import plotly.express as px

for c in tabela.columns:
    grafico = px.histogram(tabela, x=c, color='Churn')
    grafico.show()