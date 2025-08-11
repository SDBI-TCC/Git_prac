
# Lab 03 — Pull · Fetch

1) Simulate teammates changing the org repo (instructor will merge something).
2) Sync your fork:
```bash
git fetch origin
git pull
```
3) If you forked from the org, add upstream and sync:
```bash
git remote add upstream https://github.com/<org>/git_org_hands_on.git
git fetch upstream
git switch main
git merge upstream/main
git push origin main
```
