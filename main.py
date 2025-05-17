# Importamos la librería math para usar sqrt() en el cálculo de raíces
import math

print("🧮 Calculadora de ecuaciones cuadráticas")
print("Forma general: ax² + bx + c = 0")

# Solicitamos al usuario los coeficientes
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

# Verificamos si a es cero: no sería una ecuación cuadrática
if a == 0:
    print("❗ Esto no es una ecuación cuadrática.")
else:
    # Calculamos el discriminante: b^2 - 4ac
    discriminante = b**2 - 4 * a * c

    # Caso 1: Dos raíces reales y distintas
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        print(f"✅ Raíces reales y distintas: x1 = {x1:.2f}, x2 = {x2:.2f}")

    # Caso 2: Una raíz real doble
    elif discriminante == 0:
        x = -b / (2 * a)
        print(f"✅ Raíz doble: x = {x:.2f}")

    # Caso 3: Raíces complejas (discriminante negativo)
    else:
        parte_real = -b / (2 * a)
        parte_imaginaria = math.sqrt(abs(discriminante)) / (2 * a)
        print("❓ Raíces complejas:")
        print(f"x1 = {parte_real:.2f} + {parte_imaginaria:.2f}i")
        print(f"x2 = {parte_real:.2f} - {parte_imaginaria:.2f}i")
