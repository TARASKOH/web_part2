from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('category/<int:id>', views.category_by_id),
    path('product/<int:id>', views.product_by_id)
]