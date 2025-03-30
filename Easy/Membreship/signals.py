from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.utils import timezone
from .models import Payment, Membership, Plans
from django.contrib.auth.models import User

@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == "Completed":
        # Buscar el pago asociado a la factura y actualizar su estado
            pay =   Payment.objects.get(invoice=ipn.invoice, status="pending")
            pay.status="paid"
            pay.save()
            memberchip = Membership.objects.get(user=User.objects.get(id=int(pay.id_user)))
            memberchip.plan = Plans.objects.get(id=int(pay.id_plan))
            memberchip.is_active = True
            memberchip.start_date = timezone.now()
            memberchip.duration_days = 30
            memberchip.save()
            print('Pago completado')
    return True