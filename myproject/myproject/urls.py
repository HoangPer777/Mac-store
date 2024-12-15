from django.contrib import admin
from django.urls import include, path
from home import views as home
from product import views as product
from myproject import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    path('home/', home.get_home, name='home'),
    path('product/', include('product.url')),
    path('cart/', include('cart.url')),
    path('address/', include('address.url')), path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('cart/', include('product.url')),








] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
                  path('admin/', admin.site.urls),
                  path('home/', home.get_home, name='home'),
                  path('product/', include('product.url')),
                  path('cart/', include('cart.url')),
                path('address/', include('address.url')), path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
                  # path('cart/', include('product.url')),
                path('checkout/', include('checkout.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 79d543bf3bc5205beea91efbda29ac9998cb5c6d
