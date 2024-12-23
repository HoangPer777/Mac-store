from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from .forms import CouponApplyForm, CouponForm
from .models import Coupon

from django.shortcuts import render


def apply_coupon(request):
    pass
    # message = ""
    # discount_amount = 0  # Giá trị giảm được
    # if request.method == 'POST':
    #     form = CouponApplyForm(request.POST)
    #     if form.is_valid():
    #         code = form.cleaned_data['code']
    #
    #         # Tìm coupon, raise 404 nếu không tồn tại
    #         coupon = get_object_or_404(Coupon, code=code, active=True)
    #
    #         # Kiểm tra điều kiện hợp lệ
    #         if coupon.from_date <= now() <= coupon.to_date and coupon.remaining > 0:
    #             # Áp dụng mã giảm giá
    #             coupon.remaining -= 1  # Giảm số lượng còn lại
    #             coupon.save()
    #
    #             # Tính toán giảm giá (theo % và giới hạn maxValue)
    #             original_price = request.POST.get('original_price', 0)
    #             original_price = float(original_price)  # Chuyển sang float
    #
    #             discount_amount = (original_price * coupon.discount / 100)
    #             if discount_amount > coupon.maxValue:
    #                 discount_amount = float(coupon.maxValue)
    #
    #             message = f"Apply success! On sale {discount_amount}."
    #         else:
    #             message = "code coupon is valid or expired"
    #     else:
    #         message = "Form is valid!"
    # else:
    #     form = CouponApplyForm()
    #
    # return render(request, 'apply_coupon.html', {
    #     'form': form,
    #     'message': message,
    #     'discount_amount': discount_amount
    # })



def create_coupon(request):
    if request.method == 'POST':
        form = CouponForm(request.POST)

        if form.is_valid():
            print(form)
            form.save()
            return redirect('g_admin:coupon_list')
    else:
        form = CouponForm()
    return render(request, 'g_admin/Dashboard.html', {'form': form})
