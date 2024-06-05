

import re
import random

#einlesen der karten
def karten_einlesen(File1):
    wor4=[]
    with open(File1,"r") as buzzer_datai:
        inja =buzzer_datai.read()
        wor4=inja.split()
    return wor4
#generierung der karten
def generate_bingo_card(an,bzw):
    rows=0
    cols=0
    if(an==1):
        rows=5 
        cols=5

    if(an==2):
        rows=7
        cols=7

    matrix=[[None for _ in range(cols)]for _ in range(rows)]

    random.shuffle(bzw)

    word_index=0
    for i in range(rows):
        for j in range(cols):
            
            matrix[i][j]= bzw[word_index]
            word_index+=1

    
    if(an==1):
        matrix[2][2]="Joker"

    if(an==2):
        matrix[3][3]="Joker"

    return matrix
#methode zum checken der karten  
def check_bingo(card): 
    card[2][2]="X"
    rows = card 
    cols = [[card[j][i] for j in range(5)] for i in range(5)] 
    diags = [[card[i][i] for i in range(5)], [card[i][4-i] for i in range(5)]] 
    lines = rows + cols + diags 
    for line in lines: 
        line2=["X"]*5
        if (line==line2): 
            return True
    return False
#methode zum checken der karten
def check_bingo1(card): 
    card[3][3]="X"
    rows = card 
    cols = [[card[j][i] for j in range(7)] for i in range(7)] 
    diags = [[card[i][i] for i in range(7)], [card[i][6-i] for i in range(7)]] 
    lines = rows + cols + diags 
    #checkt die lines
    for line in lines: 
        line2=["X"]*7
        if (line==line2): 
            return True
    return False
#extrahieret die eingegeben größe des spiel feldes
def exrahiere(w222):
    return re.findall(r'\d+',w222)

#hier werden die relevanten sachen ausgeführt um das spiel zu spielen
def spiel_bingo(name,matrix,buzzw):
    #spiel wird gestartet
    j=True
    while j:
        print(name)
        word_index=0
        #karten werden gezogen
        random.shuffle(buzzw)
        print(buzzw[word_index])
        #karten werden angezeigt
        for row in matrix:
            
            print(row)
        input("Drück enter um das nächste word zu zihen") 
        #if statment wen alle karten gezogen worden sind
        if(word_index==len(buzzw)):print("es ist ein unendschieden")
        #überprüfung ob die karten mit den gezogenen karten übereinstimmen
        for i in range(len(matrix)):
            for j in range(len(matrix[0]if len(matrix) > 0 else 0)):
                
                if(matrix[i][j]==buzzw[word_index]):
                    matrix[i][j]="X"
                word_index+=1
        #checkt wer gewonnen hat
        if(check_bingo(matrix) and len(matrix)==5):
            print("gewonen"+"! "+name+" !")
            for row in matrix:
                print(row)
            j=False
        if(len(matrix)==7):
            if(check_bingo1(matrix)):
                print("gewonen "+"! "+name+" !")
                for row in matrix:
                    print(row)
                j=False

#start der eingabe in die kommandozeile
def Main():
    #überprüfung der eingabe
    w1=input()
    if w1=="newround":
        print("wie großsoll das spiel feld sein")
        w2=input()
        w22=exrahiere(w2)
        w224=w22[0]+w22[1]
        frag=0
        #entscheidung wie großdas spielfeld werden soll
        if(w224=="55"):frag=1
        if(w224=="77"):frag=2
        if(w224 != "77" and w224 != "55"):
            print("leider kan das spiel gerda nur 7*7 und 5*5 felder generiern, im nächsten update werden wir emröglischen verschieden typen von felder genereiren zu lassan du wirst wieder an den anfang gebracht")
            Main()
        if(frag>0):
            #einlesen und generirung der karten
            buzzerworter=input()
            buzzw=karten_einlesen(buzzerworter)
            matrix=generate_bingo_card(frag,buzzw)
            playeranzahl=input()
            playername=input()
            spiel_bingo(playername,matrix,buzzw)
    elif(w1 != "joinround"): 
        #falls jemand was falsch ein gibt kann man auch mit try und catch machen
        print("solch ein Befehl exsetiert nicht")
        Main()
    
    
    if(w1=="joinround"):
        roudnfile=input()
        playername2=input()
    elif(w1 != "newround"):
        print("solch ein Befehl exsetiert nicht")
        Main()
    

    
Main()