from django.urls import path, include
from products.views import *
urlpatterns = [
    path('view/<str:poll_id>',productsview.as_view()),
    path('show/',productsshow.as_view()),
]