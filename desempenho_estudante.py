media_aluno = [8, 5, 9, 8]

def escola(media_estudante):
    valor = []

    for i in media_estudante:
        if i:
            valor.append(i)
            media = sum(valor) / len(valor)
            
    if media >= 6:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'

    return valor, media, situacao

valor, media, situacao = escola(media_aluno)

print(valor)

print (f'O(a) estudante obteve uma média de {media}, com a sua maior nota de {max(valor)} pontos e a menor nota de {min(valor)} pontos e foi {situacao}')
