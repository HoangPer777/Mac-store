
const cartLink = document.querySelector('.cart-icon');
const cartBadge = document.getElementById('cart-badge');

function updateCartBadge(newCount) {
    if (newCount > 0) {
        cartBadge.style.display = 'inline-block';
        cartBadge.textContent = newCount;
    } else {
        cartBadge.style.display = 'none';
    }
}

let cartCount = 0;
const addToCartButtons = document.querySelectorAll('.add-to-cart');


addToCartButtons.forEach(button => {
    button.addEventListener('click', () => {
        const productId = button.getAttribute('data-product-id');
        cartCount += 1;
        addToCart(productId);
        updateCartBadge(cartCount);
    });
});

document.addEventListener('DOMContentLoaded', () => {
    // Gửi yêu cầu GET đến backend để lấy số lượng sản phẩm hiện tại
    fetch(`/cart/total-items/`)
        .then(response => response.json())
        .then(data => {
            // Cập nhật badge với dữ liệu từ server
            updateCartBadge(data.total_items);
        })
        .catch(error => console.error('Error:', error)); // Bắt lỗi
});

// Khởi tạo ban đầu
updateCartBadge(cartCount);
cartLink.addEventListener('click', (e) => {
    // Không ngăn chặn sự kiện mặc định
    console.log("Đi đến trang giỏ hàng");
});
function addToCart(productId) {
    fetch(`/product/add/` + productId + `/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(),
        },
        body: JSON.stringify({ quantity: 1 })
    })
        .then(response => response.json()) // Chờ phản hồi từ server
        .then(data => {
            if (data.success) {
                // Cập nhật số lượng sản phẩm trong giỏ hàng
                updateCartBadge(data.total_items);
            } else {
                alert('Không thể thêm sản phẩm. Vui lòng thử lại!');
            }
        })
        .catch(error => console.error('Error:', error)); // Bắt lỗi
}


function getCSRFToken() {
    const cookie = document.cookie.split(';').find(item => item.trim().startsWith('csrftoken='));
    return cookie ? cookie.split('=')[1] : '';
}
