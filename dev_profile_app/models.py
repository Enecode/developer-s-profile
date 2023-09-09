from django.db import models
from django.urls import reverse


class AllData(models.Model):
    developers = models.ManyToManyField('Developer', blank=True)
    projects = models.ManyToManyField('Project', blank=True)
    stacks = models.ManyToManyField('Stack', blank=True)
    technologies = models.ManyToManyField('Technology', blank=True)

    def __str__(self):
        return f"{self.developers} {self.projects} {self.stacks} {self.technologies}"

class Developer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to='developers/', null=True, blank=True)
    stacks = models.ManyToManyField('Stack', blank=True)
    projects = models.ManyToManyField('Project', blank=True)
    email = models.EmailField()
    bio = models.TextField()
    skills = models.CharField(max_length=250)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    website = models.URLField(blank=True)
    
    GENDER_STATUS = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    address = models.CharField(max_length=220)
    gender = models.CharField(max_length=20, choices=GENDER_STATUS, default='male')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse('developer_detail', args=[str(self.id)])


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    technologies = models.ManyToManyField('Technology', blank=True)
    project_url = models.URLField()

    def __str__(self):
        return self.title

class Stack(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
