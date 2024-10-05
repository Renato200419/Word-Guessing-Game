# src/word_selector.py
import random
import os

def seleccionar_palabra():
    """Selecciona una palabra aleatoria de words.txt y muestra un mensaje de confirmación."""
    # Obtener la ruta absoluta del archivo words.txt
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_words = os.path.join(ruta_actual, '../words.txt')
    
    # Abrir el archivo words.txt usando la ruta absoluta
    with open(ruta_words, 'r') as file:
        palabras = file.readlines()

    # Seleccionar una palabra aleatoria
    palabra_seleccionada = random.choice(palabras).strip()

    # Imprimir el mensaje solicitado
    #print("La palabra ha sido seleccionada. ¡Comienza a adivinar!")
    return palabra_seleccionada

