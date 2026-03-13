# ES6 Classes

This project focuses on learning **object-oriented programming in JavaScript using ES6 classes**.
It introduces class creation, getters and setters, inheritance, static methods, metaprogramming, and symbols.

---

### Explanation 0

This task introduces the concept of ES6 classes.
A class named `ClassRoom` is created to represent a classroom with a maximum student capacity. The constructor receives a number and stores it internally using an underscore-prefixed property `_maxStudentsSize`. This demonstrates the basic structure of a class and how class properties are initialized.

---

### Explanation 1

This task demonstrates how to create multiple instances from a class.
The function `initializeRooms` imports the `ClassRoom` class and returns an array containing three classroom objects with different capacities. This highlights how classes allow reusable object creation.

---

### Explanation 2

This task introduces **getters and setters**.
The class `HolbertonCourse` stores course information including the course name, duration, and the list of students. Each attribute is validated before assignment to ensure correct data types. Getters allow controlled access to the properties, while setters enforce validation when updating values.

---

### Explanation 3

This task focuses on class methods.
The `Currency` class represents a currency using a name and a code. A method named `displayFullCurrency` returns a formatted string combining both attributes. This demonstrates how methods can operate on class properties to produce meaningful output.

---

### Explanation 4

This task introduces **static methods** and interaction between classes.
The `Pricing` class represents a price using an amount and a currency object. It includes a method that returns a formatted price string, as well as a static method used to convert prices using a conversion rate. Static methods belong to the class itself rather than to individual instances.

---

### Explanation 5

This task introduces the concept of **abstract classes**.
The `Building` class acts as a base class that requires subclasses to implement the method `evacuationWarningMessage`. If a class extends `Building` without implementing this method, an error is thrown. This ensures that all derived classes provide their own evacuation message behavior.

---

### Explanation 6

This task demonstrates **inheritance** in ES6 classes.
The class `SkyHighBuilding` extends the `Building` class and inherits its properties. It adds a new attribute representing the number of floors and overrides the evacuation message method to provide a message specific to tall buildings.

---

### Explanation 7

This task explores how to customize the default string representation of an object.
The `Airport` class overrides the `toString()` method so that when the object is converted to a string, it returns the airport code. This demonstrates how objects can control their own string output.

---

### Explanation 8

This task introduces **metaprogramming with `Symbol.toPrimitive`**.
The `HolbertonClass` defines how the object behaves when it is converted to primitive values. When converted to a number it returns the class size, and when converted to a string it returns the class location. This allows the object to behave differently depending on the context.

---

### Explanation 9

This task fixes issues related to **hoisting and class usage order**.
Classes must be defined before they are used to create objects. The solution ensures that both `HolbertonClass` and `StudentHolberton` are declared before instances are created. Additional corrections include fixing constructor parameters and properly accessing class properties.

---

### Explanation 10

This task demonstrates advanced class behavior using **`Symbol.species`**.
The `Car` class includes a `cloneCar` method that creates a new instance of the same class as the original object. By using `Symbol.species`, subclasses that extend `Car` will correctly clone objects using their own constructor rather than the base class constructor.
