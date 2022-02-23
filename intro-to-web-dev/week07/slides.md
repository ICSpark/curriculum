# Day 7

## Objective
- Document Object Model

## Table of Contents
1. **Review Game**
2. **Review Previous Project**
3. **Lecture and Activities**
  * Browser Rendering a Webpage 
  * Document Object Model
  * Changing HTML elements
4. **Project in Breakout Sessions with Mentors**
  * My Pokedex

## Lecture and Activities

### Browser Rendering a Web Page 
* Person wants to visit a website
* The device will render a browser, which creates the DOM of the page by creating JS objects for each HTML element
* The browser will request the HTML for the website to the server, and the server will send it to the browser


### Document Object Model
* When a web page is loaded, the browser creates a Document Object Model (DOM) of the page
* The DOM is constructed as a tree of Objects
* Each tag in the html document is constructed as an object in the DOM
  * Nested elements in the html document are treated as “children” or “branches” in the DOM

### The DOM Object Model
* The document object represents your web page 
* If you want to access any HTML element, you start with accessing document 
* Examples of methods to use to find elements are shown below

```
document.getElementById(id) - Find a element by element id
document.getElementsByTagName(name) - Find elements by tag name
document.getElementsByClassName(name) - Find elements by class name
```

### Document Object Model
* With the DOM, JavaScript can do things like...
  * Change all the HTML elements in the page
  * Change all the HTML attributes in the page
  * Change all the CSS styles in the page
  * Remove existing HTML elements and attributes
  * Add new HTML elements and attributes 
  * React to all existing HTML events in the page

### Review on Objects
* Properties are the name:value pairs in an object
* Methods are actions that can be performed on objects 
* Remember this as you access the document object! The pattern should look familiar - just like how we would access properties or methods of any object  

### DOM Properties and Methods
* DOM properties are values (of HTML elements) that you can set or change
* DOM methods are actions you perform (on HTML elements)

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
### Finding HTML Elements
* Often times you want to manipulate HTML elements 
* To do that, you need to find the elements first
* You can do this by:
  * Finding HTML elements by id 
  * Finding HTML elements by tag name
  * Finding HTML elements by class name 
  * Finding HTML elements by CSS selectors 

### Changing HTML Elements
* We can change the inner HTML of an element, the attribute value of an element, and style of an element using DOM properties
* To change the innerHTML of the h1 above, we can do:
  * document.getElementById("title").innerHTML = "My new webpage!"; 
* To change the id of the h1 above, we can do:
  * document.getElementById("title").id = "newId"; 
* To change the color of the h1 above, we can do: 
  * document.getElementById("title").style.color = "red"; 

* Ex. ``` <h1 id="title>My webpage </h1> ```
* Where attribute could be an id, class, src, href, etc. In this example "title" is the attribute
* Where the innerHTML is "My webpage"

* Look out what we just did and notice the pattern below
  * Change innerHTML: 
     * document.getElementById("title").innerHTML = "My new webpage!"; 
  * Change attribute:
     * document.getElementById("title").id = "newId"; 
  * Change style:
    * document.getElementById("title").style.color = "red"; 

* We always use document to first access our HTML element, then we can access different methods or properties
  * Change innerHTML: 
    * document.getElementById("title").innerHTML = "My new webpage!"; 
  * Change attribute:
    * document.getElementById("title").id = "newId"; 
  * Change style:
    * document.getElementById("title").style.color = "red"; 

* Notice how you always have to type document.getElementById(id) every time you want to access your element and change something about it! 
* How do we avoid typing all of this out every single time?
  * Change innerHTML: 
    * document.getElementById(id).innerHTML = "somethingNew!"; 
  * Change attribute:
    * document.getElementById(id).attribute = "newAttribute"; 
  * Change style:
    * document.getElementById(id).style.color = "styleValue"; 

* We can put this in a variable! 
* Ex. ```var element = document.getElementById(id); ```
  * Change innerHTML: 
    * element.innerHTML = "somethingNew!"; 
  * Change attribute:
    * element.attribute = "newAttribute"; 
  * Change style:
    * element.style.property = "styleValue"; 
* look at how much shorter this code became! 



 
## Project in Breakout Sessions with Mentors
* Go to: [My Pokedex](https://github.com/junior-devleague/my-pokedex)
