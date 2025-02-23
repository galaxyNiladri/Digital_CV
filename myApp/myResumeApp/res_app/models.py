from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class PersonalDetails(models.Model):
    name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=20)
    address = models.TextField()


class Education(models.Model):
    degree = models.CharField(max_length=100)
    institute_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    grade = models.DecimalField(max_digits=3, decimal_places=2)


class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = RichTextField()


class Skills(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=20)


class Awards_recognitions(models.Model):
    description = RichTextField()

class Certifications(models.Model):
    description = RichTextField()
