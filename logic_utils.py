def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int):
    """
    Compare guess to secret and return (outcome, message).

    Both guess and secret are always integers. There is no type
    conversion here on purpose -- the caller (app.py) is responsible
    for making sure secret is always an int, so this function never
    has to guess at types or catch a TypeError.

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"


def get_temperature_emoji(guess: int, secret: int) -> str:
    """
    Return an emoji hint based on how close the guess is to the secret.

    🔥 = very close (within 3)
    🌡️ = somewhat close (within 10)
    🥶 = far away (more than 10)
    """
    distance = abs(guess - secret)

    if distance == 0:
        return "🎯"
    if distance <= 3:
        return "🔥"
    if distance <= 10:
        return "🌡️"
    return "🥶"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome in ["Too High", "Too Low"]:
        return max(0, current_score - 10)

    if outcome == "Win":
        return current_score

    return current_score


def coach_feedback(guesses: list, secret: int) -> str:
    """
    Look at the full guess history and give feedback on the player's
    strategy. This is the required AI evaluation/reliability feature:
    it reviews behavior (the guesses) and produces a judgment about
    how efficient the strategy was.
    """
    if not guesses:
        return "No guesses were made, so there's nothing to review yet."

    if len(guesses) == 1:
        return "You solved it in one guess! Lucky or a great instinct. 🍀"

    distances = [abs(g - secret) for g in guesses]

    improving_steps = 0
    for i in range(1, len(distances)):
        if distances[i] < distances[i - 1]:
            improving_steps += 1

    improvement_ratio = improving_steps / (len(distances) - 1)

    if improvement_ratio >= 0.75:
        return (
            "🎯 Great strategy! Almost every guess got closer to the "
            "answer, which looks like an efficient narrowing-down approach."
        )
    elif improvement_ratio >= 0.4:
        return (
            "🙂 Decent strategy. Some guesses got closer, but a few moved "
            "away from the answer. Try adjusting your range more "
            "consistently based on each hint."
        )
    else:
        return (
            "🔄 Your guesses jumped around a lot rather than steadily "
            "narrowing in on the answer. Try picking the middle of the "
            "remaining possible range each time."
        )