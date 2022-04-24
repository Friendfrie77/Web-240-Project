/* hero img animation */
const hero = document.querySelector('.hero');

const tl= new TimelineMax();

/* tl.fromTo(hero, .8, {height: "0%"}, {height:"35%", ease: Power2.easeInOut})
.fromTo(hero, .95, {width: "70%"}, {width: "100%", ease: Power2.easeInOut});
/* mobile hambuger menu */
$('.hamburger').click(function(){
$    (".nav").toggleClass("mobile-nav");
$    (this).toggleClass("is-active");
});
