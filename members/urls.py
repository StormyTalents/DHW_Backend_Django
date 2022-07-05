from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete')
]