REM from source dir get text to docs/gettext (gettext is example but recommended.) -b: (action)
REM .pot
sphinx-build source docs/gettext -b gettext

REM source/{locale/{language}}
REM Create .po

REM sphinx-intl update -p docs/gettext  # If the language directory already exists, just using this command!
sphinx-intl update -p docs/gettext -l zh_TW -l en
REM sphinx-intl update -p docs/gettext -l en  It't ok {-l multiple language}


REM Translator in ...

REM 
REM sphinx-build -E -b html source docs/zh-tw  -D language=zh_TW
sphinx-build -b html source docs/zh_TW  -D language=zh_TW
sphinx-build -b html source docs/en     -D language=en
