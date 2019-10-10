from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from webapp.forms import ProjectForm
from webapp.models import Project
from django.views.generic import ListView, DetailView, CreateView, UpdateView



class ProjectsView(ListView):
    template_name = 'project/list.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['-created_at']
    paginate_by = 4
    paginate_orphans = 1

    def get_queryset(self):
        return Project.objects.all().filter(project_status='active')


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


class ProjectDeleteView(View):
    redirect_url = 'projects_view'
    model = Project
    pk_kwargs_url = 'pk'

    def get(self, request, *args, **kwargs):
        project = self.get_object()
        return render(request, 'project/delete.html', context={'project': project})

    def post(self, request, *args, **kwargs):
        self.project = self.get_object()
        self.project.project_status = 'blocked'
        self.project.save()
        return redirect(self.get_redirect_url())

    def get_object(self):
        pk = self.kwargs.get(self.pk_kwargs_url)
        project = get_object_or_404(self.model, pk=pk)
        return project

    def get_redirect_url(self):
        return self.redirect_url


