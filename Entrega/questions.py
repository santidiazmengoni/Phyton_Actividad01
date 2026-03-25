import random

words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
] 

word = random.choice(words)
guessed = []
attempts = 6

print("¡Bienvenido al Ahorcado!")
print()

# INICIALIZO VARIABLE DEL PUNTAJE
puntaje = 0

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

print(f"Puntaje del jugador: {puntaje}")