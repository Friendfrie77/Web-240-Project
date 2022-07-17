/* counter animations */
document.addEventListener('DOMContentLoaded',function counters(){
    var counter = document.getElementById('spaycounter');
    counter.innerText = '0';
    const updateCounter = () => {
      const target = +counter.getAttribute('data-target');
      const c = +counter.innerText
      const increment = target/1000;
      if(c < target){
        counter.innerText= `${Math.ceil(c+increment)}`};
        setTimeout(updateCounter, 1);
    };
    updateCounter();
  });

/* News slideshow */
let currentSlide = 1;

function showSlide(n){
  let i;
  let slides = document.getElementsByClassName("news-slide");
  if (n > slides.length) {currentSlide = 1}
  if (n < 1) {displaySlide = slides.length}
  for (i = 0; i < slides.length; i++){
    slides[i].style.display = "None";
  }
  slides[currentSlide - 1].style.display= "Block";
}
showSlide(currentSlide);

function changeslide(n){
  showSlide(currentSlide += n);
};
/* gsap index page animations */
// gsap.registerPlugin(ScrollTrigger);
// ScrollTrigger.create({
//     trigger:"#section-1",
//     start:"top top",
//     end: "bottom bottom",
//     pin: "#index-content-1"
// })

// ScrollTrigger.create({
//     trigger:"#section-2",
//     start:"top top",
//     end: "bottom 150ppx",
//     pin:"#index-content-2"
// })

  