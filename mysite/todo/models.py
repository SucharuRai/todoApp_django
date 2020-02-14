from django.db import models

# Create your models here.
class Name(models.Model):
    todo_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_name