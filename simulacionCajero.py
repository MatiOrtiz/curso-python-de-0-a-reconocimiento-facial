saldo= 2000

print("1. Ingreso de dinero")
print("2. Retiro de dinero")
print("3. Mostrar dinero")
print("4. Salir")

seleccion= int(input("Seleccionar: "))

if seleccion==1:
    ingreso= int(input("Monto ingresado: "))
    saldo+= ingreso
    print(f"Su nuevo saldo es {saldo}")
elif seleccion==2:
    egreso= int(input("Monto a retirar: "))
    saldo-=egreso
    print(f"Su nuevo saldo es {saldo}")
elif seleccion==3:
    print(f"El saldo de su cuenta es {saldo}")
else: 
    print("Salió exitosamente, muchas gracias")