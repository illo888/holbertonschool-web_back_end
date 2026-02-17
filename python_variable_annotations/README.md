# Python Variable Annotations

## 📌 Description
This project introduces Python type annotations and demonstrates how they can improve code readability, maintainability, and static analysis. It covers annotating variables, functions, and complex data structures, as well as understanding duck typing and validating code using mypy.

## 🎯 Learning Objectives
By the end of this project, you should be able to explain:

- What type annotations are in Python 3  
- How to use type annotations to specify function signatures and variable types  
- What duck typing means in Python  
- How to validate your code using mypy  

## 🛠 Requirements
- All files interpreted on **Ubuntu 20.04 LTS** using **Python 3.9**
- First line of every file must be:
- Code must follow **pycodestyle (version 2.5)**
- All files must be executable
- All modules, classes, and functions must contain proper documentation strings
- File length will be checked using `wc`

## 📂 Project Structure
Example:
0-add.py
1-concat.py
2-floor.py
3-to_str.py
...
## 🧪 Running mypy
To validate type annotations:
```bash
mypy .
🧩 Task 0: Basic Annotations – add
In this task, I created a simple function named add that demonstrates how to use type annotations in Python. The function takes two parameters, both of type float, and returns their sum as a float.

The purpose of this task is to introduce Python’s type‑hinting system and show how annotations make code easier to understand and validate using tools like mypy.

✔ What I did in this task
Created the file 0-add.py with the correct shebang line.

Wrote a fully documented module and function, following Holberton’s documentation requirements.

Implemented the function using proper type annotations:

python
def add(a: float, b: float) -> float:
    return a + b
Ensured the file is executable using chmod +x.

Tested the function using 0-main.py to confirm:

The output is correct.

The annotations appear properly in __annotations__.

This task serves as the foundation for understanding how Python handles type hints and how they improve code clarity and maintainability.
