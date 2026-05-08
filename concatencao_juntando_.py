nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

def concatenacao(nome, sobrenome):
    for n, s in zip(nome, sobrenome):
        print('nomes completo: {} {}'.format(n.capitalize(), s.capitalize()))
            
concatenacao(nomes, sobrenomes)
