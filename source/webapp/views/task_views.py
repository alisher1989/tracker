from django.urls import reverse, reverse_lazy

from webapp.forms import TaskForm
from webapp.models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



class IndexView(ListView):
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    model = Task
    ordering = ['-created_at']
    paginate_by = 4
    paginate_orphans = 1


class TaskView(DetailView):
    template_name = 'task/task.html'
    context_object_name = 'task'
    model = Task


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task/create.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task/update.html'
    form_class = TaskForm
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('index')





