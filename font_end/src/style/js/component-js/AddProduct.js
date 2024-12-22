// Hàm thêm nhóm tùy chọn mới vào container cụ thể
function addOptionGroup(containerId) {
    // Tạo các phần tử mới
    const optionGroup = document.createElement('div');
    const select = document.createElement('select');
    const secondSelect = document.createElement('select');
    const removeButton = document.createElement('button');

    // Thêm class và nội dung cho các phần tử
    optionGroup.classList.add('option-group');

    select.classList.add('option-select');
    select.innerHTML = `
        <option value="size">Kích thước</option>
        <option value="color">Màu sắc</option>
        <option value="material">Chất liệu</option>
        <option value="style">Kiểu dáng</option>
        <option value="title">Tiêu đề</option>
    `;

    secondSelect.classList.add('option-select');
    secondSelect.innerHTML = `
        <option value="size">Kích thước</option>
        <option value="color">Màu sắc</option>
        <option value="material">Chất liệu</option>
        <option value="style">Kiểu dáng</option>
        <option value="title">Tiêu đề</option>
    `;

    removeButton.classList.add('remove-option-button');
    removeButton.innerHTML = '×';
    removeButton.onclick = function () {
        removeOptionGroup(removeButton);
    };

    // Thêm các phần tử con vào nhóm tùy chọn
    optionGroup.appendChild(select);
    optionGroup.appendChild(secondSelect);
    optionGroup.appendChild(removeButton);

    // Lấy container cần thao tác và thêm nhóm tùy chọn
    const container = document.getElementById(containerId);
    container.appendChild(optionGroup);
}

// Hàm xóa nhóm tùy chọn
function removeOptionGroup(button) {
    const optionGroup = button.parentElement; // Lấy nhóm tùy chọn
    const container = optionGroup.parentElement; // Xác định container hiện tại
    container.removeChild(optionGroup); // Xóa nhóm tùy chọn khỏi container
}

document.getElementById('fileInput').addEventListener('change', function (event) {
    const files = Array.from(event.target.files);
    const imagePreviewContainer = document.getElementById('imagePreviewContainer');
    const uploadIcon = document.getElementById('uploadIcon');
    const dragDropText = document.getElementById('dragDropText');


    uploadIcon.style.display = 'none';
    dragDropText.style.display = 'none';


    let currentImages = Array.from(imagePreviewContainer.getElementsByTagName('img'));
    let totalImages = currentImages.length + files.length;

    if (totalImages > 10) {
        files.splice(10 - currentImages.length);
    }

    files.forEach((file) => {
        const reader = new FileReader();
        reader.onload = function (e) {
            const wrapper = document.createElement('div');
            wrapper.classList.add('image-wrapper');

            const img = document.createElement('img');
            img.src = e.target.result;
            img.classList.add('preview-image');
            img.onclick = function () {
                showPreview(
                    [...Array.from(imagePreviewContainer.getElementsByTagName('img')).map(img => img.src)],
                    currentImages.length
                );
            };

            wrapper.appendChild(img);


            if (imagePreviewContainer.getElementsByClassName('image-wrapper').length === 0) {
                const primaryIcon = document.createElement('span');
                primaryIcon.className = 'primary-icon';
                primaryIcon.innerHTML = '★';
                primaryIcon.title = 'Primary Image';
                wrapper.appendChild(primaryIcon);
            }

            imagePreviewContainer.appendChild(wrapper);


            wrapper.classList.add('image-wrapper');

            img.src = e.target.result;
            img.classList.add('preview-image');

            const overlay = document.createElement('div');
            overlay.classList.add('image-overlay');

            // Icon View
            const viewIcon = document.createElement('span');
            viewIcon.className = 'icon view-icon fas fa-eye';
            viewIcon.onclick = function () {
                showPreview(
                    [...Array.from(imagePreviewContainer.getElementsByTagName('img')).map(img => img.src)],
                    currentImages.length
                );
            };

            // Icon Delete
            const deleteIcon = document.createElement('span');
            deleteIcon.className = 'icon delete-icon fas fa-trash';
            deleteIcon.onclick = function () {
                const confirmation = confirm('Bạn có chắc chắn muốn xóa hình ảnh này?');
                if (confirmation) {
                    wrapper.remove();
                }
            };

            overlay.appendChild(viewIcon);
            overlay.appendChild(deleteIcon);
            wrapper.appendChild(img);
            wrapper.appendChild(overlay);

            imagePreviewContainer.appendChild(wrapper);
        };
        reader.readAsDataURL(file);
    });


    setTimeout(() => {

        const moreImagesDiv = document.querySelector('.more-images');
        if (moreImagesDiv) {
            moreImagesDiv.remove();
        }


        const maxVisibleImages = 3;
        const totalChildren = imagePreviewContainer.querySelectorAll('.image-wrapper').length;

        if (totalChildren > maxVisibleImages) {
            const excessImages = totalChildren - maxVisibleImages;
            const moreImagesDiv = document.createElement('div');
            moreImagesDiv.className = 'more-images';
            moreImagesDiv.innerText = `+${excessImages}`;
            moreImagesDiv.onclick = function () {
                showPreview(
                    [...Array.from(imagePreviewContainer.getElementsByTagName('img')).map(img => img.src)]
                );
            };


            const lastVisibleImage = imagePreviewContainer.querySelectorAll('.image-wrapper')[maxVisibleImages - 1];
            lastVisibleImage.appendChild(moreImagesDiv);
        }
    }, 0);
});


function showPreview(images, startIndex = 0) {
    const previewModal = document.createElement('div');
    previewModal.className = 'preview-modal';

    const closeButton = document.createElement('span');
    closeButton.className = 'close-preview';
    closeButton.innerHTML = '×';
    closeButton.onclick = function () {
        document.body.removeChild(previewModal);
    };

    const carousel = document.createElement('div');
    carousel.className = 'carousel';

    images.forEach((imageSrc, index) => {
        const img = document.createElement('img');
        img.src = imageSrc;
        img.classList.add('carousel-image');
        if (index === startIndex) {
            img.style.display = 'block';
        } else {
            img.style.display = 'none';
        }

        img.addEventListener('wheel', function (event) {
            event.preventDefault();
            const scaleStep = 0.1;
            let scale = parseFloat(img.getAttribute('data-scale')) || 1;
            scale += event.deltaY < 0 ? scaleStep : -scaleStep;
            scale = Math.min(Math.max(0.5, scale), 3);
            img.style.transform = `scale(${scale})`;
            img.setAttribute('data-scale', scale);
        });
        img.addEventListener('dblclick', function () {
            img.style.transform = 'scale(1)';
            img.setAttribute('data-scale', 1);
        });

        carousel.appendChild(img);
    });

    let currentIndex = startIndex;

    const prevButton = document.createElement('button');
    prevButton.className = 'carousel-button prev';
    prevButton.innerHTML = '◀';
    prevButton.onclick = function () {
        const images = carousel.querySelectorAll('.carousel-image');
        images[currentIndex].style.display = 'none';
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        images[currentIndex].style.display = 'block';
    };

    const nextButton = document.createElement('button');
    nextButton.className = 'carousel-button next';
    nextButton.innerHTML = '▶';
    nextButton.onclick = function () {
        const images = carousel.querySelectorAll('.carousel-image');
        images[currentIndex].style.display = 'none';
        currentIndex = (currentIndex + 1) % images.length;
        images[currentIndex].style.display = 'block';
    };

    previewModal.appendChild(closeButton);
    previewModal.appendChild(prevButton);
    previewModal.appendChild(carousel);
    previewModal.appendChild(nextButton);
    document.body.appendChild(previewModal);
}