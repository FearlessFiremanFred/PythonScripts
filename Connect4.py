def printcurrent(game):
    for i in range(len(game)):
        for a in range(len(game[i])):
            print(game[a][len(game)-1-i],end="  ")
        print("\n")
def p1move(game):
    veri=0
    while veri == 0:
        try:
            column= input("column p1? (A or B or C or D or E or F or G)")
            for i in range(len(game)):
                if column in game[i]:
                    veri=1
        except:
            veri=0
    for i in range(len(game)):
        if column in game[i]:
            game[i].insert(game[i].index("0"),"1")
            game[i].remove("0")
    return game  
def p2move(game):
    veri=0
    while veri == 0:
        try:
            column= str(input("column p2? (A or B or C or D or E or F or G)"))
            for i in range(len(game)):
                print("veri = 1")
                if column in game[i]:
                    veri=1
                    print("veri = 1")
        except:
            veri=0
    for i in range(len(game)):
        if column in game[i]:
            game[i].insert(game[i].index("0"),"2")
            game[i].remove("0")
    return game
def checkf(check):
    a=2
p1=input("who will be playing?")
p2=input("who will be playing?")
A=["A","0","0","0","0","0","0"]
B=["B","0","0","0","0","0","0"]
C=["C","0","0","0","0","0","0"]
D=["D","0","0","0","0","0","0"]
E=["E","0","0","0","0","0","0"]
F=["F","0","0","0","0","0","0"]
G=["G","0","0","0","0","0","0"]
game=[A,B,C,D,E,F,G]
check=0
printcurrent(game)
while check == 0:
    game = p1move(game)
    game = printcurrent(game)
    check = checkf(check)
    game = p2move(game)
    game = printcurrent(game)
    check = checkf(check)
