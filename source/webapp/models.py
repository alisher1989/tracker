from django.db import models


class Task(models.Model):
    summary = models.CharField(max_length=50, null=False, blank=False, verbose_name='summary')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='descripton')
    status = models.ForeignKey('webapp.Status', related_name='task_status', on_delete=models.PROTECT, null=True, blank=True, verbose_name='status')
    type = models.ForeignKey('webapp.Type', related_name='task_type', on_delete=models.PROTECT, null=True, blank=True, verbose_name='type')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    def __str__(self):
        return self.summary

class Type(models.Model):
    type = models.CharField(max_length=50, verbose_name='type')

    def __str__(self):
        return self.type


class Status(models.Model):
    status = models.CharField(max_length=50, verbose_name='status')


    def __str__(self):
        return self.status
