
// Reto: https://adventjs.dev/es/challenges/2024/

// Los elfos están trabajando en un sistema para verificar las listas de regalos de 
// los niños 👧👦. Sin embargo, ¡algunas listas están incompletas y faltan números!

// Tu tarea es escribir una función que, dado un array de números, encuentre todos los
// números que faltan entre 1 y n (donde n es el tamaño del array o el número más alto 
// del array).

// Eso sí, ten en cuenta que:
//  - Los números pueden aparecer más de una vez y otros pueden faltar
//  - El array siempre contiene números enteros positivos
//  - Siempre se empieza a contar desde el 1

function findMissingNumbers(nums: number[]): number[] {
    const limit:number = Math.max(...nums);
    let values = new Array(limit).fill(0).map((_,i) => i + 1)    
    
    const c1 = new Set(nums)
    const c2 = new Set(values)

    return [...c2.difference(c1)]
}