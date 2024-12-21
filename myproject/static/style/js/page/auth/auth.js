const container = document.querySelector(".container");
const togglePasswords = document.querySelectorAll(".toggle-password");


document.addEventListener("DOMContentLoaded", function () {
    const container = document.getElementById("container");
    const registerButton = document.querySelector(".register-button");
    const loginButton = document.querySelector(".login-button");

    // Kiểm tra sự kiện chuyển sang giao diện đăng ký
    registerButton.addEventListener("click", function () {
        container.classList.add("right-panel-active");
        window.history.pushState({}, "", "/auth/register/");
        console.log("URL changed to: /auth/register/");
    });

    // Kiểm tra sự kiện chuyển sang giao diện đăng nhập
    loginButton.addEventListener("click", function () {
        container.classList.remove("right-panel-active");
        window.history.pushState({}, "", "/auth/login/");
        console.log("URL changed to: /auth/login/");
    });
});


// Hiển thị/Ẩn mật khẩu
togglePasswords.forEach((togglePassword) => {
    togglePassword.addEventListener("click", function () {
        const passwordInput = document.querySelector(
            this.getAttribute("data-toggle")
        );

        const type =
            passwordInput.getAttribute("type") === "password" ? "text" : "password";
        passwordInput.setAttribute("type", type);

        this.classList.toggle("fa-eye-slash");
    });
});

window.onload = () => {
    if (!localStorage.getItem("isLoggedIn")) {
        localStorage.removeItem("isLoggedIn");
        localStorage.removeItem("userEmail");
    }
};


// Xử lý logic đăng nhập
document.querySelector("#login-form").addEventListener("submit", function (e) {
    e.preventDefault(); // Ngăn form gửi GET request mặc định

    let csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    let data = {
        email: document.getElementById('login_email').value,
        password: document.getElementById('login_password').value
    };

    fetch("/auth/login/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if (data.success) {
                alert("Login successful!");
                window.location.assign(data.redirect_url);
            } else {
                alert("Error: " + data.message);
            }
        })
        .catch(error => console.error("Error:", error));
});




document.addEventListener("DOMContentLoaded", function () {
    const registerForm = document.querySelector('form[action="/auth/register/"]');
    registerForm.addEventListener("submit", async function (e) {
        e.preventDefault(); // Ngăn form submit mặc định

        // Lấy dữ liệu từ form
        const formData = {
            full_name: document.getElementById("full_name").value,
            display_name: document.getElementById("display_name").value,
            email: document.getElementById("email").value,
            password: document.getElementById("password").value,
            confirm_password: document.getElementById("confirm_password").value,
        };

        try {
            // Gửi request dạng JSON
            const response = await fetch("/auth/register/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
                },
                body: JSON.stringify(formData),
            });

            const result = await response.json();
            if (response.ok) {
                alert("Register successful!");
                console.log(result);
            } else {
                alert("Register failed: " + result.message);
                console.log(result);
            }
        } catch (error) {
            console.error("Error:", error);
        }
    });
});