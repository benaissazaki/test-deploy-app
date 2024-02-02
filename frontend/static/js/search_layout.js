var searchForm = document.getElementById('search-form');
var rightFormContainer = document.getElementById('right-search');
var middleFormContainer = document.getElementById('middle-search');
var searchField = document.getElementById('product-search');
var middleLinks = document.getElementById('middle-links');
var rightLinks = document.getElementById('right-links');
var cancelLink = document.getElementById('cancel-link');

searchField.addEventListener('input', function() {
    middleFormContainer.innerHTML = ''; // Clear previous content
    middleFormContainer.appendChild(searchForm);
    searchField.focus();
    if (searchField.value.trim() !== '') {
        // If there is input, switch to the search layout
        cancelLink.style.display = 'inline-block';
        middleLinks.style.display = 'none';
        rightLinks.style.display = 'none';
    } else {
        // If whitespaces are entered switch to the search layout
        cancelLink.style.display = 'inline-block';
        middleLinks.style.display = 'none';
        rightLinks.style.display = 'none';  
    }
});

cancelLink.addEventListener('click', function(event) {
    // Prevent the default behavior of the anchor element
    event.preventDefault(); 
    rightFormContainer.innerHTML = ''; 
    cancelLink.style.display = 'none';
    middleLinks.style.display = 'inline-block';
    rightLinks.style.display = 'inline-block';
    // Move the content back to its initial spot
    rightFormContainer.appendChild(searchForm);
    searchField.value = ''; // Clear the input value
    searchField.blur(); // Remove focus from the input field
});
