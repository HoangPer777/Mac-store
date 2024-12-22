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

    def save(self, commit=True):
        product = super().save(commit)

        # Lưu các ảnh nếu có
        if 'product_images' in self.files:
            for image in self.files.getlist('product_images'):
                # Upload ảnh lên Cloudinary
                upload_result = cloudinary_upload(image)
                image_url = upload_result.get('url')

                # Tạo mới ProductImage cho mỗi ảnh đã upload
                ProductImage.objects.create(
                    product=product,
                    image=image_url
                )
        return product