
# Lab 02 — Branch · Merge

1) Make a new branch:
```bash
git switch -c feat/readme-note
echo "- Added my name to attendees" >> README.md
git add README.md
git commit -m "docs: add my attendee note"
```
2) Merge into `main` locally and push (if org `main` is protected, use a PR instead):
```bash
git switch main
git merge feat/readme-note
git push origin main
```
