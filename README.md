# quickquestion
ask chatgpt quick questions from the terminal

`qq "my question?"` or just `qq`

it will scan the files in the current directory

optionally you can provide context and a glob of the files to exclude:

```
 $ qq "does this library work?" --context "it's a trick question" --exclude_glob="**/*.py"
                                                                                                             qq                                                                                                              
┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃   ┃ question                                                                                                                                ┃ context                              ┃ sources                              ┃
┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ q │ 'does this library work?'                                                                                                               │ "it's a trick question"              │ 'quickquestion.egg-info/SOURCES.txt' │
│ a │ '\n\nUnfortunately, this is a trick question and there is no definitive answer. It depends on the specific library and how it is used.' │ 'quickquestion.egg-info/SOURCES.txt' │                                      │
└───┴─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴──────────────────────────────────────┴──────────────────────────────────────┘
```
