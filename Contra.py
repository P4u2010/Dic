import random

# Definir los caracteres posibles para la contraseña
caracteres_contrasena = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Solicitar al usuario la longitud de la contraseña
longitud_contrasena = int(input("Introduce la longitud de la contraseña: "))

# Variable para almacenar la contraseña generada
contrasena_generada = ""

# Generar la contraseña aleatoria
for _ in range(longitud_contrasena):
    contrasena_generada += random.choice(caracteres_contrasena)


print(f"Contraseña generada: {contrasena_generada}")
