from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import StatusForm
from django.views import View
from webapp.models import Status
from django.views.generic import TemplateView



class StatusesView(TemplateView):
    template_name = 'status/statuses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        return context


class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'status/create_status.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            Status.objects.create(
                status=form.cleaned_data['new_status'],
            )
            return redirect('statuses_view')
        else:
            return render(request, 'status/create_status.html', context={'form': form})

class StatusUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        status = get_object_or_404(Status, pk=pk)
        form = StatusForm(data={
            'new_status': status.status
        })
        return render(request, 'status/status_update.html', context={'form': form, 'status': status})


    def post(self, request, pk, *args, **kwargs):
        status = get_object_or_404(Status, pk=pk)
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status.status = form.cleaned_data['new_status']
            status.save()
            return redirect('statuses_view')
        else:
            return render(request, 'status/status_update.html', context={'form': form, 'status': status})


class StatusDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        status = get_object_or_404(Status, pk=pk)
        return render(request, 'status/status_delete.html', context={'status': status})

    def post(self, request, pk, *args, **kwargs):
        status = get_object_or_404(Status, pk=pk)
        try:
            status.delete()
            return redirect('statuses_view')
        except:
            return render(request, 'error.html')