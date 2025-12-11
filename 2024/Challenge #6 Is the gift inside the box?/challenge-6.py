
# Reto: https://adventjs.dev/es/challenges/2024/6

# Ya hemos empaquetado cientos de regalos 🎁… pero a un elfo se le ha
# olvidado revisar si el regalo, representado por un asterisco *, está 
# dentro de la caja.

# La caja tiene un regalo (*) y cuenta como dentro de la caja si:
#   - Está rodeada por # en los bordes de la caja.
#   - El * no está en los bordes de la caja.

# Ten en cuenta entonces que el * puede estar dentro, fuera o incluso no estar. 
# Y debemos devolver true si el * está dentro de la caja y false en caso contrario.

def inBox(box):
    
    found = False
    
    for i in range(1, len(box)-1):
        for j in range(1, len(box[i])-1):
            if box[i][j] == '*':
                found = True                
                if '#' not in [box[i-1][j], box[i+1][j], box[i][j-1], box[i][j+1]]:
                    return False
    
    return found