def suma(numero3, numero2):
    return print("el resultado de suma es: ", (numero3+numero2))

def resta(numero3, numero2):
    return print("El resultado de la resta es: " (numero3-numero2))

while True:
    try:
        numero3 = int(input("Por favor ingresa el primer numero: "))
        numero2 = int(input("Por favor ingresa el segundo numero: "))
        if numero3 > 0 and numero2 > 0:
            break
        else: print("por favor ingresa un numero positivo")
    except: print("Por favor ingresa un numero")
    
while True:
    print("1- sumar  2- restar")
    opcion = int(input("por favor dijita 1 0 2"))
    if opcion == 1:
        suma(numero3, numero2)
        break
    elif opcion == 2:
        resta(numero3, numero2)
        break
    else: print("eligio una opcion equivocada!")
    
print("hola fernando")