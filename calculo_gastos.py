km = int(input('Para onde será seu destino? '))

gasolina = map(lambda custo_gasolina: custo_gasolina * 150)
gasolina = list(gasolina)


valor_hotel = int(input('Quantos dias você vai passar? '))
def hotel(diaria):
    hotel_diaria = 0
    hotel_diaria += diaria * 150

    return hotel_diaria
hotel_diaria = hotel(valor_hotel)

comida = int(input('valor gasto com comida? '))
passeio = int(input('Valor gasto com passeio'))
def passeio_geral_comida(geral):
    geral = 0
    resultado += comida + passeio

    return resultado 
resultado = passeio_geral_comida(comida, passeio)


print('Com base nos gastos definidos, uma viagem de {} dias para {} saindo de Recife custaria {} reais'.format())
