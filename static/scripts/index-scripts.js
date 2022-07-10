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
/* gsap index page animations */
gsap.registerPlugin(ScrollTrigger);
ScrollTrigger.create({
    trigger:"#section-1",
    start:"top top",
    end: "bottom 10px",
    pin: "#index-content-1"
})

ScrollTrigger.create({
    trigger:"#section-2",
    start:"top top",
    end: "bottom 150ppx",
    pin:"#index-content-2"
})

  