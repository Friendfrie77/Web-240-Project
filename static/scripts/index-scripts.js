/* gsap index page animations */
gsap.registerPlugin(ScrollTrigger);
ScrollTrigger.create({
    trigger:"#section-1",
    start:"top top",
    end: "bottom 150px",
    pin: "#index-content-1"
})

ScrollTrigger.create({
    trigger:"#section-2",
    start:"top top",
    end: "bottom 150ppx",
    pin:"#index-content-2"
})
/* flip card aninmations */

/* setting constents */
const pictures = gsap.utils.toArray(".cat-card");
  