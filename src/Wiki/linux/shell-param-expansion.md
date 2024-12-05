# Shell Parameter Expansion

https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html

## ${parameter:-word}

If parameter is unset or null, the expansion of word is substituted.\\
Otherwise, the value of parameter is substituted.

## ${parameter:=word}

If parameter is unset or null, the expansion of word is assigned to parameter.
The value of parameter is then substituted. **Positional** parameters and **special**
parameters may not be assigned to in this way.

## ${parameter:?word}

If parameter is null or unset, the expansion of word (or a message to that
effect if word is not present) is written to the standard error and the shell,
if it is not interactive, exits. Otherwise, the value of parameter is
substituted.

## ${parameter:+word}

If parameter is null or unset, nothing is substituted, otherwise the expansion
of word is substituted.

## ${parameter:offset} and ${parameter:offset:length}

```bash
$ a="12345"
$ echo ${a:1:2}
23
$ echo ${a:1:-1}
234
```

## ${parameter#word} and ${parameter##word}

  * `#` deletes the shortest match.
  * `##` deletes the longest match.

```bash
$ a="1231245"
$ echo ${a#*1}
231245
$ echo ${a##*1}
245
```

## ${parameter%word} and ${parameter%%word}

Same as above but matches from end (trailling).

## ${parameter/pattern/string}

Substitutes first pattern match with string.

## ${parameter^pattern} and ${parameter^^pattern} and \${parameter,pattern} and \${parameter,,pattern}

  * ^ makes upper-case.
  * , makes lower-case.

Makes all matched characters in pattern upper/lower-case. Pattern should now atempt to match more than 1 character. 
