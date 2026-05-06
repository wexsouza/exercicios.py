tab = int(input('Digite a tabuada desejada: '))

def tabuada(inteiro):
    for num in range(1, 11):
        result = num * inteiro
        print(f'Sua tabuada {inteiro} x {num} = {result}')
    

tabuada(tab)

