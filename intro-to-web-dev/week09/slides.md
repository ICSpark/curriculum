# Day 9

## Objective
- Handling Events

## Table of Contents
1. **What is an Event?**
2. **Reacting to Events**
3. **Mouse Events**
4. **Keyboard Events** 
5. **Live code & Exercise**
6. **Project in Breakout Sessions with Mentors**

## Lecture and Activities

### EVENTS
* Actions that happen on webpages 
* Examples:
  * User clicks
  * Web page loaded
  * Mouse moves over an element
  * Input field is changed
  * User presses a key on the keyboard 


### REACTING TO EVENTS
* We can react to events in different ways
  * Assign events using HTML DOM (1)
  * Add an EventListener (2)
  * Assign HTML event attributes (3)
```javascript
var button = document.getElementById("button");

button.onclick = function () {                    // 1)
  button.innerHTML = "Changed!"; 
};

button.addEventListener("click", function(){       // 2)
  button.innerHTML = "Changed!";
});
// ----------------------------------------------
<button onclick="changeText()">Click me!</button>  // 3)
```

### Using Mouse Properties & Methods
* Event handler functions are passed an argument: the event object 
* The event object holds information about that specific event 
* We can then use the properties of the event using dot notation 

```javascript
window.addEventListener("mousemove", function(event){
  console.log(event.clientX);
});
```

### Keyboard Events and Properties 
* Event handler functions are passed an argument: the event object 
* The event object holds information about that specific event 
* We can then use the properties of the event using dot notation 

```javascript
window.addEventListener("keydown", function(event){
  // If right arrow is pressed...
  if (event.keyCode === 39) {
    left = left + 10;
    character.style.left = left + "px";
  } else {
    console.log("Press the right arrow key!");
  }
});
```
 
## Project in Breakout Sessions with Mentors
* Go to: [Fishtank](https://github.com/junior-devleague/fishtank)
