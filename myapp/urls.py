from django.contrib import admin
from django.urls import path
from . import views

app_name ='myapp'
urlpatterns = [
    path('',views.index),
    #path('products/',views.products,name='products'),
    #path('products/<int:id>/',views.product_detail,name="product_detail"),
    #path('products/<int:id>/',views.product_detail_1,name="product_detail_1"),
    #path('products/<int:id>/',views.product_detail_1,name="product_detail_1"),
    #path('products//',views.product_detail_2,name="product_detail_2"),

    #path('products/add/',views.add_product,name='add_product'),
    #path('products/update/<int:id>',views.update_product,name='update_product'),
    #path('products/delete/<int:id>',views.delete_product,name='delete_product')
]

# nameを指定すると<a href="{% url 'myapp:products' %}">Cancel</a>こんな感じで呼びされるようになる