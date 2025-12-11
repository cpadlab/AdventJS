
# Reto: https://adventjs.dev/es/challenges/2024/5

# Los elfos 🧝🧝‍♂️ de Santa Claus han encontrado un montón de botas mágicas desordenadas
# en el taller. Cada bota se describe por dos valores:
#   - type indica si es una bota izquierda (I) o derecha (R).
#   - size indica el tamaño de la bota.

# Tu tarea es ayudar a los elfos a emparejar todas las botas del mismo tamaño que tengan
# izquierda y derecha. Para ello, debes devolver una lista con los pares disponibles después
# de emparejar las botas.

# ¡Ten en cuenta que puedes tener más de una zapatilla emparejada del mismo tamaño!

def organizeShoes(shoes):

    shoe_pairs = {}
    
    for shoe in shoes:
        size = shoe['size']
        type_ = shoe['type']
        
        if size not in shoe_pairs:
            shoe_pairs[size] = {'I': 0, 'R': 0}
        shoe_pairs[size][type_] += 1
    
    result = []
    for size, counts in shoe_pairs.items():    
        pairs = min(counts['I'], counts['R'])
        result.extend([size] * pairs)
    
    return sorted(result)