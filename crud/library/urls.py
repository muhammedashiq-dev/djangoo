from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.read,name='read'),
    path('',views.create,name ='create'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('page/',views.list,name='page_list')
]
