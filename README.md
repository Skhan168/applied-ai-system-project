# 🎮 Game Glitch Investigator: The Impossible Guesser

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

## 📝 Document Your Experience

- The game's purpose is to let a player pick a difficulty level and try to guess a secret number within a certain range, while getting "Too High" or "Too Low" hints and watching their score change based on their guesses.
- I found several bugs: the hints could tell me to go higher and then lower around the same number, the final "answer" at game over could be outside the expected range, the score could drop below zero, and restarting the game did not always reset things cleanly.
- To fix these issues, I cleaned up the game logic and moved it into `logic_utils.py`, corrected how guesses are compared to the secret number so the hints are accurate, and made sure the scoring and state behave consistently across guesses and restarts. I also updated the tests so `check_guess()` is covered by pytest and verified that they pass.

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
# Example:
# python -m pytest -q
# 1 passed in 0.02s
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]