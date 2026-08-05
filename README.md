# 🎮 Game Glitch Investigator: The Impossible Guesser

## 📌 Base Project and Original Scope

This project extends my **Number Guessing Game** (originally built in Module 1). The original system let a player pick a difficulty level, guess a secret number within a range, and get "Too High"/"Too Low" hints while their score adjusted based on guess count. The original scope was a simple, self-contained guessing game with no evaluation of player strategy — it just tracked wins, losses, and score.

This project extends that base by fixing the original bugs (bad hints, invalid game-over states, broken score floor, incomplete restarts) and adding a new AI-driven **Coach Feedback** feature that evaluates the player's guessing strategy after each game.

## ▶️ Running and Testing the System

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run the game:**
```bash
python -m streamlit run app.py
```

**Run the automated tests:**
```bash
pytest tests/test_logic.py -v
```

**Run the evaluation script:**
```bash
python evaluate.py
```

**Sample run — steady narrowing strategy:**
​```
Difficulty: Normal (1-100)
Guess 1: 70 → Too High
Guess 2: 12 → Too Low
Guess 3: 10 → Too Low
Guess 4: 6 → Too Low
Guess 5: 3 → Correct! Final score: 60

Coach Feedback: "🎯 Great strategy! Almost every guess got closer to the
answer, which looks like an efficient narrowing-down approach."
​```

**Sample run — scattered guesses:**
​```
Difficulty: Normal (1-100)
Guess 1: 70 → Too High
Guess 2: 100 → Too High
Guess 3: 60 → Too High
Guess 4: 50 → Too High
Guess 5: 40 → Too High
Guess 6: 30 → Too Low
Guess 7: 35 → Too Low
Guess 8: 38 → Correct! Final score: 30

Coach Feedback: "🙂 Decent strategy. Some guesses got closer, but a few
moved away from the answer. Try adjusting your range more consistently
based on each hint."
​```


## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Investigate why the secret number and score behave inconsistently between guesses and restarts.
3. **Fix the Logic.** Make sure the "Higher/Lower" hints match the actual secret number and that the score updates reasonably.
4. **Refactor & Test.**
   - Move the core game logic into `logic_utils.py`.
   - Import and use those functions from `app.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!
5. **Extend with new features.** Added emoji-based temperature hints (🥶🌡️🔥🎯) and an AI "coach" that reviews your full guess history after each game and explains whether your strategy was efficient.

## 📝 Document Your Experience

- The game's purpose is to let a player pick a difficulty level and try to guess a secret number within a certain range, while getting "Too High" or "Too Low" hints and watching their score change based on their guesses.
- I found several bugs: the hints could tell me to go higher and then lower around the same number, the final "answer" at game over could be outside the expected range, the score could drop below zero, and restarting the game did not always reset things cleanly.
- To fix these issues, I cleaned up the game logic and moved it into `logic_utils.py`, corrected how guesses are compared to the secret number so the hints are accurate, and made sure the scoring and state behave consistently across guesses and restarts. I also updated the tests so `check_guess()` is covered by pytest and verified that they pass.

## 🧠 New AI Feature: Coach Feedback

After each game ends (win or loss), a `coach_feedback()` function reviews the player's entire guess history and evaluates their strategy:

- If guesses steadily got closer to the secret number, it praises the "narrowing-down" strategy.
- If guesses were inconsistent, it gives constructive feedback.
- If guesses were scattered with no clear pattern, it suggests picking the middle of the remaining range.

This acts as the project's required **reliability/evaluation component** — it doesn't just play the game, it evaluates the quality of the play itself. See `tests/test_logic.py` for automated tests covering all three feedback branches.

## 🛡️ Reliability Component: Coach Feedback Evaluation

The `coach_feedback()` function acts as this project's evaluation mechanism — it doesn't just play the game, it evaluates the quality of the player's strategy after the fact.

| Input (guess history) | Behavior | Result |
|---|---|---|
| `[25, 38, 32, 35]` toward secret `35` | Detects each guess getting closer to the target | Returns "Great strategy! Your guesses steadily narrowed in on the secret number." |
| `[10, 45, 3, 48, 21]` toward secret `21` | Detects no consistent narrowing pattern | Returns "Your guesses were scattered with no clear pattern. Try picking the middle of your remaining range." |
| `[15, 40, 25, 30]` toward secret `30` | Detects partial/inconsistent improvement | Returns "Decent strategy, but you could narrow down more efficiently by always picking the midpoint of your remaining range." |

This is validated in `tests/test_logic.py`, which covers all three feedback branches (steady improvement, scattered, mixed) plus edge cases (empty history, single guess).

## 🎨 Design Decisions

- **Emoji hints** were added to make feedback feel more intuitive and fun without changing the core "Higher/Lower" logic.
- **Coach feedback** was chosen as the required AI feature because it directly builds on existing guess history data, and it gives a simple example of evaluating behavior rather than just reacting to it.
- The root-cause bug fix (removing the string/int mismatch) was prioritized over defensive code, per feedback from the original submission.

## 📸 Demo Walkthrough

1. User selects a difficulty (for example, Normal) and the app picks a secret number in the corresponding range.
2. User enters a first guess; if it is below the secret, the game shows a "Too Low" style hint and reduces the score.
3. User enters another guess; if it is above the secret, the game shows a "Too High" style hint and reduces the score again.
4. User continues guessing until they enter the exact secret number; the game shows a win message and stops penalizing the score.
5. If the user runs out of attempts or chooses to restart, the game reveals the correct answer (within the expected range) and can be played again with a fresh secret number and score.

## 🧪 Test Results

```text
pytest tests/test_logic.py -v

tests/test_logic.py::test_check_guess_too_low PASSED                    [  5%]
tests/test_logic.py::test_check_guess_too_high PASSED                   [ 10%]
tests/test_logic.py::test_check_guess_win PASSED                        [ 15%]
tests/test_logic.py::test_parse_guess_valid PASSED                      [ 21%]
tests/test_logic.py::test_parse_guess_empty PASSED                      [ 26%]
tests/test_logic.py::test_parse_guess_invalid PASSED                    [ 31%]
tests/test_logic.py::test_parse_guess_negative PASSED                   [ 36%]
tests/test_logic.py::test_update_score_too_high PASSED                  [ 42%]
tests/test_logic.py::test_update_score_floor_at_zero PASSED             [ 47%]
tests/test_logic.py::test_update_score_win PASSED                       [ 52%]
tests/test_logic.py::test_temperature_emoji_exact PASSED                [ 57%]
tests/test_logic.py::test_temperature_emoji_close PASSED                [ 63%]
tests/test_logic.py::test_temperature_emoji_medium PASSED               [ 68%]
tests/test_logic.py::test_temperature_emoji_far PASSED                  [ 73%]
tests/test_logic.py::test_coach_feedback_empty_history PASSED           [ 78%]
tests/test_logic.py::test_coach_feedback_single_guess PASSED            [ 84%]
tests/test_logic.py::test_coach_feedback_steady_improvement PASSED      [ 89%]
tests/test_logic.py::test_coach_feedback_mixed_guesses PASSED           [ 94%]
tests/test_logic.py::test_coach_feedback_scattered_guesses PASSED       [100%]

19 passed in 0.14s
```

## 🧪 Evaluation Script (Test Harness)

In addition to `pytest`, this project includes a standalone evaluation script that runs the core logic against predefined inputs and prints a pass/fail summary.

Run it with:
```bash
python evaluate.py
```

Sample output:
​```
[PASS] check_guess: too low
[PASS] check_guess: too high
[PASS] check_guess: win
[PASS] parse_guess: valid input
[PASS] parse_guess: empty input
[PASS] parse_guess: invalid input
[PASS] update_score: floor at zero
[PASS] update_score: win keeps score
[PASS] update_score: normal deduction
[PASS] temperature emoji: exact match
[PASS] temperature emoji: far
[PASS] coach_feedback: steady narrowing gives positive feedback
[PASS] coach_feedback: empty history handled
[PASS] coach_feedback: single guess handled

========================================
EVALUATION SUMMARY: 14/14 tests passed
========================================
​```

## 🚀 Stretch Features

**Test Harness / Evaluation Script (+2pts)**

Added `evaluate.py`, a standalone script that runs the core game logic against 14 predefined test cases covering `check_guess`, `parse_guess`, `update_score`, `get_temperature_emoji`, and `coach_feedback`. It prints a pass/fail status for each case plus a final summary count. See the "Evaluation Script" section above for how to run it and sample output.