def gato():
    from machine import Pin
    import time
    row_list = [13, 12, 14, 27]
    col_list = [26, 25, 33, 32]
    for x in range(4):
        row_list[x] = Pin(row_list[x], Pin.OUT)
        row_list[x].value(1)
    for x in range(4):
        col_list[x] = Pin(col_list[x], Pin.IN, Pin.PULL_UP)
    key_map = [["D", "#", "0", "*"],
            ["C", "9", "8", "7"],
            ["B", "6", "5", "4"],
            ["A", "3", "2", "1"]]
    def Keypad4x4Read(cols, rows):
        key = None
        for r in rows:
            r.value(0)
            result = [cols[0].value(), cols[1].value(), cols[2].value(), cols[3].value()]
            if 0 in result:
                key = key_map[rows.index(r)][result.index(0)]
            r.value(1)
        return key
    t = time.ticks_ms()
    tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    jugador = 1
    Victoria = 1
    Empate = -1
    corriendo = 0
    Juego = corriendo
    Marca = 'X'
    def DibujarTablero():
        print("\033c")  # Esta línea borra la pantalla de la terminal
        print(" %c | %c | %c " % (tablero[1], tablero[2], tablero[3]))
        print("___|___|___")
        print(" %c | %c | %c " % (tablero[4], tablero[5], tablero[6]))
        print("___|___|___")
        print(" %c | %c | %c " % (tablero[7], tablero[8], tablero[9]))
        print(" | | ")
    def ChecarPosicion(x):
        if tablero[x] == ' ':
            return True
        else:
            return False
    def ChecarVictoria():
        global Juego
        if tablero[1] == tablero[2] and tablero[2] == tablero[3] and tablero[1] != ' ':
            Juego = Victoria
        elif tablero[4] == tablero[5] and tablero[5] == tablero[6] and tablero[4] != ' ':
            Juego = Victoria
        elif tablero[7] == tablero[8] and tablero[8] == tablero[9] and tablero[7] != ' ':
            Juego = Victoria
        elif tablero[1] == tablero[4] and tablero[4] == tablero[7] and tablero[1] != ' ':
            Juego = Victoria
        elif tablero[2] == tablero[5] and tablero[5] == tablero[8] and tablero[2] != ' ':
            Juego = Victoria
        elif tablero[3] == tablero[6] and tablero[6] == tablero[9] and tablero[3] != ' ':
            Juego = Victoria
        elif tablero[1] == tablero[5] and tablero[5] == tablero[9] and tablero[5] != ' ':
            Juego = Victoria
        elif tablero[3] == tablero[5] and tablero[5] == tablero[7] and tablero[5] != ' ':
            Juego = Victoria
        elif tablero[1] != ' ' and tablero[2] != ' ' and tablero[3] != ' ' and \
                tablero[4] != ' ' and tablero[5] != ' ' and tablero[6] != ' ' and \
                tablero[7] != ' ' and tablero[8] != ' ' and tablero[9] != ' ':
            Juego = Empate
        else:
            Juego = corriendo
    print("Gato")
    print("Jugador 1 [X] --- Jugador 2 [O]\n")
    print()
    print()
    print("Cargando...")
    while Juego == corriendo:
        if time.ticks_diff(time.ticks_ms(), t) > 1000:
            key = Keypad4x4Read(col_list, row_list)
            if key == "#":
                break
            if key is not None:
                posicion = None
                if key.isdigit(): 
                    posicion = int(key)
                else:
                    pass
                if jugador % 2 != 0:
                    Marca = 'X'
                else:
                    Marca = 'O'
                try:
                    if posicion is not None and 1 <= posicion <= 9: 
                        if ChecarPosicion(posicion):
                            tablero[posicion] = Marca
                            jugador += 1
                            ChecarVictoria()
                            posicion = None
                            DibujarTablero()
                except NameError:
                    pass
        if Juego == Empate:
            print("Empate")
            break
        elif Juego == Victoria:
            jugador -= 1
            if jugador % 2 != 0:
                print("Jugador 1 Gana")
            else:
                print("Jugador 2 Gana")
            break
# Stop = 1
# def CheckWin():
#     global Game

#     if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
#         Game = Win
#     elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
#         Game = Win
#     elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
#         Game = Win
#     elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
#         Game = Win
#     elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
#         Game = Win
#     elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
#         Game = Win
#     elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
#         Game = Win
#     elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
#         Game = Win
#     elif board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and \
#             board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and \
#             board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
#         Game = Draw
#     else:
#         Game = Running


# print("Tic-Tac-Toe Game Designed By Sourabh Somani")
# print("Player 1 [X] --- Player 2 [O]\n")
# print()
# print()
# print("Please Wait...")
# time.sleep(3)

# while Game == Running:
#     os.system('cls')
#     DrawBoard()

#     if player % 2 != 0:
#         print("Player 1's chance")
#         Mark = 'X'
#     else:
#         print("Player 2's chance")
#         Mark = 'O'

#     choice = int(input("Enter the position between [1-9] where you want to mark: "))
#     if CheckPosition(choice):
#         board[choice] = Mark
#         player += 1
#         CheckWin()

#     os.system('cls')
#     DrawBoard()

#     if Game == Draw:
#         print("Game Draw")
#     elif Game == Win:
#         player -= 1
#         if player % 2 != 0:
#             print("Player 1 Won")
#         else:
#             print("Player 2 Won")

        