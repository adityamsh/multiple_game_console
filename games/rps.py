import random as rnd



class rock_paper_scissor:

    def __init__(self):
        self.skip = False


# logic for rock_paper_scissor game
    @staticmethod
    def rps(user: str) -> bool | None:

        user = user.strip().lower()
        choices = ["rock", "paper", "scissor"]

# computer choice
        computer = rnd.choice(choices)

        win_pair = {
            ("scissor", "paper"),
            ("rock", "scissor"),
            ("paper", "rock")
        }

        if user not in choices:
            raise ValueError("Invalid Input")

        if user == computer:
            return None

        if (user, computer) in win_pair:
            return True

        return False


# call to play main function to be called everywhere
    def play(self):

        user_input = input(
            "Enter rock, paper, scissor or 's' to skip: "
        )
# skip handeling
        if user_input.lower() == 's':
            self.skip = True
            return{
                "result": None,
                "game" : "rock paper scissor" ,
                "skip" : True
            }
        result = self.rps(user_input)

        return {
        "game": "rps",
        "result": result,
        "skip": False
    }