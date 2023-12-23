from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from users.forms import UserCreationForm, CreateTask, DeleteTask
from django.views.generic.base import TemplateView

from users.models import Dbase


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    

class Tasks(TemplateView):
    template_name = 'main.html'
    def get(self, request):
        all_tasks = Dbase.objects.filter(user=request.user)
        tasks_count = len(all_tasks)
        data = []
        slovar  = {}
        count = 1
        for task in all_tasks:
            slovar = {
                'text': task.text,
                'status':task.complete,
            }
            data.append(slovar)

            count += 1
        context = {
            'all_tasks': all_tasks,
            'data': data,
            'count': tasks_count,
            'form': DeleteTask(),
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = DeleteTask(request.POST)
        if form.is_valid():
            user = request.user
            text = request.POST.get('complete')
            data = Dbase(user=user, text=text, complete=False)
            data.delete()
        return redirect('/')
class CreateTasks(TemplateView):
    template_name = 'create_task.html'
    
    def get(self, request):
        context = {
            'form': CreateTask()
        }
        return render(request, self.template_name, context)
    
    def post(self,request):
        form = CreateTask(request.POST)
        if form.is_valid():
            user = request.user
            text = request.POST.get('text')
            data = Dbase(user=user, text=text, complete=False)
            data.save()
        return redirect('/')
    

class DeleteTasks(TemplateView):
    template_name = 'delete_task.html'
    def get(self, request):
        context = {
            'form': DeleteTask()
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = DeleteTask(request.POST)
        if form.is_valid():
            user = request.user
            id = request.POST.get('id')
            data = Dbase(id=id, user=user)
            data.delete()
        return redirect('/')