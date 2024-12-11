$(document).ready(function () {
    const pay = $('#pay')
    pay.on('click', function () {

        const message ={
            type:'navigate',
            url: pay.attr('data-src')
        }

        console.log(message);
        window.parent.postMessage(message, '*');
    })
})