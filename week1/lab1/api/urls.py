from django.urls import path
from api.views import product_list, product_detail, login, logout


urlpatterns = [
    path('product/', product_list),
    path('product/<int:pk>/', product_detail),
    path('login/', login),
    path('logout/', logout)
]

