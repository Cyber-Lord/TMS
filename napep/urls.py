from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('brand/', views.brand_index, name='brand'),
    path('brand/add', views.add_brand, name='add_brand'),
    path('group/', views.group_index, name='group'),
    path('group/add', views.add_group, name='add_group'),
    path('unionadmins', views.unionadmin, name='union_admin'),
    path('unionadmin/add', views.add_unionadmin, name='add_unionadmin'),
]

