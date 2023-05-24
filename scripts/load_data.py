from facturacion.models import Producto, Inventario, Cliente, Factura

def load_productos():
    productos = [
        {'nombre_producto': 'Producto 1', 'precio_producto': 10.0},
        {'nombre_producto': 'Producto 2', 'precio_producto': 15.0},
        # Agrega más productos según tus necesidades
    ]

    for data in productos:
        producto = Producto(**data)
        producto.save()
load_productos()

def load_inventario():
    inventario = [
        {'producto_id': 1, 'cantidad': 20},
        {'producto_id': 2, 'cantidad': 15},
        # Agrega más datos de inventario según tus necesidades
    ]

    for data in inventario:
        producto_id = data.pop('producto_id')
        producto = Producto.objects.get(id=producto_id)
        inventario = Inventario(producto=producto, **data)
        inventario.save()

load_inventario()


def load_clientes():
    clientes = [
        {'nombre_cliente': 'Cliente 1', 'fecha_nacimiento': '1985-01-15', 'fecha_ultima_compra': '2022-05-10'},
        {'nombre_cliente': 'Cliente 2', 'fecha_nacimiento': '1990-07-20', 'fecha_ultima_compra': '2022-04-25'},
        # Agrega más clientes según tus necesidades
    ]

    for data in clientes:
        cliente = Cliente(**data)
        cliente.save()

load_clientes()

def load_facturas():
    facturas = [
        {'cliente_id': 1, 'producto_id': 1, 'fecha_factura': '2022-05-10', 'cantidad': 3, 'total_factura': 30.0},
        {'cliente_id': 2, 'producto_id': 2, 'fecha_factura': '2022-04-25', 'cantidad': 2, 'total_factura': 30.0},
        # Agrega más datos de facturas según tus necesidades
    ]

    for data in facturas:
        cliente_id = data.pop('cliente_id')
        producto_id = data.pop('producto_id')
        cliente = Cliente.objects.get(id=cliente_id)
        producto = Producto.objects.get(id=producto_id)
        factura = Factura(cliente=cliente, producto=producto, **data)
        factura.save()

load_facturas()
# Llama a los scripts correspondientes
load_productos()
load_inventario()
load_clientes()
load_facturas()
