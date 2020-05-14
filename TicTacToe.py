class TaTeTi:

    def __init__(self, celdas='         '):
        self.celdas = celdas
        self.lineas = [[x for x in self.celdas[:3]], [x for x in self.celdas[3:6]], [x for x in self.celdas[6:9]]]

    def columnas(self):
        return [[linea[i] for linea in self.lineas] for i in range(3)]

    def diagonales(self):
        return [[self.lineas[i][i] for i in range(3)], [self.lineas[i][-(i+1)] for i in range(3)]]

    def __str__(self):
        cadena = ["---------"]
        for linea in self.lineas:
            cadena.append("| " + " ".join(linea) + " |")
        cadena.append("---------")
        return '\n'.join(cadena)

    def check_bingo(self):
        bingo = 0
        for linea in self.lineas:
            if set(linea) == {"O"} or set(linea) == {"X"}:
                bingo += 1
        for columna in self.columnas():
            if set(columna) == {"O"} or set(columna) == {"X"}:
                bingo += 1
        for diagonal in self.diagonales():
            if set(diagonal) == {"O"} or set(diagonal) == {"X"}:
                bingo += 1
        return bingo


turno = 1

miJuego = TaTeTi("         ")
print(miJuego)

while miJuego.check_bingo() == 0 and turno < 10:
    print("Enter the coordinates:", end="")
    coordenadas = input()
    if len(coordenadas.split()) > 1:
        columna, fila = coordenadas.split()
        if not columna.isnumeric() or not fila.isnumeric():
            print("You should enter numbers!")
        elif not 1 <= int(columna) <= 3 or not 1 <= int(fila) <= 3:
            print("Coordinates should be from 1 to 3!")
        elif miJuego.lineas[abs(int(fila) - 3)][int(columna) - 1] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            if turno % 2 != 0:
                miJuego.lineas[abs(int(fila) - 3)][int(columna) - 1] = "X"
                print(miJuego)
                turno += 1
            else:
                miJuego.lineas[abs(int(fila)-3)][int(columna)-1] = "O"
                print(miJuego)
                turno += 1
    else:
        print("You should enter numbers!")
if miJuego.check_bingo() == 0:
    print("Draw")
else:
    if turno % 2:
        print("O wins")
    else:
        print("X wins")
