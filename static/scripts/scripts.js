
/* mobile hambuger menu */
$('.hamburger').click(function(){
$    (".nav").toggleClass("mobile-nav");
$    (this).toggleClass("is-active");
});

/* stick navbar */
let navbar = document.getElementById("navbar");
let navPos = navbar.getBoundingClientRect().top;
let nav = document.getElementById("nav");
let mobilenav = document.getElementById("navlist")
console.log(mobilenav)
window.addEventListener("scroll", function(e) {
  let scrollPos = window.scrollY;
  if (scrollPos > navPos) {
    navbar.classList.add('sticky');
  } else {
    navbar.classList.remove('sticky');
  }
});

