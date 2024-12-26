
# Reto: https://adventjs.dev/es/challenges/2024/14

# Los renos necesitan moverse para ocupar los establos, pero no puede haber
# más de un reno por establo. Además, para que los renos estén cómodos, debemos
# minimizar la distancia total que recorren para acomodarse.

#Tenemos dos parámetros:
#   - reindeer: Un array de enteros que representan las posiciones de los renos.
#   - stables: Un array de enteros que representan las posiciones de los establos.

# Hay que mover cada reno, desde su posición actual, hasta un establo. Pero hay
# que tener en cuenta que sólo puede haber un reno por establo.

# Tu tarea es calcular el mínimo número de movimientos necesarios para que todos los
# renos acaben en un establo.

# Nota: Ten en cuenta que el array de establos siempre tendrá el mismo tamaño que el 
# array de renos y que siempre los establos serán únicos.

def min_moves_to_stables(reindeer, stables):
    
    reindeer.sort()
    stables.sort()
    
    total_moves = 0
    for r, s in zip(reindeer, stables):
        total_moves += abs(r - s)
    
    return total_moves