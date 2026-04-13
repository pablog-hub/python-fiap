# Exercício 1
# x = 1
# while x<=100:
#     print(x)
#     x+=1


#Exercício 2
# x = 50
# while x <= 100:
#     print(x)
#     x+=1

#Exercício 3
# import time
# x = 10
# while x>= 1:
#     print(x)
#     time.sleep(0.7)
#     x-=1
# print('FOGOOOO!!!')

#Exercício 4
# fim = int(input("Digite o último número a imprimir: "))
# x = 1
# while x <= fim:
#  print(x)
#  x += 2

#Exercício 5
# x = 3
# y = 1
# while y <= 10:
#     resultado = x * y
#     print(resultado)
#     y+=1

#Exercício 6
# x = int(input('Tabuada do: '))
# y = 0
# while y <= 10:
#     resultado = x * y
#     print(f'{x} x {y} = {resultado}')
# y+=1

#Exercício 7
# x = int(input('Tabuada do: '))
# z = int(input('até: '))
# y = 1
# while y <= z:
#     resultado = x * y
#     print(f'{x} x {y} = {resultado}')
#     y+=1

#Exercicio 8
# dp = float(input('Digite seu depósito inicial: '))
# taxa = float(input('Digite a taxa (em %): '))/100
# mes = 1
# while mes <= 24:
#     dp = dp + (dp * taxa)
#     print(f'Saldo do mês {mes} é de R$ {dp:.2f}')
#     mes+=1
# print(f"O ganho obtido com os juros foi de R${dp:.2f}.")

#Exercício 9
# dp = float(input('Digite seu depósito inicial: '))
# taxa = float(input('Digite a taxa (em %): '))/100
# dp1 = float(input('Valor do depósito mensal: '))
# mes = 1
# while mes <= 24:
#     dp = dp + (dp * taxa) + dp1
#     mes = mes + 1
#     print(f'Saldo do mês {mes} é de R$ {dp:.2f}')
#     mes+=1
# print(f"O ganho obtido com os juros foi de R${dp:.2f}.")


#Exercício 10
# soma = 0
# quantidade = 0
# while True:
#     num = int(input("Digite um número: "))
#     if num == 0:
#         break
#     soma += num
#     quantidade += 1
# print(quantidade)
# print(soma/quantidade)
# print(soma)

#Exercício 11
soma = 0
import time
while True:
    print('-' * 25)
    print('BEM VINDO A REGISTRADORA: ')
    print('-' * 25)
    print('Produtos: \n 1- Manga\n 2- Maça \n 3- Abacate\n 5- kiwi \n 9- Uva\n 0- Total ')
    print('-' * 25)


    produto = int(input('Digite o produto: '))

    if produto == 0:
        print('-' * 25)
        print('PROCESSANDO...')
        print('-' * 25)
        time.sleep(2)
        print(f'O total da sua compra é: R${soma}')
        print('-' * 25)
        break
    if produto not in [1, 2, 3, 5, 9]:
        print('Código inválido!')
        time.sleep(1)
        continue
    quantidade = int(input('Digite a quantidade: '))


    if produto == 1:
        soma += quantidade * 0.50
    elif produto == 2:
        soma += quantidade * 1
    elif produto == 3:
        soma += quantidade * 4
    elif produto == 5:
        soma += quantidade * 4
    elif produto == 9:
        soma += quantidade * 9















