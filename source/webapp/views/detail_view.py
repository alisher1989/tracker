from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


class DetailView(TemplateView):
    template_name = 'task/task.html'


    def get_context_data(self, **kwargs):

        context_key = 'object'
        model = None

        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context[self.context_key] = get_object_or_404(self.model, pk=pk)
        return context