
# Lab 00 — Setup

1) Fork the org repo to **your** GitHub account.
2) Clone your fork:
```bash
git clone https://github.com/<you>/git_org_hands_on.git
cd git_org_hands_on
```
3) Configure identity (if not already):
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
4) Verify remotes:
```bash
git remote -v
# optional: track the org as upstream
git remote add upstream https://github.com/<org>/git_org_hands_on.git
```
