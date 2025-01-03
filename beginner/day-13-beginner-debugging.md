# Debugging 

## Describe the Problem

- Simply describe the problem. Make it understandable. If you can't describe the problem, you can't solve it.

1. What is the purpose of the code?
2. What should the program do?
2. What is the program doing?
3. What is the program not doing?

## Reproduce the Problem

- Reproduce the problem. If you can't reproduce the problem, you can't solve it.

- Does the problem occur every time you run the program?
- At what point does the problem occur?
- Does the problem occur only when a specific condition is met?

## Play Computer

- Play computer. Execute the code in your head. 
- This can be a useful technique to understand the code flow and findings bugs.

## Fix the Errors

- Errors are not bad. They are opportunities to learn.

### Errors identified in the editor
- Errors in your editor will be highlighted, usually with a red underline - fix them when you see them. You can hover over the error to see what the problem is. Or, if you are using Vim, you can view the diagnostic.

### Errors identified in the terminal
- Some errors will not be identified until you run the program. These are runtime errors.
- They will be displayed in the terminal when you run the program.
- Read the error message. It will tell you what the problem is. The error message will usually include the line number where the error occurred along with a description of the error.

## Handle Exceptions

- We can use try-except blocks to handle exceptions. This will prevent the program from crashing when an error occurs.

```python
try:
    # code that might cause an error
except Exception as e:
    # handle the error
```

- The `except` block will catch errors of the specified type. If you don't specify a type, it will catch all errors.

```python
try:
    # code that might cause an error
except ValueError as e:
    # handle the error
except TypeError as e:
    # handle the error
except Exception as e:
    # handle the error
```

## Logical Errors

- Some errors are not caught by the editor or the terminal. These are logical errors.
- Logical errors occur when the program runs without crashing but produces incorrect results.
- To find logical errors, you need to debug the program. You can use print statements to print the values of variables at different points in the program.

```python
print("You are {age} years old.")
# outputs: You are {age} years old.
# The string is not formatted correctly. 
# This will not cause an error but will produce an incorrect output.
```

## Print Debugging

- Print debugging is a simple and effective way to debug your code.
- You can use print statements to print the values of variables at different points in the program.

```python
print(variable)
```

## Debugger

- A debugger is a tool that allows you to run your program step by step and inspect the values of variables at each step.
- You can set breakpoints in your code to pause the program at a specific point. A breakpoint is indicated by a red dot in the gutter of the editor.
- You can then inspect the values of variables and step through the code to see how it executes.
- Many debuggers will have features including:

    - Step over: Execute the current line and move to the next line.
    - Step into: If the current line calls a function, step into the function and continue debugging there. This includes into standard library functions and other modules.
    - Step out: Finish debugging the current function and return to the calling function.
    - Continue: Continue running the program until the next breakpoint is reached.
    - Watch: Add variables to a watch list to monitor their values as the program runs.

## Extra Tips

### Take a Break

- If you are stuck, take a break.
- Sometimes stepping away from the problem can help you see the solution more clearly.
- Starin at the code for too long can make it harder to see the problem and will only increase your frustration and fatigue.

### Run your code often

- Run your code often to catch errors early.
- Don't wait until you have written the entire program to run it.

### Ask for help

- Don't be afraid to ask for help.
- Sometimes a fresh pair of eyes can spot the problem quickly.

### Rubber Duck Debugging

- Explain your code to someone else, or even to an inanimate object like a rubber duck.
- This can help you identify the problem and find a solution.
