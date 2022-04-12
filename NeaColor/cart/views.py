from django.shortcuts import get_object_or_404, redirect, reverse
from .models import OrderItem, Producto
from django.views import generic
from .utils import get_or_set_order_session
from .forms import AddToCartForm, checkForm


class ProductoDetalle(generic.FormView):
    template_name = 'producto.html'
    form_class = AddToCartForm

    def get_object(self):
        return get_object_or_404(Producto, slug=self.kwargs["slug"])

    def get_success_url(self):
        return reverse("cart:carrito")

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


class CartView(generic.TemplateView):
    template_name = 'carrito.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context["order"] = get_or_set_order_session(self.request)
        return context


class IncrementarCantidad(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        order_item.cantidad += 1
        order_item.save()
        return redirect("cart:carrito")


class DecrementarCantidad(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])

        if order_item.cantidad <= 1:
            order_item.delete()
        else:
            order_item.cantidad -= 1
            order_item.save()
        return redirect("cart:carrito")


class BorrarItem(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        order_item.delete()
        return redirect("cart:carrito")


class Checkout(generic.FormView):
    template_name = "checkout.html"
    form_class = checkForm

    def get_form_kwargs(self):
        kwargs = super(Checkout, self).get_form_kwargs()
        kwargs['user_id'] = self.request.user.id
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(Checkout, self).get_context_data(**kwargs)
        context['order'] = get_or_set_order_session(self.request)
        return context

