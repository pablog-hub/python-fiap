#Exercício 1
'''nome =  'Pablo Gomes dos Anjos'
print(nome)

#Exercício 2
a = 3
b = 5
mult1 = 2*a
mult2 = 3*b
resul1 = mult1 * mult2
print(resul1)

#Exercício 3
c = 3
d = 5
e = 10.55
soma = c + d + e
print(f'Soma = {soma:.3f}')

#Exercício 4
number1 = int(input('Número 1: '))
number2 = int(input('Número 2: '))
resul2 = number1 + number2
print(f'resultado: {resul2}')

#Exercício 5
Metros = float(input('Metros: '))
print(f'Milimitros {Metros*1000}')

#Exercício 6
dias = int(input('Dias:'))
horas = int(input('Horas:'))
minutos = int(input('Minutos:'))
segundos = int(input('Segundos:'))
print(f' Seu valor em segundos: {dias*86400 + horas*3600 + minutos*60 + segundos}')

#Exercício 7
salario = float(input('Seu salário:'))
aumentoPorcentagem = float(input('Porcentagem do aumento: '))
porcentSalario = salario * aumentoPorcentagem/100
novoSalario = salario + porcentSalario
print(f'Seu novo salário é: {novoSalario:.0f}')

#Exercício 8
preco = float(input('Preço da mercadoria:'))
aumentoPorcent = float(input('Porcentagem do desconto:'))
calculo = preco * aumentoPorcent/100
novoPreco = preco - calculo
print(f'O preço com desconto é: {novoPreco:.2f}')

#Exercício 9
distancia = float(input('Qual a distância do trajeto (em km): '))
velocidade = float(input('Qual é a velociadade média do trajeto (km/h): '))
tempo = distancia /  velocidade
horas = int(tempo)
minutos = int((tempo - horas) * 60)
if tempo == 1:
    print('A viagem levará exatamente 1 hora.')
else:
    print(f'A viagem levará {horas:.0f} horas e {minutos}  minutos.')

#Exercício 10
temperaturaC = float(input('Digite a temperatura em C:'))
temperaturaF = 9 * temperaturaC/5 + 32
print(f'A temperatura em Fahrenheit é {temperaturaF}')

#Exercício 11
quantidadeKm = float(input('Quantos Km foram rodados com o carro:'))
quantidadeDias = float(input('Quantos dias você usou o carro:'))
preco1 = quantidadeKm * 0.15
preco2 = quantidadeDias * 60
print(f'O preço a pagar é: R${preco1 + preco2}.')

#Exercicio12
x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))
z = (x**2 + y**2)/ (x - y)**2
print(f'O valor de z é: {z}')

#Exercício 13
salario1 = float(input('Digite seu salário: '))
aumentoS1 = salario1 * 35/100
novoS1  = salario1 + aumentoS1
print(f'Seu novo salário é R${novoS1:.2f}')'''