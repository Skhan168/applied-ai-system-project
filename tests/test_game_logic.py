from logic_utils import check_guess


def test_check_guess_too_high():
    outcome, message = check_guess(90, 50)
    assert outcome == "Too High"
    assert "LOWER" in message