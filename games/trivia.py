import random as rnd
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
QUESTIONS_FILE = BASE_DIR / "data" / "trivia_questions.json"


with open(QUESTIONS_FILE, "r") as file:
    questions = json.load(file)


class Trivia:

    def __init__(self):
        self.skip = False

    @staticmethod
    def trivia_logic(user_input: int, difficulty: str) -> bool | None:

        if difficulty not in questions:
            raise ValueError(
                f"Invalid input: {difficulty}. "
                "Choose easy, medium or hard."
            )

        question = rnd.choice(questions[difficulty])

        print("\n" + question["question"])

        for number, option in question["options"].items():
            print(f"{number}. {option}")

        if user_input not in range(1, 5):
            return None

        return user_input == question["answer"]

    def play(self):

        difficulty = input(
            "Enter difficulty (easy, medium, hard) "
            "or 's' to skip: "
        ).strip().lower()

        if difficulty == "s":
            self.skip = True

            return {
                "game": "trivia",
                "result": None,
                "skip": True,
                "difficulty": None,
                "turns": 0
            }

        if difficulty not in questions:
            raise ValueError(
                f"Invalid difficulty: {difficulty}. "
                "Choose easy, medium or hard."
            )

        max_turns = {
            "easy": 1,
            "medium": 2,
            "hard": 3
        }

        for turn in range(1, max_turns[difficulty] + 1):

            user_input = input(
                f"\nTurn {turn}/{max_turns[difficulty]} "
                "(1-4 or 's' to skip): "
            ).strip().lower()

            if user_input == "s":
                self.skip = True

                return {
                    "game": "trivia",
                    "result": None,
                    "skip": True,
                    "difficulty": difficulty,
                    "turns": turn
                }

            try:
                user_input = int(user_input)
            except ValueError:
                raise ValueError(
                    "Answer must be a number between 1 and 4."
                )

            result = self.trivia_logic(user_input, difficulty)

            if result:
                print("Correct!")

                if turn == max_turns[difficulty]:
                    return {
                        "game": "trivia",
                        "result": True,
                        "skip": False,
                        "difficulty": difficulty,
                        "turns": turn
                    }

            else:
                print("Wrong!")

                return {
                    "game": "trivia",
                    "result": False,
                    "skip": False,
                    "difficulty": difficulty,
                    "turns": turn
                }

        return {
            "game": "trivia",
            "result": True,
            "skip": False,
            "difficulty": difficulty,
            "turns": max_turns[difficulty]
        }