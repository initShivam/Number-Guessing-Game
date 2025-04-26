🧠 Number Guessing Game

Welcome to the **Number Guessing Game!** This is a fun console-based Python game where the computer randomly selects a number between 1 and 100, and you try to guess it.

 🎮 How to Play

- The program picks a random number between **1 and 100**.
- You choose a difficulty level:
  - **Easy** → 10 attempts
  - **Hard** → 5 attempts

- After each guess, you'll get a hint:
  - "Too low." if your guess is lower than the number.
  - "Too high." if your guess is higher than the number.
  - "You got it!" if your guess is correct.

- The game ends when you either guess the number or run out of attempts.

🚀 How to Run

Make sure you have Python installed. Then, just run the script from your terminal or any Python IDE:

```bash
python guessing_game.py
```

---

📝 Sample Output

```
Welcome to the Number Guessing Game!
I am thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too low.
You have 9 attempts remaining to guess the number.
...

📌 Notes

- The game uses the `random` module to generate the secret number.
- User input is case-insensitive for difficulty level.
- Invalid inputs for difficulty level are handled with a message.
