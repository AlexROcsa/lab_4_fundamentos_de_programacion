#Calculadora de IMC (Índice de Masa Corporal)
print("Calculadora de IMC")

#Solicitamos al usuario que ingrese su peso en Kilogramos
weight = float(input("Ingrese su peso en kilogramos: "))

#Solicitamos al ususario que ingrese su altura en metros
height = float(input("Ingrese su altura en metros: "))

#Realizamos la fórmula del imc
imc = weight/ height ** 2 #IMC=Peso/altura**2

#Muestra el imc con dos decimales
print(f" Su imc es: {imc:.2f}")

if imc < 18.5: #Si el imc es menor a 18.5 el usuario tiene bajo peso
  print(" Usted tiene bajo peso ⚠️")
elif 18.5 <= imc <= 24.9: #Si el imc es mayor igual a 18.5 y menor igual a 24.9 el usuario tiene un peso normal
  print(" Usted tiene un peso normal ✅")
elif 25 <= imc <= 29.9: #Si el imc es mayor igual a 25 y menor igual a 29.9 el usuario tiene sobrepeso
  print(" Usted tiene sobrepeso ⚠️")
elif 30 <= imc <= 34.9: #Si el imc es mayor igual a 30 y menor igual a 34.9 el usuario tiene Obesidad grado I
  print(" Usted tiene Obesidad grado I ⚠️")
elif 35 <= imc <= 39.9: #Si el imc es mayor igual a 35 y menor igual a 39.9 el usuario tiene Obesidad grado II
  print(" Usted tiene Obesidad grado II ⚠️") 
elif imc >= 40: #Si el imc es mayor igual a 40 el usuario tiene Obesidad grado III
  print(" Usted tiene Obesidad grado III ⚠️")
