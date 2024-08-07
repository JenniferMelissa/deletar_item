#lista de compras
compras = ['Ovos','Macarrão','Feijão','Arroz','Leite','Chocolate']

#mostrar lista na tela
for i in range(len(compras)):
    print(f'Índice {i}: {compras[i]}.')

#tratamento de exceçoes try
try:
    #usuario informa o item que deseja retirar
    indice = int(input('\nÍndice do item que deseja retirar: '))
    #retira item da lista
    del(compras[indice])
    print('\nItem retirado com sucesso.')
except:
    print('\nNão foi possível excluir.')
finally:
    #finally
    for i in range(len(compras)):
        print(f'Índice {i}: {compras[i]}.')
