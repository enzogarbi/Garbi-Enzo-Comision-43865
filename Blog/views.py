# Importaciones necesarias para manejar las vistas, modelos y formularios.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Blog, Page
from .forms import BlogForm, PageForm

def blog_list(request):
    blogs = Blog.objects.all()  # Obtiene todos los blogs.
    return render(request, 'blog_list.html', {'blogs': blogs})

def page_detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, 'pagina_detalle.html', {'page': page})

@login_required
def blog_create(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.save()
            new_page = Page(title=new_blog.title, content=new_blog.body)
            new_page.save()
            return redirect('Blog:blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog_crear.html', {'form': form})

@login_required
def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            new_page = form.save()
            return redirect('Blog:pagina_detalle', new_page.id)
    else:
        form = PageForm()
    return render(request, 'page_crear.html', {'form': form})

@login_required
def blog_edit(request, blog_id):
    if not request.user.is_superuser:  # Comprueba si el usuario es un superusuario.
        return HttpResponseForbidden()
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('Blog:blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog_editar.html', {'form': form})

@login_required
def blog_delete(request, blog_id):
    if not request.user.is_superuser:  # Comprueba si el usuario es un superusuario.
        return HttpResponseForbidden()
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        blog.delete()  # Borra el blog.
        return redirect('Blog:blog_list')
    return render(request, 'blog_borrar.html', {'blog': blog})
