# Day 5

## Objective
- Javascript

## Table of Contents
1. **Review Game**
2. **Review Previous Project**
3. **Review JS**
  * Variables 
  * If Statements
4. **Lecture and Activities**
  * Functions
  * Console.log as a function
  * Local Variables
  * Return
5. **Project in Breakout Sessions with Mentors**
  * Cookie Monster (?)
6. **Survey**

## Lecture and Activities

### Review - Variables  
```javascript
var age = 12;
var start = true;
var name = "Jane Doe";
console.log(age)

console: ?
console: 12
```

```javascript
var age = 12;
var start = true;
var name = "Jane Doe";

age = 14;

console.log(age);

console: ?
console: 14
```
```javascript
var age = 12;
var start = true;
var name = "Jane Doe";
name = name + " Johnson";

console.log(name);

console: ? 
console: "Jane Doe Johnson"
```

```javascript
var age = 12;
var start = true;
var name = "Jane Doe";

if (age < 10) {
 console.log("Amazing.");
} else {
 console.log("Wow.");
 }
 
console: ? 
console: "Wow."
 ```
 
 ```javascript
var age = 12;
var start = true;
var name = "Jane Doe";

if (start) {
 console.log("Amazing.");
} else {
 console.log("Wow.");
 }
 
console: ? 
console: "Amazing."
 ```
 
 ### Functions
 * Blocks of code that can be called on to executed.
 * Keeps code modular and follows DRY
  * D - Don’t
  * R - Repeat
  * Y - Yourself
 * Start with the keyword function
 * Follow up with the name of the function, parenthesis, curly braces, and code to be executed.

```javascript
// Create the function
function greet() {
 console.log("Hello!");
}

// Invoke/Call/Execute/Run
greet();

console: ? 
console: "Hello."
```

### Functions
* We can add arguments to functions so we can reuse code with different arguments to get different results 
* Parameters can be added to functions to change variables inside the function 
* When calling on the function, each parameter requires an argument.
* Parameters act as variables, arguments act as values.

```javascript
// Create the function
function add(a,b) {
 console.log(a + b);
}

// Run the function
add (3,5);

console: ? 
console: 8
```

```javascript
// Create the function
function toCelsius(fahrenheit) {
 console.log((5/9)*(fahrenheit-32));
}

// Run the function
toCelsius(71);

console: ? 
console: 21.6
```

### Functions
* Create a function that prints out a greeting specifically towards that person's name to the console 
* Ex.  When I run greet("Dan"), it should print "Good Morning Dan!" to the console

### Local Variables
* Variables defined within a function become LOCAL to the function
* Local variables can only be accessed from within the function 
* Variables created inside a function
* These variables are local to the function
* Only accessible inside the function created.
 * Using a local variable outside of it’s scope will cause an error.

 ```javascript
 // Create the function
 function greet(name){
  var greeting = "Bonjour ";
  console.log(greeting + name);
 }
 
 // Run the function
 greet("John");
 
 console: ?
 console: "Bonjour John"
 ```
 
 ```javascript
 // Create the function
 function greet(name){
  var greeting = "Bonjour ";
  console.log(greeting + name);
 }
 
 console.log(greeting);
 
 console: ?
 console: "ERROR"
 ```
 ### Return
 * When JavaScript reaches a return statement, the function will stop executing 
 * Functions often compute a return value. The return value is "returned" back to the "caller" 
 * Sets the value of the called function to the returned value.
 * Once Javascript reaches a return statement, the function stops executing.
 * Can be used to write efficient functions and set functions as variables.

```javascript
// Create the function
function multiply(a,b) {
 return a*b;
}

console.log(multiply(3,5));
```
 
 
## Project in Breakout Sessions with Mentors
* Go to: [Cookie Monster](https://github.com/junior-devleague/cookie-monster)
