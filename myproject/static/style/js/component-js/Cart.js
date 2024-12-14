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

// Hàm cập nhật tổng đơn hàng
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

// Hàm cập nhật giá trị tổng tiền khi thay đổi số lượng sản phẩm
function updateTotalPrice(productId, newQuantity) {
    const productRow = document.getElementById(`product_cart_item_${productId}`);
    if (!productRow) return;

    const unitPriceElement = productRow.querySelector(".unit_price");
    const unitPrice = parseFloat(unitPriceElement.getAttribute('data-number'));

    const totalPrice = unitPrice * newQuantity;

    const totalPriceElement = productRow.querySelector(".total_price");
    totalPriceElement.innerText = totalPrice.toFixed(0) + " ₫";
    totalPriceElement.setAttribute('data-number', totalPrice);

    updateCartTotal(); // Cập nhật lại tổng giỏ hàng sau khi thay đổi số lượng
}

// Hàm cập nhật số lượng sản phẩm trên server
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
                console.log("Số lượng đã được cập nhật:", data);

                const row = document.querySelector(`[data-key="${data.data.product_id}"]`);
                const totalPriceContainer = row.querySelector('.total_price');
                totalPriceContainer.textContent = data.data.total_price.toLocaleString() + " ₫";

                updateCartTotal(); // Cập nhật tổng đơn hàng
            } else {
                alert(data.message);
            }
        })
        .catch(error => console.error("Lỗi khi cập nhật số lượng:", error));
}

// Hàm lấy CSRF token từ cookie
function getCSRFToken() {
    const cookieValue = document.cookie.match(/csrftoken=([^;]+)/);
    return cookieValue ? cookieValue[1] : "";
}


function updateCartTotal() {
    let total = 0;
    document.querySelectorAll('.total_price').forEach(price => {
        let priceText = price.textContent.replace(/[^\d,.]/g, ''); // Loại bỏ ký tự không phải số
        console.log("Price Text: ", priceText); // In ra giá trị chưa xử lý

        let parsedPrice = parseFloat(priceText.replace(',', ''));
        console.log("Parsed Price: ", parsedPrice); // In ra giá trị đã phân tích

        if (!isNaN(parsedPrice)) {
            total += parsedPrice;
        }
    });

    console.log("Total Price: ", total); // In ra tổng tiền

    // Kiểm tra xem tổng tiền có hợp lệ không
    if (isNaN(total)) {
        console.error("Total value is invalid!");
        total = 0; // Đặt giá trị là 0 nếu không hợp lệ
    }

    const orderTotalElement = document.getElementById('order_total');
    if (orderTotalElement) {
        orderTotalElement.textContent = total.toLocaleString('vi-VN') + " ₫";
    } else {
        console.error("Element with id 'order_total' not found.");
    }
}




function updateTotalPrice(productId, newQuantity) {

    const productRow = document.getElementById(`product_cart_item_${productId}`);
    if (!productRow) return;


    const unitPriceElement = productRow.querySelector(".unit_price");
    const unitPrice = parseFloat(unitPriceElement.getAttribute('data-number'));


    const totalPrice = unitPrice * newQuantity;


    const totalPriceElement = productRow.querySelector(".total_price");
    totalPriceElement.innerText = totalPrice.toFixed(0) + " ₫";


    totalPriceElement.setAttribute('data-number', totalPrice);

    updateCartTotal();
}
function updateCartTotal() {
    let cartTotal = 0;

    document.querySelectorAll('.product_cart_item').forEach(row => {
        const totalPriceElement = row.querySelector(".total_price");
        if (totalPriceElement) {
            const totalPrice = parseFloat(totalPriceElement.getAttribute('data-number'));

            if (isNaN(totalPrice)) {
                console.error("Giá trị tổng tiền không hợp lệ:", totalPrice);
            } else {
                cartTotal += totalPrice;
            }
        }
    });

    const orderTotalElement = document.getElementById('order_total');
    if (isNaN(cartTotal)) {
        console.error("Tổng giỏ hàng không hợp lệ:", cartTotal);
    } else {
        orderTotalElement.innerText = cartTotal.toFixed(0) + " ₫";
    }
}



function getCSRFToken() {
    const cookieValue = document.cookie.match(/csrftoken=([^;]+)/);
    return cookieValue ? cookieValue[1] : "";
}

document.addEventListener('DOMContentLoaded', function () {
    updateCartTotal();
});
