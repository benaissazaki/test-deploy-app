var filterbar = document.getElementById("filterbar");
if (filterbar) {
    var cloneCreated = false;
    var filterbarClone = filterbar.cloneNode(true); 
    var lastScrollTopCategoryPage = 0;

    function hideFilterbar(filterbarClone) {
        this.document.body.removeChild(filterbarClone);
        return false;
    }

    function showFilterbar(direction) {
        switch(direction) {
            case 'up':
                filterbarClone.style.top = "80px";
                break;
            case 'down':
                filterbarClone.style.top = "0px";
                break;
        }
        filterbarClone.style.width = '100%';
        filterbarClone.style.padding = '0 10px';
        filterbarClone.style.position = 'fixed';
        filterbarClone.style.zIndex = '1';
        this.document.body.appendChild(filterbarClone);
        return true;
    }
    
    window.addEventListener("scroll", function() {
        filterbarCurrentPosition = filterbar.getBoundingClientRect();
        filterbarCurrentYPosition = filterbarCurrentPosition.y;
        filterbarCurrentPositionHeight = filterbarCurrentPosition.height;
        var currentScroll = document.documentElement.scrollTop;

        if (filterbarCurrentYPosition >= (0 + filterbarCurrentPositionHeight)) {
            if (cloneCreated) {
                cloneCreated = hideFilterbar(filterbarClone);   
            }
        }
        if (currentScroll > lastScrollTopCategoryPage && currentScroll > filterbarCurrentYPosition) {
            // Scrolling down, hide the navbar
            if (cloneCreated) {
                cloneCreated = hideFilterbar(filterbarClone);
            }
            if (filterbarCurrentYPosition <= 0) {
                // stick filterbar to the top as you reach it by scrolling down
                cloneCreated = showFilterbar('down'); 
            }

        } else {
            if (filterbarCurrentYPosition < 0) {
                // Scrolling up or at the top, show the navbar
                cloneCreated = showFilterbar('up');
            }
        }
        lastScrollTopCategoryPage = currentScroll;
    });     
    
    const filter = document.querySelector('.filter-link');
    const sidebar = document.getElementById('sidebar');

    window.addEventListener('click', function(event) {
        if (event.target.classList.value === filter.classList.value) {
            sidebar.style.display = 'block';
        } else {
            sidebar.style.display = 'none';
        }
    });

} 