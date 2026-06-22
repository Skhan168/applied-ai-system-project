	# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The first time I ran the game, the UI loaded and I could enter guesses, but the behavior of the hints and results felt inconsistent. I noticed that some hints did not line up with my guesses, and the final answer at game over did not look like a normal secret number. On another run, the game even revealed the secret number to me in the UI and still gave me a strange score when I guessed it correctly. I also saw that using the restart option did not really reset the game unless I manually reloaded the browser page. I also noticed that the score could drop below zero to `-30`, which did not seem like intended game behavior.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 32, then 33 | Hints should consistently move me toward the same secret number | 32 showed "Higher" and 33 showed "Lower" | none |
| Play until attempts run out | Game should reveal a valid secret number in the normal range | Game-over message said the answer was `-35` | none |
| Enter the visible secret number exactly | Game should show a win with a sensible score update | I won, but the score displayed as `70` | none |
| Click restart after finishing a round | Game should reset without needing a browser refresh | Game would not restart correctly unless I reloaded the page | none | Keep guessing wrong until score drops | Score should stay within a reasonable minimum or reset properly | Score dropped below zero to `-30` | none |

## 2. How did you use AI as a teammate?

I used ChatGPT as my main AI teammate on this project, but I was the one actually navigating the files, making edits, and running the code. Most of the time, I tried to figure things out myself first and then asked ChatGPT for help only when I got stuck or wasn’t sure about the next step. One correct suggestion it gave me was to move the core game logic into `logic_utils.py` and then import those functions in `app.py` so the code was cleaner and easier to test. I verified that this was right by saving my changes, running the Streamlit app, and confirming it still worked the way I expected.

There were also moments when the AI’s suggestions were a bit ahead of where I was or assumed details that didn’t match my exact project. In those cases, I had to slow down, double‑check the starter code, and decide which parts of its advice actually applied to my files. I verified what was really correct by re‑running the app and pytest instead of blindly following every suggestion. That helped me treat the AI as a guide, while I stayed in control of the actual debugging and refactoring.


---

## 3. Debugging and testing your fixes

To decide whether a bug was really fixed, I tried to reproduce the original problem, make a targeted change, and then repeat the same steps to see if the behavior changed. I manually tested the app by running Streamlit, making wrong and right guesses, and watching how the hints and score reacted after my changes. I also checked that the refactor didn’t break the game by confirming that the UI still loaded correctly and that the gameplay flow felt normal. On top of that, I used pytest to test the `check_guess()` function after I moved it into `logic_utils.py`. I wrote a test to confirm that when the guess was higher than the secret, the function returned `"Too High"` and a message telling the player to go lower. When `python -m pytest -q` reported `1 passed`, it gave me extra confidence that my refactor had not changed the core logic. ChatGPT helped me understand that the function was now returning both an outcome and a message, which is why the test needed to unpack two values, but I wrote and ran the test myself.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the script from top to bottom every time the user interacts with a widget, which can reset values if you are not careful. To keep important things like the secret number, score, and attempts from changing on every rerun, you have to store them in `st.session_state`. I would explain it to a friend by saying that normal variables disappear each time Streamlit refreshes, but session state is like a special dictionary that remembers values across those reruns. Seeing how the game behaved before and after fixing the state issues made the idea more concrete. When state wasn’t handled correctly, the game felt random and inconsistent even though the UI looked fine. Once values were stored properly in session state, the game became predictable and more like a normal number‑guessing game.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse in future projects is working in small, clear steps and testing after each change instead of editing everything at once. That made it much easier to spot where something went wrong and gave me more confidence when a change actually fixed a bug. I also liked using pytest as a quick way to check that important parts of my logic still worked after a refactor.

Next time I work with AI on a coding task, I want to be even more intentional about using it only when I hit a real roadblock or need a second opinion, instead of asking it for a full solution right away. I’ll also keep verifying suggestions by running the code and tests myself. This project made me see AI‑generated code as a starting point or guide, not as something I can trust without my own debugging, testing, and judgment.
