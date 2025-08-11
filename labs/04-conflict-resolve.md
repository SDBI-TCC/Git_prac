
# Lab 04 — Conflict · Resolve (Pairs)

1) Pair up. Both of you create a branch named with your handle, e.g. `feat/poem-<handle>`.
2) Both edit the SAME line in `assignments/poem.txt` differently.
3) Person A opens a PR and merges.
4) Person B pulls and gets a conflict:
```bash
git pull
# Open the file and resolve <<<<<<< ======= >>>>>>> markers
git add assignments/poem.txt
git commit -m "fix: resolve poem conflict"
git push
```
5) Person B opens/merges their PR.
