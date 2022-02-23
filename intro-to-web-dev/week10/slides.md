# Day 10

## Objective
- Animations, Pseudo-classes, Web Design

## Table of Contents
1. **CSS Keyframe Animations**
2. **Define the Animation**
3. **Assign the Animation**
4. **Pseudo-classes**
5. **Live code & Exercise **
6. **Website Design - Typography, Spacing, Color **
7. **Project **


## Lecture and Activities

### CSS Keyframe Animations
* We can animate HTML elements using CSS with two steps:
* Step 1: Define an animation 
* Step 2: Assign the animation 

### Define Animation
* We define an animation using the @keyframes keyword 
* Inside, we specify what CSS properties we want to change and when to change it

```javascript
/* The animation code */
@keyframes example {
  from {background-color: red;}
  to {background-color: yellow;}
}
```

### Assign Animation
* We assign an animation using the animation-name property 
* We can set the animation-duration and more properties to fine-tune how we want our animation displayed

```javascript
/* The element to apply the animation to */
div {
  width: 100px;
  height: 100px;
  background-color: red;
  animation-name: example;
  animation-duration: 4s;
}
```

### Pseduo-Classes
* Used to define a special state of an element 
* Use ":" in CSS to define the pseudo-class 
* Can be used to do things like...
  * Style an element when a mouse hovers over it 

```javascript
div:hover {
  background-color: blue;
}
```
 
### Web Design
* Success of a web application or website also depends on the design 
 
### Web Design - Typography 
* Use repetition (same fonts) for consistency and hierarchy for clear visual order 
* Add slight changes in color and style for heading types and keep it consistent! 
* Choose display fonts for headings, and text fonts for text 

### Web Design - Spacing 
* How far apart or how close shows which sections are related to each other 

### Web Design - Color
* Color calls attention and gives personality 
* Find a main color and supporting colors that match a mood (~3) 
 
## Project in Breakout Sessions with Mentors
* Go to: [Pop-Up-Penguin](https://github.com/junior-devleague/pop-up-penguin)
