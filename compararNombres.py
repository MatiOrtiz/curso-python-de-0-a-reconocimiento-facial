name1= input("name1: ")
name2= input("name2: ")

if name1[0].lower()==name2[0].lower() or name1[-1].lower()==name2[-1].lower():
    print("Hay coincidencia")
else:
    print("No hay coincidencia")