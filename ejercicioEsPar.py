n1= int(input("n1: "))
n2= int(input("n2: "))

if n1%2==0 and n2%2==0:
    print("Ambos numeros son pares")
elif n1%2==0:
    print(f"El numero {n1} es par")
elif n2%2==0:
    print(f"El numero {n2} es par")
else:
    print("Ambos numeros son impares")