// Tab functionality
const tabButtons = document.querySelectorAll('.tab-button');
const contents = document.querySelectorAll('.content');

tabButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Remove active class from all buttons and add to the clicked button
        tabButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');

        // Show the associated content section, hide others
        const tab = button.getAttribute('data-tab');
        contents.forEach(content => {
            content.id === tab ? content.classList.add('active') : content.classList.remove('active');
        });
    });
});

// Accordion functionality
const accordions = document.querySelectorAll('.accordion');

accordions.forEach(accordion => {
    accordion.addEventListener('click', () => {
        // Close all accordion panels
        accordions.forEach(acc => {
            if (acc !== accordion) {
                acc.classList.remove('active');
                acc.nextElementSibling.style.maxHeight = null;
            }
        });

        // Toggle the clicked accordion
        accordion.classList.toggle('active');
        const panel = accordion.nextElementSibling;

        // Open or close the clicked panel
        if (accordion.classList.contains('active')) {
            panel.style.maxHeight = panel.scrollHeight + "px";
        } else {
            panel.style.maxHeight = null;
        }
    });
});
