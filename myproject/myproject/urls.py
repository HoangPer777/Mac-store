from django.contrib import admin
from django.urls import include, path
from home import views as home
from product import views as product
from myproject import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('home/', home.get_home, name='home'),
                  path('product/', include('product.url')),
                  path('cart/', include('cart.url')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
