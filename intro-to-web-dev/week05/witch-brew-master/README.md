# witch-brew

It is that time of the year young witches and wizards! Today we will be brewing a secret recipe for our Halloween stew. Users will have a set of ingredients to choose from (in the form of images). When a user clicks on an image, they will add that to the mix by increasing the ingredient count. If the number and type of ingredients match your recipe, you will display the name of the recipe on the page!

## Objective
Use **JavaScript Event Listeners** to track the ingredients being added to the mix on click of the image, **If Statements** to check whether the right amount of ingredients have been added, and *CSS Keyframe Animations** to simulate the cauldron bubbling and changing colors.

## Prerequisites
To complete this project, students should have the following:
* Basic understanding of HTML structure and attributes.
* Basic understanding of CSS properties.
* Basic understanding of JavaScript and DOM.

## Your Challenge

### Part I
To complete Part I, fulfill the following requirements:
1. Set up your project file structure through the command line.
2. Create the following:
* HTML, CSS, JS file
* Folder called assets
3. Link all of your files correctly.

### Part II HTML
To complete Part II, fulfill the following requirements in HTML:

This is the order in which you should create the elements and the nesting relationships. Elements within a certain element are indented. In the end you should have 1 container with a top and bottom section. The top section will contain an ingredients section with 5 images, a count section with 5 h2 elements, and a button. The bottom section will contain an empty div and an h1 as follows.

* ```div``` with a class of "container".

  * ```div``` with a class of "top-section".

    * ```div``` with a class of "ingredients".
      * ```img``` with the source for the bat and id of "bat".
      * ```img``` with the source for the frog and id of "frog".
      * ```img``` with the source for the hat and id of "hat".
      * ```img``` with the source for the pumpkin and id of "pumpkin".
      * ```img``` with the source for the scale and id of "scale".

    * ```div``` with an id of "count".
      * ```h2``` with an id of "batcount". This h2 should contain the text: Bat: 0.
      * ```h2``` with an id of "frogcount". This h2 should contain the text: Frog: 0.
      * ```h2``` with an id of "hatcount". This h2 should contain the text: Hat: 0.
      * ```h2``` with an id of "pumpkincount". This h2 should contain the text: Pumpkin: 0.
      * ```h2``` with an id of "scalecount". This h2 should contain the text: Dragon Scale: 0.

    * ```button``` with an id of "start".

  * ```div``` with a class of "bottom-section".
    * ```div``` with an id of "cauldron".
    * ```h1``` with an id of "product". This h1 should contain the text: Nothing yet.     

### Part III CSS
To complete Part III, fulfill the following requirements in CSS:

1. We will start by building the cauldron. In your HTML, you created an empty div with an id of cauldron. In your CSS, target this div, and set the following properties:
* width: 300px;
* height: 300px;
* border-radius: 200px;
* border: 20px solid black;
* background-color: pink;

2. Use your creativity and imagination to make this site something Grandma Witch would be proud of! Use your knowledge of Flex Box and CSS properties to make your page nice and spooky. Shown below is one example of how you could lay out your page.

![Example Layout](https://github.com/junior-devleague/witch-brew/blob/master/assets/example-layout.jpg)

### Part IV JS
To complete Part IV, fulfill the following requirements in JS:
1. Use ```document.getElementById``` to grab elements from our HTML to use in our JS file. Grab the following elements and store them in variables to be used later on:
* Images of our ingredents:
  * bat image
  * frog image
  * hat image
  * pumpkin image
  * scale image
* Button to start the "mixing" of ingredients:
  * button
* Text areas to store how many ingredients we are using:
  * h1 with id of product
  * h2 with id of batcount
  * h2 with id of frogcount
  * h2 with id of hatcount
  * h2 with id of pumpkincount
  * h2 with id of scalecount

2. Create the following variables to store how many ingredients a user wants to throw into the stew:
* var batCount
* var frogCount
* var hatCount
* var pumpkinCount
* var scaleCount

Set the values of all of these variables to 0.

3. Add ```Event Listeners``` to each image to listen for a click event. When someone clicks on the ingredient, we will "add" that to our stew and the following should happen:
* The count of that ingredient will increase by 1.
* The ```innerHTML``` of the h2 storing our ingredient count will change to show how many ingredients have been thrown in. Hint: https://www.w3schools.com/jsref/prop_html_innerhtml.asp

4. Add an ```Event Listener``` to the button to listen for a click event. When someone clicks on the button, you are going to use an ```If Statement``` to check if it matches your secret recipe. If it does, the ```innerHTML``` of the product div will display the name of your recipe! If not, the ```innerHTML``` of the product div will display something like "Try Again!". Your secret recipe is how many ingredients are needed to form your stew.

For example, my secret recipe is Froggy Witch Stew! It will take at least 3 bats and 2 scales. Thus, my if statement will look something like this.

```JavaScript
if (batCount >= 3 && scaleCount >= 2) {
  //Change the innerHTML of my product div to "Foggy Witch Soup!"
} else {
  //Change the innerHTML of my product div to "Try again!"
}
```

### Stretch Goals
1. Add your own custom ingredient images to the mix.
2. Create 3 more secret recipes using different comparison operators (==, !=, >, < ...etc.).
3. Create an animation using CSS keyframes to change the background color of this brew continuously. Hint: https://www.w3schools.com/css/css3_animations.asp
