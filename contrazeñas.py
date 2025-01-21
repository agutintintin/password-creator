import random
digitos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

long = int( input("Escribe la longuitud de la contraseña") )
password = ""

for i in range( long ):
    password += random.choice(digitos)
print("La contraseña es:", password)
     
