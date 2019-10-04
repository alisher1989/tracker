from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import TypeForm
from django.views import View
from webapp.models import Type
from django.views.generic import TemplateView


class TypesView(TemplateView):
    template_name = 'type/types.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context


class TypeCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TypeForm()
        return render(request, 'type/create_type.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            Type.objects.create(
                type=form.cleaned_data['new_type'],
            )
            return redirect('types_view')
        else:
            return render(request, 'type/create_type.html', context={'form': form})


class TypeUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        type = get_object_or_404(Type, pk=pk)
        form = TypeForm(data={
            'new_type': type.type
        })
        return render(request, 'type/type_update.html', context={'form': form, 'type': type})


    def post(self, request, pk, *args, **kwargs):
        type = get_object_or_404(Type, pk=pk)
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type.type = form.cleaned_data['new_type']
            type.save()
            return redirect('types_view')
        else:
            return render(request, 'type/type_update.html', context={'form': form, 'type': type})


class TypeDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        type = get_object_or_404(Type, pk=pk)
        return render(request, 'type/type_delete.html', context={'type': type})

    def post(self, request, pk, *args, **kwargs):
        type = get_object_or_404(Type, pk=pk)
        try:
            type.delete()
            return redirect('types_view')
        except:
            return render(request, 'error_type.html')