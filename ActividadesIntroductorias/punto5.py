# INICIALIZO TOTAL
total = 0

# ACUMULO PRECIOS INGRESADOS
while True:
    precio = float(input("Ingrese el precio del producto (ingresar 0 para finalizar):"))
    if precio == 0:
        break # TERMINA LA ITERACION SI SE CUMPLE LA CONDICION
    total += precio

print(f"Precio total {total}")