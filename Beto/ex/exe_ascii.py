ALFABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
n = 10

n = int(n/2)
for l in range(0, n):
    for j in range(1, (n+1)-l):
        print(" ", end="")
    for j in range(0, l+1):
        print(ALFABET[j], end="")
    for j in range(0, l)[::-1]:
        print(ALFABET[j], end="")

 
    print("")
for l in range(0, n+1)[::-1]:
 
    for j in range(1, (n+1)-l):
        print(" ", end="")
    for j in range(0, l+1):
        print(ALFABET[j], end="")
    for j in range(0, l)[::-1]:
        print(ALFABET[j], end="")

    print("")