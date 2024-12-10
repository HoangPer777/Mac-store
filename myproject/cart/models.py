from django.db import models

# Create your models here.
class Cart(object):
    def __init__(self, request):
        """Khởi tạo giỏ hàng với session"""
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """Thêm sản phẩm vào giỏ hàng"""
        product_id = str(product.id)
        if product_id in self.cart:
            if update_quantity:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'quantity': quantity, 'price': str(product.price)}
        self.save()

    def remove(self, product):
        """Xóa sản phẩm khỏi giỏ hàng"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def save(self):
        """Lưu giỏ hàng vào session"""
        self.session.modified = True

    def __iter__(self):
        """Duyệt qua các sản phẩm trong giỏ hàng"""
        for product_id, item in self.cart.items():
            yield item

    def __len__(self):
        """Trả về tổng số lượng sản phẩm trong giỏ hàng"""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """Trả về tổng giá của giỏ hàng"""
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())
