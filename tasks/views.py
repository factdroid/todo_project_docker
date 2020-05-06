from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task

# Create your views here.
class TaskListAndCreate(CreateView):
    model = Task
    template_name = 'task_list.html'
    fields = ('title',)
    success_url = '/tasks/'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.filter(creator=self.request.user)
        return context

class TaskUpdateView(UpdateView):
    model = Task
    fields = ('title','complete')
    template_name = 'update_task.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.creator != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('tasklistcreate')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.creator != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)   
    