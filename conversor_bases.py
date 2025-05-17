print("Conversor de Sistemas Numéricos")
print("1. Decimal a Binario")
print("2. Decimal a Hexadecimal")
print("3. Binario a Decimal")
print("4. Hexadecimal a Decimal")

opcion = input("Elige una opción (1-4): ")

if opcion == "1":
    numero = int(input("Ingresa un número decimal: "))
    print("Binario:", bin(numero)[2:])

elif opcion == "2":
    numero = int(input("Ingresa un número decimal: "))
    print("Hexadecimal:", hex(numero)[2:].upper())

elif opcion == "3":
    numero = input("Ingresa un número binario: ")
    print("Decimal:", int(numero, 2))

elif opcion == "4":
    numero = input("Ingresa un número hexadecimal: ")
    print("Decimal:", int(numero, 16))
