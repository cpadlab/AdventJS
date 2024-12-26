
# Reto: https://adventjs.dev/es/challenges/2024/16

# Los elfos están trabajando arduamente para limpiar los caminos llenos de nieve mágica ❄️.
# Esta nieve tiene una propiedad especial: si dos montículos de nieve idénticos y adyacentes
# se encuentran, desaparecen automáticamente.

# Tu tarea es escribir una función que ayude a los elfos a simular este proceso. El camino se
# representa por una cadena de texto y cada montículo de nieve un carácter.

# Tienes que eliminar todos los montículos de nieve adyacentes que sean iguales hasta que no
# queden más movimientos posibles.

def remove_snow(s: str) -> str:
    stack = []

    for char in s:
        if stack and stack[-1] == char:stack.pop()
        else:stack.append(char)

    return "".join(stack)