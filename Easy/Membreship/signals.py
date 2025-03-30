from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from .models import Payment

@receiver(valid_ipn_received)
def payment_notification(sender,request, **kwargs):
      ipn = sender
      if ipn.payment_status == "Completed":
        # Marcar el pago como completado en tu base de datos

           Payment.objects.filter(user=request.user, status="pending").update(status="paid")
           print('Siuuuu, completado')
      return True
