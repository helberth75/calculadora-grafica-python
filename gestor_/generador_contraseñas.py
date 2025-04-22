import random
import string

def generar_contraseña(longitud_min=8, longitud_max=16, incluir_simbolos=True):
    # Asegurarnos de que la longitud esté dentro del rango
    if longitud_min < 1:
        raise ValueError("La longitud mínima debe ser al menos 1.")
    if longitud_max < longitud_min:
        raise ValueError("La longitud máxima no puede ser menor que la longitud mínima.")
    
    # Elegir una longitud aleatoria dentro del rango
    longitud = random.randint(longitud_min, longitud_max)
    
    # Definir el conjunto de caracteres
    caracteres = string.ascii_letters + string.digits  # Letras y números
    if incluir_simbolos:
        caracteres += string.punctuation  # Agregar caracteres especiales
    
    # Generar una contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return contraseña

# Interacción con el usuario
def main():
    longitud_min = int(input("Introduce la longitud mínima de la contraseña: "))
    longitud_max = int(input("Introduce la longitud máxima de la contraseña: "))
    incluir_simbolos = input("¿Quieres incluir símbolos especiales? (sí/no): ").lower() == "sí"
    
    # Generar la contraseña
    try:
        contraseña = generar_contraseña(longitud_min, longitud_max, incluir_simbolos)
        print(f"Contraseña generada: {contraseña}")
    except ValueError as e:
        print(f"Error: {e}")

# Ejecutar el programa
if __name__ == "__main__":
    main()