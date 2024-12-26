
// Reto: https://adventjs.dev/es/challenges/2024/24

// En el Polo Norte, los elfos tienen dos árboles binarios mágicos que generan energía 🌲🌲 
// para mantener encendida la estrella navideña ⭐️. Sin embargo, para que funcionen correctamente,
// los árboles deben estar en perfecta sincronía como espejos 🪞.

// Dos árboles binarios son espejos si:
//  - Las raíces de ambos árboles tienen el mismo valor.
//  - Cada nodo del primer árbol debe tener su correspondiente nodo en la posición opuesta en el segundo árbol.

// Y el árbol se representa con tres propiedades value, left y right. Dentro de estas dos últimas 
// va mostrando el resto de ramas (si es que tiene):

function isTreesSynchronized(tree1, tree2) {
    
    if (!tree1) {return [true, ''];}
    if (tree1.value !== tree2.value) {return [false, tree1.value];}

    const sinc1 = isTreesSynchronized(tree1.left, tree2.right)[0];
    const sinc2 = sinc1 && isTreesSynchronized(tree1.right, tree2.left)[0];

    return [sinc1 && sinc2, tree1.value];
}