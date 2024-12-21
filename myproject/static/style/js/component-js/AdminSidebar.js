document.addEventListener("DOMContentLoaded", function () {
    var menus = document.querySelectorAll("#accordionExample .menu");

    menus.forEach(function (menu) {
        menu.querySelector("a").addEventListener("click", function (event) {

            var submenu = menu.querySelector("ul");
            if (submenu) {


                menus.forEach(function (otherMenu) {
                    if (otherMenu !== menu && otherMenu.querySelector("ul")) {
                        otherMenu.querySelector("ul").style.display = "none";
                    }
                });

                if (submenu.style.display === "block") {
                    submenu.style.display = "none";
                } else {
                    submenu.style.display = "block";
                }
            }
        });
    });
});
