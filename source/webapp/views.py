from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import TaskForm
from django.views import View
from webapp.models import Task
from django.views.generic import TemplateView


class IndexView(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'index.html', context={
            'tasks': tasks
        })

class TaskView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task.html', context={
            'task': task
        })

class TaskCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type'],
                created_at=form.cleaned_data['created_at']
            )
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'create.html', context={'form': form})


class TaskUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(data={
            'summary': task.summary,
            'description': task.description,
            'status': task.status,
            'type': task.type,
            'created_at': task.created_at
        })
        return render(request, 'update.html', context={'form': form, 'task': task})


    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data['summary']
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.type = form.cleaned_data['type']
            task.created_at = form.cleaned_data['created_at']
            task.save()
            return redirect('article_view', pk=task.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'task': task})


class TaskDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'delete.html', context={'task': task})

    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')


