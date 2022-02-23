class SearchBar extends HTMLElement {
    constructor() {
        // Always call super constructor first!
        super();

        // Create a shadow root
        let shadow = this.attachShadow({ mode: 'open' });

        let container = document.createElement('div');

        container.setAttribute('class', 'topnav')

        // Create an input element
        let input = document.createElement('input');

        input.setAttribute('type', "text");

        input.setAttribute('placeholder', "Search...");

        // adding the input element into the container
        container.append(input);

        let style = document.createElement('style');

        // must use ``
        style.textContent = `
        /* Add a black background color to the top navigation bar */
        .topnav {
            overflow: auto;
            background-color: coral;
        }

        /* Style the search box inside the navigation bar */
        .topnav input[type=text] {
            border: none;
            font-size: 18px;
            float: right;
            padding: 6px;
            margin-top: 4px;
            margin-right: 16px;
            margin-bottom: 4px;
        }`;

        // adding the style and container into the shadow element
        shadow.appendChild(container);
        shadow.appendChild(style)
    }
}

// defining custom tag with the new class
customElements.define('search-bar', SearchBar);