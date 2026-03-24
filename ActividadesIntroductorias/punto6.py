# INGRESO NUMERO N
N = int(input("Ingrese un numero: "))

# CREO LISTAS
numeros_restantes = []
multiplos_5 = []

# AGREGO A LISTAS
for i in range(1, N + 1):
    if i % 5 == 0:
        multiplos_5.append(i)
    else:
        numeros_restantes.append(i)

# IMPRIMO LISTAS
print(f"Multiplos de 5: {multiplos_5}")
print(f"Numeros restantes: {numeros_restantes}")


