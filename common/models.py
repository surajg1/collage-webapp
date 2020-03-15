from django.db import models

# Create your models here.
class Admin(models.Model):
    a_name = models.CharField(max_length=200)
    a_email = models.CharField(max_length=200)
    a_password = models.CharField(max_length=200)

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=200)
    teacher_email = models.CharField(max_length=200)
    teacher_password = models.CharField(max_length=200)
    teacher_qualification = models.CharField(max_length=200)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    
class Slink(models.Model):
    link_name = models.CharField(max_length = 200)
    link = models.CharField(max_length = 200)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    
class Notice(models.Model):
    title = models.CharField(max_length = 200)
    link = models.CharField(max_length = 200)
    discription = models.CharField(max_length = 200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
class Ebook(models.Model):
    ebook_name = models.CharField(max_length = 200)
    link = models.CharField(max_length = 200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
 