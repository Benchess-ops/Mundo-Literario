from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('preguntas_frecuentes/', views.preguntas_frecuentes, name='preguntas_frecuentes'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('cuenta/', views.cuenta, name='cuenta'),
    path('buscar_categoria/', views.buscar_categoria, name='buscar_categoria'),
    path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('carrito/agregar/<int:libro_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('venta/eliminar/<int:item_id>/', views.eliminar_item_carrito, name='eliminar_item_carrito'),
    path('vaciar/', views.vaciar_carrito, name='vaciar_carrito'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('metodo_pago/', views.metodo_pago, name='metodo_pago'),
    path('metodo_pago_debito/', views.metodo_pago_debito, name='metodo_pago_debito'),
    path('procesar_pago_debito/', views.procesar_pago_debito, name='procesar_pago_debito'),
    
]
