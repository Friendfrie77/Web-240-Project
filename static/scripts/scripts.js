
/* mobile hambuger menu */
function noScroll() {
  const hambuger = document.getElementById('hamburger-menu')
  const body = document.getElementById('body')
  if(hambuger.classList.contains('is-active')){
    body.classList.add('noScroll')
  }else{
    body.classList.remove('noScroll')
  }
}
$('.hamburger').click(function(){
$    (".nav").toggleClass("mobile-nav");
$    (this).toggleClass("is-active");
     noScroll()
});

/* stick navbar */
let navbar = document.getElementById("navbar");
let navPos = navbar.getBoundingClientRect().top;
let nav = document.getElementById("nav");
let mobilenav = document.getElementById("navlist")
window.addEventListener("scroll", function(e) {
  let scrollPos = window.scrollY;
  if (scrollPos > navPos) {
    navbar.classList.add('sticky');
  } else {
    navbar.classList.remove('sticky');
  }
});

