# ES6 Basic - Task 0: Const or let?

## Description
This task focuses on replacing `var` with modern ES6 variable declarations.

## Objective
- Use `const` when a variable is not reassigned.
- Use `let` when a variable will be reassigned or modified.

## Files
- `0-constants.js`

## What was changed
- In `taskFirst`, `var` was replaced with `const`
- In `taskNext`, `var` was replaced with `let`

## Explanation
### `const`
Used for variables that should not be reassigned after initialization.

### `let`
Used for variables whose values may change later in the code.

## Final Code
```js
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
Expected Output:
I prefer const when I can. But sometimes let is okay

  return combination;
}
