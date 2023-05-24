"""
URL configuration for facturacion_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from facturacion.views import obtener_lista_precios, obtener_productos_minimo_existencia, \
    obtener_clientes_compras_fecha, obtener_valor_total_productos_2000, obtener_ultima_fecha_compra, guardar_factura, crear_factura

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reportes/crear-factura/', crear_factura),
    path('reportes/guardar-facturas/', guardar_factura),
    path('reportes/lista-precios/', obtener_lista_precios),
    path('reportes/productos-minimo-existencia/', obtener_productos_minimo_existencia),
    path('reportes/clientes-compras-fecha/', obtener_clientes_compras_fecha),
    path('reportes/valor-total-productos-2000/', obtener_valor_total_productos_2000),
    path('reportes/ultima-fecha-compra/', obtener_ultima_fecha_compra),
]

