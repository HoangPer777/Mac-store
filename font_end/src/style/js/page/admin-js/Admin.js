$(document).ready(function () {

    const sidebar = $('.nav-item');
    const body = $('#body iframe');
    console.log(body);

    Array.from(sidebar).forEach(function (item) {
        var src= ($(item).attr('data-src'));
        if (src){
            console.log(src)
        }
    })
})