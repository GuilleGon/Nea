from django.shortcuts import get_object_or_404, reverse
from .models import Producto
from django.views import generic
from .utils import get_or_set_order_session
from .forms import AddToCartForm




class ProductoDetalle(generic.FormView):
    template_name = 'producto.html'
    form_class = AddToCartForm

    def get_object(self):
        return get_object_or_404(Producto, slug=self.kwargs["slug"])

    def get_success_url(self):
        return reverse("home")

    def form_valid(self, form):
        order = get_or_set_order_session(self.request)
        producto = self.get_object()

        item_filter = order.items.filter(producto=producto)
        if item_filter.exists():
            item = item_filter.first()
            item.cantidad += int(form.cleaned_data['cantidad'])
            item.save()
        
        else:
            new_item = form.save(commit=False)
            new_item.producto = producto
            new_item.order = order
            new_item.save()

        return super(ProductoDetalle, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductoDetalle, self).get_context_data(**kwargs)
        context['producto'] = self.get_object()
        return context