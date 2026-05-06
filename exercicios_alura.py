#Nesse exercicio vemos a escolha de numeros de forma aleatoria:
from math import choice
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
print(choice(lista))
#--------------------------------------------------------------------------------------------------------------

# crie um programa que sorteia aleatoriamente um numero inteiro positivo menor que 100
from random import randrange
print(randrange(100))
#---------------------------------------------------------------------------------------------------------------
from math import pow

p = int(input('Digite um número: '))
p_2 = int(input('Deseja elevar a quantos?: '))

resultado = pow(p, p_2)
print(f'{p} elevado {p_2} = {resultado:.0f}')

#------------------------------------------------------------------------------------

from random import randrange
sorteador = int(input('Qual é a quantidade de participantes: '))
print(randrange(1, sorteador + 1))

#------------------------------------------------------------------------------------
from random import randrange
nome = str(input('Digite é seu nome: '))
print('Olá, {}, o seu token de acesso é {}! Seja bem-vindo(a)!'.format(nome, randrange(1000, 9999, 2)))
#-------------------------------------------------------------------------------------
import random

frutas = ['maça', 'banana', 'uva', 'pêra', 'manga', 'coco', 'melância', 'mamão', 'laranja', 'abacaxi', 'kiwi', 'ameixa']
salada = random.sample(frutas, k=3)
print(salada)

        




