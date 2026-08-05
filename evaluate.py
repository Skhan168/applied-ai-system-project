"""
Evaluation script for Game Glitch Investigator.
Runs the core game logic against a fixed set of predefined inputs
and prints a pass/fail summary -- this is the project's automated
test harness, separate from pytest, meant to be run as a standalone report.
"""

from logic_utils import (
    check_guess,
    parse_guess,
    update_score,
    get_temperature_emoji,
    coach_feedback,
)


def run_case(name, actual, expected):
    passed = actual == expected
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {name}")
    if not passed:
        print(f"       expected={expected!r}, got={actual!r}")
    return passed


def main():
    results = []

    results.append(run_case(
        "check_guess: too low",
        check_guess(50, 80)[0], "Too Low"
    ))
    results.append(run_case(
        "check_guess: too high",
        check_guess(90, 50)[0], "Too High"
    ))
    results.append(run_case(
        "check_guess: win",
        check_guess(50, 50)[0], "Win"
    ))

    ok, val, err = parse_guess("50")
    results.append(run_case("parse_guess: valid input", (ok, val), (True, 50)))

    ok, val, err = parse_guess("")
    results.append(run_case("parse_guess: empty input", ok, False))

    ok, val, err = parse_guess("abc")
    results.append(run_case("parse_guess: invalid input", ok, False))

    results.append(run_case(
        "update_score: floor at zero",
        update_score(5, "Too Low", 1), 0
    ))
    results.append(run_case(
        "update_score: win keeps score",
        update_score(100, "Win", 1), 100
    ))
    results.append(run_case(
        "update_score: normal deduction",
        update_score(100, "Too High", 1), 90
    ))

    results.append(run_case(
        "temperature emoji: exact match",
        get_temperature_emoji(50, 50), "🎯"
    ))
    results.append(run_case(
        "temperature emoji: far",
        get_temperature_emoji(10, 50), "🥶"
    ))

    feedback = coach_feedback([70, 12, 10, 6, 3], 3)
    results.append(run_case(
        "coach_feedback: steady narrowing gives positive feedback",
        "Great strategy" in feedback, True
    ))

    feedback = coach_feedback([], None)
    results.append(run_case(
        "coach_feedback: empty history handled",
        "nothing to review" in feedback.lower(), True
    ))

    feedback = coach_feedback([42], 42)
    results.append(run_case(
        "coach_feedback: single guess handled",
        "one guess" in feedback.lower(), True
    ))

    total = len(results)
    passed = sum(results)
    print()
    print("=" * 40)
    print(f"EVALUATION SUMMARY: {passed}/{total} tests passed")
    print("=" * 40)


if __name__ == "__main__":
    main()