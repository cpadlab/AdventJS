
// Reto: https://adventjs.dev/es/challenges/2024/25

function execute(code) {
    let acc = 0
    
    const processCode = (block) => {
        let i = 0;
        while (i < block.length) {
            const curr = block[i];

            if (curr === '+') {acc++;
            } else if (curr === '-') {acc--;
            } else if (curr === '[') {
                const end = block.indexOf(']', i);
                const newCode = block.slice(i + 1, end);
                while (acc !== 0) {processCode(newCode);}
                i = end;
            } else if (curr === '{') {
                if (acc === 0) {i = block.indexOf('}', i);}
            }
            i++;
        }
    };

    code = code.replaceAll('>', '');
    processCode(code);

    return acc
}