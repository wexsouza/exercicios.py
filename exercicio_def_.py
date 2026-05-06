lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

def motor(leitura):
    tam = len(leitura)
    max_v = leitura[0]
    min_v = leitura[0]
    soma_v = sum(leitura)

    for index in leitura:

        if index > max_v:
            max_v = index
        if index < min_v:
            min_v = index

    return tam, max_v, min_v, soma_v
    
tam, max_v, min_v, soma_v = motor(lista)

print(f'A lista possui {tam} números em que o maior número é {max_v} e o menor número é {min_v}. A soma dos valores presentes nela é igual a {soma_v}')
print(motor(lista))
