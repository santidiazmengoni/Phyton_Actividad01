# INGRESO CANTIDAD DE SEGUNDOS
segundos = int(input("Ingrese la cantidad de segundos: "))

# CALCULO HORAS, MINUTOS Y SEGUNDOS
horas = segundos // 3600

# CALCULO EL RESTO PARA SABER LOS MINUTOS Y SEGUNDOS RESTANTES EN BASE A ESO
resto = segundos % 3600

minutos = resto // 60
segundos_restantes = resto % 60

print(f"{segundos} son {horas} horas, {minutos} minutos y {segundos_restantes} segundos")