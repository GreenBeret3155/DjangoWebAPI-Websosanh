from django.urls import path, re_path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    re_path(r'^api/products/?$', views.products_list),
    re_path(r'^api/keys/?$', views.keys_list),
    re_path(r'^api/products/pk/(?P<id>\d+)/?$', views.product_detail),
    re_path(r'^api/products/key_id/(?P<key_id>\d+)/?$', views.products_by_key_id),
    path('api/keys/search/<str:key_name>/', views.keys_by_name),
    path('api/keys/hots/<str:key_name>/', views.keys_hot),
    # path('api/products', views.products_list , name='products_list'),
    # path('api/products/search/<int:pk>', views.product_detail , name='keys_list'),
    # path('api/products/search?key_id=<int:key_id>', views.products_by_id , name='products_by_id'),
    # path('api/keys', views.keys_list , name='keys_list'),

]