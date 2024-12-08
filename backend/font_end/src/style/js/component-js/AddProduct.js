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

    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
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
const images_placeholder = document.getElementById("images_placeholder");
const input_list_image = document.getElementById("input_list_image");
const list_image_hidden = document.getElementById("list_image_hidden");
const add_more = document.getElementById("add_more");
const input_more = document.getElementById("input_more");






images_placeholder.addEventListener("click", (e) => {
    input_list_image.click();
})

input_list_image.addEventListener("change", (e) => {
    const files = e.target.files;
    Array.from(files).forEach(file => {

        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {

                // const img = document.createElement("img");
                // img.src = e.target.result.toString();
                // img.alt = file.name;
                // img.classList.add("image_item");
                // list_image_hidden.appendChild(img);
                // images_placeholder.style.display = "none";
                // list_image_hidden.style.display = "flex";


                //Create wrap image
                const wrap_image = document.createElement("div");
                wrap_image.classList.add("image_wrap");

                // Create img
                const img = document.createElement("img");
                img.src = e.target.result.toString();
                img.alt = file.name;
                img.classList.add("image_item");
                wrap_image.appendChild(img);

                // Create delete btn
                const delete_btn =document.createElement("i");
                delete_btn.classList.add("remove_item","fa-regular","fa-circle-xmark");
                wrap_image.appendChild(delete_btn);

                delete_btn.addEventListener("click", (e) => {
                    list_image_hidden.removeChild(delete_btn.parentElement);
                    if (list_image_hidden.childElementCount ===1 ){
                        images_placeholder.style.display = "flex";
                        list_image_hidden.style.display = "none";
                    }
                })




                list_image_hidden.appendChild(wrap_image);
                images_placeholder.style.display = "none";
                list_image_hidden.style.display = "flex";


            }
            reader.readAsDataURL(file);

        }
    })

})




add_more.addEventListener("click", (e) => {
    input_more.click();
})



input_more.addEventListener("change", (e) => {
    const files = e.target.files;
    Array.from(files).forEach(file => {

        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {

                //Create wrap image
                const wrap_image = document.createElement("div");
                wrap_image.classList.add("image_wrap");

                // Create img
                const img = document.createElement("img");
                img.src = e.target.result.toString();
                img.alt = file.name;
                img.classList.add("image_item");
                wrap_image.appendChild(img);

                // Create delete btn
                 const delete_btn =document.createElement("i");
                 delete_btn.classList.add("remove_item","fa-regular","fa-circle-xmark");
                 wrap_image.appendChild(delete_btn);

                 delete_btn.addEventListener("click", (e) => {
                     list_image_hidden.removeChild(delete_btn.parentElement);
                     if (list_image_hidden.childElementCount ===1 ){
                         images_placeholder.style.display = "flex";
                         list_image_hidden.style.display = "none";
                     }
                 })




                list_image_hidden.appendChild(wrap_image);
                images_placeholder.style.display = "none";
                list_image_hidden.style.display = "flex";

            }
            reader.readAsDataURL(file);

        }
    })

})
