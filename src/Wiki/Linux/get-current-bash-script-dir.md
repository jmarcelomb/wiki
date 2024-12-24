# How to get current script directory in bash
```bash
#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

```

is a useful one-liner which will give you the full directory name of the script no matter where it is being called from.

It will work as long as the last component of the path used to find the script is not a symlink (directory links are OK). If you also want to resolve any links to the script itself, you need a multi-line solution:

```bash
#!/usr/bin/env bash

# Resolve the script's directory, even if it's a symlink
SCRIPT_SOURCE=${BASH_SOURCE[0]}
while [ -L "$SCRIPT_SOURCE" ]; do
  DIR=$(cd -P "$(dirname "$SCRIPT_SOURCE")" >/dev/null 2>&1 && pwd)
  SCRIPT_SOURCE=$(readlink "$SCRIPT_SOURCE")
  [[ $SCRIPT_SOURCE != /* ]] && SCRIPT_SOURCE=$DIR/$SCRIPT_SOURCE
done
DIR=$(cd -P "$(dirname "$SCRIPT_SOURCE")" >/dev/null 2>&1 && pwd)

cd "$DIR" || {
  echo "Error: Failed to change directory to $DIR"
  exit 1
}
```

This last one will work with any combination of aliases, source, bash -c, symlinks, etc.

Beware: if you cd to a different directory before running this snippet, the result may be incorrect!

Also, watch out for $CDPATH gotchas, and stderr output side effects if the user has smartly overridden cd to redirect output to stderr instead (including escape sequences, such as when calling update_terminal_cwd >&2 on Mac). Adding >/dev/null 2>&1 at the end of your cd command will take care of both possibilities.

To understand how it works, try running this more verbose form:

```bash
#!/usr/bin/env bash

SOURCE=${BASH_SOURCE[0]}
while [ -L "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  TARGET=$(readlink "$SOURCE")
  if [[ $TARGET == /* ]]; then
    echo "SOURCE '$SOURCE' is an absolute symlink to '$TARGET'"
    SOURCE=$TARGET
  else
    DIR=$( dirname "$SOURCE" )
    echo "SOURCE '$SOURCE' is a relative symlink to '$TARGET' (relative to '$DIR')"
    SOURCE=$DIR/$TARGET # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
  fi
done
echo "SOURCE is '$SOURCE'"
RDIR=$( dirname "$SOURCE" )
DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )
if [ "$DIR" != "$RDIR" ]; then
  echo "DIR '$RDIR' resolves to '$DIR'"
fi
echo "DIR is '$DIR'"
```
And it will print something like:
```
SOURCE './scriptdir.sh' is a relative symlink to 'sym2/scriptdir.sh' (relative to '.')
SOURCE is './sym2/scriptdir.sh'
DIR './sym2' resolves to '/home/ubuntu/dotfiles/fo fo/real/real1/real2'
DIR is '/home/ubuntu/dotfiles/fo fo/real/real1/real2'
```

## References 
- [How do I get the directory where a Bash script is located from within the script itself?](https://stackoverflow.com/questions/59895/how-do-i-get-the-directory-where-a-bash-script-is-located-from-within-the-script)