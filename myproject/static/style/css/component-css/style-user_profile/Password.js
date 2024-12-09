



document.querySelectorAll('.toggle_pass')
    .forEach( function(eyeIcon) {
        eyeIcon.addEventListener('click', function (e) {
            e.preventDefault();

            const pass = eyeIcon.parentElement.getElementsByTagName('input')[0];
            if (pass && pass.type === 'password') {
                pass.type = 'text';
                eyeIcon.classList.remove('fa-eye');
                eyeIcon.classList.add('fa-eye-slash');
            } else if (pass) {
                pass.type = 'password';
                eyeIcon.classList.remove('fa-eye-slash');
                eyeIcon.classList.add('fa-eye');
            }
        })
});