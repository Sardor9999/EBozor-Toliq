from django.urls import path
from .views import index, add_book,add_order,add_customer,add_user, update_user, delete_user, product_detail, add_product, Category

urlpatterns = [
    path('', index, name='index'),
    path('add/book/', add_book, name="add_book"),
    path('add/product/', add_product, name='add_product'),
    path('product/<int:pk>/', product_detail, name="product_detail"),
    path('add/order', add_order, name="add_order"),
    path('add/customer', add_customer, name="add_customer"),
    path('add/category', Category, name='Category'),
    path('add/user/', add_user, name="add_user"),
    path('update/<int:pk>/', update_user, name="update_user"),
    path('delete/<int:pk>/', delete_user, name="delete_user"),

]
