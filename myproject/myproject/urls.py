from django.contrib import admin as django_admin
from django.urls import include, path
from home import views as home
from product import views as product
from myproject import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
                    path('', home.get_home, name='default_home'),
                  path('django_admin/', django_admin.site.urls),
                  # path('home/', home.get_home, name='home'),
                  path('home/',  include('home.urls')),
                  path('product/', include('product.url')),
                  path('cart/', include('cart.url')),
                    path('address/', include('address.url')),
                  path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
                  # path('cart/', include('product.url')),
                  path('auth/', include('auth.urls')),
                     # path('checkout/', include('checkout.urls')),
                     path('admin/', include('g_admin.url')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

