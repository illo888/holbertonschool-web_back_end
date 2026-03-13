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
├── 2-arrow.js
├── 3-default-parameter.js
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

# Task 2: Arrow Functions

## Description

This task demonstrates how to rewrite a traditional JavaScript function using **ES6 arrow function syntax**.

Arrow functions inherit `this` from their surrounding scope, which means we no longer need to store `this` inside another variable like `self`.

## File

## Solution

```javascript
export default function getNeighborhoodsList() {
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  this.addNeighborhood = (newNeighborhood) => {
    this.sanFranciscoNeighborhoods.push(newNeighborhood);
    return this.sanFranciscoNeighborhoods;
  };
}
---
```
# Task 3: Parameter Defaults

## Description

This task demonstrates the use of **default parameters in ES6**.

Default parameters allow a function to use predefined values when arguments are not provided.

In the original function, conditional statements were used to check if parameters were `undefined`.  
Using ES6, we can simplify the function by assigning default values directly in the parameters.
---
```
## File
---
```
## Solution

```javascript
export default function getSumOfHoods(initialNumber, expansion1989 = 89, expansion2019 = 19) {
  return initialNumber + expansion1989 + expansion2019;
}
```
---

# Task 4: Rest Parameter Syntax

## Description

This task demonstrates the use of **rest parameters in ES6**.

Rest parameters allow a function to accept an indefinite number of arguments and store them in an array.

## File

## Solution

```javascript
export default function returnHowManyArguments(...args) {
  return args.length;
}
```
---

# Task 5: The Wonders of Spread Syntax

## Description

This task demonstrates the use of the **spread operator (`...`) in ES6**.

The spread syntax allows arrays and strings to be expanded into individual elements.

## File

## Solution

```javascript
export default function concatArrays(array1, array2, string) {
  return [...array1, ...array2, ...string];
}
