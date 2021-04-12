from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


def validate_my_age(age):
    if age < 20:
        raise ValidationError("Age you entered is invalid")


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    age = models.PositiveIntegerField(validators=[validate_my_age])
    address = models.CharField(max_length=50)


class Company(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    staff_no = models.PositiveIntegerField()


class Vehicle(models.Model):
    model = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()


class Driver(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    # for one to many relation: forward relation
    # v_detail = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    # for one to many relation: reverse relation
    # v_detail = models.ForeignKey(Vehicles, on_delete=models.CASCADE, related_name='vehicle_drivers')
    # one to one relation
    v_detail = models.OneToOneField(Vehicle, on_delete=models.CASCADE)


# Many to Many Relation ...........................................................................
# class User(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#
#
# class Group(models.Model):
#     name = models.ForeignKey(User, on_delete=models.CASCADE)
#     group = models.ForeignKey(User, on_delete=models.CASCADE)
#     status = models.BooleanField()


# .......... one to one .......................................................................
class User1(models.Model):
    name = models.CharField(max_length=100)


class Address(models.Model):
    street = models.CharField(max_length=100)


class UserDetail(models.Model):
    age = models.PositiveIntegerField()
    user = models.OneToOneField(User1, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)


# -------------------------------------------------------------------------

class Author(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    age = models.PositiveIntegerField()


class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_books')



