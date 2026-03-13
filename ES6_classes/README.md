## Task 0: You used to attend a place like this at some point

### Description
This task introduces the basics of ES6 classes.

### File
`0-classroom.js`

### Solution

```javascript
export default class ClassRoom {
  constructor(maxStudentsSize) {
    this._maxStudentsSize = maxStudentsSize;
  }
}
```
---
### Explanation

The ClassRoom class accepts one parameter, maxStudentsSize, and stores it in the _maxStudentsSize property.
## Task 1: Let's make some classrooms

### Description
Create a function named `initializeRooms` that returns an array of 3 `ClassRoom` objects.

### File
`1-make_classrooms.js`

### Solution

```javascript
import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
  return [
    new ClassRoom(19),
    new ClassRoom(20),
    new ClassRoom(34),
  ];
}
```
---
### Explanation

The function creates three ClassRoom instances with sizes 19, 20, and 34 and returns them in an array.
