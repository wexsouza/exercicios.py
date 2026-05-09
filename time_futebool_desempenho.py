gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

def calcular_pontos(gols, golsadv):
    ponto = 0
    vitoria = 0
    empate = 0
    derrota = 0
    resultado1 = len(gols) * 3
    

    for i1, i2 in zip(gols, golsadv):
        
        if i1 > i2:
            ponto += 3
            vitoria += 1
        elif i1 == i2:
            ponto += 1
            empate += 1
        elif i1 < i2:
            ponto += 0
            derrota += 1

    aprov = (ponto / resultado1) 

    return ponto, vitoria, empate, derrota, aprov, resultado1

ponto, vitoria, empate, derrota, aprov, resultado1 = calcular_pontos(gols_marcados, gols_sofridos)

print('A pontuação do time foi de {} e seu aproveitamento foi de {}%'.format(ponto, resultado1))