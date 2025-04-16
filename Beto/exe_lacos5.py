n = 20
master = ""

for i in range(1, n):
    divisores = 0
    for a in range(1, n):
        if(i % a == 0):
            divisores += 1
       
    if(divisores == 2): #primos
        divisoresa = 0
        i += 2
 
        for a in range(1, n):
            if(i % a == 0):
                divisoresa += 1
                
        if(divisoresa == 2): #primos 
            master += format( f"({i-2} e {i}), ")
               
print(master[:-2])  
 


           