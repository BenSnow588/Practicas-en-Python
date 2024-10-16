print("Menu")
print("1.Suma de numero")
print("2.Resta de numeros")
print("3.Multiplicacion de numeros")
print("4.Division de numeros")
print("0.Salir")

Num = int(input("Ingrese un opcion del menu: "))
while Num != 0:
  if Num == 1:
    x = float(input("Ingrese el primer numero:"))
    y = float(input("Ingrese el segundo numero: "))
    print("El resultado de la suma es: " + str(x+y))
    Num = int(input("Ingrese un opcion del menu: ")) #LLamo a la variable Num inicial para que me pida ingresar una opcion del menu (hago lo mismo con cada condicion)
  elif Num == 2:
    x = float(input("Ingrese el primer numero:"))
    y = float(input("Ingrese el segundo numero: "))
    print("El resultado de la resta es: " + str(x-y))
    Num = int(input("Ingrese un opcion del menu: "))
  elif Num == 3:
    x = float(input("Ingrese el primer numero:"))
    y = float(input("Ingrese el segundo numero: "))
    print("El resultado de la multiplicacion es: "+ str(x*y))
    Num = int(input("Ingrese un opcion del menu: "))
  elif Num == 4:
    x = float(input("Ingrese el primer numero:"))
    y = float(input("Ingrese el segundo numero: "))
    print("El resultado de la division es: "+ str(x/y))
    Num = int(input("Ingrese un opcion del menu: "))
print("Gracias")
