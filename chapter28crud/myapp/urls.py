from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name='read'),
    path('create',views.home,name='create')
    # path('update',views.home,name='update'),
    # path('delete',views.home,name='delete'),

]