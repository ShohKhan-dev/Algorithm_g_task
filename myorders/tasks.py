

import random
from celery import shared_task

from .models import Order


@shared_task(name="checking_status")
def set_status():

    orders = Order.objects.filter(status='waiting')

    for order in orders:
        order.return_new_update()

    return "successfully Order status changed!"