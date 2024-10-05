# src/game_logic.py
import random

def adivinar_letra(letra, palabra, progreso, intentos_restantes):
    # Verificar si la letra está en la palabra secreta
    if letra in palabra:
        # Actualizar el progreso con la letra adivinada
        progreso = [letra if letra == c else progreso[i] for i, c in enumerate(palabra)]
        mensaje = f"¡Correcto! La letra '{letra}' está en la palabra."
    else:
        # Reducir el número de intentos restantes si la letra no está en la palabra
        intentos_restantes -= 1
        mensaje = f"La letra '{letra}' no está en la palabra. Te quedan {intentos_restantes} intentos."

    # Retornar el progreso actualizado, los intentos restantes y el mensaje
    return progreso, intentos_restantes, mensaje

def dar_pista(palabra, progreso, pistas_disponibles):
    # Verificar si hay pistas disponibles
    if pistas_disponibles > 0:
        # Crear una lista de letras que aún no han sido adivinadas
        letras_faltantes = [letra for letra, prog in zip(palabra, progreso) if prog == '_']

        # Seleccionar una letra aleatoria de las letras faltantes
        if letras_faltantes:
            pista = random.choice(letras_faltantes)
            # Actualizar el progreso con la letra revelada
            progreso = [pista if c == pista else p for c, p in zip(palabra, progreso)]
            pistas_disponibles -= 1  # Reducir la cantidad de pistas disponibles
            mensaje = f"Pista: La letra '{pista}' está en la palabra."
        else:
            mensaje = "No quedan letras por revelar."
    else:
        mensaje = "No te quedan pistas disponibles."
    
    return progreso, pistas_disponibles, mensaje