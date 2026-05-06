nota = [ 6.0, 7.0, 9.0, 5.0]

def boletim(lista):
    media = sum(lista) / len(lista)
    if media >= 6:
        situacao = 'Aprovado(a)'
    else:
        situacao = 'Reprovado(a)'
    return (media, situacao)

media, situacao = boletim(nota)

print(f'O(a) estudante atingiu uma média de {media}, e foi {situacao}')