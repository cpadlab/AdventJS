
# Reto: https://adventjs.dev/es/challenges/2024/7

# ¡El grinch 👹 ha pasado por el taller de Santa Claus! Y menudo desastre ha montado. 
# Ha cambiado el orden de algunos paquetes, por lo que los envíos no se pueden realizar.

# Por suerte, el elfo Pheralb ha detectado el patrón que ha seguido el grinch para 
# desordenarlos. Nos ha escrito las reglas que debemos seguir para reordenar los paquetes. 
# Las instrucciones que siguen son:

# Recibirás un string que contiene letras y paréntesis.

# Cada vez que encuentres un par de paréntesis, debes voltear el contenido dentro de ellos.

# Si hay paréntesis anidados, resuelve primero los más internos.

# Devuelve el string resultante con los paréntesis eliminados, pero con el contenido volteado 
# correctamente.

def fix_packages(packages):
    
    if '(' not in packages:
        return packages
    
    start = packages.rindex('(')
    count = 1
    end = start + 1
    
    while count > 0 and end < len(packages):
        if packages[end] == '(':
            count += 1
        elif packages[end] == ')':
            count -= 1
        end += 1
    
    before = packages[:start]
    inside = packages[start + 1:end - 1][::-1]
    after = packages[end:]
    
    return fix_packages(before + inside + after)