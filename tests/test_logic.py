from logic_utils import (
    check_guess,
    update_score,
    parse_guess,
    get_temperature_emoji,
    coach_feedback,
)


def test_check_guess_too_low():
    outcome, message = check_guess(50, 80)
    assert outcome == "Too Low"


def test_check_guess_too_high():
    outcome, message = check_guess(90, 50)
    assert outcome == "Too High"


def test_check_guess_win():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_parse_guess_valid():
    ok, value, err = parse_guess("50")
    assert ok is True and value == 50


def test_parse_guess_empty():
    ok, value, err = parse_guess("")
    assert ok is False


def test_parse_guess_invalid():
    ok, value, err = parse_guess("abc")
    assert ok is False


def test_parse_guess_negative():
    ok, value, err = parse_guess("-5")
    assert ok is True and value == -5


def test_update_score_too_high():
    score = update_score(current_score=100, outcome="Too High", attempt_number=1)
    assert score == 90


def test_update_score_floor_at_zero():
    score = update_score(current_score=5, outcome="Too Low", attempt_number=2)
    assert score == 0


def test_update_score_win():
    score = update_score(current_score=100, outcome="Win", attempt_number=3)
    assert score == 100


def test_temperature_emoji_exact():
    emoji = get_temperature_emoji(guess=50, secret=50)
    assert emoji == "🎯"


def test_temperature_emoji_close():
    emoji = get_temperature_emoji(guess=48, secret=50)
    assert emoji == "🔥"


def test_temperature_emoji_medium():
    emoji = get_temperature_emoji(guess=42, secret=50)
    assert emoji == "🌡️"


def test_temperature_emoji_far():
    emoji = get_temperature_emoji(guess=10, secret=50)
    assert emoji == "🥶"


def test_coach_feedback_empty_history():
    feedback = coach_feedback(guesses=[], secret=50)
    assert "No guesses" in feedback


def test_coach_feedback_single_guess():
    feedback = coach_feedback(guesses=[50], secret=50)
    assert "one guess" in feedback


def test_coach_feedback_steady_improvement():
    feedback = coach_feedback(guesses=[70, 12, 10, 6, 3], secret=3)
    assert "Great strategy" in feedback


def test_coach_feedback_mixed_guesses():
    feedback = coach_feedback(guesses=[70, 100, 60, 50, 40, 30, 35], secret=38)
    assert "Decent strategy" in feedback or "jumped around" in feedback


def test_coach_feedback_scattered_guesses():
    feedback = coach_feedback(guesses=[10, 90, 5, 95, 2, 99], secret=50)
    assert "jumped around" in feedback or "Decent strategy" in feedback