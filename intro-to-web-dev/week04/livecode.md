## Live Coding Example

| :warning: Warning                 |
| --------------------------------- |
| - Use Atom for the following code |

### HTML

```html
<h1 id="demo">try to click me</h1>
```

### JavaScript

```javascript
console.log("Hello World!");

var name = "Oscar";
var age = 19;
var enrolledInCollege = true;

// we can put those variable into an object
var person = {
  name,
  age,
  enrolledInCollege,
};

// what do you think this will print?
console.log(person);

// lets do some math
console.log(3 + 4); // addition
console.log(3 - 4); // subtraction
console.log(3 * 4); // multiplication
console.log(3 / 4); // division
console.log(3 ** 4); // exponentiation

// there is also the Math object
console.log(Math.pow(3, 4));
console.log(Math.round(Math.log(81) / Math.log(3)));

// lets compare things
console.log(3 > 4);
console.log(3 < 4);
console.log(3 == 4);

// strict comparison
console.log(0 == "0");
console.log(0 === "0");

// adding an EventListener
document.getElementById("demo").addEventListener("click", function () {
  console.log("clicked");
});
```

## Bonus

learn more about `let` versus `var` [here](https://stackoverflow.com/questions/762011/whats-the-difference-between-using-let-and-var)
