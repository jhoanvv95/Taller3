import random

def generar_tablero(dimensiones=5, letra_principal='0', letra_buscar='8'):
    # Crear un tablero con la letra principal
    tablero = [[letra_principal for _ in range(dimensiones)] for _ in range(dimensiones)]
    
    # Posicionar la letra a buscar aleatoriamente
    pos_x = random.randint(0, dimensiones - 1)
    pos_y = random.randint(0, dimensiones - 1)
    tablero[pos_x][pos_y] = letra_buscar
    
    return tablero

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))

def main():
    # Obtener las dimensiones y letras del usuario
    dimensiones = input("Ingrese las dimensiones del tablero (por defecto 5x5): ")
    dimensiones = int(dimensiones) if dimensiones else 5
    
    letra_principal = input("Ingrese la letra principal (por defecto '0'): ")
    letra_principal = letra_principal if letra_principal else '0'
    
    letra_buscar = input("Ingrese la letra a buscar (por defecto '8'): ")
    letra_buscar = letra_buscar if letra_buscar else '8'
    
    # Generar y mostrar el tablero
    tablero = generar_tablero(dimensiones, letra_principal, letra_buscar)
    imprimir_tablero(tablero)

if __name__ == "__main__":
    main()
