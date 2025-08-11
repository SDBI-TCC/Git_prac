
# Lab 01 — Clone · Commit · Push

1) Create a feature branch and make your first commit:
```bash
git switch -c feat/hello
python src/greet.py
git add src/greet.py
git commit -m "chore: baseline greet run"
```
2) Edit `src/calc.py` and change A and B. Commit:
```bash
git add src/calc.py
git commit -m "feat: adjust calc constants"
```
3) Push your branch to your fork:
```bash
git push -u origin feat/hello
```
4) Open a Pull Request from your fork → org repo.
