#Clase Crud (Clase final)
import os
os.system ('cls')
opcion = ""
boleta = []

#CREATE
def agregar_producto(nombre, precio):
    producto = {"nombre": nombre, "precio": precio}
    boleta.append(producto)
    print (f"Producto '{nombre}' agregado correctamente.")

#READ
def calcular_total():
    total = 0
    for producto in boleta:
        total = total + producto["precio"]
    return total

def mostrar_boleta():
    if len(boleta) == 0:
        print("La boleta está vacía.")
    else:
        print("\n------ BOLETA ------")
        for producto in boleta:
            print(f"  {producto['nombre']}  -  ${producto['precio']}")
        print(f"  TOTAL: ${calcular_total()}")
        print("--------------------\n")

#UPDATE
def actualizar_precio(nombre, nuevo_precio):
    for producto in boleta:
        if producto["nombre"] == nombre:
            producto["precio"] = nuevo_precio
            print(f"Precio de '{nombre}' actualizado a ${nuevo_precio}.")
            return 
    print(f"Producto '{nombre}' no encontrado.")

#DELETE
def eliminar_producto(nombre):
    for producto in boleta:
        if producto["nombre"] == nombre:
            boleta.remove(producto)
            print(f"Producto '{nombre}' eliminado correctamente.")
            return
    print(f"Producto '{nombre}' no encontrado.")

while opcion != "5":
    os.system('cls')
    print ("------Programa boleta------")
    print ("1. Añadir producto")
    print ("2. Ver boleta")
    print ("3. Actualizar precio de un producto")
    print ("4. Eliminar producto")
    print ("5. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_producto(input("Ingrese el nombre del producto: "), int(input ("Ingrese precio del producto: ")))
        input ("Presione ENTER para continuar")
   
    elif opcion == "2":
        mostrar_boleta()
        input ("Presione ENTER para continuar")

    elif opcion == "3":
        actualizar_precio(input("Ingrese nombre del producto: "), int(input("Ingrese el nuevo precio: ")))
        input ("Presione ENTER para continuar")

    elif opcion == "4":
        eliminar_producto(input("Ingrese nombre del producto a eliminar: "))
        input ("Presione ENTER para continuar")
    
    else:
        print("Ingrese una opción válida")
        input("Presione ENTER para continuar")
        