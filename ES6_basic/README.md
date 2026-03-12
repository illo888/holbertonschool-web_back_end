# ES6 Basic

This project is part of the **Holberton School Web Back-End curriculum**.
It focuses on learning the fundamentals of **ECMAScript 2015 (ES6)** and understanding modern JavaScript syntax.

The project introduces features such as:

* `const` and `let`
* Block scope
* Arrow functions
* Template literals
* Spread and Rest operators
* Iterators and loops

---

# Learning Objectives

At the end of this project, you should be able to explain:

* What ES6 is
* New features introduced in ES6
* The difference between a constant and a variable
* Block-scoped variables
* Arrow functions
* Default function parameters
* Rest and Spread parameters
* Template strings
* Object properties in ES6
* Iterators and `for-of` loops

---

# Requirements

* Ubuntu **20.04 LTS**
* NodeJS **20.x.x**
* npm **9.x.x**
* Allowed editors:

  * `vi`
  * `vim`
  * `emacs`
  * `VS Code`

Additional requirements:

* All files must end with a **new line**
* All code must use the **.js extension**
* Code will be tested using **Jest**
* Code will be analyzed using **ESLint**
* All functions must be **exported**

---



---

# Project Structure

```
ES6_basic/
│
├── 0-constants.js
├── 1-block-scoped.js
├── README.md

```
# Task 0: Const or let?

## Description

This task focuses on replacing `var` with modern ES6 variable declarations.

## File

```
0-constants.js
```

## Solution

```javascript
export function taskFirst() {
  const task = 'I prefer const when I can.';
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  let combination = 'But sometimes let';
  combination += getLast();

  return combination;
}
```

## Explanation

* `const` is used when a variable should **not change**.
* `let` is used when a variable **can be modified**.

---

# Task 1: Block Scope

## Description

This task demonstrates the concept of **block scoping in ES6**.

Variables declared with `var` are not block scoped and can overwrite variables outside the block.

Using `let` or `const` prevents this behavior.

## File

```
1-block-scoped.js
```

## Solution

```javascript
export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    let task = true;
    let task2 = false;
  }

  return [task, task2];
}
```

## Explanation

* `var` does not respect block scope.
* `let` and `const` are **block scoped**.
* Variables declared inside the `if` block will not overwrite outer variables.

---

# Expected Output

```bash
[ false, true ]
[ false, true ]
```

---

# Author

Holberton School
Web Back-End Program
