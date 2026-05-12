estados = ['Salvador', 'Fortaleza', 'Natal', 'Aracaju']
def gasolina(kilometro):
    gastos_gasolina = 0
    
    if kilometro == 'Salvador':
        gastos_gasolina += kilometro * 5
    elif kilometro == 'Fortaleza':
        gastos_gasolina += kilometro * 5
    elif kilometro == 'Natal':
        gastos_gasolina += kilometro * 5
    elif kilometro == 'Aracaju':
        gastos_gasolina += kilometro * 5

    return gastos_gasolina 
gastos_gasolinia = gasolina(estados)

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
