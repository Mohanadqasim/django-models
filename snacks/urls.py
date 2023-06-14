from django.contrib import admin
from django.urls import path
from .views import Snack_List_View, Snack_Detail_View,Snack_List_View

urlpatterns = [
    path('', Snack_List_View.as_view(),name='snack_list'),
    path('<int:pk>/', Snack_Detail_View.as_view(),name='snack_detail'),
]