from django.contrib import admin
from django.urls import path
from .views import product_view, ProductsView, product_detail
from Project8.views import home, loginpage
from . import views

from Project8.views import about_us
from Project8.views import contact_us,login,register_page

from django.conf import settings

from django.conf.urls.static import static


appname='products'
urlpatterns = [
path('', views.product_view, name='product_view'),
path('products-cb',ProductsView.as_view()),

path('<int:product_id>/', views.product_detail, name='product_detail')



]











