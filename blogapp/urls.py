from django.urls import path #importa la funcion path() de django.urls
from . import views #importa todas las views del directorio en el que estoy, osea blogapp
#url patterns
urlpatterns = [
#asignamos una view (post_list) al url root, y luego le asignamos un nombre leible
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #es el link que quiero en el html
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]