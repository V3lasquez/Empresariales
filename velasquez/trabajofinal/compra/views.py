from django.shortcuts import render,redirect, get_object_or_404, HttpResponse

# Create your views here.
from .models import Empleado
from .models import Proveedor
from .models import Producto
from .models import OrdenCompra
from .models import Pago


def casa(request):
    return render(request, 'login.html')
def home(request):
    proveedoresListado = Proveedor.objects.all()
    return render(request,"GestionProveedor.html",{"proveedores":proveedoresListado})
def registrarproveedor(request):
    id = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    pais = request.POST["txtpais"]
    telefono = request.POST["txttelefono"]
    proveedor = Proveedor.objects.create(id=id, nombre=nombre, pais=pais, telefono=telefono)
    return redirect("/")
def edicionproveedor(request,id):
    proveedor=Proveedor.objects.get(id=id)
    return render(request, "editarproveedor.html", {"proveedores":proveedor})
def editarproveedor(request):
    id = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    pais = request.POST["txtpais"]
    telefono = request.POST["txttelefono"]
    proveedores=Proveedor.objects.get(id=id)
    proveedores.nombre = nombre
    proveedores.pais= pais
    proveedores.telefono= telefono
    proveedores.save()
    return redirect("/")
def eliminarproveedor(request,id):
    proveedor=Proveedor.objects.get(id=id)
    proveedor.delete()
    return redirect("/")
def verproducto(request, id):
    proveedor = get_object_or_404(Proveedor, pk=id)
    productos = Producto.objects.filter(proveedor=proveedor)
    return render(request, 'productos_proveedor.html', {'proveedor': proveedor,'productos':productos})


def homeempleado(request):
    empleadosListado = Empleado.objects.all()
    return render(request, 'GestionEmpleados.html',{"empleados":empleadosListado})
def registrarempleado(request):
    id = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    direccion = request.POST["txtdireccion"]
    dni = request.POST["txtdni"]
    email = request.POST["txtemail"]
    empleado = Empleado.objects.create(id=id, nombre=nombre, apellido=apellido, direccion=direccion, dni=dni, email=email)
    return redirect("/empleados")
def edicionempleado(request,id):
    empleado=Empleado.objects.get(id=id)
    return render(request, "editarempleado.html", {"empleados":empleado})
def editarempleado(request):
    id = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    direccion = request.POST["txtdireccion"]
    dni = request.POST["txtdni"]
    email = request.POST["txtemail"]
    empleados=Empleado.objects.get(id=id)
    empleados.nombre = nombre
    empleados.apellido= apellido
    empleados.direccion= direccion
    empleados.dni= dni
    empleados.email= email
    empleados.save()
    return redirect("/empleados")
def eliminarempleado(request,id):
    empleado=Empleado.objects.get(id=id)
    empleado.delete()
    return redirect("/empleados")

def homeproducto(request):
    productosListado = Producto.objects.all()
    proveedoresListado = Proveedor.objects.all()
    return render(request, 'GestionProducto.html',{"productos":productosListado, "proveedores":proveedoresListado})
def registrarproducto(request):
    id = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["txtprecio"]
    producto = Producto.objects.create(id=id, nombre=nombre, descripcion=descripcion, precio=precio)
    return redirect("/productos")
def edicionproducto(request,id):
    producto=Producto.objects.get(id=id)
    proveedor=Proveedor.objects.all()
    return render(request, "editarproducto.html", {"productos":producto,"proveedores":proveedor})
def editarproducto(request):
    if request.method == 'POST':
        id = request.POST["txtid"]
        nombre = request.POST.get("txtnombre")
        descripcion = request.POST["txtdescripcion"]
        precio = request.POST["txtprecio"]
        proveedor_id = request.POST["txtproveedor"]

        producto = get_object_or_404(Producto, id=id)
        proveedor = get_object_or_404(Proveedor, id=proveedor_id)

        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        producto.proveedor = proveedor
        producto.save()
        return redirect("/productos")
def eliminarproducto(request,id):
    producto=Producto.objects.get(id=id)
    producto.delete()
    return redirect("/productos")


def homecompra(request):
    comprasListado = OrdenCompra.objects.all()
    productosListado = Producto.objects.all()
    proveedoresListado = Proveedor.objects.all()
    empleadosListado = Empleado.objects.all()
    return render(request, 'GestionOrdenCompra.html',{"compras":comprasListado,"productos":productosListado,"proveedores":proveedoresListado,"empleados":empleadosListado})
def registrarordencompra(request):
    if request.method == 'POST':
        id = request.POST.get("txtid")
        fec_emision = request.POST.get("txtfec_emision")
        cantidad = request.POST.get("txtcantidad")
        prec_unitario = request.POST.get("txtprec_unitario")
        total = request.POST.get("txttotal")
        producto_id = request.POST.get('txtproducto')
        proveedor_id = request.POST.get('txtproveedor')
        empleado_id = request.POST.get('txtempleado')
        producto = get_object_or_404(Producto, id=producto_id)
        proveedor = get_object_or_404(Proveedor, id=proveedor_id)
        empleado = get_object_or_404(Empleado, id=empleado_id)
        
        compra = OrdenCompra.objects.create(id=id, fec_emision=fec_emision, cantidad=cantidad, prec_unitario=prec_unitario,empleado_id=empleado_id,
                                            total=total,producto=producto, proveedor=proveedor, empleado=empleado)
        return redirect("/ordencompra")
def eliminarcompra(request,id):
    compra=OrdenCompra.objects.get(id=id)
    compra.delete()
    return redirect("/ordencompra")

def homepago(request):
    pagos = Pago.objects.all()
    ordenpagos = Proveedor.objects.all()
    return render(request, 'GestionPagos.html',{"pagos":pagos, "ordenpago":ordenpagos})
def registrarpago(request):
    id = request.POST["txtid"]
    fec_pago = request.POST["txtfec_pago"]
    descuento = request.POST["txtdescuento"]
    met_pago = request.POST["txtmet_pago"]
    total_id = request.POST["txttotal"]
    
    orden_compra = get_object_or_404(OrdenCompra, id=total_id)
    
    pago = Pago.objects.create(id=id, fec_pago=fec_pago, descuento=descuento, met_pago=met_pago,total=orden_compra )
    return redirect("/pagos")