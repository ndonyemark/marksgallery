from django.shortcuts import render, redirect
from .models import Image

# Create your views here.

def index(request):
    images = Image.get_all_images()
    title = "View all posted pictures"
    return render(request, 'index.html', {'title': title, "images": images})

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        searched_categories = Image.search_by_category(search_term)
        message = f'{search_term}'
        return render(request, 'search.html', {'message': message, 'categories': searched_categories})
    
    else:
        message = "Sorry but none of your images has such a term"
        return render(request, 'search.html', {'message': message})
    
