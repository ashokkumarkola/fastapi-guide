```bash
git log --oneline

# Start interactive rebase
# git rebase -i <commit_hash>^
git rebase -i a1b2c3d^


# pick → drop
# pick a1b2c3d bad commit
drop a1b2c3d bad commit

# Fix conflicts
git add .
git rebase --continue

# Force push
git push origin branch-name --force-with-lease

#
git pull --rebase


#
git revert <commit_hash>
```
