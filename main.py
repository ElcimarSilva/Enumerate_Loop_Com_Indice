lista_vendedores = ["Marcus", "Amanda", "Ale", "Carol"]
lista_vendas = [15,20,10,30]

#for vendedor in lista_vendedores:
   # print(vendedor)


#tamanho_lista = len(lista_vendedores)
#for i in range (tamanho_lista): # Irá executar de acordo com o numero de itens da lista
   #print(lista_vendedores[i])
   # print(lista_vendas[i])


# Enumerate (soluciona o caso acima onde precisa de gambi para pegar a posição na lista)
# Enumarate pega o indice que é vendedor e cria um enumerador da lista
#depois mostra sequencialmente
for i, vendedor in enumerate(lista_vendedores):
    print(vendedor)
    print(lista_vendas[i])