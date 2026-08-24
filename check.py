print('-' * 40)
print('SISTEMA DE NOTA DO 2° SEMESTRE'.center(40))
print('-' * 40)

print('-' * 40)
check = []
for cps in range(1,4):
    cp = float(input(f'Digite o valor da {cps} check point: '))
    check.append(cp)
print('-' * 40)

menorcp = min(check)
somacp = sum(check) - menorcp


print('-' * 40)
sps = []
for sp in range(1,3):
    spss = float(input(f'Digite o valor da {sp} sprint: '))
    sps.append(spss)
somasps = sum(sps)
print('-' * 40)

print('-' * 40)
gs = []
for gbs in range(1):
    gbss = float(input(f'Digite o valor da global solucion: '))
    gs.append(gbss)
somags = sum(gs)
print('-' * 40)

media = ((somacp + somasps)/4) * 0.4 + somags * 0.6

print('-' * 40)
print(f'Sua média do 2° Semestre é {media:.1f}')
print(f'Seu menor check point foi {menorcp:.1f}')
print('-' * 40)







