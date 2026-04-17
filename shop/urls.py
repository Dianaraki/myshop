from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.basty_bet, name='basty_bet'),
    
    
    path('catalog/', views.katalog, name='katalog'),
    
    
    path('catalog/category/<int:sanat_id>/', views.katalog, name='katalog_sanat'),
    
    
    path('product/<int:tauar_id>/', views.tauar_detail, name='tauar_detail'),

    path('category/add/', views.sanat_qosu, name='sanat_qosu'),
    path('product/add/', views.tauar_qosu, name='tauar_qosu'),
    path('product/<int:pk>/review/', views.pikir_qaldyru, name='pikir_qaldyru'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]