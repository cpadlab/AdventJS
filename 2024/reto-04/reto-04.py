
# Reto: https://adventjs.dev/es/challenges/2024/4

# ¡Es hora de poner el árbol de Navidad en casa! 🎄 Pero este año queremos que sea especial.
# Vamos a crear una función que recibe la altura del árbol (un entero positivo entre 1 y 100)
# y un carácter especial para decorarlo.

# La función debe devolver un string que represente el árbol de Navidad, construido
#  de la siguiente manera:
#   - El árbol está compuesto de triángulos de caracteres especiales.
#   - Los espacios en blanco a los lados del árbol se representan con guiones bajos _.
#   - Todos los árboles tienen un tronco de dos líneas, representado por el carácter #.
#   - El árbol siempre debe tener la misma longitud por cada lado.
#   - Debes asegurarte de que el árbol tenga la forma correcta usando saltos de línea \n para cada línea.

def create_xmas_tree(height, ornament):
    
    tree = ''

    for i in range(1, height + 1):
        
        spaces = '_' * (height - i)
        tree += spaces + ornament * (2 * i - 1) + spaces + '\n'

    trunk = '_' * (height - 1) + '#' + '_' * (height - 1)
    tree += trunk + '\n'
    tree += trunk

    return tree