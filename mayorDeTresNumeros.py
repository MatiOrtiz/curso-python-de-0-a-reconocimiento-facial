n1= int(input("n1: "))
n2= int(input("n2: "))
n3= int(input("n3: "))

if n1>=n2:
    if n1>=n3:
        mayor= n1
    else:
        mayor= n3
elif n1<n2:
    if n2>=n3:
        mayor= n2
    else:
        mayor= n3

print(f"El numero mayor es {mayor}")