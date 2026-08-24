# Start game
#    ↓
# Choose Trivia
#    ↓
# Start timer
#    ↓
# Run Trivia
#    ↓
# Receive result
#    ↓
# Stop timer
#    ↓
# Send result + time to scoring.py
#    ↓
# Get final score
#    ↓
# Update player's total
#    ↓
# Move to next game
from games.trivia import trivia
from games.guess_number import guess_num
from games.rps import rps
class game_manager:

    def __innit__(self, Name:str):
        self.name = Name
        self.points = 0
        self.games = [
            trivia(),
            rps(),
            guess_num()
        ]

    
        




    

    


