# INGRESO NUMERO N
N = int(input("Ingrese un numero: "))

# IMPRIMO DEL 1 AL N SIN MULTIPLOS DE 5
for i in range(N):
    if i % 5 == 0:
        continue # SALTEA LO QUE CUMPLA LA CONDICION
    print(i)

