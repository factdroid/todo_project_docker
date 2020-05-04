from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task

# Create your views here.
class TaskListAndCreate(CreateView):
    model = Task
    template_name = 'task_list.html'
    fields = '__all__'
    success_url = '/tasks/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context

class TaskUpdateView(UpdateView):
    model = Task
    fields = ('title','complete')
    template_name = 'update_task.html'

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('tasklistcreate')
    