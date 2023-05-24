from django import forms
from .models import Facturas

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Facturas
        fields = ['id_cliente', 'id_producto', 'fecha_factura', 'cantidad', 'total_factura']
