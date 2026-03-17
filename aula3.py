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

# #Exercício 5
# # num1 = float(input('Digite o primeiro número: '))
# # num2 = float(input('Digite o segundo número: '))
# # operação = int(input('Escolha a opção:\n 1- Soma\n 2- Subtração\n 3- Divisão\n 4- Multiplicação\n'))
# # if operação == 1:
# #     print(num1 + num2)
# # elif operação == 2:
# #     print(num1 - num2)
# # elif operação == 3:
# #     print(num1 / num2)
# # elif operação == 4:
# #     print(num1 * num2)
# # else:
# #     print('Esaa opção não existe')

# #Exercício 6
# casa = float(input('Qual o valor da casa: '))
# sal = float(input('Qual seu salário: '))
# anos = float(input('Quantos anos você quer pagar a casa: '))
# parcela = casa/(anos*12)
# limite = sal * 30/100
# if parcela <= limite:
#     print(f'O valor da parcela é {parcela: .2f}')
# else:
#    print('Prestação Negada')

# #Exercício 7
# kWh = float(input('Quantidade de kWh consumida: '))
# inst = str(input('Tipo de instalação:\n R- Residências\n I- Indústrias\n C- Comércios\n Opcão: ')).upper()
# if inst == 'R':
#     kWh <= 500
#     print(f'O valor a pagar é R${kWh*0.40}')
# elif inst == 'R':
#     kWh > 500
#     print(f'O valor a pagar é R${kWh * 0.65}')
# elif inst == 'I':
#     kWh <= 1000
#     print(f'O valor a pagar é R${kWh * 0.55}')
# elif inst == 'I':
#     kWh > 1000
#     print(f'O valor a pagar é R${kWh * 0.60}')
# elif inst == 'C':
#     kWh <= 1000
#     print(f'O valor a pagar é R${kWh * 0.55}')
# elif inst == 'C':
#     kWh <= 1000
#     print(f'O valor a pagar é R${kWh * 0.60}')
# else:
#     print('Erro: Tipo de instalação inválido!')

# #Exercício 8
# nota1 = float(input('Digite sua primeira nota: '))
# nota2 = float(input('Digite sua segunda nota: '))
# media = (nota1 + nota2) / 2
# if media < 6:
#     print('Você foi reprovado!')
# else:
#     print('Parabéns, você foi aprovado!)

# #Exercício 9
# nota1 = float(input('Digite sua primeira nota: '))
# nota2 = float(input('Digite sua segunda nota: '))
# media = (nota1 + nota2) / 2
# if media < 4:
#     print('Você foi reprovado!')
# elif media == 4:
#     print('Você está de exame!')
# elif media < 6:
#     print('Você está de exame!')
# else:
#     print('Parabéns, você foi aprovado!')