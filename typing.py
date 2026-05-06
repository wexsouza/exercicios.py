notas = [5.9, 10.5]

def media(lista: list = [0]) -> float:
    calculo = sum(lista) / len(lista)
    return calculo

calculo = media(notas)
print(calculo)