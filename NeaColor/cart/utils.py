from .models import Orden

def get_or_set_order_session(request):
    orden_id = request.session.get('orden_id', None)
    if orden_id is None:
        order = Orden()
        order.save()
        request.session['orden_id'] = order.id
    else:
        try:
            order = Orden.objects.get(id = orden_id, orden=False)
        except Orden.DoesNotExist:
            order = Orden()
            order.save()
            request.session['orden_id'] = order.id

    if request.user.is_authenticated and order.user is None:
        order.user = request.user
        order.save()

    return order