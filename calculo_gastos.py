<<<<<<< HEAD
periodo = int(input('Periodo para hospedagem: '))
cidade = {'Salvador': 850, 'Fortaleza': 800, 'Natal': 300, 'Aracaju': 550}
destino = str(input('Qual será seu destino: ')).capitalize()
comida = int(input('Quanto gastará em comida: '))
valor_passeio = int(input('Passeios pago aparte: '))

hotel = lambda gastos_hotel: (gastos_hotel * 150)
valor_total = hotel(periodo)
=======
km = int(input('Para onde será seu destino? '))

gasolina = map(lambda custo_gasolina: custo_gasolina * 150)
gasolina = list(gasolina)

>>>>>>> 6f16654e45811c2e52090e136e568032ee24b03d

def gasolina(onde, ask):
    ida = 0
    total = 0
    for c, km in onde.items():
        if ask == c:
            ida += (km / 14) * 5
            total += ida * 2              
    return ida, total
ida, total = gasolina(cidade, destino)

def valor_geral(food, costs):
    general_costs = food + costs
    return general_costs
general_costs = valor_geral(comida, valor_passeio)

print('Com base nos gastos definidos, uma viagem de {} dias para {} saindo de Recife custaria {:.2f} reais, valores em comida e passeio {} reias'.format(periodo, destino, total, general_costs)) 



