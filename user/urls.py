from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('reksadana/', views.reksadana, name='reksadana'),
    path('reksadana/sell/<int:id>', views.reksadana_sell, name='reksadana_sell'),
    path('reksadana/sellall', views.reksadana_sell_all, name='reksadana_sell_all'),
]