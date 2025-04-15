n = 6
atual = 1
anterior = 0

for i in range(0, n):
    print(anterior)
    atualaux = anterior
    anterior = atual - anterior
    atual = atualaux