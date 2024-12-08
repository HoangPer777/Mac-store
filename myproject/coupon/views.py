from django.shortcuts import render, get_object_or_404
from .forms import CouponApplyForm
from .models import Coupon
from django.utils.timezone import now

def apply_coupon(request):
    if request.method == 'POST':
        form = CouponApplyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            coupon = get_object_or_404(Coupon, code=code, active=True)
            if coupon.from_date <= now() <= coupon.to_date and coupon.remaining > 0:
                # Mã hợp lệ, xử lý giảm giá
                coupon.remaining -= 1
                coupon.save()
                message = "Mã giảm giá đã được áp dụng!"
            else:
                message = "Mã giảm giá không hợp lệ hoặc đã hết hạn!"
        else:
            message = "Form không hợp lệ!"
    else:
        form = CouponApplyForm()
        message = ""

    return render(request, 'apply_coupon.html', {'form': form, 'message': message})

