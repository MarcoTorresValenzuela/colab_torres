from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length =128)
    last_name = models.CharField(max_length =128)
    
class Course(models.Model):
    name = models.CharField(max_length =128)
    description = models.CharField(max_length =500)
    
class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete = models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete = models.PROTECT)
    start_date = models.DateField()

class Student(models.Model):
    first_name = models.CharField(max_length =128)
    last_name = models.CharField(max_length =128)
    email = models.CharField(max_length =128)

class Subscription(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete = models.PROTECT)
    student_id = models.ForeignKey(Student, on_delete = models.PROTECT)
    