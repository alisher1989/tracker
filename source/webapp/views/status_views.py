from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import StatusForm
from django.views import View
from webapp.models import Status
from django.views.generic import CreateView, DetailView
from .base_views import ListView, UpdateView, DeleteView


class StatusesView(ListView):
    template_name = 'status/statuses.html'
    model = Status
    context_key = 'statuses'


class StatusCreateView(CreateView):
    model = Status
    template_name = 'status/create_status.html'
    form_class = StatusForm

    def get_success_url(self):
        return reverse('statuses_view')



class StatusUpdateView(UpdateView):
    model = Status
    template_name = 'status/status_update.html'
    form_class = StatusForm
    context_object_name = 'status'

    def get_redirect_url(self):
        return reverse('statuses_view')




class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'status/status_delete.html'
    context_object_name = 'status'
    error_page = 'error.html'

    def get_redirect_url(self):
        return reverse('statuses_view')

# class StatusDeleteView(View):
#     def get(self, request, pk, *args, **kwargs):
#         status = get_object_or_404(Status, pk=pk)
#         return render(request, 'status/status_delete.html', context={'status': status})
#
#     def post(self, request, pk, *args, **kwargs):
#         status = get_object_or_404(Status, pk=pk)
#         try:
#             status.delete()
#             return redirect('statuses_view')
#         except:
#             return render(request, 'error.html')