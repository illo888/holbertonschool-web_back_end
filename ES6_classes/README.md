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
