# 🎮 Game Glitch Investigator: The Impossible Guesser

## 📌 Base Project

This project extends **Game Glitch Investigator** (Module 1), a Streamlit-based number guessing game. The original goal was to let a player pick a difficulty level and guess a secret number, receiving "Too High"/"Too Low" hints while a score tracked their performance. That original version had several bugs, including inconsistent hints and score handling.

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



## 🎨 Design Decisions

- **Emoji hints** were added to make feedback feel more intuitive and fun without changing the core "Higher/Lower" logic.
- **Coach feedback** was chosen as the required AI feature because it directly builds on existing guess history data, and it gives a simple example of evaluating behavior rather than just reacting to it.
- The root-cause bug fix (removing the string/int mismatch) was prioritized over defensive code, per feedback from the original submission.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects a difficulty (for example, Normal) and the app picks a secret number in the corresponding range.
2. User enters a first guess; if it is below the secret, the game shows a "Too Low" style hint and reduces the score.
3. User enters another guess; if it is above the secret, the game shows a "Too High" style hint and reduces the score again.
4. User continues guessing until they enter the exact secret number; the game shows a win message and stops penalizing the score.
5. If the user runs out of attempts or chooses to restart, the game reveals the correct answer (within the expected range) and can be played again with a fresh secret number and score.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```text
python -m tests.test_logic

--- Testing check_guess ---
guess=50, secret=80 -> Too Low | 📈 Go HIGHER!
guess=90, secret=50 -> Too High | 📉 Go LOWER!
guess=50, secret=50 -> Win | 🎉 Correct!

--- Testing parse_guess ---
'50' -> ok=True, value=50, err=None
'' -> ok=False, value=None, err=Enter a guess.
'abc' -> ok=False, value=None, err=That is not a number.
'-5' -> ok=True, value=-5, err=None

--- Testing update_score ---
score after Too High from 100 -> 90
score after Too Low from 5 -> 0
score after Win from 100 -> 100

--- Testing get_temperature_emoji ---
guess=50, secret=50 -> 🎯
guess=48, secret=50 -> 🔥
guess=42, secret=50 -> 🌡️
guess=10, secret=50 -> 🥶

--- Testing coach_feedback ---
empty history -> No guesses were made, so there's nothing to review yet.
one guess -> You solved it in one guess! Lucky or a great instinct. 🍀
steadily improving guesses -> 🎯 Great strategy! Almost every guess got closer to the answer, which looks like an efficient narrowing-down approach.
mixed guesses -> 🙂 Decent strategy. Some guesses got closer, but a few moved away from the answer. Try adjusting your range more consistently based on each hint.
scattered guesses -> 🔄 Your guesses jumped around a lot rather than steadily narrowing in on the answer. Try picking the middle of the remaining possible range each time.

All tests passed!
```


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]