from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import TaskForm, StatusForm, TypeForm
from django.views import View
from webapp.models import Task, Status, Type
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'partial/templates/task/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskView(TemplateView):
    template_name = 'partial/templates/task/task.html'


    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=pk)
        return context

class TaskCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'partial/templates/task/create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type'],
            )
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'partial/templates/task/create.html', context={'form': form})


class TaskUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForm(data={
            'summary': task.summary,
            'description': task.description,
            'status': task.status_id,
            'type': task.type_id
        })
        return render(request, 'partial/templates/task/update.html', context={'form': form, 'task': task})


    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data['summary']
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.type = form.cleaned_data['type']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'partial/templates/task/update.html', context={'form': form, 'task': task})


class TaskDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        return render(request, 'partial/templates/task/delete.html', context={'task': task})

    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')

class StatusesView(TemplateView):
    template_name = 'partial/templates/status/statuses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        return context


class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'partial/templates/status/create_status.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            Status.objects.create(
                status=form.cleaned_data['new_status'],
            )
            return redirect('statuses_view')
        else:
            return render(request, 'partial/templates/status/create_status.html', context={'form': form})

class StatusUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        status = get_object_or_404(Status, pk=pk)
        form = StatusForm(data={
            'new_status': status.status
        })
        return render(request, 'partial/templates/status/status_update.html', context={'form': form, 'status': status})


    def post(self, request, pk, *args, **kwargs):
        status = get_object_or_404(Status, pk=pk)
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status.status = form.cleaned_data['new_status']
            status.save()
            return redirect('statuses_view')
        else:
            return render(request, 'partial/templates/status/status_update.html', context={'form': form, 'status': status})


class StatusDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        status = get_object_or_404(Status, pk=pk)
        return render(request, 'partial/templates/status/status_delete.html', context={'status': status})

    def post(self, request, pk, *args, **kwargs):
        status = get_object_or_404(Status, pk=pk)
        try:
            status.delete()
            return redirect('statuses_view')
        except:
            return render(request, 'error.html')


class TypesView(TemplateView):
    template_name = 'partial/templates/type/types.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context


class TypeCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TypeForm()
        return render(request, 'partial/templates/type/create_type.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            Type.objects.create(
                type=form.cleaned_data['new_type'],
            )
            return redirect('types_view')
        else:
            return render(request, 'partial/templates/type/create_type.html', context={'form': form})


class TypeUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        type = get_object_or_404(Type, pk=pk)
        form = TypeForm(data={
            'new_type': type.type
        })
        return render(request, 'partial/templates/type/type_update.html', context={'form': form, 'type': type})


    def post(self, request, pk, *args, **kwargs):
        type = get_object_or_404(Type, pk=pk)
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type.type = form.cleaned_data['new_type']
            type.save()
            return redirect('types_view')
        else:
            return render(request, 'partial/templates/type/type_update.html', context={'form': form, 'type': type})


class TypeDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        type = get_object_or_404(Type, pk=pk)
        return render(request, 'partial/templates/type/type_delete.html', context={'type': type})

    def post(self, request, pk, *args, **kwargs):
        type = get_object_or_404(Type, pk=pk)
        try:
            type.delete()
            return redirect('types_view')
        except:
            return render(request, 'error_type.html')