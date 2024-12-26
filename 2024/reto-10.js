
// Reto: https://adventjs.dev/es/challenges/2024/10

// Los elfos programadores están creando un pequeño ensamblador mágico para controlar las 
// máquinas del taller de Santa Claus.

// Para ayudarles, vamos a implementar un intérprete sencillo que soporte las siguientes 
// instrucciones mágicas:
//   - MOV x y: Copia el valor x (puede ser un número o el contenido de un registro) en el registro y
//   - INC x: Incrementa en 1 el contenido del registro x
//   - DEC x: Decrementa en 1 el contenido del registro x
//   - JMP x y: Si el valor del registro x es 0 entonces salta a la instrucción en el índice y y sigue ejecutándose el programa desde ahí.

// Comportamiento esperado:
//   - Si se intenta acceder, incrementar o decrementar a un registro que no ha sido inicializado, se tomará el valor 0 por defecto.
//   - El salto con JMP es absoluto y lleva al índice exacto indicado por y.
//   - Al finalizar, el programa debe devolver el contenido del registro A. Si A no tenía un valor definido, retorna undefined.

function compile(instructions) {
    
    const registers = {};
    let i = 0;

    while (i < instructions.length) {

        const instruction = instructions[i];
        const parts = instruction.split(' ');
    
        switch (parts[0]) {

            case 'MOV':
                const value = isNaN(parts[1]) ? (registers[parts[1]] || 0) : parseInt(parts[1], 10);
                registers[parts[2]] = value;
                break;
    
            case 'INC':
                const regInc = parts[1];
                registers[regInc] = (registers[regInc] || 0) + 1;
                break;
    
            case 'DEC':
                const regDec = parts[1];
                registers[regDec] = (registers[regDec] || 0) - 1;
                break;
    
            case 'JMP':
                const regJmp = parts[1];
                const indexJmp = parseInt(parts[2], 10);
                if ((registers[regJmp] || 0) === 0) {
                    i = indexJmp;continue;
                }

            break;
        }

        i++;
    }
    
    return registers['A'] !== undefined ? registers['A'] : undefined;

}