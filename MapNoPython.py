import pandas as pd
import openpyxl

lista_precos = [1000, 1500, 1250, 2500]

def adicionar_imposto(preco):
    return preco * 1.1

# forma tracional: usando for
# precos_com_imposto = []
# for preco in lista_precos:
#     precos_com_imposto.append(adicionar_imposto(preco))
# print(precos_com_imposto)

# usando o map
# precos_com_imposto2 = list (map(adicionar_imposto, lista_precos))
# print (precos_com_imposto2)

tabela = pd.read_excel("Base Vendas.xlsx")
tabela['Preco Com Imposto'] = list(map(adicionar_imposto, tabela['Preco Unitario']))
print(tabela)

#Exportar para excel
#tabela.to_excel("Base vendas atualizada.xlsx")