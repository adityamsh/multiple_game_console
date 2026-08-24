# Games with no difficulty
# Factors:
# 1. final result
# 2. choice (skip)

# Games with difficulty
# Factors:
# 1. final result
# 2. difficulty
# 3. number of turns
# 4. skip
# 5. time


# --- Score Configurations ---

GUESS_RULES = {
    "easy": {"base": 100, "max_turns": 1, "bonus": 0},
    "medium": {"base": 150, "max_turns": 3, "bonus": 30},
    "hard": {"base": 200, "max_turns": 6, "bonus": 60},
}

TRIVIA_RULES = {
    "easy": {"base": 100, "max_turns": 1, "bonus": 0},
    "medium": {"base": 100, "max_turns": 2, "bonus": 25},
    "hard": {"base": 150, "max_turns": 3, "bonus": 50},
}


# --- Scoring Functions ---

def score_rps(result: bool | None, skip: bool = False) -> int:

    if skip:
        return -50

    if result is None:
        return 0

    if not result:
        return -100

    return 100


def difficulty_levels_rule(
    game_rules: dict,
    result: bool,
    difficulty: str,
    no_turns: int,
    time: float,
    skip: bool = False
) -> int:

    if skip:
        return -50

    if not result:
        return -100

    rule = game_rules.get(difficulty)

    if not rule:
        raise ValueError(
            f"Invalid difficulty level: {difficulty}"
        )

    remaining_turns = max(
        0,
        rule["max_turns"] - no_turns
    )

    points = (
        rule["base"]
        + (remaining_turns * rule["bonus"])
    )

    if game_rules == GUESS_RULES and time < 20:
        points += (20 - time) * 3

    if game_rules == TRIVIA_RULES and time < 15:
        points += (15 - time) * 3

    return round(points)


def score_guess_num(
    result: bool,
    difficulty: str,
    no_turns: int,
    time: float,
    skip: bool = False
) -> int:

    return difficulty_levels_rule(
        GUESS_RULES,
        result,
        difficulty,
        no_turns,
        time,
        skip
    )


def score_trivia(
    result: bool,
    difficulty: str,
    no_turns: int,
    time: float,
    skip: bool = False
) -> int:

    return difficulty_levels_rule(
        TRIVIA_RULES,
        result,
        difficulty,
        no_turns,
        time,
        skip
    )