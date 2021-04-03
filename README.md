# PyPrintSystem
A library of printing tools that you can use in your python3 project

## Functions:

### STDOut
```python
p(message, mode = 'i', verbose = False, prefix = "", suffix = linesep)
```
Printing to `STDOut`. Allows suffix's, prefix's, and verbosity. (ret: str)
- `message`: (str) The message to be printed to `STDOut`
- `mode`: (char) Mode selection (see below)
- `verbose`: (bool) Choose whether to display verbose messaging
- `prefix`: (str) Text to print before mode indicator
- `suffix`: (str) Text to print after `message`

#### Example:
```python
>>> import PyPrintSystem
>>> PyPrintSystem.p("Hello, world!", 's')
[+] Hello, world!
>>>
```

<br />
<br />

### STDIn
```python
i(message, mode = 'i')
```

Input from `STDIn`. (ret: str)
- `message`: (str) The prompt message
- `mode`: (char) Mode selection (see below)

#### Example:
```python
>>> import PyPrintSystem
>>> PyPrintSystem.i("Task failed! Would you like to re-try? ", 'e')
Tasked failed! Would you like to re-try? (STDIn) yes
'yes'
>>> 
```

<br />
<br />

### DoHeart
```python
doHeart(message, iterations = 1, delayTime = 0.1)
```

Just a nice graphical display, throwback to old Call of Duty modding. (ret: str)
- `message`: (str) Message to loop to `STDOut`
- `iterations`: (int) Number of iterations to loop for
- `delayTime`: (float) Delay between each iteration

#### Example:
```python
>>> import PyPrintSystem
>>> PyPrintSystem.doHeart("Meowdy!", 4)
[<3] Meowdy!
>>> 
```

### Modes
There are 5 modes in total, they are as follows:
- `v`: Verbose, `message` is suffixed with `[#]`
- `e`: Error, `message` is suffixed with `[-]`, input is red
- `s`: Success, `message` is suffixed with `[+]`, input is green
- `w`: Warning, `message` is suffixed with `[*]`, input is yellow
- `i`: Information, `message` is suffixed with `[!]`, input is blue

`Verbose` should have a boolean passed to detect whether to print or not. A system like this should be passed:

```python
#!/usr/bin/env python3
from sys import argv
from PyPrintSystem import *

if argv[1] == "-v":
    verbose = True
else:
    verbose = False

p("Starting application", 'v', verbose)
p("Welcome!", 's')
p("Exitting application", 'v', verbose)
doHeart("Goodbye!", 2)
```

#### Output:
```python
# python3 Test.py -v 
[#] Starting application
[+] Welcome!
[#] Exitting application
[<3] Goodbye!

# python3 Test.py
[+] Welcome!
[<3] Goodbye!

```
