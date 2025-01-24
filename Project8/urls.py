"""
URL configuration for Project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from Project8.views import home, loginpage, log_out
from Project8.views import about_us
from Project8.views import contact_us,login,register_page

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products-fb/', include('products.urls')),
    path('products-cb/',include('products.urls')),
    path('', include('sabad.urls')),





    path('',home),

    path('about_us',about_us),

    path('contact_us',contact_us),

    path('login',loginpage),

    path('register',register_page),

    path('logout',log_out)


]

urlpatterns =urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns =urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)