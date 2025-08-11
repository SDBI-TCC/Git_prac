
# Lab 03 — Pull · Fetch · Sync

1) Instructor merges a change in the org repo.
2) Sync your fork via `upstream`:
```bash
git fetch upstream
git switch main
git merge upstream/main
git push origin main
```
If you didn't add upstream earlier, do it now:
```bash
git remote add upstream https://github.com/<org>/git_org_hands_on.git
```
