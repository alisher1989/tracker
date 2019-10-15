from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy

from webapp.forms import TypeForm

from webapp.models import Type
from django.views.generic import CreateView, UpdateView, DeleteView
from .base_views import ListView


class TypesView(ListView):
    template_name = 'type/types.html'
    model = Type
    context_key = 'types'



class TypeCreateView(CreateView):
    model = Type
    template_name = 'type/create_type.html'
    form_class = TypeForm

    def get_success_url(self):
        return reverse('types_view')




# class TypeUpdateView(UpdateView):
#     model = Type
#     template_name = 'type/type_update.html'
#     form_class = TypeForm
#     context_object_name = 'type'
#
#     def get_redirect_url(self):
#         return reverse('types_view')
class TypeUpdateView(UpdateView):
    model = Type
    template_name = 'type/type_update.html'
    form_class = TypeForm
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('types_view')


# class TypeDeleteView(DeleteView):
#     model = Type
#     template_name = 'type/type_delete.html'
#     context_object_name = 'type'
#     error_page = 'error_type.html'
#
#     def get_redirect_url(self):
#         return reverse('types_view')

class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'type/type_delete.html'
    context_object_name = 'type'
    pk_kwargs_url = 'pk'

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get(self.pk_kwargs_url)
        obj = get_object_or_404(self.model, pk=pk)
        return obj

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            return redirect('statuses_view')
        except:
            return render(request, 'error_type.html')

