from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import TodosUserModel
from .forms import CreateTodoForm, ViewTodoForm


# Create your views here.
@login_required(login_url='accounts:login')
def authenticated(request):
    todos_form = ViewTodoForm(request.GET)
    if todos_form.is_valid():
        status = todos_form.cleaned_data.get('status')
        labels = todos_form.cleaned_data.get('labels')
    else:
        status = 'Pendiente'
        labels = None

    todos = TodosUserModel.objects.filter(user=request.user)

    if status:
        todos = todos.filter(status=status)

    if labels:
        todos = todos.filter(labels__in=labels)

    todos = todos.order_by('due_date')

    return render(request, 'todos/authenticated.html', {'todos': todos, 'todos_form': todos_form})


@login_required(login_url='accounts:login')
def create_todo(request):
    if request.method == 'POST':
        todos_form = CreateTodoForm(request.POST)
        if todos_form.is_valid():
            todo = todos_form.save(commit=False)
            todo.save()
            todos_form.save_m2m()
            messages.success(request, 'Tarea creada correctamente')
            return redirect('todos:authenticated')
    else:
        todos_form = CreateTodoForm()
    return render(request, template_name='todos/create.html', context={'todos_form': todos_form})


@login_required(login_url='accounts:login')
def view_todo(request, todo_id):
    original_todo = TodosUserModel.objects.get(id=todo_id)
    if request.method == 'POST':
        todo_observations = ViewTodoForm(request.POST)
        if todo_observations.is_valid():
            new_observations = todo_observations.cleaned_data['observations']
            if original_todo.observations is None:
                original_todo.observations = new_observations
            else:
                original_todo.observations += "\n" + new_observations
            original_todo.save()
            messages.success(request, 'Observación agregada correctamente')
            return redirect('todos:view_todo', todo_id=todo_id)
    else:
        todo_observations = ViewTodoForm()

    try:
        todo_detail = TodosUserModel.objects.get(id=todo_id)
        return render(request, template_name='todos/view.html',
                      context={'todo_detail': todo_detail, 'todos_observations': todo_observations})
    except TodosUserModel.DoesNotExist:
        return render(request, template_name='todos/view.html')


@login_required(login_url='accounts:login')
def modify_todo(request, todo_id):
    try:
        todo_modify = TodosUserModel.objects.get(id=todo_id)
    except TodosUserModel.DoesNotExist:
        return redirect('todos:authenticated')

    if request.method == 'POST':
        todos_form = CreateTodoForm(request.POST, instance=todo_modify)
        if todos_form.is_valid():
            todo = todos_form.save(commit=False)
            todo.user = request.user
            todo.save()
            todos_form.save_m2m()
            messages.success(request, 'Tarea actualizada correctamente')
            return redirect('todos:authenticated')
    else:
        todos_form = CreateTodoForm(instance=todo_modify)

    return render(request, template_name='todos/modify.html',
                  context={'todos_form': todos_form, 'todo_id': todo_modify.id})


@login_required(login_url='accounts:login')
def complete_todo(request, todo_id):
    todo_complete = TodosUserModel.objects.get(id=todo_id)
    todo_complete.status = 'completada'
    todo_complete.save()
    messages.success(request, 'Tarea completada')
    return redirect('todos:authenticated')


@login_required(login_url='accounts:login')
def delete_todo(request, todo_id):
    todo_delete = TodosUserModel.objects.get(id=todo_id)
    if request.user == todo_delete.user:
        todo_delete.delete()
        messages.success(request, 'Tarea eliminada correctamente')
        return redirect('todos:authenticated')
