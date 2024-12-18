from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post

def post_list(request):
    # Captura el término de búsqueda
    query = request.GET.get('q')
    if query:
        # Filtra los posts por título
        posts = Post.objects.filter(title__icontains=query) 
    else:
        # Muestra todos los posts
        posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
