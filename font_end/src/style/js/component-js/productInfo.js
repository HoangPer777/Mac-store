const tabButtons = document.querySelectorAll('.tab-button');
const contents = document.querySelectorAll('.content');

tabButtons.forEach(button => {
    button.addEventListener('click', () => {
        tabButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');

        const tab = button.getAttribute('data-tab');
        contents.forEach(content => {
            content.id === tab ? content.classList.add('active') : content.classList.remove('active');
        });
    });
});

// Handle accordion toggle
const accordions = document.querySelectorAll('.accordion');

accordions.forEach(accordion => {
    accordion.addEventListener('click', () => {
        accordion.classList.toggle('active');
        const panel = accordion.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
});