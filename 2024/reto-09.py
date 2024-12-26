
# Reto: https://adventjs.dev/es/challenges/2024/9

# Los elfos están jugando con un tren 🚂 mágico que transporta regalos. Este tren
#  se mueve en un tablero representado por un array de strings.

# El tren está compuesto por una locomotora (@), seguida de sus vagones (o), y debe
# recoger frutas mágicas (*) que le sirve de combustible. El movimiento del tren sigue
# las siguientes reglas:

# Recibirás dos parámetros board y mov.
#   - board es un array de strings que representa el tablero:
#   - @ es la locomotora del tren.
#   - o son los vagones del tren.
#   - * es una fruta mágica.
#   - · son espacios vacíos.

# mov es un string que indica el próximo movimiento del tren desde la cabeza del tren @:
#   - 'L': izquierda
#   - 'R': derecha
#   - 'U': arriba
#   - 'D': abajo.

# Con esta información, debes devolver una cadena de texto:
#   - 'crash': Si el tren choca contra los bordes del tablero o contra sí mismo.
#   - 'eat': Si el tren recoge una fruta mágica (*).
#   - 'none': Si avanza sin chocar ni recoger ninguna fruta mágica.

from typing import List, Literal

def moveTrain(board: List[str], mov: Literal['U', 'D', 'R', 'L']) -> Literal['none', 'crash', 'eat']:
  
    for i, row in enumerate(board):
        if '@' in row:
            x, y = i, row.index('@')
            break

    if mov == 'U':new_x, new_y = x - 1, y
    elif mov == 'D':new_x, new_y = x + 1, y
    elif mov == 'L':new_x, new_y = x, y - 1
    elif mov == 'R':new_x, new_y = x, y + 1

    if new_x < 0 or new_x >= len(board) or new_y < 0 or new_y >= len(board[0]):return 'crash'
    if board[new_x][new_y] in ['@', 'o']:return 'crash'

    if board[new_x][new_y] == '*':return 'eat'

    return 'none'