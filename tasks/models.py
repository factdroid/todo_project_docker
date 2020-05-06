from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.
class Task(models.Model):

    title = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasklistcreate', args=[str(self.id)])
