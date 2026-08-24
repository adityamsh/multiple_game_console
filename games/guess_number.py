import random as rnd


# difficulty level : range of numbers to guess between
difficulty_limits = {
    "easy": 100,
    "medium": 500,
    "hard": 1000
}


class guess_number:

    def __init__(self):
        self.skip = False

    # Logical function
    @staticmethod
    def guess_num_logic(user: int, difficulty: str) -> bool:

        max_limit = difficulty_limits[difficulty]

        computer = rnd.randint(1, max_limit)

        return user == computer

    # Main function
    def play(self):

        difficulty = input(
            "Enter 's' to skip or enter difficulty ->\n"
            "easy\n"
            "medium\n"
            "hard\n: "
        ).strip().lower()

        # Skip handling
        if difficulty == 's':
            self.skip = True

            return {
                "result": None,
                "game": "guess_num",
                "skip": True,
                "difficulty": None,
                "turns": 0
            }

        # Difficulty validation
        if difficulty not in difficulty_limits:
            raise ValueError(
                f"Invalid difficulty level: {difficulty}. "
                "Choose easy, medium or hard."
            )

        attempts = {
            "easy": 3,
            "medium": 5,
            "hard": 7
        }

        for turn in range(1, attempts[difficulty] + 1):

            user_input = input(
                f"Guess the number (1-{difficulty_limits[difficulty]}) "
                "or 's' to skip: "
            ).strip().lower()

            # Skip during game
            if user_input == 's':
                self.skip = True

                return {
                    "result": None,
                    "game": "guess_num",
                    "skip": True,
                    "difficulty": difficulty,
                    "turns": turn
                }

            user = int(user_input)

            result = self.guess_num_logic(user, difficulty)

            if result:
                print("Correct!")

                return {
                    "result": True,
                    "game": "guess_num",
                    "skip": False,
                    "difficulty": difficulty,
                    "turns": turn
                }

            print("Wrong!")

        return {
            "result": False,
            "game": "guess_num",
            "skip": False,
            "difficulty": difficulty,
            "turns": attempts[difficulty]
        }