from django.db import models
from django_mysql.models import ListCharField
from django.contrib.auth.models import User
class result_model(models.Model):
    jobid = models.CharField(max_length=20, null=True, blank=True)
    jobname = models.CharField(max_length=20, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    Q_P = models.CharField(max_length=20)
    Q_P_S = models.TextField()
    PDB = models.FileField(upload_to="PDB/", max_length=300 , null=True , default=None , blank= True )
    DSM = models.TextField(blank = True)
    DMM = models.FileField(upload_to="DMM/", max_length=300, null=True, default=None , blank=True)
    MSF = models.FileField(upload_to="MSF/", max_length=300, null=True, default=None , blank=True)
    PC = models.CharField(max_length=100)
    List = models.FileField(upload_to="Mutation_list" , max_length=300 , null=True , blank=True , default=None)
    Forcefield = models.CharField(max_length=100 , blank=True)
    MLK = models.CharField(max_length=100 , blank=True)