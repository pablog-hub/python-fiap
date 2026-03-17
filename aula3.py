# #Exercício 1
# velocidade = float(input('Digite sua velocidade: '))
# if velocidade > 80:
#     multa = velocidade - 80
#     print(f'Você foi multado em {multa*5} reais')
# else:
#     print('Você está dentro dos limites')

# #Exercicio 2
# a = float(input('Digite o valor: '))
# b = float(input('Digite o valor: '))
# c = float(input('Digite o valor: '))
#
# maior = a
# if b >= a and b >= c:
#     maior = b
# if c >= a and c >= b:
#     maior = c
# print((f'O maior é: {maior}'))
#
# menor = a
# if b<= a and b<= a:
#     menor = b
# if c <= a and c<= b:
#     menor = c
#
# print((f'O menor é: {menor}'))


# #Exercício 3
# salario = float(input('Digite seu salário: '))
# if salario > 1250:
#     aumento = salario * 0.1
# else:
#     aumento = salario * 0.15
#
# print(f'Seu aumento é:  {aumento}')

# #Exercício 4
# dist = float(input('Digite a distância que irá percorrer: '))
# if dist <= 200:
#     passagem = dist * 0.50
# else:
#     passagem = dist * 0.45
#
# print(f'Sua passagem custa R${passagem}')

#Exercício 5
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operação = int(input('Escolha a opção:\n 1- Soma\n 2- Subtração\n 3- Divisão\n 4- Multiplicação\n'))
if operação == 1:
    print(num1 + num2)
elif operação == 2:
    print(num1 - num2)
elif operação == 3:
    print(num1 / num2)
elif operação == 4:
    print(num1 * num2)
else:
    print('Esaa opção não existe')
