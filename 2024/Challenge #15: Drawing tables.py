
# Reto: https://adventjs.dev/es/challenges/2024/15

# Al Polo Norte ha llegado ChatGPT y el elfo Sam Elfman está trabajando en una
# aplicación de administración de regalos y niños.

# Para mejorar la presentación, quiere crear una función drawTable que reciba un
# array de objetos y lo convierta en una tabla de texto.

#La tabla dibujada debe representar los datos del objeto de la siguiente manera:
#   - Tiene una cabecera con el nombre de la columna.
#   - El nombre de la columna pone la primera letra en mayúscula.
#   - Cada fila debe contener los valores de los objetos en el orden correspondiente.
#   - Cada valor debe estar alineado a la izquierda.
#   - Los campos dejan siempre un espacio a la izquierda.
#   - Los campos dejan a la derecha el espacio necesario para alinear la caja.

def draw_table(data: list[dict[str, str | int]]) -> str:

    columns = list(data[0].keys())
    max_lengths = {col: len(col.capitalize()) for col in columns}

    for row in data:
        for col in columns:max_lengths[col] = max(max_lengths[col], len(str(row[col])))

    def format_row(row: list[str]) -> str:return "| " + " | ".join(f"{val.ljust(max_lengths[col])}" for val, col in zip(row, columns)) + " |"
    separator = "+" + "+".join("-" * (max_lengths[col] + 2) for col in columns) + "+"

    return "\n".join([separator, format_row([col.capitalize() for col in columns]), separator] + [format_row([str(row[col]) for col in columns]) for row in data] + [separator])