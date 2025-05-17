# Calculadora de Propinas con división entre personas

# Paso 1: Pedir el total de la cuenta
total_cuenta = float(input("Ingrese el total de la cuenta: $"))

# Paso 2: Pedir el porcentaje de propina
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))

# Paso 3: Pedir cuántas personas van a pagar
cantidad_personas = int(input("¿Cuántas personas pagarán la cuenta? "))

# Paso 4: Calcular el valor de la propina
valor_propina = total_cuenta * porcentaje_propina / 100

# Paso 5: Calcular el total a pagar (cuenta + propina)
total_pagar = total_cuenta + valor_propina

# Paso 6: Calcular cuánto paga cada persona
monto_por_persona = total_pagar / cantidad_personas

# Paso 7: Mostrar los resultados
print("\n--- Detalle de la cuenta ---")
print("Propina: $", round(valor_propina, 2))
print("Total a pagar (con propina): $", round(total_pagar, 2))
print("Cada persona debe pagar: $", round(monto_por_persona, 2))
