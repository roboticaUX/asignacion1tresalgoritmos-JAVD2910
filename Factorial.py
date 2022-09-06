def factorial(n): #Se definio una funcion con el nombre de factorial, que sepende de n
    if n== 0 or n == 1: #Esto es para cuando ingresamos un 0 o un 1
        return 1
    else: 
        return n*factorial(n-1)

n= factorial(10)
print(n)        