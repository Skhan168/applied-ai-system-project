# Model Card: Game Glitch Investigator (Extended)

## Limitations and Biases

This system is a simple rule-based number guessing game with an added coach feedback feature — it is not a machine learning model, so "bias" here means logic bias rather than data bias. The coach's feedback is based on a simple rule (whether each guess got numerically closer to the secret), so it can't detect smarter strategies that don't look like steady narrowing (e.g., a valid binary-search-style guess that temporarily "overshoots"). The game also only works with a small numeric range and has no support for multiplayer or persistent history across sessions.

**Future improvements:** I'd like to add persistent history across sessions, support for a wider range of difficulty tiers, and a coach feedback model that can recognize valid non-linear strategies (like binary search) instead of only rewarding steady narrowing.

## Potential Misuse

This is a low-risk educational game, so misuse potential is minimal. The main risk is a player relying on the "Developer Debug Info" panel to see the secret number and cheat, which defeats the purpose of the game. In a real deployment, that debug panel would need to be removed or password-protected.

## What Surprised Me During Testing

I was surprised that the coach feedback correctly distinguished between very different guess patterns without me hardcoding any specific numbers — steadily narrowing guesses reliably triggered the "Great strategy" message, while my scattered test run correctly triggered the "Decent strategy" message instead. This confirmed the underlying ratio-based logic was working as intended.

## AI Collaboration

I used AI (Perplexity) throughout this project for debugging, design, and implementation help.

**Helpful suggestion:** The AI helped me identify that my original bug was rooted in `app.py` converting the secret number to a string on even attempts, rather than in `check_guess()` itself. This let me fix the actual root cause instead of continuing to patch around it.

**Flawed suggestion:** In my original Module 1 submission, the AI-influenced fix I made added a `try/except TypeError` fallback inside `check_guess()` to handle the string/int mismatch instead of removing the mismatch entirely. This was flawed because it hid the bug instead of fixing it, which is exactly what my grader feedback called out. In this project, I corrected that by removing the type conversion at its source in `app.py`, so `check_guess()` never has to guess at types again.

## Testing Summary

I wrote automated tests in `tests/test_logic.py` covering all logical branches: `check_guess` (win, too high, too low), `parse_guess` (valid input, empty input, invalid input, negative numbers), `update_score` (normal deduction, score floor at 0, win case), `get_temperature_emoji` (exact match, close, medium, far), and `coach_feedback` (empty history, single guess, steady improvement, mixed guesses, scattered guesses). All 19 automated tests passed on the current implementation, and a separate standalone evaluation script (`evaluate.py`) independently confirmed 14/14 predefined checks pass. I also manually played the game twice and confirmed the coach feedback matched the actual guess pattern in both cases.