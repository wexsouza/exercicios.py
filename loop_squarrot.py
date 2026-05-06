from math import sqrt
lista = [2, 8, 15, 23, 91, 112, 256]
raiz = []

for i in lista:
    #square_r = i**(1/2)  .... versão que eu fiz
    raiz.append(sqrt(i))

for i in range(len(raiz)):

    if raiz[i] // 1 == raiz[i]: 
        
        print(f' O número {lista[i]} possui raiz quadrada inteira igual a {int(raiz[i])}')
        #msg = ('Essa raiz é inteira: ')
        #print('{} {} = {}'.format(msg, i, square_r))
        
   # else:
       # msg = ('Essa não raiz é inteira: ')
       # print('{} {} = {}'.format(msg, i, square_r))
      