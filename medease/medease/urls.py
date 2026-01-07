"""
URL configuration for medease project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginusr, name='login'),
    path('logout/', views.logoutusr, name='logout'),
    path('address/', views.address, name='address'),
    path('medicines/', views.medicine_list, name='medicine_list'),
    path('medicine/<int:id>/', views.medicine_detail, name='medicine_detail'),
    path('cart/', views.cart, name='cart'),
    path('doctor/', views.doctor, name='doctor'),
    path('lab_tests/', views.lab_tests, name='lab_tests'),
    path('lab-tests/', views.lab_tests, name='lab_tests'),
    path('lab-test/<int:id>/', views.lab_test_detail, name='lab_test_detail'),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('search/', views.global_search, name='global_search'),
    path('address-upload/', views.address_upload_page, name='address_upload'),
    path('offers/', views.offer_page, name='offers'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)