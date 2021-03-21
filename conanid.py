print("Menu de opciones \n")
print("Presiona 1 si quieres convertir de numero a texto")
print("Presiona 2 si quieres convertir de texto a numero\n")

option = int(input("Que opcion eliges?: "))

if option == 1:
    print("coversor de numero a palabra \n")
    option1 = int(input("Que numero quieres convertir a palabra?: "))

    if option1 == 1:
        print("el numero es 'uno'")
    elif option1 == 2:
        print("el numero es 'dos'")
    elif option1 == 3:
        print("el numero es 'tres'")
    else: 
        print("numero no registrado")  

elif option == 2:
    print("conversor de palabra a numero \n")
    option2 = input("Que palabra quieres convertir a numero?: ")

    if option2 == "uno":
        print("la palabra es '1'")
    elif option2 == "dos":
        print("el palabra es '2'")
    elif option2 == "tres":
        print("la palabra es '3'")
    else:
        print("palabra no registrada")

else:
    print("opcion invalida")

print("Gracias por usar el sistema")