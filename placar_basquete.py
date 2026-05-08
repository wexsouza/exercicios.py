participante1 = [8, 5, 6, 7, 4]                   #minha array de valores

def participante(media):                          # motor  
    valor = []
                                        # minha lista                                                  # resultado da media
    for i in media:                              # percorre a lista 
        if i != max(media) and i != min(media):                             # primeira condição
            valor.append(i) 
            resultado = sum(valor) / len(valor)                

    return valor, resultado                              # retorno 

valor, resultado = participante(participante1)
print(valor, resultado)



