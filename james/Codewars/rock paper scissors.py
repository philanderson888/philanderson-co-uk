'''
Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.
'''

def rps(p1, p2):
    if p1 == 'scissors' and p2 == 'paper':
        return "Player 1 won!"
    elif p1 == 'scissors' and p2 == 'rock':
        return "Player 2 won!"
    
    if p1 == 'rock' and p2 == 'paper':
        return "Player 2 won!"
    elif p1 == 'rock' and p2 == 'scissors':
        return "Player 1 won!"
    
    if p1 == 'paper' and p2 == 'scissors':
        return "Player 2 won!"
    elif p1 == 'paper' and p2 == 'rock':
        return "Player 1 won!"
    else:
        return "Draw!"
    