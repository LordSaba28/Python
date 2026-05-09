const navbar = document.querySelector(".navbar");

let idleTimer;

window.addEventListener("scroll", () => {

    const scrollY = window.scrollY;

    /* ADD SCROLLED STYLE */

    if(scrollY > 50){
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }

    /* DYNAMIC DARKENING */

    const maxScroll =
        document.body.scrollHeight - window.innerHeight;

    const scrollProgress =
        Math.min(scrollY / maxScroll, 1);

    const opacity =
        0.15 + (scrollProgress * 0.8);

    navbar.style.background =
        `rgba(20, 3, 5, ${opacity})`;

    /* REMOVE IDLE WHILE SCROLLING */

    navbar.classList.remove("idle");

    clearTimeout(idleTimer);

    idleTimer = setTimeout(() => {
        navbar.classList.add("idle");
    }, 1200);
});