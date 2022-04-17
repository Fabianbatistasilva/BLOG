from django.shortcuts import render, redirect
from django .contrib import auth, messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


def user_login(request):
    
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        check = auth.authenticate(request, username=usuario, password=senha)
        print(check)
        if check is not None:
            login(request, check)
            return redirect('home')
        else:
            messages.info(request, 'Usuario ou Senha Incorretos')
            return render(request, 'paginas/login.html')
        
    else:
        return render(request, 'paginas/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
def register(request):
    try:
        usuario=User.objects.get(username=request.POST['usuario'])
        if usuario:
            messages.info(request,'usuario já existe')
            return render(request,'paginas/cadastro.html')
    except:
        if request.method=='POST':
            user_accounts=request.POST.get('usuario')
            email_accounts=request.POST.get('email')
            pass_accounts=request.POST.get('senha')
            word_accounts=request.POST.get('senha_2')
            verifica_senha_1_simbolos=pass_accounts.isalnum()
            verifica_senha_2_simbolos=word_accounts.isalnum()
            caracteres_pass=len(pass_accounts)
            caracteres_word=len(pass_accounts)

            if caracteres_pass<6 or caracteres_word<6 or caracteres_pass==12 or caracteres_word==12:
                messages.info(request,'coloquei um valor entre 6 e 12 caracteres')
            elif pass_accounts!=word_accounts:
                messages.info(request,'senhas não compativeis')
            elif verifica_senha_1_simbolos==False and verifica_senha_2_simbolos==False:
                messages.info(request,'não adicione simbolos')
            add=User.objects.create_user(username=user_accounts,password=pass_accounts)
            add.save()
            return redirect('login')
        else:
            return render(request,'paginas/cadastro.html')
    return render(request,'paginas/cadastro.html')