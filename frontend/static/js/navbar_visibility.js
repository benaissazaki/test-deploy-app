var lastScrollTop = 0;
var navbar = document.getElementById("navbar");
var navbarHeight = navbar.offsetHeight;

window.addEventListener("scroll", function() {
  var currentScroll = document.documentElement.scrollTop;

  if (currentScroll > lastScrollTop && currentScroll > navbarHeight) {
    // Scrolling down, hide the navbar
    navbar.style.top = "-" + navbarHeight + "px";
  } else {
    // Scrolling up or at the top, show the navbar
    navbar.style.top = "0";
  }

  lastScrollTop = currentScroll;
});