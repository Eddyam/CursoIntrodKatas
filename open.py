""" def main():
    open("/path/to/mars.jpg")

if __name__ == "__main__":
    main() """

# Controlando excepciones
try:
    open('config.txt')
except FileNotFoundError:
    print("No se pudo encontrar el archivo config.txt")

