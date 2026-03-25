import random

# AGRUPO LA LISTA DE PALABRAS POR CATEGORÍAS
categorias = {
    "tipos_datos": ["cadena", "entero", "lista"],
    "conceptos": ["python", "programa", "variable", "funcion", "bucle"]
}

print("¡Bienvenido al Ahorcado!")
print()

# MUESTRO CATEGORIAS DISPONIBLES
print("Categorías disponibles:")
for cat in categorias:
    print(f". {cat}")

# ELEGIR CATEGORIA POSIBLE
categoria = input("Elegí una categoría: ")
while categoria not in categorias:
    categoria = input("Categoría inválida, elegí nuevamente entre las de la lista: ")

print()

# CREO NUEVA LISTA DE PALABRAS DE LA CATEGORIA SELECCIONADA 
palabras = categorias[categoria]

# PARA QUE NO SE REPITAN LAS PALABRAS EN LAS SIGUIENTES RONDAS UTILIZO EL random.sample()
palabras_sample = random.sample(palabras,len(palabras)) # CANTIDAD DE RONDAS = CANTIDAD DE PALABRAS EN LA CATEGORIA

# AGREGO PUNTAJE TOTAL PARA EL FIN DEL JUEGO
puntaje_total = 0 

# AGREGO LA ITERACION DEL FOR PARA JUGAR VARIAS RONDAS
for word in palabras_sample:

    # INICIALIZO LAS VARIABLES DENTRO DEL FOR PARA CADA RONDA
    guessed = []
    attempts = 6
    puntaje = 0

    # MENSAJE DE INICIO DE RONDA
    print("Nueva Palabra")
    print()

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
    
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            puntaje += 6 # 6 PUNTOS SI ADIVINA LA PALABRA
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")

        # AGREGO MODIFICACIÓN, NO SE PUEDE INGRESAR MAS DE UNA LETRA, UN NÚMERO O OTRO CARÁCTER INVÁLIDO
        if len(letter) > 1 or not letter.isalpha():
            print(f"Entrada no válida")
            print()
            continue

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje -= 1 # -1 PUNTO SI LA LETRA ES INCORRECTA
            print("Esa letra no está en la palabra.")
    
        print()

    else:
        puntaje = 0 # PERDER DEJA EL PUNTAJE EN 0
        print(f"¡Perdiste! La palabra era: {word}")

    # MODIFICO EL MENSAJE PARA MOSTRAR EL PUNTAJE DE CADA RONDA
    print(f"Puntaje de la ronda: {puntaje}")
    print()

    puntaje_total += puntaje # ACUMULO EL PUNTAJE

# MENSAJE FINAL DEL JUEGO
print(f"No quedan mas palabras dentro de la categoría seleccionada, puntaje total: {puntaje_total}. Fin del juego.")