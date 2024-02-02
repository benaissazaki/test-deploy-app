const mainPhoto = document.querySelector('.main-photo');
const smallPhotos = document.querySelectorAll('.small-photo');
const indicators = document.querySelectorAll('.active-indicator, .indicator');

const lastIndex = smallPhotos.length - 1;
const firstIndex = 0;
let currentIndex = 0;
let lastClicked;

// smallPhotos[currentIndex].style.opacity = '0.4';
smallPhotos[currentIndex].style.color = 'rgba(0, 0, 0, 0.8)'; 
smallPhotos[currentIndex].style.border = '2px solid rgb(2, 141, 247)';

function nextSlide() {
    if (lastIndex !== 0) {
        currentIndex = (currentIndex + 1) % smallPhotos.length;
        mainPhoto.src = smallPhotos[currentIndex].src;
        updateIndicators('next');    
    }
}

function prevSlide() {
    if (lastIndex !== 0) {
        currentIndex = (currentIndex - 1 + smallPhotos.length) % smallPhotos.length;
        mainPhoto.src = smallPhotos[currentIndex].src;
        updateIndicators('prev');    
    }
}

function swapPhotos(index) {
    if (lastIndex !== 0) {
        mainPhoto.src = smallPhotos[index].src;
        lastClicked = currentIndex;
        currentIndex = index;
        updateIndicators('click');    
    }
}

function updateIndicators(action) {
    indicators.forEach(indicator => indicator.classList.replace('active-indicator', 'indicator'));
    indicators[currentIndex].classList.add('active-indicator');
    switch (action) {
        case 'next':
            if (currentIndex === firstIndex) {
                // smallPhotos[currentIndex].style.opacity = '0.4'; 
                smallPhotos[currentIndex].style.color = 'rgba(0, 0, 0, 0.8)'; 
                smallPhotos[currentIndex].style.border = '2px solid rgba(2, 141, 247, 1)';
                smallPhotos[lastIndex].style.opacity = '1';
                smallPhotos[lastIndex].style.border = '2px solid transparent';
            } else {
                smallPhotos[currentIndex - 1].style.opacity = '1';
                smallPhotos[currentIndex - 1].style.border = '2px solid transparent';
                // smallPhotos[currentIndex].style.opacity = '0.4';
                smallPhotos[currentIndex].style.color = 'rgba(0, 0, 0, 0.8)'; 
                smallPhotos[currentIndex].style.border = '2px solid rgb(2, 141, 247)';
            }
            break;
        case 'prev':
            if (currentIndex === lastIndex) {
                // smallPhotos[currentIndex].style.opacity = '0.4';
                smallPhotos[currentIndex].style.color = 'rgba(0, 0, 0, 0.8)'; 
                smallPhotos[currentIndex].style.border = '2px solid rgb(2, 141, 247)';
                smallPhotos[firstIndex].style.opacity = '1';
                smallPhotos[firstIndex].style.border = '2px solid transparent';

            } else {
                smallPhotos[currentIndex + 1].style.opacity = '1';
                smallPhotos[currentIndex + 1].style.border = '2px solid transparent';
                // smallPhotos[currentIndex].style.opacity = '0.4';
                smallPhotos[currentIndex].style.color = 'rgba(0, 0, 0, 0.8)'; 
                smallPhotos[currentIndex].style.border = '2px solid rgb(2, 141, 247)';
            }
            break;
        case 'click':
            smallPhotos[lastClicked].style.opacity = '1';
            smallPhotos[lastClicked].style.border = '2px solid transparent';
            // smallPhotos[currentIndex].style.opacity = '0.4';
            smallPhotos[currentIndex].style.color = 'rgba(0, 0, 0, 0.8)'; 
            smallPhotos[currentIndex].style.border = '2px solid rgb(2, 141, 247)';
            break;
    }
}

smallPhotos.forEach((smallPhoto, index) => {
    smallPhoto.addEventListener('click', () => {
        swapPhotos(index);
    });
}); 

smallPhotos.forEach(function(smallPhoto, index) {
    smallPhoto.addEventListener('click', function() {
        if (index === currentIndex) {
            smallPhoto.style.opacity = '1';
            smallPhoto.style.transition = 'opacity 0.3s ease-in-out';
        }
    });

    smallPhoto.addEventListener('mouseover', function() {
        if (index !== currentIndex) {
            smallPhoto.style.opacity = '0.4';
            smallPhoto.style.transition = 'opacity 0.3s ease-in-out';
        }
    });

    smallPhoto.addEventListener('mouseout', function() {
        if (index !== currentIndex) {
            smallPhoto.style.opacity = '1';
            smallPhoto.style.transition = 'opacity 0.3s ease-in-out';
        }
    });
});
