from product.models import Product
from django.shortcuts import render, get_object_or_404

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] =  int(quantity)
        else:
            self.cart[product_id]['quantity'] +=  int(quantity)

        # Cập nhật session để lưu trạng thái mới của giỏ hàng
        self.save()

    def save(self):
        # Đánh dấu session là đã thay đổi
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids).prefetch_related('images')

        for product in products:
            primary_image = product.images.filter(is_primary=True).first()
            self.cart[str(product.id)]['product'] = product
            self.cart[str(product.id)][
                'product_image'] = primary_image.image if primary_image else None  # Lưu đối tượng ảnh, không phải URL

        for item in self.cart.values():
            item['id'] = item['product'].id
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        total_price = sum(int(item['price']) * item['quantity'] for item in self.cart.values())
        if total_price <= 0:
             print("Giá trị tổng không hợp lệ:", total_price)
             return 0
        return total_price


    def clear(self):
        del self.session['cart']
        self.save()

    def update(self, product, quantity):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] = int(quantity)
            self.save()


