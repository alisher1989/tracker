from django.urls import reverse, reverse_lazy

from webapp.forms import ProjectForm
from webapp.models import Project
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProjectsView(ListView):
    template_name = 'project/list.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['-created_at']
    paginate_by = 4
    paginate_orphans = 1


class ProjectView(DetailView):
    template_name = 'project/project.html'
    context_object_name = 'project'
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project/create.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})



class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('projects_view')