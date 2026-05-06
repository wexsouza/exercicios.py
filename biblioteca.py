from icecream import ic
alunos = {
    'Ana': 6,
    'Bruno': 4,
    'Carlos': 8,
    'Daniela': 3,
    'Eduardo': 7
}
aprovados = []
media = 0
reprovados = []

for nome, nota in alunos.items():
    
    if nota >= 5:
        aprovados.append((nome, nota))
        media += nota
    else:
        reprovados.append(nome)


soma = media / len(aprovados)

ic(aprovados, round(soma, 2))
ic(reprovados)
    