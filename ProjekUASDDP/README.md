# Kahoot CLI (Python)

Simple command-line Kahoot-like quiz game written in Python.

Run the game:

```powershell
python .\kahoot.py
```

Menu options:
- `Play quiz`: Start playing the loaded questions (timed)
- `Add question`: Add a new question interactively
- `Save questions`: Save current questions to `questions.json`
- `Export sample questions to file`: same as save
- `Quit`: Exit the program

The game loads `questions.json` if present, otherwise uses built-in sample questions.
