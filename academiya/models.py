from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Planet(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.name)

class Candidate(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    planet = models.ForeignKey('Planet', max_length=50, db_index=True, on_delete=models.CASCADE)
    age = models.IntegerField()
    email = models.EmailField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.name, self.planet, self.age, self.email)

class Answers(models.Model):
    value = models.CharField(max_length=150)
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return '{}'.format(self.value)




class Test_task(models.Model):
    orden = models.SlugField(unique=True)
    name = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)


class Master(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    planet = models.ForeignKey('Planet',max_length=50, db_index=True, on_delete=models.CASCADE, related_name="planet")
    orden = models.ForeignKey('Test_task', on_delete=models.CASCADE, related_name="ord")

    def get_master_planet(name):
        return Master.objects.all()

    def __str__(self):
            return '{}'.format(self.name, self.planet, self.orden)
