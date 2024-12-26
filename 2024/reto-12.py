
# Reto: https://adventjs.dev/es/challenges/2024/12

# Estás en un mercado muy especial en el que se venden árboles de Navidad 🎄. Cada uno viene decorado
# con una serie de adornos muy peculiares, y el precio del árbol se determina en función de los adornos
# que tiene.
#   - *: Copo de nieve - Valor: 1
#   - o: Bola de Navidad - Valor: 5
#   - ^: Arbolito decorativo - Valor: 10
#   - #: Guirnalda brillante - Valor: 50
#   - @: Estrella polar - Valor: 100

# Normalmente se sumarían todos los valores de los adornos y ya está…

# Pero, ¡ojo! Si un adorno se encuentra inmediatamente a la izquierda de otro de mayor valor, en lugar 
# de sumar, se resta su valor.

def calculatePrice(ornaments):

    values = { '*': 1, 'o': 5, '^': 10, '#': 50, '@': 100 }
    
    total = 0
    i = 0
    
    while i < len(ornaments):
        
        if ornaments[i] not in values:return 'undefined'
            
        current_value = values[ornaments[i]]
        
        if i + 1 < len(ornaments) and ornaments[i + 1] in values:
            if values[ornaments[i + 1]] > current_value:total -= current_value
            else:total += current_value
        else:total += current_value
            
        i += 1
        
    return total