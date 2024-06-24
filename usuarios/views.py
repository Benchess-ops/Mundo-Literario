from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redirigir a alguna página de éxito
            return redirect('ruta_de_exito')
        else:
            # Mostrar un mensaje de error
            messages.error(request, 'Credenciales inválidas')
    
    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('ruta_de_inicio')




