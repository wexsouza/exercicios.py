nome_aluno = str(input('Nome do Aluno: '))
planilha = int(input('Digite as notas do aluno: '))
semestre = int(input('Digite o semestre/Mes: '.capitalize()))

mes = {'Janeiro': 1, 'Fevereiro': 2, 'Março': 3, 'Abril': 4, 'maio': 5,'Junho': 6, 'Julho': 7, 'Agosto': 8, 'Setembro': 9, 'Outubro': 10, 'Novembro': 11, 'Dezembro': 12 }

nota = map(lambda media: media / semestre)
nota = list(nota)

def aulas(avaliacao):
    membro = []
    if membro[1] >= 5:
        print('Parabens! {}, você está aprovado!'.format(membro))
    return membro

