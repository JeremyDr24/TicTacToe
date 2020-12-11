import math
import random

size = 4

def myTicTacToe(grille, monSymbole):
   # on va gagner en un seul coup

   global j, i
   for i in range(0, 4):  # lines
       sum = 0
       for j in range(0, 4):
           sum = sum + grille[i][j]
           if sum == 3 * monSymbole:
               for j in range(0,4):
                   if grille[i][j] == 0:
                       return (i, j)

   for j in range(0, 4):  # columns
       sum = 0
       for i in range(0, 4):
           sum = sum + grille[i][j]
           if sum == 3 * monSymbole:
               for i in range(0, 4):
                   if grille[i][j] == 0:
                       return i, j

   sum = 0  # diagonales
   for i in range(0, 4):
       sum = sum + grille[j][j]
       if sum == 3 * monSymbole:
           for i in range(0, 4):
               if grille[i][i] == 0:
                   return i, i

   sum = 0
   for i in range(0, 4):
       sum = sum + grille[i][3 - i]
       if sum == 3 * monSymbole:
           for i in range(0, 4):
               if grille[i][3 - i] == 0:
                   return i, 3 - i

   for i in range(0, 3):  # squares
       for j in range(0, 3):
           sum = grille[i][j] + grille[i + 1][j] + grille[i][j + 1] + grille[i + 1][j + 1]
           if sum == 3 * monSymbole:
               if grille[i][j] == 0:
                   return i, j

               elif grille[i + 1][j] == 0:
                   return i + 1, j

               elif grille[i][j + 1] == 0:
                   return i, j + 1

               elif grille[i + 1][j + 1] == 0:
                   return i + 1, j + 1
   # l'ordi va gagner en un seul coup
   for i in range(0, 4):  # lines
       sum = 0
       for j in range(0, 4):
           sum = sum + grille[i][j]
           if sum == -3 * monSymbole:
               for j in range(0, 4):
                   if grille[i][j] == 0:
                       return (i, j)

   for j in range(0, 4):  # columns
       sum = 0
       for i in range(0, 4):
           sum = sum + grille[i][j]
           if sum == -3 * monSymbole:
               for i in range(0, 4):
                   if grille[i][j] == 0:
                       return (i, j)

   sum = 0  # diagonales
   for j in range(0, 4):
       sum = sum + grille[j][j]
       if sum == -3 * monSymbole:
           for j in range(0, 4):
               if grille[j][j] == 0:
                   return j, j

   sum = 0
   for j in range(0, 4):
       sum = sum + grille[j][3 - j]
       if sum == -3 * monSymbole:
           for j in range(0, 4):
               if grille[j][3 - j] == 0:
                   return j, 3 - j

   for i in range(0, 3):  # squares
       for j in range(0, 3):
           sum = grille[i][j] + grille[i + 1][j] + grille[i][j + 1] + grille[i + 1][j + 1]
           if sum == -3 * monSymbole:
               if grille[i][j] == 0:
                   return (i), (j)

               elif grille[i + 1][j] == 0:
                   return (i + 1), (j)

               elif grille[i][j + 1] == 0:
                   return (i), (j + 1)

               elif grille[i + 1][j + 1] == 0:
                   return (i + 1), (j + 1)

   # pour avoir 2 sum==3*monSymbole a la fois
   global sum_line, sum_column, sum_diagonal, sum_diagonal2, sum_square
   for i in range(0, 4):
       sum_line = 0
       for j in range(0, 4):
           sum_line = sum_line + grille[i][j]

   for j in range(0, 4):
       sum_column = 0
       for i in range(0, 4):
           sum_column = sum_column + grille[i][j]

   sum_diagonal = 0
   for j in range(0, 4):
       sum_diagonal = sum_diagonal + grille[j][j]

   sum_diagonal2 = 0
   for j in range(0, 4):
       sum_diagonal2 = sum_diagonal2 + grille[j][3 - j]

   for i in range(0, 3):
       for j in range(0, 3):
           sum_square = grille[i][j] + grille[i + 1][j] + grille[i][j + 1] + grille[i + 1][j + 1]

   list_sum = []
   for i in range(0, 4):
       for j in range(0, 4):
           if sum_line == 2 * monSymbole:
               list_sum.append("sum_line")
           elif sum_column == 2 * monSymbole:
               list_sum.append("sum_column")
           elif sum_diagonal == 2 * monSymbole:
               list_sum.append("sum_diagonal")
           elif sum_diagonal2 == 2 * monSymbole:
               list_sum.append("sum_diagonal2")
           elif sum_square == 2 * monSymbole:
               list_sum.append("sum_square")
   while len(list_sum) == 2:
       return i, j

   # on gagne presque(a sum==3*monSymbole)
   for i in range(0, 4):  # lines
       sum = 0
       for j in range(0, 4):
           sum = sum + grille[i][j]
           if sum == 2 * monSymbole:
               if grille[i][j] == 0:
                   return i, j

   for j in range(0, 4):  # columns
       sum = 0
       for i in range(0, 4):
           sum = sum + grille[i][j]
           if sum == 2 * monSymbole:
               if grille[i][j] == 0:
                   return i, j

   sum = 0  # diagonales
   for j in range(0, 4):
       sum = sum + grille[j][j]
       if sum == 2 * monSymbole:
           for j in range(0, 4):
               if grille[j][j] == 0:
                   return j, j

   sum = 0
   for j in range(0, 4):
       sum = sum + grille[j][3 - j]
       if sum == 2 * monSymbole:
           for j in range(0, 4):
               if grille[j][3 - j] == 0:
                   return j, 3 - j

   for i in range(0, 3):  # squares
       for j in range(0, 3):
           sum = grille[i][j] + grille[i + 1][j] + grille[i][j + 1] + grille[i + 1][j + 1]
           if sum == 2 * monSymbole:
               if grille[i][j] == 0:
                   return (i), (j)

               elif grille[i + 1][j] == 0:
                   return (i + 1), (j)

               elif grille[i][j + 1] == 0:
                   return (i), (j + 1)

               elif grille[i + 1][j + 1] == 0:
                   return (i + 1), (j + 1)

   # pour le debut du jeu,et avec ces coups, on peut toujours avoir une sum >=2
   if grille[1][1] == 0:
       return 1, 1
   elif grille[1][2] == 0:
       return 1, 2
   elif grille[2][2] == 0:
       return 2, 2
   elif grille[2][1] == 0:
       return 2, 1


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
        (x,y) = myTicTacToe(grille, monSymbole)
        # (x, y) = tictactoeRandom(grille, monSymbole)
        affecterSymbole(grille, monSymbole, x, y)
        (winner, finished) = check(grille)

        print("Student player")
        affichage(grille)