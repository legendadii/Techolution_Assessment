from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('<int:pk>/', views.user_detail, name='user_detail'),
    path('new/', views.user_create, name='user_create'),
    path('<int:pk>/edit/', views.user_update, name='user_update'),
    path('<int:pk>/delete/', views.user_delete, name='user_delete'),
    path('<int:user_id>/checkout/<int:book_id>/', views.checkout_book, name='checkout_book'),
    path('checkin/<int:log_id>/', views.checkin_book, name='checkin_book'),
]
