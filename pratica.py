while True:
    nome = str(input('Digite o nome do aluno: '))
    for i in range(3):
        nota = float(input('Digite a nota do aluno: '))
    para_loop = str(input('parar loop S/N?: ')).capitalize
    if para_loop == 'S':
        break
    else:
       

lista_alunos = []
lista_notas = []

def escola(studant, grade):
    lista_alunos.append(studant)
    lista_notas.append(grade)
escola(nome, nota)

grades = []

for i in range(0, len(lista_notas), 3):
    grades.append(lista_notas[i], lista_notas[i+1], lista_notas[i+2])


