# Day 8

## Objective
- Document Object Model Part II

## Table of Contents
1. **Review Game**
2. **Review Previous Project**
3. **Lecture and Activities**
  * DOM Review
  * Creating and Appending Elements
4. **Project in Breakout Sessions with Mentors**
  * Upgraded Chatbot

## Lecture and Activities

### Document Object Model
* When a web page is loaded, the browser creates a Document Object Model (DOM) of the page
* The DOM is constructed as a tree of Objects
* The DOM tree is something we can change!
* Using DOM in JS, we can add and remove elements, change their style and attributes...etc. 

### DOM Properties and Methods
* We can find and change HTML elements using the following methods and properties, but how do we add elements? 

* Finding HTML elements
```
document.getElementById(id)           - Find a element by element id
document.getElementsByTagName(name)   - Find elements by tag name
document.getElementsByClassName(name) - Find elements by class name
```

* Changing HTML elements
```
element.innerHTML = new html content - Change the inner HTML of an element
element.attribute = new value        - Change the attribute value of an HTML element
element.style.property = new style   - Change the style of an HTML element 
```
### Creating and Appending Elements
When we want to add HTML elements, here are the steps we need to take:
1. Create the HTML element 
2. Append it to an existing element 

* When we want to add HTML elements, here are the steps we need to take:
1. Create the HTML element using the .createElement method
2. Append it to an existing element using the .appendChild method 

Ex.
```javascript
var para = document.createElement('p);
para.innerHTML = "Hi";

document.body.appendChild(para);
```

 
## Project in Breakout Sessions with Mentors
* Go to: [Upgraded Chatbot](https://github.com/ICSpark/intro-to-web-dev/blob/master/07%20-%20Document%20Object%20Model%20Part%20I/project-chatbot.md)
