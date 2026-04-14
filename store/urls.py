from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('alltrendingbooks/', views.all_trendingbooks, name='all_trendingbooks'),
    path('allofferbooks/',views.all_offerbooks,name='all_offerbooks'),
    path('allnewbooks/',views.all_newbooks,name='all_newbooks'),
    path('allbestbooks/',views.all_best,name='all_best'),
    path('allanime/',views.all_anime,name='all_anime'),
    path('allpack/',views.all_pack,name='all_pack'),
    path('allkids/',views.all_kids,name='all_kids'),
    path('search/', views.search_books, name='search_books'),
    path('book/<int:id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('update-cart/<int:id>/', views.update_cart, name='update_cart'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('payment/', views.payment, name='payment'),
    path('buy-now/<int:id>/', views.buy_now, name='buy_now'),

]