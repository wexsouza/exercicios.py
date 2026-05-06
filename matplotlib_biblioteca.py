import matplotlib.pyplot as plt

estudantes = ['João', 'Maria', 'José']
notas = [8.5, 9, 6.5]

plt.bar(x= estudantes, height = notas)
plt.show()

estudantes_2 = ['João', 'Maria', 'José', 'Ana']
from random import choice

print(choice(estudantes_2))