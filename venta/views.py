from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import UsuarioForm
from django.contrib.auth import authenticate, login


def index_view(request):
    libros = Libro.objects.all()
    carrito = request.session.get('carrito', {})
    libros_con_carrito = []

    for libro in libros:
        if str(libro.id) in carrito:
            libros_con_carrito.append({
                'libro': libro,
                'cantidad': carrito[str(libro.id)],
                'subtotal': libro.precio * carrito[str(libro.id)]
            })
        else:
            libros_con_carrito.append({
                'libro': libro,
                'cantidad': 0,
                'subtotal': 0
            })

    context = {
        'libros': libros_con_carrito
    }

    return render(request, 'index.html', context)


def preguntas_frecuentes(request):
    return render(request, 'preguntas_frecuentes.html')


def quienes_somos(request):
    return render(request, 'quienes_somos.html')


def cuenta(request):
    if request.method == 'POST':
        if 'login_email' in request.POST:
            email = request.POST.get('login_email')
            password = request.POST.get('login_password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'cuenta.html', {'error_message': 'Credenciales inválidas para iniciar sesión.'})

        elif 'email' in request.POST:
            form = UsuarioForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index')
                else:
                    return render(request, 'cuenta.html', {'error_message': 'Error al autenticar después del registro.'})
            else:
                return render(request, 'cuenta.html', {'form': form})

    return render(request, 'cuenta.html')


def buscar_categoria(request):
    return render(request, 'buscar_categoria.html')


def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            usuario = authenticate(email=usuario.email, password=request.POST['password'])
            if usuario is not None:
                login(request, usuario)
                return redirect('cuenta')
    form = UsuarioForm()
    return render(request, 'venta/cuenta.html', {'form': form})


def agregar_al_carrito(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    carrito = request.session.get('carrito', {})

    if str(libro_id) in carrito:
        carrito[str(libro_id)] += 1
    else:
        carrito[str(libro_id)] = 1

    request.session['carrito'] = carrito
    return redirect('index')


def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    libros = Libro.objects.filter(id__in=carrito.keys())
    carrito_items = []
    for libro in libros:
        carrito_items.append({
            'libro': libro,
            'cantidad': carrito[str(libro.id)],
            'subtotal': libro.precio * carrito[str(libro.id)]
        })
    total = sum(item['subtotal'] for item in carrito_items)
    return render(request, 'ver_carrito.html', {'carrito_items': carrito_items, 'total': total})


def eliminar_item_carrito(request):
    if request.method == 'POST':
        libro_id = request.POST.get('libro_id')
        libro = get_object_or_404(Libro, id=libro_id)
        carrito = request.session.get('carrito', {})

        if str(libro.id) in carrito:
            del carrito[str(libro.id)]
            request.session['carrito'] = carrito

    return redirect('ver_carrito')


def vaciar_carrito(request):
    request.session['carrito'] = {}
    return redirect('ver_carrito')


def metodo_pago(request):
    if request.method == 'POST':
        opcion = request.POST.get('opcion')
        if opcion == 'retiro':
            lugar_retiro = request.POST.get('lugar_retiro')
            return render(request, 'confirmacion_retiro.html', {'lugar_retiro': lugar_retiro})
        elif opcion == 'online':
            metodo_pago = request.POST.get('metodo_pago')
            if metodo_pago == 'tarjeta':
                return redirect('metodo_pago_debito')

    return render(request, 'metodo_pago.html')


def metodo_pago_debito(request):
    if request.method == 'POST':
        nombre_tarjeta = request.POST.get('nombre_tarjeta')
        numero_tarjeta = request.POST.get('numero_tarjeta')
        fecha_expiracion = request.POST.get('fecha_expiracion')
        cvv = request.POST.get('cvv')
        return redirect('procesar_pago_debito')

    return render(request, 'formulario_debito.html')


def procesar_pago_debito(request):
    return render(request, 'confirmacion_pago.html')

