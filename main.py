import math
import random

size = 4

def myTicTacToe(grille, monSymbole):
    x=-1#à definir
    y=-1#à definir

    return (x, y)

def check(tab):
    global sum
    sum = 0
    motif = 0

    global finished
    finished = False
    global winner
    winner = -1


    #check lines
    for i in range(0,4):
        sum = 0
        for j in range(0,4):
            sum = sum + tab[i][j]
        #print("lines" + str(sum))
        if math.fabs(sum) == 4:
            motif = sum

    #check columns
    for i in range(0,4):
        sum = 0
        for j in range(0,4):
            sum = sum + tab[j][i]
        #print("columns" + str(sum))
        if math.fabs(sum) == 4:
            motif = sum

    #check diags
    sum = 0
    for j in range(0,4):
        sum = sum + tab[j][j]
    if math.fabs(sum) == 4:
        motif = sum

    sum = 0
    for j in range(0,4):
        sum = sum + tab[j][3 - j]
    if math.fabs(sum) == 4:
        motif = sum

    #check squares
    for i in range(0,3):
        for j in range(0,3):
            sum = tab[i][j]+tab[i+1][j]+tab[i][j+1]+tab[i+1][j+1]
            if math.fabs(sum) == 4:
                motif = sum

    if motif == 4:
        finished = True
        winner = 1
    elif motif == -4:
        finished = True
        winner = -1
    else :
        finished = True
        winner = 0
        for i in range(0,4):
            for j in range(0, 4):
                if tab[i][j] == 0:
                    finished = False

    return (winner, finished)


def tictactoeRandom(grille, monSymbole) :
    x = random.randint(0,(size - 1))
    y = random.randint(0,(size - 1))

    #print(grille[x][y])

    #while (grille[x][y] == monSymbole or (grille[x][y] + monSymbole) == 0):
    while(grille[x][y] == -1 or grille[x][y] == 1):
        x = random.randint(0, (size - 1))
        y = random.randint(0, (size - 1))

    return (x,y)

def affecterSymbole(grille, monSymbole, x, y):
    #print(grille)
    #print(x, y)
    grille[x][y] = monSymbole
    #print(grille)

def affichage(grille):
    for i in range(0, size):
        ch = ""
        for j in range(0, size):
            ch += str(grille[i][j])+" "
        print(ch)
    print()




grille = [0]*size
for i in range(size):
        grille[i] = [0] * size

affichage(grille)

winner = 0
finished = False

while (winner == 0 and finished == False):
    monSymbole = -1
    #print(grille)
    (x,y) = tictactoeRandom(grille, monSymbole)

    affecterSymbole(grille, monSymbole, x, y)
    #print(grille)

    print("Dummy player")
    affichage(grille)
    (winner, finished) = check(grille)

    if (winner == 0 and finished == False):
        monSymbole = 1
        #(x,y) = myTicTacToe(grille, monSymbole)
        (x, y) = tictactoeRandom(grille, monSymbole)
        affecterSymbole(grille, monSymbole, x, y)
        (winner, finished) = check(grille)

        print("Student player")
        affichage(grille)