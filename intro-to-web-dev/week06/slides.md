# Day 6

## Objective
- Javascript

## Table of Contents
1. **Review Game**
2. **Review Previous Project**
3. **Lecture and Activities**
  * JS Data Types 
  * Arrays
  * Objects
4. **Project in Breakout Sessions with Mentors**
  * Lunchtime
5. **Survey**

## Lecture and Activities

### JS Data Types 
* Previously Covered JS Data Types
  * Strings (e.g. "Jane", "Hello World!", "Blah") 
  * Numbers (e.g. 3, 5, 12, 23.2)
  * Booleans (true or false) 
* Other data types, also known as data structures since they organize and collect different types of data
  * Arrays
  * Objects


### Arrays
* Are data structures that allow us to:
  * Store multiple data types into one variable
  * Associate each data value with a position inside the array.
    * Associated positions are called an index or indices
    * Indices start at 0.

```javascript
var arr1 = ["pen", "paper"];

var arr2 = [32, "hi", 99, [32,44]];

// Arrays

var cabinet = ["notebook", "marker", "soccer ball", "camera"];
console.log(cabinet[0]); // will print out "notebook"

```

### Objects 
* Are data structures that work similarly to arrays
  * Stores multiple data types into one variable
  * Associates data with name: value pairs
    * Ex. In the car object, the name is Fiat, color is grey, and model is 500
* We can access values in an object using dot notation 
  * Example 
    * console.log(car.name) // Prints out "Fiat" 
    * console.log(car.color) // Prints out "grey" 
    * How do we print the model to the console? 

 ```javascript
 var car = {
  name: "Fiat",
  color: "grey",
  model: 500
 }
 ```
 
 ### Objects 
 * If we think about objects as a variable of variables, we can store any kind of data in a name:value pair, including functions! 
 * When a function is associated with an object, we call it a method
 * We can execute a method in the same way that we call a function

```javascript
 var car = {
  name: "Fiat",
  model: 500,
  weight: 850,
  color: "white",
  start: function() {
    console.log("Engine on.");
  },
  drive: function() {
    console.log("Vroom vroom.");
  },
  brake: function() {
    console.log("Slow slow.");
  },
  stop: function() {
    console.log("Engine off.");
  },
 }
 
 // What will car.start() do?
 // Print "Engine on."
```
 
 
## Project in Breakout Sessions with Mentors
* Go to: [Lunch Time](https://github.com/junior-devleague/lunchtime)
