from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, help_text="Reaproveitamento, transferência, pré-requisitos, etc")

    def __str__(self):
        return self.name

class Process(models.Model):
    name = models.CharField(max_length=100, help_text="Nome do processo e do aluno")
    idcode = models.IntegerField(help_text="Número do processo")
    date = models.DateField()
    archive = models.FileField(upload_to='', help_text='Um arquivo .pdf com todos os documentos do processo')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    PROCESS_STATUS = (
        ('C', 'Concluído'),
        ('P', 'Pendente'),
    )
    status = models.CharField(max_length=1,choices=PROCESS_STATUS, blank=True, default='P', help_text='O estado do processo: pendente ou concluído')

    def __str__(self):
        return '{0} ({1})'.format(self.name,self.status)

    def __int__(self):
        return self.idcode

    def getDate(self):
        return self.date

    def getArchive(self):
        return self.archive

    def getCategory(self):
        return self.category

    def get_absolute_url(self):
        return reverse('process-detail', args=[str(self.id)])
# Create your models here.
