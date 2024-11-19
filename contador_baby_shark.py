
'''   
1) Contar cuantas palabras tiene la cancion en total
2) Contar cuantas veces tiene la palabra shark 
3) Contar cuantas tiene la palabra doo
'''



def contador_total(cancion):  # Cuenta el total de palabras de la canción
     palabras_cancion = cancion.split()
     total_palabras = len(palabras_cancion) 
     return total_palabras

def contador_palabra(cancion,palabra): # Cuenta el total de apariciones de una palabra especifica
    palabras_cancion = cancion.split()
    total_palabras = len(palabras_cancion) 
    rta = palabras_cancion.count(palabra)
    return rta

cancion = '''
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark!
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark!
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark!
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark!
Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt!
Run away, doo doo doo doo doo doo
Run away, doo doo doo doo doo doo
Run away, doo doo doo doo doo doo
Run away!
Safe at last, doo doo doo doo doo doo
Safe at last, doo doo doo doo doo doo
Safe at last, doo doo doo doo doo doo
Safe at last!
It’s the end, doo doo doo doo doo doo
It’s the end, doo doo doo doo doo doo
It’s the end, doo doo doo doo doo doo
It’s the end!
''' 

palabras_cancion = contador_total(cancion)
print("1) La canción tiene: ", palabras_cancion, " palabras en total")

cantidad_shark = contador_palabra(cancion,"shark,")


cantidad_doo = contador_palabra(cancion,"doo")

print("2) La palabra shark se repite:" ,cantidad_shark, " veces")

print("3) La palabra doo se repite:" ,cantidad_doo, " veces")