from django.shortcuts import render, redirect
from .models import Pedido
from django.contrib.auth.decorators import login_required

@login_required
def crear_pedido(request):
    # Suponiendo que tienes lógica para obtener el carrito del usuario actual
    carrito = request.user.carrito

    # Crear un nuevo pedido con el carrito del usuario actual
    nuevo_pedido = Pedido.objects.create(usuario=request.user)
    
    # Asignar los items del carrito al pedido
    for item_carrito in carrito.items.all():
        nuevo_pedido.items.add(item_carrito)

    # Calcular el total del pedido
    nuevo_pedido.calcular_total()

    # Limpiar el carrito del usuario
    carrito.items.clear()

    return redirect('ruta_hacia_detalles_del_pedido')
