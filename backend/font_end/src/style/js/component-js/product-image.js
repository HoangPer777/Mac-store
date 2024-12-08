// Select elements for the carousel
const productImage = document.getElementById("product-image");
const prevButton = document.querySelector(".prev");
const nextButton = document.querySelector(".next");
const colorOptions = document.querySelectorAll(".color-option");

// Array of image sources
const images = [
    "../../../resource/Image/2024_3_20_638465487457411344_macbook-air-m3-13-2024-xam-1.jpg", // Grey
    "../../../resource/Image/2024_3_20_638465487289151222_macbook-air-m3-13-2024-xanh-1.jpg", // Blue Black
    "../../../resource/Image/2024_3_20_638465245213555683_macbook-air-m3-13-2024-bac-1.jpg", // Silver
    "../../../resource/Image/2024_3_20_638465302276858353_macbook-air-m3-13-2024-vang-1.jpg"  // Yellow
];

let currentImageIndex = 0;

// Function to update the displayed image and selected color option
function updateImage(index) {
    productImage.src = images[index];

    // Update the "selected" class for color options
    colorOptions.forEach((opt, optIndex) => {
        opt.classList.toggle("selected", optIndex === index);
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
    option.addEventListener("click", () => {
        currentImageIndex = index; // Set the current index to the selected color's index
        updateImage(currentImageIndex);
    });
});

// Initial image display
updateImage(currentImageIndex);
