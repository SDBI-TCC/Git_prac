
# Lab 06 — Reset (safe local practice)

> Use a throwaway branch on your fork. `reset --hard` discards changes.

1) Create three commits:
```bash
git switch -c feat/reset-play
echo "A" > reset.txt && git add reset.txt && git commit -m "A"
echo "B" >> reset.txt && git add reset.txt && git commit -m "B"
echo "C" >> reset.txt && git add reset.txt && git commit -m "C"
git log --oneline --graph
```
2) Soft reset one commit back (keeps changes staged):
```bash
git reset --soft HEAD~1
git status
```
3) Mixed reset (unstage but keep changes):
```bash
git reset --mixed HEAD~1
git status
```
4) Hard reset (discard working changes) — only if you're sure:
```bash
git reset --hard HEAD~1
```
5) Push your final state to your fork.
