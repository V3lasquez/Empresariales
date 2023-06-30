from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from compra import views as app_views

urlpatterns = [
    path('', views.home, name='proveedores'),
    path('registrarproveedor', views.registrarproveedor),
    path('edicionproveedor/<id>', views.edicionproveedor),
    path('editarproveedor', views.editarproveedor),
    path('eliminarproveedor/<id>', views.eliminarproveedor),
    
    path('empleados/', views.homeempleado, name='empleados'),
    path('registrarempleado', views.registrarempleado),
    path('empleados/edicionempleado/<id>', views.edicionempleado),
    path('editarempleado', views.editarempleado),
    path('empleados/eliminarempleado/<id>', views.eliminarempleado),
    
    path('productos/', views.homeproducto, name='productos'),
    path('registrarproducto', views.registrarproducto),
    
    path('ordencompra/', views.homecompra, name='ordencompra'),
    path('registrarordencompra', views.registrarordencompra),
]