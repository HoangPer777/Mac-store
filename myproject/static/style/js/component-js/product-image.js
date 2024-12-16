// Select elements for the carousel
const productImage = document.getElementById("product-image");
const prevButton = document.querySelector(".prev");
const nextButton = document.querySelector(".next");
const colorOptions = document.querySelectorAll(".color-option img");

// Array of image sources (dynamically retrieved from img-item elements)
const images = Array.from(colorOptions).map(option => option.src);

let currentImageIndex = 0;

// Function to update the displayed image and selected color option
function updateImage(index) {
    productImage.src = images[index];

    // Update the "selected" class for color options
    colorOptions.forEach((opt, optIndex) => {
        opt.parentElement.classList.toggle("selected", optIndex === index);
    });
}

// Event listeners for previous and next buttons
prevButton.addEventListener("click", () => {
    currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
    updateImage(currentImageIndex);
});

nextButton.addEventListener("click", () => {
    currentImageIndex = (currentImageIndex + 1) % images.length;
    updateImage(currentImageIndex);
});

// Event listeners for color options
colorOptions.forEach((option, index) => {
    option.parentElement.addEventListener("click", () => {
        currentImageIndex = index; // Set the current index to the selected color's index
        updateImage(currentImageIndex);
    });
});

// Initial image display
updateImage(currentImageIndex);
