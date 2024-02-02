let currIndex = 0;
const itemsPerPage = 3;
const imageSize = 350;
const totalItems = document.querySelectorAll('.carousel img').length;

function changeSlide(direction) {
    currIndex += direction * itemsPerPage;

    if (currIndex < 0) {
        currIndex = totalItems - itemsPerPage;
    } else if (currIndex >= totalItems) {
        currIndex = 0;
    }

    const translateValue = -currIndex * (imageSize + 10) + 'px'; // 10px for margin between images
    document.querySelector('.carousel').style.transform = 'translateX(' + translateValue + ')';
}