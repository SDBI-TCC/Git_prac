
# Lab 05 — Rebase · Squash (on YOUR fork)

> Do NOT rebase the org `main`. Only your branch on your fork.

1) Create three messy commits:
```bash
git switch -c feat/rebase-demo
echo "line1" > notes.txt && git add notes.txt && git commit -m "wip 1"
echo "line2" >> notes.txt && git add notes.txt && git commit -m "wip 2"
echo "line3" >> notes.txt && git add notes.txt && git commit -m "oops typo"
```
2) Interactive rebase the last 3 commits and squash:
```bash
git rebase -i HEAD~3
# mark second/third commits as 'squash' or 'fixup', edit final message
```
3) Force‑push **to your fork** (safe here):
```bash
git push -u origin feat/rebase-demo --force-with-lease
```
4) Open a PR to the org repo.
