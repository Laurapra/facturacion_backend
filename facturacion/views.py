from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import connection
from .models import Factura, Cliente, Producto
# Create your views here.

#esta consulta funciona
def obtener_lista_precios(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT nombre_producto, precio_producto FROM productos")
        data = cursor.fetchall()

    response = []
    for row in data:
        response.append({
            'nombre_producto': row[0],
            'precio_producto': float(row[1])
        })

    return JsonResponse(response, safe=False)

#esta consulta funciona
def obtener_productos_minimo_existencia(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT p.nombre_producto, I.cantidad "
                        "FROM productos p JOIN INVENTARIO I ON p.id_producto=I.id_producto WHERE I.cantidad <=5;")
        data = cursor.fetchall()

    response = []
    for row in data:
        response.append({
            'nombre_producto': row[0],
            'cantidad': row[1]
        })

    return JsonResponse(response, safe=False)
#consulta sirve
def obtener_clientes_compras_fecha(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT nombre_clientes, fecha_nacimiento, fecha_ultima_compra FROM clientes WHERE fecha_ultima_compra BETWEEN '2000-02-01' AND '2000-05-25' AND fecha_nacimiento >= CURRENT_DATE - INTERVAL '35 YEARS';")
        data = cursor.fetchall()

    response = []
    for row in data:
        response.append({
            'nombre_cliente': row[0],
            'fecha_nacimiento': row[1].strftime('%Y-%m-%d'),
            'fecha_ultima_compra': row[2].strftime('%Y-%m-%d')
        })

    return JsonResponse(response, safe=False)

#consulta sirve
def obtener_valor_total_productos_2000(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT P.nombre_producto, SUM(F.total_facturas) AS total_vendido "
                       "FROM productos P "
                       "JOIN facturas F ON P.id_producto = F.id_producto "
                       "WHERE date_part('year', F.fecha_factura) = 2000 "
                       "GROUP BY P.nombre_producto")
        data = cursor.fetchall()

    response = []
    for row in data:
        response.append({
            'nombre_producto': row[0],
            'valor_total': float(row[1])
        })

    return JsonResponse(response, safe=False)

#consulta sirve
def obtener_ultima_fecha_compra(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT c.id_clientes, c.fecha_factura, "
                       "(c.fecha_factura + INTERVAL '30 days') AS proxima_compra "
                       "FROM facturas c "
                       "ORDER BY c.fecha_factura DESC "
                       "LIMIT 1")
        data = cursor.fetchone()

    response = {
        'id_cliente': data[0],
        'fecha_factura': data[1].strftime('%Y-%m-%d'),
        'proxima_compra': data[2].strftime('%Y-%m-%d')
    }

    return JsonResponse(response)


#consulta sirve
@csrf_exempt
def crear_factura(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id_cliente = data.get('id_cliente')
        id_producto = data.get('id_producto')
        fecha_factura = data.get('fecha_factura')
        cantidad = data.get('cantidad')
        total_factura = data.get('total_factura')

        try:
            cliente = Cliente.objects.get(id=id_cliente)
            producto = Producto.objects.get(id=id_producto)
            
            factura = Factura(
                cliente=cliente,
                producto=producto,
                fecha_factura=fecha_factura,
                cantidad=cantidad,
                total_factura=total_factura
            )
            factura.save()

            return JsonResponse({'mensaje': 'Factura creada exitosamente.'}, status=200)
        except (Cliente.DoesNotExist, Producto.DoesNotExist) as e:
            return JsonResponse({'error': 'Cliente o producto no encontrado.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Ocurrió un error al crear la factura.'}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)


@csrf_exempt
def guardar_factura(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id_cliente = data.get('id_cliente')
        id_producto = data.get('id_producto')
        fecha_factura = data.get('fecha_factura')
        cantidad = data.get('cantidad')
        total_factura = data.get('total_factura')

        try:
            cliente = Cliente.objects.get(id=id_cliente)
            producto = Producto.objects.get(id=id_producto)
            
            factura = Factura(
                cliente=cliente,
                producto=producto,
                fecha_factura=fecha_factura,
                cantidad=cantidad,
                total_factura=total_factura
            )
            factura.save()

            return JsonResponse({'status': 'success'})
        except (Cliente.DoesNotExist, Producto.DoesNotExist) as e:
            return JsonResponse({'status': 'error', 'message': 'Cliente o producto no encontrado.'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Ocurrió un error al guardar la factura.'}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Método no permitido'})