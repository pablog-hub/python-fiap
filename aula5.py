compras = ['Arroz', 'feijão','frango','batata']
compras_novo = compras
compras_novo = compras.copy() #copy the same list but separately

compras_novo.append('maça')
print(compras_novo)
print(compras[0:3]) #0 = start : 3 = cut

print(compras[-1:]) # -1 = show the last element and on so
del compras_novo[0] # delete the index you want
print(compras_novo)

compras_novo.clear() #clear the list
print(compras_novo)

compras += ['salada', 'salmão'] # add an item
print(compras)

compras.extend('agua') # slice the item
print(compras)

compras.extend(['limao', 'mamao']) #add item
print(compras)

