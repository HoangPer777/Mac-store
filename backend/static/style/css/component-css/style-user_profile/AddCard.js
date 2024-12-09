function openAddCardOverlay() {
    document.getElementById("add-card-overlay").style.display = "block";
}


function closeAddCardOverlay() {
    document.getElementById("add-card-overlay").style.display = "none";
}


window.onclick = function(event) {
    const overlay = document.getElementById("add-card-overlay");
    const container = document.querySelector(".add-card-container");
    if (event.target === overlay) {
        closeAddCardOverlay();
    }
}