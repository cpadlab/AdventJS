
# Reto: https://adventjs.dev/es/challenges/2024/21

# Santa Claus 🎅 está decorando un árbol de Navidad mágico 🪄, que este año tiene una 
# estructura especial en forma de árbol binario. Cada nodo del árbol representa un regalo,
#  y Santa quiere saber la altura del árbol para colocar la estrella mágica en la punta.

# Tu tarea es escribir una función que calcule la altura de un árbol binario. La altura 
# de un árbol binario se define como el número máximo de niveles desde la raíz hasta una 
# hoja. Un árbol vacío tiene una altura de 0.

def tree_height(tree):
    if tree is None:return 0
    if tree.get('left') is None and tree.get('right') is None:return 1
    return max(tree_height(tree.get('left')), tree_height(tree.get('right'))) + 1