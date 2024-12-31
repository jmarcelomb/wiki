When it comes to submodules, I like to use the following command:
```sh
git submodule update --init --recursive --remote
```

Other git commands:

```bash
git log --oneline
```

```bash
git log --stat # (files changed)
```
```bash
git log -p # (files diff)
```
```bash
git diff # shows the difference in files not commited
```
```bash
git log --oneline --decorate --graph --all # see all branchs at once
```
```bash
git reset HEAD~1 #( reset of local changes and the arguments is where to go when reset)
```
```bash
git revert HEAD # (revert commit to remote branches and the argument is the commit to be reverted)
```
```bash
git rebase -i start # rebase with interactive
```
```bash
git tag <tag_name> commit
```
```bash
git describe
```
