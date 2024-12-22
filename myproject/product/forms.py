from django import forms
from .models import Product, ProductImage
from cloudinary.uploader import upload as cloudinary_upload

class ProductForm(forms.ModelForm):
    product_images = forms.FileField(widget=forms.ClearableFileInput(attrs={'allow_multiple_selected': False}), required=False)

    class Meta:
        model = Product
        fields = '__all__'

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and not isinstance(image, str):  # Kiểm tra nếu image không phải URL
            # Upload ảnh lên Cloudinary
            upload_result = cloudinary_upload(image)
            # Trả về URL của ảnh đã upload
            return upload_result.get('url')
        return image


