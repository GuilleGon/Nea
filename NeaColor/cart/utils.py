from .models import Orden

def get_or_set_order_session(request):
    order_id = request.session.get('order_id', None)
    if order_id is None:
        order = Orden()
        order.save()
        request.session['order_id'] = order.id
    else:
        try:
            order = Orden.objects.get(id = order_id, ordenado=False)
        except Orden.DoesNotExist:
            order = Orden()
            order.save()
            request.session['order_id'] = order.id

    if request.user.is_authenticated and order.user is None:
        order.user = request.user
        order.save()

    return order
