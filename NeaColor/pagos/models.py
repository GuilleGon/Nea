from django.db import models

from cart.models import Orden


class Payment(models.Model):
    order = models.ForeignKey(Orden, related_name="payments", on_delete=models.CASCADE)
    transaction_amount = models.DecimalField(
        "Valor de la transaccion", max_digits=10, decimal_places=2
    )
    installments = models.IntegerField("Parcelas")
    payment_method_id = models.CharField("Método de Pagamento", max_length=250)
    email = models.EmailField()
    doc_number = models.BigIntegerField()
    mercado_pago_id = models.CharField(max_length=250, blank=True, db_index=True)
    mercado_pago_status = models.CharField(max_length=250, blank=True)
    mercado_pago_status_detail = models.CharField(max_length=250, blank=True)


    def __str__(self):
        return f"Pago {self.id}"
