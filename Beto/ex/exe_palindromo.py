n = 9
for l in range(1, n+1):
    for j in range(1, (n+1)-l):
        print(" ", end="")
    for j in range(1, l+1):
        print(j, end="")
    for j in range(1, l)[::-1]:
        print(j, end="")
    print("")
 