# print("Bienvenido al Juego de Adivinanza de Palabras!")
# print("La configuración inicial del juego se ha completado.")

# src/main.py
from word_selector import seleccionar_palabra
from game_logic import adivinar_letra

def main():
    # Seleccionar la palabra secreta
    palabra = seleccionar_palabra()

    # Inicializar el progreso con guiones bajos y los intentos restantes
    progreso = ['_'] * len(palabra)
    intentos_restantes = 5  # Número máximo de intentos permitidos


    print(f"Palabra: {' '.join(progreso)}")

    # Bucle principal del juego
    while intentos_restantes > 0 and '_' in progreso:
        # Solicitar al jugador que adivine una letra
        letra = input("Adivina una letra: ").lower()

        # Llamar a la función adivinar_letra para verificar la letra y actualizar el progreso
        progreso, intentos_restantes, mensaje = adivinar_letra(letra, palabra, progreso, intentos_restantes)

        # Mostrar el mensaje de retroalimentación
        print(mensaje)
        print(f"Palabra: {' '.join(progreso)}")

    # Verificar si el jugador ganó o perdió
    if '_' not in progreso:
        print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
    else:
        print(f"Lo siento, has perdido. La palabra era: {palabra}")

# Ejecutar la función main() si se llama directamente este archivo
if __name__ == "__main__":
    main()
