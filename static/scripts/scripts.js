
/* mobile hambuger menu */
$('.hamburger').click(function(){
$    (".nav").toggleClass("mobile-nav");
$    (this).toggleClass("is-active");
});

gsap.registerPlugin(ScrollTrigger);

gsap.utils.toArray(".panel").forEach((panel, i) => {
  ScrollTrigger.create({
    trigger: panel,
    start: "top top", 
    pin: true, 
    pinSpacing: false 
  });
});


ScrollTrigger.create({
  snap: 1 / 4 // snap whole page to the closest section!
});