from django.db import models


# class CommonInfo(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.PositiveIntegerField()

#     class Meta:
#         abstract = True


# class Student(CommonInfo):
#     home_group = models.CharField(max_length=5)


# class ExamCenter(models.Model):
#     center_name = models.CharField(max_length=50)
#     city = models.CharField(max_length=70)

# class Student(ExamCenter):
#     name = models.CharField(max_length=40)
#     roll = models.IntegerField()

from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class MyPerson(Person):
    class Meta:
        proxy = True

    def do_something(self):
       
        pass
