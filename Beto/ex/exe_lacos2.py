n = 12
atual = 1
anterior = 0
master = ""

for i in range(0, n):
    master += str(anterior)[::-1] + "," + " "
    atualaux = anterior
    anterior = atual + anterior
    atual = atualaux
    
    
print(master[::-1])
    