from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('register/',views.register, name='register'),
     path('account/', include('django.contrib.auth.urls')),
    # path('logout/',auth_views.LogoutView.as_view(template_name='registration/login.html'), name='logout'),
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)