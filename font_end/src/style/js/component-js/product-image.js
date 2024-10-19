function changeImage(element) {
    const newImage = element.getAttribute('data-image');
    document.getElementById('main-image').src = newImage;
}
