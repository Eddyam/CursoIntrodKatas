# Se genera error tipo Is a directory config.txt
""" def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se pudo encontrar el archivo config.txt")

if __name__ == '__main__':
    main() """

#Manejar de las excepciones FileNotFoundError y PermissionError
""" def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se pudo encontrar el archivo config.txt")
    except IsADirectoryError:
        print("Se encontro config.txt pero es un directorio, no se puede leer.")
    except PermissionError:
        print("El archivo tiene errores de permiso.")

"""

# Agrupar excepciones de la misma naturaleza
""" def main():
    try:
        configuration = open('configt.txt')
    except FileNotFoundError:
        print("No se pudo encontrar el archivo config.txt")
    except IsADirectoryError:
        print("Se encontro config.txt pero es un directorio, no se puede leer...")
    except (BlockingIOError, TimeoutError):
        print("Sistema de archivos con mucha carga, no se puede completar la lectura del archivo de configuración")

if __name__ == '__main__':
    main() """ 

# Acceder al error asociado a la excepcion
try:
    open("mars.jpg")
except FileNotFoundError as err:
    print("Hay un problema intentando leer el archivo", err)

# Acceder directamente a los atributos de error. 

try:
    open("mars.jpg")
except OSError as err:
    if err.errno == 2:
        print("No se puedo encontrar el archivo mars.jpg")
    elif err.errno == 13:
        print("Se encontro config.txt pero no se puede leer.")

# Generacion de excepciones
def water_left(astronauts, water_left, days_left):
    #Excepcion de tipo de dato no admitidos con TypeError
    for argument in [astronauts, water_left, days_left]:
        try:
            argument / 10
        except TypeError:
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")

    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    
    # Verifica falta de agua 
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")

    return f"Total water left after {days_left} days is: {total_water_left} liters."


print(water_left("5",100,2))