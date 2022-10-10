from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update', views.updatehtml, name='update'),
    path('update/<int:id>', views.update, name='update'),
    path('tags', views.updatehtml2, name='tags'),
    path('tagsin', views.updatehtml3, name='tagsin'),
]