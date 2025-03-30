from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from .models import Payment

@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == "Completed":
        # Buscar el pago asociado a la factura y actualizar su estado
        Payment.objects.filter(invoice=ipn.invoice, status="pending").update(status="paid")
        print('Siuuuu, completado')
    return True