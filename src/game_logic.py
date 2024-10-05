# src/game_logic.py

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