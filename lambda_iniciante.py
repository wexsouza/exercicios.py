n1 = float(input('Digite a 1° nota do(a) estudante: '))
n2 = float(input('Digite a 2° nota do(a) estudante: '))
n3 = float(input('Digite a 3° nota do(a) estudante: '))

media_ponderavel = lambda x, y, z: (x*3 + y*2 + z*5) / 10
media_estudante = media_ponderavel(n1, n2, n3)

print(f'o estudante atingiu uma media de {media_estudante}')