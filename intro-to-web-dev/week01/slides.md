# Day 1

## Objective
- Intro to HTML, CSS, JS

## Table of Contents
1. **Game**
2. **Short Lecture**
  * Intro to HTML, CSS, JS
3. **Live Code or Activity**
  * Coding HTML and CSS in Codepen.io
4. **Project in Breakout Sessions with Mentors**
  * My First Webpage
5. **Survey**

## Short Lecture

### Intro to HTML, CSS, JS 
Building a website
- A website is a collection of web pages and resources (images, videos..etc.) 
- Coding allows us to give instructions to the computer to build our website 
- Computers don't understand regular English, we code websites by using the programming languages HTML, CSS, JS

HTML, CSS, JS: 3 Languages to build a website
- **HTML** (**H** yper **T** ext **M** arkup **L** anguage)
  - Website content (e.g. headings, paragraphs, text, images...etc.)
- **CSS** (**C** ascading **S** tyle **S** heets)
  - Website style (e.g. colors, layout, font...etc.)
- **JS** (**J** ava **S** cript)
  - Website function (e.g. triggering something to happen on click...etc.) 

## Live Code or Activity

### Coding HTML and CSS in Codepen.io 
- For now we will use Codepen to practice, this is a “playground” for developers to test code out 
- We will set up an official text editor later
- Navigate to https://codepen.io/. In the top left corner, click on "Start Coding".

### Create HTML elements

1. An HTML element is the basic building block of a webpage. [Elements](https://w3schools.com/html/html_elements.asp) have the following structure. Elements consist of a **start tag** and **end tag**, with content in between. More information about the element can be found in the start tag in the form of **attributes** (e.g. id, class, src, href...etc.).

```HTML
<h1 id="title">Hello World!</h1>
```

2. In Codepen, practice creating the following HTML elements. The tag name is in parenthesis. Create elements in Codepen by typing the tag name, then pressing tab:
* headings (**h1**, **h2**, **h3**, **h4**, **h5**, **h6**)
* paragraph (**p**)
* image (**img**)
* link (**a**)
* button (**button**)
* unordered list (**ul**) with list items (**li**)
* ordered list (**ol**) with list items (**li**)
* div (**div**)

``` html
<!-- Headings -->
<h1>Title1</h1>
<h2>Title2</h2>
<h3>Title3</h3>
<h4>Title4</h4>
<h5>Title5</h5>
<h6>Title6</h6>

<!-- Paragraph -->
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

<!-- Link -->
<a href="https://www.w3schools.com/html/html_links.asp">Learn about Links</a>

<!-- Image -->
<img src=https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12231413/Labrador-Retriever-MP.jpg"" alt="A puppy">

<!-- Button -->
<button>Click Me!</button>

<!-- Unordered List -->
<ul>
  <li>List Item1</li>
  <li>List Item2</li>
  <li>List Item3</li>
</ul>

<!-- Ordered List -->
<ol>
  <li>List Item1</li>
  <li>List Item2</li>
  <li>List Item3</li>
</ol>
```

3. We can also nest elements. This is useful if we want to organize our code into sections as follows.

``` HTML
<div class="profile-container">
  <div class="profile">
    <h2>Lizzy</h2>
    <p>I have two puppies.</p>
  </div>

  <div class="profile">
    <h2>Lizzy</h2>
    <p>I have two puppies.</p>
  </div>
</div>
```

4. [Semantic elements](https://www.w3schools.com/html/html5_semantic_elements.asp) are elements that clearly describe its meaning to the browser and developer (e.g. ```nav```, ```article```, ```section```...etc).

``` HTML
  <nav>
    <ul>
      <li>Home</li>
      <li>Members</li>
      <li>About</li>
      <li>Contact</li>
    </ul>
  </nav>
```

### Style elements in CSS

1. To add style to our elements, we need to [select](https://www.w3schools.com/css/css_selectors.asp) which elements to style, then specify which [properties](https://www.w3schools.com/cssref/default.asp) to change. Here are 10 CSS properties:
- background-color 
- color 
- font-size 
- font-weight 
- width
- height
- opacity
- background-image 

2. We can select elements by tag name, ids, or classes as follows:

``` html
<h1>Title1</h1>
<h1>Title2</h1>

<p id="p1">Paragraph 1</p>

<p>Paragraph 2</p>

<div class="profile">
  <h2>Bob</h2>
  <p>I like pizza.</p>
</div>

<div class="profile">
  <h2>Sally</h2>
  <p>I am 21 years old.</p>
</div>
```

``` css
/* Select all h1 elements and change the text color to red. */
h1 {
  color: red;
}
/* Select the element with id of p1 and change the background color to blue and position it 100px from the left and 150 px from the top of the window. */
#p1 {
  background-color: blue;
  position: fixed;
  left: 100px;
  top: 150px;
}
/* Select all elements with class of profile and change the width, height, and color. */
.profile {
  width: 300px;
  height: 500px;
  color: yellow;
}
/* Select all h2 elements within the class of profile and change the text color to red. */
.profile h2 {
  color: red;
}
```

## Project in Breakout Sessions with Mentors
1. [My first webpage](project.md)
