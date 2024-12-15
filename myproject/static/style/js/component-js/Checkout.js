$(document).ready(function () {
    const pay = $('#pay')
    pay.on('click', function () {
        const message = {
            type: 'navigate',
            url: pay.attr('data-src'),
        }
        console.log(message);
        window.parent.postMessage(message, '*');
    })
})
document.addEventListener('DOMContentLoaded', () => {
    const backButton = document.getElementById('back');

    const targetURL = backButton.getAttribute('data-src');

    backButton.addEventListener('click', () => {
        if (targetURL) {
            window.location.href = targetURL;
        } else {
            window.history.back();
        }
    });
});
