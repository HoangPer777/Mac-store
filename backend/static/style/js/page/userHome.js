let slideIndex = 0;
let slideInterval;

function showSlide(index) {
    const slides = document.getElementsByClassName("carousel-slide");
    const dots = document.getElementsByClassName("dot");

    if (index >= slides.length) slideIndex = 0;
    if (index < 0) slideIndex = slides.length - 1;

    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
        dots[i].classList.remove("active");
    }

    slides[slideIndex].style.display = "block";
    dots[slideIndex].classList.add("active");
}

function nextSlide() {
    slideIndex++;
    showSlide(slideIndex);
}

function startCarousel() {
    showSlide(slideIndex);
    slideInterval = setInterval(nextSlide, 3000);
}

function stopCarousel() {
    clearInterval(slideInterval);
}

document.querySelector(".prev").addEventListener("click", function () {
    slideIndex--;
    showSlide(slideIndex);
    stopCarousel();
    startCarousel();
});

document.querySelector(".next").addEventListener("click", function () {
    slideIndex++;
    showSlide(slideIndex);
    stopCarousel();
    startCarousel();
});

const dots = document.querySelectorAll('.dot');
dots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
        slideIndex = index;
        showSlide(slideIndex);
        stopCarousel();
        startCarousel();
    });
});

window.onload = startCarousel;
