"""orders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework import routers
from django_rest_passwordreset.views import reset_password_confirm, reset_password_request_token
router = routers.SimpleRouter()
router.register(r'user', UserViewSet)
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/register', RegisterUser.as_view()),
    path('api/v1/', include(router.urls)),
    path('user/register/confirm', Сonfirmation.as_view()),
    path('user/login', LoginUser.as_view()),
    path('user/contact', ContactView.as_view()),
    path('user/contacts', ContactAPIList.as_view()),
    path('user/details', DetailUser.as_view()),
    path('user/passwordreset', reset_password_request_token),
    path('user/passwordreset/confirm', reset_password_confirm),
    path('shops', ShopView.as_view()),
    path('categories', CategoryView.as_view()),
    path('products', ProductView.as_view()),
    path('partner/update', PartnerUpdate.as_view()),
    path('partner/state', PartnerState.as_view()),
    path('partner/orders', PartnerOrders.as_view()),
    path('cart', CartView.as_view()),
    path('order', OrderView.as_view()),
]
