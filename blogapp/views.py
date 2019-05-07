from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.
#creamos una funcion post:list() que toma el request y devuelve return los valores llamando a la funcion render que pone todo junto en nuestro template el.html
""" ESTA ES LA FUNCION ORIGINAL
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blogapp/post_list.html', {'posts': posts})

"""
# esta es la funcion sin el filtro solo ordenada por fecha de publicacion el - antes del argumento en order_by es descendente
def post_list(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'blogapp/post_list.html', {'posts': posts})