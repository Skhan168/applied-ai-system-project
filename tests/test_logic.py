from logic_utils import (
    check_guess,
    update_score,
    parse_guess,
    get_temperature_emoji,
    coach_feedback,
)

print("--- Testing check_guess ---")

outcome, message = check_guess(50, 80)
print(f"guess=50, secret=80 -> {outcome} | {message}")
assert outcome == "Too Low"

outcome, message = check_guess(90, 50)
print(f"guess=90, secret=50 -> {outcome} | {message}")
assert outcome == "Too High"

outcome, message = check_guess(50, 50)
print(f"guess=50, secret=50 -> {outcome} | {message}")
assert outcome == "Win"

print("\n--- Testing parse_guess ---")

ok, value, err = parse_guess("50")
print(f"'50' -> ok={ok}, value={value}, err={err}")
assert ok is True and value == 50

ok, value, err = parse_guess("")
print(f"'' -> ok={ok}, value={value}, err={err}")
assert ok is False

ok, value, err = parse_guess("abc")
print(f"'abc' -> ok={ok}, value={value}, err={err}")
assert ok is False

ok, value, err = parse_guess("-5")
print(f"'-5' -> ok={ok}, value={value}, err={err}")
assert ok is True and value == -5

print("\n--- Testing update_score ---")

score = update_score(current_score=100, outcome="Too High", attempt_number=1)
print(f"score after Too High from 100 -> {score}")
assert score == 90

score = update_score(current_score=5, outcome="Too Low", attempt_number=2)
print(f"score after Too Low from 5 -> {score}")
assert score == 0

score = update_score(current_score=100, outcome="Win", attempt_number=3)
print(f"score after Win from 100 -> {score}")
assert score == 100

print("\n--- Testing get_temperature_emoji ---")

emoji = get_temperature_emoji(guess=50, secret=50)
print(f"guess=50, secret=50 -> {emoji}")
assert emoji == "🎯"

emoji = get_temperature_emoji(guess=48, secret=50)
print(f"guess=48, secret=50 -> {emoji}")
assert emoji == "🔥"

emoji = get_temperature_emoji(guess=42, secret=50)
print(f"guess=42, secret=50 -> {emoji}")
assert emoji == "🌡️"

emoji = get_temperature_emoji(guess=10, secret=50)
print(f"guess=10, secret=50 -> {emoji}")
assert emoji == "🥶"

print("\n--- Testing coach_feedback ---")

feedback = coach_feedback(guesses=[], secret=50)
print(f"empty history -> {feedback}")
assert "No guesses" in feedback

feedback = coach_feedback(guesses=[50], secret=50)
print(f"one guess -> {feedback}")
assert "one guess" in feedback

feedback = coach_feedback(guesses=[70, 12, 10, 6, 3], secret=3)
print(f"steadily improving guesses -> {feedback}")
assert "Great strategy" in feedback

feedback = coach_feedback(guesses=[70, 100, 60, 50, 40, 30, 35], secret=38)
print(f"mixed guesses -> {feedback}")
assert "Decent strategy" in feedback or "jumped around" in feedback

feedback = coach_feedback(guesses=[10, 90, 5, 95, 2, 99], secret=50)
print(f"scattered guesses -> {feedback}")
assert "jumped around" in feedback or "Decent strategy" in feedback

print("\nAll tests passed!")