from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class ChoreList(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

class Chore(models.Model):
    id = models.AutoField(primary_key=True)
    chore_list_id = models.ForeignKey(ChoreList, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, blank=True)