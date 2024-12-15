# Simple Interpreter

This repository contains a simple interpreter for a basic programming language that supports scoped operations and variable assignments.

--- 

## Table of Contents

1. [Overview](#overview)
2. [Supported Operations](#supported-operations)
3. [Rules](#rules)
4. [Example Program](#example-program)
5. [Implementation Details](#implementation-details)
6. [Usage](#usage)
7. [Code Structure](#code-structure)

--- 

## Overview

The interpreter executes code written in a simple programming language with the following features:

## Supported Operations

1. **Assign a variable to an integer value:**
   ```
   x = 99
   ```
   Syntax: `<name> = <integer value>`

2. **Assign a variable to another variable's value:**
   ```
   x = y
   ```
   Syntax: `<name> = <another name>`

3. **Open a scope:**
   ```
   scope {
   ```

4. **Close the last opened scope:**
   ```
   }
   ```

5. **Print the value of a variable:**
   ```
   print x
   ```
   Syntax: `print <variable name>`
   - Prints the variable's value to the screen.
   - Prints `null` if the variable does not exist.

--- 

## Rules

- Variables can be reassigned to new values.
- All variables declared or reassigned inside a scope (including nested scopes) are removed when the scope is exited.

--- 

## Example Program

### Input Code
```
x = 1
print x
scope {
 x = 2
 print x
 scope {
   x = 3
   y = x
   print x
   print y
 }
 print x
 print y
}
print x
```

### Output
```
1
2
3
3
2
null
1
```

--- 

## Implementation Details

The interpreter works by:
1. Parsing the input program line by line.
2. Maintaining a stack to track variable scopes.
3. Managing variable assignments and their lifetimes within scopes.
4. Printing the correct output for `print` statements.

--- 

## Usage

### Prerequisites
- Python 3.x

### Running the Interpreter
1. Clone this repository:
   ```
   git clone https://github.com/IgorAmi52/Simple-Interpreter.git
   cd simple_interpreter
   ```
2. Run the interpreter with a program file:
   ```
   python main.py <program_file>
   ```

--- 

## Code Structure

- **`main.py`**: Main starting point.
- **`interpreter.py`**: Interpreter class that parses and executes the program.

