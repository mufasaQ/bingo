import random 
  
bingo_rules = { 
    'B': 5, 
    'I': 5, 
    
    'N': 5, 
    'G': 5, 
    'O': 5
} 
  
# Define a function to generate a randomized Bingo ball 
  
  
def get_bingo_ball(used_balls): 
    all_balls = [i for i in range(1, 26)] 
    available_balls = set(all_balls) - used_balls 
    if available_balls: 
        ball = random.choice(list(available_balls)) 
        used_balls.add(ball) 
        return ball 
    else: 
        return None
  
# Define a function to check if a Bingo card has a winning combination 
  
  
def check_bingo(card): 
    rows = card 
    cols = [[card[j][i] for j in range(5)] for i in range(5)] 
    diags = [[card[i][i] for i in range(5)], [card[i][4-i] for i in range(5)]] 
    lines = rows + cols + diags 
    for line in lines: 
        if len(set(line)) == 1 and line[0] != 0: 
            return True
    return False
  
  
def generate_card(): 
    card = [[0]*5 for i in range(5)] 
    used_numbers = set() 
    for i in range(5): 
        for j in range(5): 
            if j == 2 and i == 2: 
                continue
            while True: 
                number = random.randint(i*5+1, i*5+5) 
                if number not in used_numbers: 
                    card[i][j] = number 
                    used_numbers.add(number) 
                    break
    return card 
  
# Play a game of Bingo 
  
  
def play_bingo(): 
    # Generate two Bingo cards 
    card1 = generate_card() 
    card2 = generate_card() 
  
    # Print out the two Bingo cards 
    print("Bingo Card 1:") 
    for row in card1: 
        print(' '.join([str(n).rjust(2) for n in row])) 
    print() 
    print("Bingo Card 2:") 
    for row in card2: 
        print(' '.join([str(n).rjust(2) for n in row])) 
    print() 
  
    # Start the Bingo game loop 
    used_balls = set() 
    while True: 
        # Generate a new Bingo ball 
        ball = get_bingo_ball(used_balls) 
        if ball is None: 
            print("All Bingo balls have been drawn. The game is a tie.") 
            break
  
        # Print out the new Bingo ball 
        print("New Bingo ball: ", ball) 
  
        # Check if either player has a winning Bingo card 
        if check_bingo(card1): 
            print("Bingo! Player 1 wins!") 
            break
        if check_bingo(card2): 
            print("Bingo! Player 2 wins!") 
            break
  
        # Wait for player input before drawing the next ball 
        input("Press Enter to draw the next Bingo ball...") 
  
        # Update the Bingo cards with the new ball 
        for i in range(5): 
            for j in range(5): 
                if card1[i][j] == ball: 
                    card1[i][j] = "X"
                if card2[i][j] == ball: 
                    card2[i][j] = "X"
  
        # Print out the updated Bingo cards 
        print("Bingo Card 1:") 
        for row in card1: 
            print(' '.join([str(n).rjust(2) if isinstance( 
                n, int) else n.rjust(2) for n in row])) 
        print() 
        print("Bingo Card 2:") 
        for row in card2: 
            print(' '.join([str(n).rjust(2) if isinstance( 
                n, int) else n.rjust(2) for n in row])) 
        print() 
  
  
play_bingo() 