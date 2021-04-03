# PyPrintSystem
A library of text printing tools that you can use in your Python3 project 

## Usage:
STDOUT:
You can use the function `p()`

    p(message, mode = 'i', verbose = False, prefix = "", suffix = linesep)
Example:

    verbose = True
    p("Hello, world", 's', verbose, "!!") # Prints "!![+] Hello, world\r\n"
    
* message: the text to write to the screen
* mode: What type of message it is (v(erbose), e(rror), s(uccess), w(arning), i(nformation)), default: i(nformation)
* verbose: Whether to desplay verbose messages or not, default: False
* prefix: Text before the []
* Suffix: Text at the end of the message

STDIN:
You can use the function `i()`

    i(message, mode = 'i', verbose = False)
Example:

    i("What is your name? ", 'i', False) # Inputs "What is your name", returns the user input
    
 * message: the text to write to the screen
 * mode: What type of message it is (v(erbose), e(rror), s(uccess), w(arning), i(nformation)), default: i(nformation)
 * verbose: Whether to desplay verbose messages or not, default: False
 
 SPECIAL:
 There is a special function, called `doHeart()`
 
 `doHeart()` is a reference to Call of Duty modding, where a specific mod called DoHeart will cause the admin name to flash colors on the side of the screen.
 
     doHeart(message, iterations = 1, delayTime = 0.1)
 Example:
 
     doHeart("Welcome, to my cool thingo", 3, 0.2)
     
 * message: The message to display to the screen
 * iterations: How many times the colors will repeat
 * delayTime: delay between colors changing

