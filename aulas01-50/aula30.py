"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

carroPassouRadar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
velCarroPassRadar1 = velocidade > RADAR_1
carroMultadoRadar1 = carroPassouRadar1 and velCarroPassRadar1

if velCarroPassRadar1: 
    print('Carro acima do limite de velocidade.')
else: 
    print('Tudo OK, carro no limite de velocidade.')

if carroPassouRadar1:
    print('Carro passou no radar 1.')

if carroMultadoRadar1:
    print('Carro multado em radar 1.')