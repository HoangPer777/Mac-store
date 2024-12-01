$(document).ready(function(){
    const iframe = $('#iframe');

    iframe.on('load', function() {
        const iframeDoc = iframe[0].contentWindow.document;
        const status = $(iframeDoc).find('.status');
        const btn= $(iframeDoc).find('.btn');
        const wrap_price = $(iframeDoc).find('.wrap_price');

        status.remove();
        btn.remove()
        wrap_price.css('padding-top', '40px');
    });


    const back_btn = $('#back_btn');
    back_btn.on('click', function () {

        const message = {
            type: 'openUserProfile',
            src: $(back_btn).attr('data-src'),
        }

        console.log(message);
        window.parent.postMessage(message, '*')
    })



});
