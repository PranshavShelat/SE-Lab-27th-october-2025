# **Lab 5 — Static Code Analysis  **

File: inventory\_system.py    
Tools Used: Pylint, Flake8, Bandit  

| Issue Type | Tool | Line(s) | Description | Fix |
| :---- | :---- | :---- | :---- | :---- |
| Mutable default argument | *Pylint (W0102)* | 8 | logs=\[\] was used as a default parameter; this creates a shared list across calls | Changed default to None and initialized inside the function |
| Bare except: block | *Pylint (W0702)* / *Bandit (B110)* | 19 | Generic exception handling (try/except/pass) hides real errors | Replaced with except Exception as e: and added a proper error message |
| Use of eval() | *Bandit (B307)* | 59 | eval() executes arbitrary code — high-risk security issue | Removed the eval() line entirely |
| File handling issues | *Pylint (W1514, R1732)* | 26, 32 | Used open() without encoding or context manager | Replaced with with open(..., encoding="utf-8") |
| Invalid naming convention | *Pylint (C0103)* | Multiple | Function names not in snake\_case | Renamed to add\_item, remove\_item, get\_qty, etc. |
| Missing function docstrings | *Pylint (C0116)* | Multiple | Functions lacked descriptive docstrings | Added concise docstrings for all functions |
| Unused imports | *Flake8 (F401)* / *Pylint (W0611)* | 2, 3 | logging and ast were imported but never used | Removed unused imports |
| Missing blank lines between functions | *Flake8 (E302, E305)* | Multiple | Functions not separated by 2 blank lines | Added required blank lines per PEP 8 |
| Line too long | *Flake8 (E501)* | 15 | Line exceeded 79 characters | Broke the long string into two lines |
| Missing module docstring | *Pylint (C0114)* | 1 | No description at top of file | Added a one-line module docstring at the top |

