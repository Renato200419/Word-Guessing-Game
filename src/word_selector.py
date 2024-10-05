# src/word_selector.py
import random

def seleccionar_palabra():
    #Selecciona una palabra aleatoria de words.txt y devuelve un mensaje de confirmación.
    with open('words.txt', 'r') as file:
        palabras = file.readlines()
    palabra_seleccionada = random.choice(palabras).strip()
    print("La palabra ha sido seleccionada. ¡Comienza a adivinar!")
    return palabra_seleccionada
