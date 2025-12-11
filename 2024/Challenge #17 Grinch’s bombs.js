
// Reto: https://adventjs.dev/es/challenges/2024/17

// El Grinch ha estado haciendo de las suyas en el Polo Norte y ha sembrado bombas de carbón explosivo 💣 en la 
// fábrica de juguetes de los duendes. Quiere que todos los juguetes queden inutilizados y por eso ha dejado una
// cuadrícula donde algunas celdas tienen carbón explosivo (true) y otras están vacías (false).

// Los duendes necesitan tu ayuda para mapear las zonas peligrosas. Cada celda vacía debe mostrar un número que 
// indique cuántas bombas de carbón explosivo hay en las posiciones adyacentes, incluidas las diagonales.

function detectBombs(grid) {
    
    const result = [];
    const parsedValue = { true: 1, false: 0, undefined: 0 };

    for (let i = 0; i < grid.length; i++) {
        for (let j=0; j<grid[0]?.length; j++) {
            
            result[i] = result[i] ?? [];

            const ySide = parsedValue[grid[i-1]?.[j]] + parsedValue[grid[i+1]?.[j]];
            const xSide = parsedValue[grid[i]?.[j-1]] + parsedValue[grid[i]?.[j+1]];
            const upperDiagonal = parsedValue[grid[i-1]?.[j-1]] + parsedValue[grid[i-1]?.[j+1]];
            const lowerDiagonal = parsedValue[grid[i+1]?.[j-1]] + parsedValue[grid[i+1]?.[j+1]];

            result[i][j] = ySide + xSide + upperDiagonal + lowerDiagonal;
        }
    }

    return result;

}