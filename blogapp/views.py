from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
# Create your views here.
#creamos una funcion post:list() que toma el request y devuelve return los valores llamando a la funcion render que pone todo junto en nuestro template el.html
""" ESTA ES LA FUNCION ORIGINAL
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blogapp/post_list.html', {'posts': posts})

"""
# esta es la funcion sin el filtro solo ordenada por fecha de publicacion el - antes del argumento en order_by es descendente

#vista para la lista de posts (el repeater)
def post_list(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'blogapp/post_list.html', {'posts': posts})

#vista para el detalle del post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    Post.objects.get(pk=pk)
    return render(request, 'blogapp/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blogapp/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blogapp/post_edit.html', {'form': form})