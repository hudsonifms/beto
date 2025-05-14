#execicio 4 
import random

sexo = [
    "Masculino", "Feminino"
]
nomes_brasileiros = [
    "Maria", "José", "Ana", "João", "Antônio", "Francisco", "Carlos", "Paulo", "Pedro", "Lucas",
    "Marcos", "Luiz", "Raimundo", "Sebastião", "Domingos", "Gabriel", "Rafael", "Bruno", "Felipe", "Gustavo",
    "Rodrigo", "Matheus", "Thiago", "Vinícius", "André", "Fernando", "Diego", "Eduardo", "Leandro", "Ricardo",
    "Sandra", "Cláudia", "Patrícia", "Aline", "Juliana", "Camila", "Fernanda", "Vanessa", "Amanda", "Tatiane",
    "Larissa", "Letícia", "Sabrina", "Jéssica", "Daniela", "Gabriela", "Natália", "Isabela", "Helena", "Beatriz" 
]


lista = []
for i in range(5000): 
    lista.append([random.choice(nomes_brasileiros), random.randint(1, 90), random.choice(sexo)])
    
for pessoa in lista:
    print(f"Nome: {pessoa[0]} | Idadade: {pessoa[1]} | Sexo: {pessoa[2]}")
    
    
  