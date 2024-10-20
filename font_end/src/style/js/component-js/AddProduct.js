
// For Primary Image


const primaryImg = document.getElementById("primary_img");
const placeholderImg = document.getElementById("placeholder");
const imgInput = document.getElementById("image_input");
const displayImg = document.getElementById("display_img");
const imageHidden = document.getElementById("image_hidden");
const xIcon = document.getElementById("remove_img");



primaryImg.addEventListener("click", (e) => {
    imgInput.click();
})


imgInput.addEventListener("change", (e) => {
    const file = e.target.files[0];

    if (file){
        const reader = new FileReader();
        reader.onload = function (e){
            displayImg.src = e.target.result;

            imageHidden.style.display = "block";
            placeholderImg.style.display = 'none';

        }

        reader.readAsDataURL(file);
    }

})



xIcon.addEventListener("click", (e) => {
    e.stopPropagation()
    placeholderImg.style.display = "flex";
    imageHidden.style.display = "none";
    displayImg.src = "";
    imgInput.value = "";

})



// For list Image