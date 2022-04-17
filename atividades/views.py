
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Cate_por_tipo, blog
from django.contrib.auth.decorators import login_required
from django .contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

@login_required(redirect_field_name=('login'))

def home(request):
    categoria=Cate_por_tipo.objects.all()
    todos=blog.objects.all()
    blogs=blog.objects.all()
    paginator=Paginator(blogs,2)
    page=request.GET.get('p')
    blogs=paginator.get_page(page)
    return render(request,'paginas/index.html',{'blogs':blogs,'todos':todos,'categoria':categoria})
def user(request):
    usuario=get_object_or_404(blog,id=id)
    return render(request,'paginas/blog_especifico.html',{'usuario':usuario})
def busca(request):
    categoria=Cate_por_tipo.objects.all()
    todos=blog.objects.all()
    termo=request.GET.get('termo')
    if termo =='':
        messages.info(request,'Por favor pesquise um valor no Campo')
        categoria=Cate_por_tipo.objects.all()
        todos=blog.objects.all()
        blogs=blog.objects.all()
        paginator=Paginator(blogs,2)
        page=request.GET.get('p')
        blogs=paginator.get_page(page)
        return render(request,'paginas/index.html',{'blogs':blogs,'todos':todos,'categoria':categoria})
    else:
        termo=request.GET.get('termo')
        tipo=blog.objects.filter(titulo__icontains=termo)
        if len(tipo) == 0:
            messages.info(request,'Não existe nenhum blog com este Titulo')
            categoria=Cate_por_tipo.objects.all()
            todos=blog.objects.all()
            blogs=blog.objects.all()
            paginator=Paginator(blogs,2)
            page=request.GET.get('p')
            blogs=paginator.get_page(page)
            return render(request,'paginas/index.html',{'blogs':blogs,'todos':todos,'categoria':categoria})
        else:
            paginator=Paginator(tipo,2)
            page=request.GET.get('p')
            tipo=paginator.get_page(page)
            print(tipo.paginator.page_range)
            return render(request,'paginas/blog_especifico.html',{'tipo':tipo,'todos':todos,'categoria':categoria})


        
def categoria_blog(request,id):
    categoria=Cate_por_tipo.objects.all()
    todos=blog.objects.all()
    busca_blog=get_object_or_404(blog,id=id)
    return render(request,'paginas/todos.html',{'busca_blog':busca_blog,'todos':todos,'categoria':categoria})
def categoria(request,id):
    categoria=Cate_por_tipo.objects.all()
    todos=blog.objects.all()
    id_blog=id
    busca_categoria=blog.objects.all().filter(categoria=id_blog)
    return render(request,'paginas/tipos.html',{'busca_categoria_livro':busca_categoria,'id_blog':id_blog,'todos':todos,'categoria':categoria})

def blog_novo_indo(request):
    try:
       titulo=blog.objects.get(titulo=request.POST['Titulo'])
       print(titulo)
       if titulo:
            messages.info(request,'BLOG COM ESTE TITULO JÁ EXISTE')
            return render(request,'paginas/crie_o_seu.html')
    except:
        if request.method=='POST':
            titulo_blog=request.POST.get('Titulo')
            texto_blog=request.POST.get('conteudo')
            imagem_blog=request.FILES.get('imagem')
            print(imagem_blog)
            categoria_blog=request.POST.get('categorias')
            nome_blog=request.POST.get('nome')
            data_blog=request.POST.get('data')
            if categoria_blog=='1':
                add=blog.objects.create(titulo=titulo_blog,conteudo_blog=texto_blog,imagem=imagem_blog,categoria_id=1,nome_do_autor=nome_blog,publicado=data_blog)
                add.save()
                return redirect('home')
            elif categoria_blog=='2':
                add=blog.objects.create(titulo=titulo_blog,conteudo_blog=texto_blog,imagem=imagem_blog,categoria_id=2,nome_do_autor=nome_blog,publicado=data_blog)
                add.save()
                return redirect('home')
            elif categoria_blog=='3':
                add=blog.objects.create(titulo=titulo_blog,conteudo_blog=texto_blog,imagem=imagem_blog,categoria_id=3,nome_do_autor=nome_blog,publicado=data_blog)
                add.save()
                return redirect('home')
        else:
            return render(request,'paginas/crie_o_seu.html')
    return render(request,'paginas/crie_o_seu.html')