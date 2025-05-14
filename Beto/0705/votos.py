#execicio 4 
import random

candNomes = [
    "Joao", "Edvaldo", "Edna", "Branco"
]

candVotos = [0,0,0,0]


for _ in range(1000):
    candVotos[random.randint(0,3)] += 1
 
for i in range(4)   : 
    print(f"{candNomes[i]} -> Votos: {candVotos[i]} | {(candVotos[i] / 1000) * 100:.2f}%")
    
    
  