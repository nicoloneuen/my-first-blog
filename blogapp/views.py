from django.shortcuts import render

# Create your views here.
#creamos una funcion post:list() que toma el request y devuelve return los valores llamando a la funcion render que pone todo junto en nuestro template el.html
def post_list(request):
	return render(request, 'blogapp/post_list.html', {})
