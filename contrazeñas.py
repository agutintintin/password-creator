import random
digitos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

long = int( input("Escribe la longuitud de la contraseña") )
pasword = ""

for i in range( long ):
    pasword += random.choice(digitos)
print("La contrseña es:", pasword)
     
