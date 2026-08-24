from score_calculator import score_rps, score_guess_num, score_trivia


def calculate_round_score(game_record: dict) -> int:
    """Calculate the score for an individual game record."""

    game_name = game_record.get("game", "").lower()
    result = game_record.get("result", False)
    skip = game_record.get("skip", False)
    difficulty = game_record.get("difficulty", "easy")
    turns = game_record.get("turns", 1)
    time_taken = game_record.get("time", 0.0)

    if game_name == "rps":
        return score_rps(
            result=result,
            skip=skip
        )

    elif game_name in ("guess_num", "guess"):
        return score_guess_num(
            result=result,
            difficulty=difficulty,
            no_turns=turns,
            time=time_taken,
            skip=skip
        )

    elif game_name == "trivia":
        return score_trivia(
            result=result,
            difficulty=difficulty,
            no_turns=turns,
            time=time_taken,
            skip=skip
        )

    else:
        raise ValueError(f"Unknown game: {game_name}")


def show_final_results(game_history: list[dict]) -> int:
    """Print the scoreboard and return the cumulative score."""

    total_score = 0

    print("\n" + "=" * 65)

    print(
        f"{'GAME':<12} | "
        f"{'OUTCOME':<8} | "
        f"{'DIFF':<8} | "
        f"{'TURNS':<5} | "
        f"{'TIME(s)':<7} | "
        f"{'SCORE':<6}"
    )

    print("-" * 65)

    for record in game_history:

        score = calculate_round_score(record)
        total_score += score

        # Determine outcome
        if record.get("skip", False):
            outcome = "SKIP"
        elif record.get("result", False):
            outcome = "WIN"
        else:
            outcome = "LOSS"

        game_name = record.get("game", "N/A").upper()

        difficulty = record.get("difficulty", "-")
        turns = record.get("turns", "-")
        time_taken = record.get("time", 0.0)

        time_str = f"{time_taken:.1f}"

        print(
            f"{game_name:<12} | "
            f"{outcome:<8} | "
            f"{str(difficulty):<8} | "
            f"{str(turns):<5} | "
            f"{time_str:<7} | "
            f"{score:>+5}"
        )

    print("=" * 65)
    print(f"FINAL TOTAL SCORE: {total_score} pts")
    print("=" * 65 + "\n")

    return total_score