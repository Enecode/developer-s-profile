from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager, Group, Permission,
                                        PermissionsMixin)
from django.db import models
from django.urls import reverse

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

from django.db import models


class Developer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    profile_picture = models.ImageField(upload_to='images/', blank=True)
    technology_stacks = models.ManyToManyField('TechnologyStack')
    contact_email = models.EmailField(unique=True)
    bio = models.TextField()
    skills = models.CharField(max_length=250)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    website = models.URLField(blank=True)
    projects = models.ManyToManyField('Project')

    GENDER_STATUS = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    address = models.CharField(max_length=220)
    gender = models.CharField(max_length=20, choices=GENDER_STATUS, default='male')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.projects}"


    def get_absolute_url(self):
        return reverse('developer_detail', args=[str(self.id)])




class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    technologies_used = models.CharField(max_length=250)
    project_url = models.URLField()
    project_image = models.ImageField(upload_to='images/', blank=True)
    developer_project = models.ManyToManyField('Developer')

    def __str__(self):
        return f"{self.title} - {', '.join(str(developer) for developer in self.developer_project.all())}"
    
    def __str__(self):
        return self.developer_project

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])

class TechnologyStack(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=250)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('contact_detail', args=[str(self.id)])

class DeveloperProject(models.Model):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    is_currently_working = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.developer}"


    
    def get_absolute_url(self):
        return reverse('developer_project_detail', args=[str(self.id)])