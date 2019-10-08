
from django.urls import reverse

from webapp.forms import TypeForm

from webapp.models import Type
from django.views.generic import CreateView
from .base_views import ListView, UpdateView, DeleteView


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




class TypeUpdateView(UpdateView):
    model = Type
    template_name = 'type/type_update.html'
    form_class = TypeForm
    context_object_name = 'type'

    def get_redirect_url(self):
        return reverse('types_view')


class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'type/type_delete.html'
    context_object_name = 'type'
    error_page = 'error_type.html'

    def get_redirect_url(self):
        return reverse('types_view')



# class TypeUpdateView(View):
#     def get(self, request, pk, *args, **kwargs):
#         type = get_object_or_404(Type, pk=pk)
#         form = TypeForm(data={
#             'type': type.type
#         })
#         return render(request, 'type/type_update.html', context={'form': form, 'type': type})
#
#
#     def post(self, request, pk, *args, **kwargs):
#         type = get_object_or_404(Type, pk=pk)
#         form = TypeForm(data=request.POST)
#         if form.is_valid():
#             type.type = form.cleaned_data['type']
#             type.save()
#             return redirect('types_view')
#         else:
#             return render(request, 'type/type_update.html', context={'form': form, 'type': type})
#
#
# class TypeDeleteView(View):
#     def get(self, request, pk, *args, **kwargs):
#         type = get_object_or_404(Type, pk=pk)
#         return render(request, 'type/type_delete.html', context={'type': type})
#
#     def post(self, request, pk, *args, **kwargs):
#         type = get_object_or_404(Type, pk=pk)
#         try:
#             type.delete()
#             return redirect('types_view')
#         except:
#             return render(request, 'error_type.html')