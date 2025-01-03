document.addEventListener("DOMContentLoaded", function () {
    // Dropdown trong Sidebar
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
                submenu.style.display = submenu.style.display === "block" ? "none" : "block";
            }
        });
    });

    // Dropdown trong ChartComponent
    var chartDropdownToggle = document.getElementById("chartDropdownToggle");
    var chartDropdownMenu = document.getElementById("chartDropdownMenu");

    if (chartDropdownToggle && chartDropdownMenu) {
        chartDropdownToggle.addEventListener("click", function () {
            chartDropdownMenu.classList.toggle("hidden");
        });

        document.addEventListener("click", function (e) {
            if (!chartDropdownToggle.contains(e.target) && !chartDropdownMenu.contains(e.target)) {
                chartDropdownMenu.classList.add("hidden");
            }
        });
    }
});
