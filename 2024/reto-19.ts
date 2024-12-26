
// Reto: https://adventjs.dev/es/challenges/2024/19

// ¡Se acerca el día para repartir regalos! Necesitamos apilar los regalos que 
// transportaremos en el trineo 🛷 y para eso los vamos a meter en cajas 📦.

// Los regalos se pueden meter en 4 cajas distintas, donde cada caja soporta
//  1, 2, 5, 10 de peso y se representan así:

/*
1: |_|
*/

// Tu misión es que al recibir el peso de los regalos, uses las mínimas cajas posibles
//  y que, además, las apiles de menos peso (arriba) a más peso (abajo). Siempre 
// alineadas a la izquierda.

// Además, ten en cuenta que al apilarlas, se reusa el borde inferior de la caja.

/*
distributeWeight(1)
// Devuelve:
//  _
// |_|
*/

// Nota: ¡Ten cuidado con los espacios en blanco! No añadas espacios en blanco a la 
// derecha de una caja si no son necesarios.

type BoxRepresentations = {
    1: string[]
    2: string[]
    5: string[]
    10: string[]
}
  
function distributeWeight(weight: number): string {

    const weights = [10, 5, 2, 1]
    const boxRepresentations: BoxRepresentations = { 1: [" _ ", "|_|"] , 2: [" ___ ", "|___|"], 5: [" _____ ", "|     |", "|_____|"], 10: [" _________ ", "|         |", "|_________|"] }
    let remainingWeight = weight
    let boxes: (keyof BoxRepresentations)[] = []
  
    for (let i = 0; i < weights.length; i++) {
        if(weights[i] <= remainingWeight) {
            remainingWeight -= weights[i]
            boxes.push(weights[i] as keyof BoxRepresentations)
            i = -1
        }
    }
  
    boxes.reverse()
  
    if(boxes.length <= 1) {return boxRepresentations[boxes[0] as keyof BoxRepresentations].join('\n')}
  
    let result: string = ''

    console.log('boxes length', boxes.length)

    for (let i = 0; i < boxes.length; i++) {
        const currentBox = [...boxRepresentations[boxes[i]]]
        if(boxRepresentations[boxes[i + 1]]) {
            
            const nextBox = [...boxRepresentations[boxes[i + 1]]]
            currentBox[currentBox.length - 1] += nextBox[0].slice(currentBox[currentBox.length - 1].length)
            nextBox.shift()
            
            if(i > 0) {currentBox.shift()}

            currentBox[currentBox.length - 1] = currentBox[currentBox.length - 1].trim()
            let currentBoxStr = currentBox.join('\n')
            result += currentBoxStr + '\n'

        } else {
            currentBox.shift()
            let currentBoxStr = currentBox.join('\n')
            result += currentBoxStr
        }
    }
    
    return result
}