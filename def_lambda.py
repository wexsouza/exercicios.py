nota = float(input('Digite a nota do(a) estudante: '))

def qualitativo(x):
    return x + 0.5
print(qualitativo(nota))

# transformando o resultando em uma unica linha, mesma idea mas direto ao ponto 

qualitativo = lambda x: x + 0.5
print(qualitativo(nota))