# n = input("Digite o valor: ")
n1 = 12
n2 = 18

for i in range(1, min(n1,n2)):
    if(n1 % i == 0 and n2 % i == 0):
        maxdivisor = i

print(i)


#12 18