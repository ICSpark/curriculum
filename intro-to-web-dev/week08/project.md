# Chatty Chatbot

Create a simple chatbot using HTML, CSS, and JS.

## Objective
Use what you have learned (If statements, functions, DOM...etc.) to create a simple chatbot that users can interact with.

## Your Challenge
1. Create a folder called "chatbot".
2. Open the folder in Atom and create the following files:
  * index.html
  * styles.css
  * app.js
3. In your index.html file, initialize the file using the shortcut ```!```, then press tab. You should get something like the following.

``` html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>

</body>
</html>
```

4. Link your CSS and JS files as follows.

``` html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="styles.css">
  <title>Document</title>
</head>
<body>

  <script src="app.js"></script>
</body>
</html>
```

## Part I: HTML
1. In your HTML file, create the following with the correct nested indented structure below. (The input, button, and p should be nested inside of the div):
  * ```div``` with an id of "container"
    * ```input``` with an id of "input"
    * ```button``` with an id of "button"
    * ```p``` with an id of "output" (no text inside)

## Part II: CSS
1. Target the ```body``` element
  * Set the ```margin``` to ```0px```
2. Target the ```div``` with an id of "container"
  * Set the ```width``` to ```calc(100vw)``` to make the container fit the full width of your screen
  * Set the ```height``` to ```calc(100vh)``` to make the container fit the full height of your screen
  * Set the ```background-color``` to ```green``` (or a color of your choice!)
  * Activate flexbox! HINT: Use ```display```...
  * Use flexbox to change the direction of items to column 
  * Use flexbox to center items horizontally and vertically
3. Target the ```input``` with an id of "input"
  * Set the ```width``` to ```500px```
  * Set the ```height``` to ```50px```
  * Set the ```font-size``` to ```30px```
4. Target the ```button``` with an id of "button"
  * Set the ```font-size``` to ```30px```
  * Set the ```padding``` to ```10px```
  * Set the ```margin-top``` to ```20px```
5. Target the ```p``` with an id of "output"
  * Set the ```font-size``` to ```30px```

## Part III: JS
1. Store the ```input```, ```button```, and ```p``` element in variables using the DOM method ```document.getElementById(elementId)```. An example is shown below:

``` javascript
var yourVariableName = document.getElementById("yourElementId");
```

2. Add an ```EventListener``` to the button that will listen for a "click event". This can be done using the pattern below:

``` javascript
button.addEventListener("click", function(){

});
```

3. When the button is clicked, we want to check the input to see what the user has typed. We can access the value of the input using ```input.value```. Create an ```if statement``` that checks if the user says "Hi". For a review of if statements, look at: https://www.w3schools.com/js/js_if_else.asp.
  * If the user says "Hi", change the ```innerHTML``` of your ```p``` element (that you should have stored in a variable at this point!) to respond with "Hi, how are you doing?" (or text of your choice)
  * Else if the user says "Good", change the ```innerHTML``` of your ```p``` element to respond with "Great! Bye!" (or text of your choice)
  * Else, change the ```innerHTML``` of your ```p``` element to respond with "Sorry! I don't understand." (or text of your choice)

4. Do you notice how limited your chatbot is? If the user types in "HI" with all capitals, or "Hi whats up?", the chatbot response will be "Sorry! I don't understand." How can we modify our code to understand and respond to more possible input values? Here are some ideas:
  * Convert the ```input.value``` string to uppercase letters - Resource: https://www.w3schools.com/jsref/jsref_touppercase.asp  
  * Use the logical operator ```||``` (OR) to accept multiple values (e.g. if the ```input.value``` is "Hi" OR "Hey" OR "Yo", then respond with "Hi, how are you doing?") - Resource: https://www.w3schools.com/js/js_comparisons.asp
  * Allow values that *include* "Hi" or "Hey"..etc. to be accepted (so that values like "Hi whats up?") can be responded to appropriately - Resource: https://www.w3schools.com/jsref/jsref_includes.asp
  * Create an array of related responses (e.g. an array for greetings, questions...etc.), and check if the ```input.value``` includes any of the array elements, then output the appropriate response - Resource: Think about how you could do this using String - https://www.w3schools.com/js/js_string_methods.asp or Array methods - https://www.w3schools.com/js/js_array_methods.asp

## Stretch Goal

1. Create and append dialogue elements (e.g. ```p``` elements that are styled to look like dialogue bubbles) to the page every time you click on the button. This will show a record of the conversation (like a text messaging app). Resource: https://www.w3schools.com/jsref/met_document_createelement.asp

