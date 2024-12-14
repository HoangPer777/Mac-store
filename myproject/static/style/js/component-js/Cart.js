document.addEventListener('DOMContentLoaded', function () {
    // Hàm định dạng tiền tệ
    function formatCurrency(amount) {
        if (isNaN(amount)) {
            console.error("Số không hợp lệ:", amount);
            return "Giá trị không hợp lệ";
        }
        return new Intl.NumberFormat('vi-VN', {
            style: 'currency',
            currency: 'VND',
        }).format(amount);
    }

    // Áp dụng định dạng cho tất cả các giá trị có class .priceFormat
    const priceElements = document.querySelectorAll('.priceFormat');
    priceElements.forEach(function(element) {
        const rawPrice = element.getAttribute('data-number');
        const formattedPrice = formatCurrency(parseFloat(rawPrice));
        element.textContent = formattedPrice;
    });

    // Cập nhật tổng giỏ hàng khi trang đã được tải
    updateCartTotal();
});

function decreaseQuantity(button) {
    const quantityContainer = button.parentElement.querySelector(".num");
    if (!quantityContainer) return;

    let currentQuantity = parseInt(quantityContainer.innerText);

    if (currentQuantity > 1) {
        currentQuantity -= 1;
        quantityContainer.innerText = currentQuantity;

        const productId = button.dataset.productId;

        updateQuantityOnServer(productId, currentQuantity);
        updateTotalPrice(productId, currentQuantity);
    }
}
function updateOrderTotal() {
    let total = 0;
    document.querySelectorAll('.total_price').forEach(function(price) {
        const priceValue = parseFloat(price.getAttribute('data-number'));
        if (!isNaN(priceValue)) {
            total += priceValue;
        }
    });

    // Cập nhật tổng giá trị đơn hàng
    document.getElementById('order_total').textContent = total.toLocaleString() + " ₫";
}


function increaseQuantity(button) {
    const quantityContainer = button.parentElement.querySelector(".num");
    if (!quantityContainer) return;

    let currentQuantity = parseInt(quantityContainer.innerText);

    currentQuantity += 1;
    quantityContainer.innerText = currentQuantity;

    const productId = button.dataset.productId;

    updateQuantityOnServer(productId, currentQuantity);
    updateTotalPrice(productId, currentQuantity);
}

function updateQuantityOnServer(productId, newQuantity) {

    if (isNaN(newQuantity) || newQuantity <= 0) {
        alert('Số lượng không hợp lệ!');
        return;
    }

    fetch('/cart/update-quantity/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken()
        },
        body: JSON.stringify({
            product_id: productId,
            quantity: newQuantity
        })
    })
        .then(response => {
            if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
            return response.json();
        })
        .then(data => {
            if (data.status === "success") {
                console.log("Quantity updated:", data);

                const row = document.querySelector(`[data-key="${data.data.product_id}"]`);
                const totalPriceContainer = row.querySelector('.total_price');
                totalPriceContainer.textContent = data.data.total_price.toLocaleString() + " ₫";

                updateOrderTotal();
            } else {
                alert(data.message);
            }
        })
        .catch(error => console.error("Error updating quantity:", error));
}


function updateTotalPrice(productId, newQuantity) {

    const productRow = document.getElementById(`product_cart_item_${productId}`);
    if (!productRow) return;


    const unitPriceElement = productRow.querySelector(".unit_price");
    const unitPrice = parseFloat(unitPriceElement.getAttribute('data-number'));


    const totalPrice = unitPrice * newQuantity;


    const totalPriceElement = productRow.querySelector(".total_price");
    totalPriceElement.innerText = totalPrice.toFixed(0) + " ₫";


    totalPriceElement.setAttribute('data-number', `${totalPrice}`);


    updateCartTotal();
}
function updateCartTotal() {
    let total = 0;

    // Lặp qua tất cả các phần tử có class .total_price
    document.querySelectorAll('.total_price').forEach(function(priceElement) {
        const priceText = priceElement.getAttribute('data-number');
        const priceValue = parseFloat(priceText);

        if (!isNaN(priceValue)) {
            total += priceValue;
        } else {
            console.error("Giá trị không hợp lệ trong tổng tiền:", priceText);
        }
    });

    // Hiển thị tổng tiền
    const orderTotalElement = document.getElementById('order_total');
    if (orderTotalElement) {
        orderTotalElement.textContent = total.toLocaleString('vi-VN') + " ₫";
    } else {
        console.error("Không tìm thấy phần tử có id 'order_total'.");
    }
}



function getCSRFToken() {
    const cookieValue = document.cookie.match(/csrftoken=([^;]+)/);
    return cookieValue ? cookieValue[1] : "";
}

document.addEventListener('DOMContentLoaded', function () {
    updateCartTotal();
});
function removeCart(productId) {
    const csrfToken = getCSRFToken();
    fetch(`/cart/remove/${productId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ product_id: productId })
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                const cartItem = document.getElementById(`product_cart_item_${productId}`);
                if (cartItem) {
                    cartItem.remove();
                }
                const totalPriceElement = document.getElementById('order_total');
                totalPriceElement.textContent = data.new_total_price + ' ₫';
            } else {
                alert(data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while removing the item.');
        });
}
