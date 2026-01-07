from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginusr, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutusr, name='logout'),
    path('address/', views.address, name='address'),
    path('add-address/', views.add_address, name='add_address'),
    path('medicine/', views.medicine_list, name='medicine_list'),
    path('medicine/<int:id>/', views.medicine_detail, name='medicine_detail'),
    path('cart/', views.cart, name='cart'),
    path('doctor/', views.doctor, name='doctor'),
    path('lab-tests/', views.lab_tests, name='lab_tests'),
    path('lab-test/<int:id>/', views.lab_test_detail, name='lab_test_detail'),
    path('healthcare/', views.healthcare, name='healthcare'),
]
