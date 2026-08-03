#using the for we can do that him traverse a list
compras = ['Arroz', 'feijão','frango','batata']
produto = (input("Digite um número a pesquisar na lista: "))
for i in compras:
 if i == produto:
   print("Elemento encontrado!")
   break
else:
 print("Elemento não encontrado.")

#range a number
 for num in range(1,4,2):
    print(num)