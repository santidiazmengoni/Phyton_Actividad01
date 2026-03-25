# INGRESO LISTA DE PALABRAS
palabras = input("Ingrese una lista de palabras separadas por espacios: ")

# CONVIERTO A LISTA
lista_palabras = palabras.split() # DEFAULT SEPARA POR " "

# CREO LISTA DE PALABRAS MAYORES A 3 LETRAS
palabras_largas = []

for p in lista_palabras:
    if len(p) > 3:
        palabras_largas.append(p)

oracion = " ".join(palabras_largas)

# IMPRIMO 
print(f"La oracion final es: {oracion}")

