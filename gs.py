import time
print('-' * 45) 
print('   SPACE MODULE MONITORING SYSTEM WARTECH')
print('-' * 45)

ciclos = int(input('Quantos ciclos de leitura deseja realizar: '))
print('=' * 45)

listaVibrcao = []
listaTemperatura = []
listaLatencia = []
listaCpu = []

qntLeituras = 0
qntCriticas = 0

mensagem = ''

contador = 1
while contador <= ciclos:

    print('\n'f'                 Ciclo {contador}  \n')


    pontos = 1
    while pontos <= 5:
        print('=' * 45)
        print(f'Ponto S{pontos}:') 

        vibracao = float(input('Vibração (g): '))
        qntLeituras += 1
        temperatura = float(input('Temperatura (°C): '))
        qntLeituras += 1
        latencia = float(input('Latência (ms): '))
        qntLeituras += 1
        cpu = float(input('Uso de CPU do computador de bordo (%): '))
        qntLeituras += 1

        print('=' * 45)
        print('Processando...')
        time.sleep(0.8)

        listaVibrcao.append(vibracao)
        listaTemperatura.append(temperatura)
        listaLatencia.append(latencia)
        listaCpu.append(cpu)

    
        if vibracao > 5:
            mensagem += f'Vibração crítica de {vibracao}g detectada no ponto S{pontos} (ciclo {contador})!\n'
            qntCriticas += 1

        elif vibracao < -5:
            mensagem += f'Vibração crítica de {vibracao}g detectada no ponto S{pontos} (ciclo {contador})!\n'
            qntCriticas += 1

        else:
            mensagem += ''

        if temperatura > 120:
            mensagem += f'Temperatura crítica de {temperatura}°C detectada no ponto S{pontos} (ciclo {contador})!\n'
            qntCriticas += 1

        elif temperatura < -150:
            mensagem += f'Temperatura crítica de {temperatura}°C detectada no ponto S{pontos} (ciclo {contador})!\n '
            qntCriticas += 1

        else:
            mensagem += ''

        if latencia > 800:
            mensagem += f'Latência crítica de {latencia}ms detectada no ponto S{pontos} (ciclo {contador})!\n'
            qntCriticas += 1

        else:
            mensagem += ''

        if cpu > 85:
            mensagem += f'Uso de CPU crítico de {cpu}% (ciclo {contador})!\n'
            qntCriticas += 1

        else:
            mensagem += ''

        pontos+=1
    contador+=1


indice = 0
somaVibracao = 0
maiorVibracao = listaVibrcao[0]
menorVibracao = listaVibrcao[0]

while indice < len(listaVibrcao):
    valor = listaVibrcao[indice]
    somaVibracao += valor

    if valor > maiorVibracao:
        maiorVibracao = valor

    if valor < menorVibracao:
        menorVibracao = valor

    indice += 1

mediaVibracao = somaVibracao / len(listaVibrcao) 


indice = 0
somaTemperatura = 0
maiorTemperatura = listaTemperatura[0]
menorTemperatura = listaTemperatura[0]

while indice < len(listaTemperatura):
    valor = listaTemperatura[indice]
    somaTemperatura += valor

    if valor > maiorTemperatura:
        maiorTemperatura = valor

    if valor < menorTemperatura:
        menorTemperatura = valor

    indice += 1

mediaTemperatura = somaTemperatura / len(listaTemperatura)


indice = 0
somaLatencia = 0
maiorLatencia = listaLatencia[0]
menorLatencia = listaLatencia[0]

while indice < len(listaLatencia):
    valor = listaLatencia[indice]
    somaLatencia += valor

    if valor > maiorLatencia:
        maiorLatencia= valor

    if valor < menorLatencia:
        menorLatencia = valor

    indice += 1

mediaLatencia = somaLatencia / len(listaLatencia)


indice = 0
somaCpu = 0
maiorCpu = listaCpu[0]
menorCpu = listaCpu[0]

while indice < len(listaCpu):
    valor = listaCpu[indice]
    somaCpu += valor

    if valor > maiorCpu:
        maiorCpu= valor

    if valor < menorCpu:
        menorCpu = valor

    indice += 1

mediaCpu = somaCpu / len(listaCpu)


situacao = (qntCriticas/qntLeituras) * 100 

if situacao > 30:
    alerta = 'ESTADO GERAL: RISCO ELEVADO - Acionar protocolo de emergência'

elif situacao >= 10 and situacao <= 30:
    alerta = 'ESTADO GERAL: ATENÇÃO - Monitoramento intensificado recomendado'

else:
    alerta = 'ESTADO GERAL: NORMAL - Módulo operando dentro dos limites de segurança'

print('\n')
print('=' * 72)
print('RELATÓRIO FINAL'.center(72))
print('=' * 72)
print('\n')

if mensagem != '':
    print('ALERTAS:')
    print(mensagem)

print(f'Vibração        Média: {mediaVibracao:.2f} g   | Máx: {maiorVibracao:.2f} g   | Mín: {menorVibracao:.2f} g')
print(f'Temperatura     Média: {mediaTemperatura:.2f}°C | Máx: {maiorTemperatura:.2f}°C | Mín: {menorTemperatura:.2f}°C')
print(f'Latência        Média: {mediaLatencia:.2f} ms | Máx: {maiorLatencia:.2f} ms | Mín: {menorLatencia:.2f} ms')
print(f'Uso CPU         Média: {mediaCpu:.2f}% | Máx: {maiorCpu:.2f}% | Mín: {menorCpu:.2f}%')

print('\n')
print('-' * 72)
print(alerta)
print('-' * 72)

