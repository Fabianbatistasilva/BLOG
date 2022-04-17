from django.urls import path
from . import views
urlpatterns =[
    path('', views.home,name='home'),
    path('user/', views.user,name='user'),
    path('busca/', views.busca,name='busca'),
    path('categoria_blogs/<int:id>', views.categoria_blog,name='categoria'),
    path('categoria/<int:id>', views.categoria,name='tipos'),
    path('blog_novo', views.blog_novo_indo,name='novo')
]