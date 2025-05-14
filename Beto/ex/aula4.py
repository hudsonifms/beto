
'''

1 - var de controle
2 - condicai de controle
3 - att da var de controle

'''
# var de controle
# i = 0

# # condição de parada
# while i < 10:
#     if i % 2 == 0:
        
#          print(f"i = {i}")
#     #att da var
#     i = i + 1 #incremento
    
    
# criar lço de repetição que dependa da respota do user p continuar o laco

resp = 's'
while resp == 's':
    print("ainda estou repetindo")

    while True:
        resp = input("Deseja continuar? (s = sim / n = não) ").lower()
  
        if(resp == 's'  or resp == 'n'):
            break
print("terminei!!!!!")