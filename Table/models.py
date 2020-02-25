from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100, default='')
    code = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100, default='')
    subject = models.ManyToManyField(Subject)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100, default='')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    roll = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name




