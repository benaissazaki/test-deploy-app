const dropdownButton = document.getElementById('dropdown-button');
const dropDownContent = document.querySelector('.dropdown-content');

function updateButtonStyle(action) {
    switch(action) {
        case 'open':
            dropdownButton.classList.add('hovered');
            dropDownContent.style.display = 'block';
            break;
        case 'close':
            dropdownButton.classList.remove('hovered'); 
            dropDownContent.style.display = 'none';
            break;
    }
}

dropDownContent.addEventListener('click', function(event) {
    updateButtonStyle('open');
});

dropdownButton.addEventListener('click', function(event) {
    event.preventDefault();
    updateButtonStyle('open');
})

window.addEventListener('click', function(event) {
    if (event.target !== dropdownButton && !dropDownContent.contains(event.target)) {
        updateButtonStyle('close');
    }
})
