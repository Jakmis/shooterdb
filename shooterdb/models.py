from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import JSONField
# Create your models here.
class Club(models.Model):
    club_id = models.CharField(max_length=10, unique=True, verbose_name="ID")
    name = models.CharField(max_length=100, verbose_name="Name")
    
    def __str__(self):
        return f"{self.club_id} - {self.name}"

class Person(models.Model):
    person_id = models.CharField(max_length=10, unique=True, verbose_name="ID")
    fname = models.CharField(max_length=50, verbose_name="First Name")
    sname = models.CharField(max_length=50, verbose_name="Surname")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Club")

    def __str__(self):
        return f"{self.person_id} - {self.fname} {self.sname} | {self.club}"

class Shooter(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"Shooter: {self.person}"

class Specialization(models.Model):
    TYPES = [
        ('rifle', 'Puška'),
        ('pistol', 'Pistole'),
        ('shotgun', 'Brokovnice'),
    ]
    code = models.CharField(max_length=20, choices=TYPES, unique=True)

    def __str__(self):
        return dict(self.TYPES).get(self.code, self.code)

class Trainer(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    specialization = models.ManyToManyField(Specialization)

    def __str__(self):
        return f"Trainer: {self.person}"
    
class Referee(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    specialization = models.ManyToManyField(Specialization)

    def __str__(self):
        return f"Referee: {self.person}"
    
class Gun(models.Model):
    TYPES_OF_GUNS = [
        ('rifle', 'Puška'),
        ('pistol', 'Pistole'),
    ]
    gun_type = models.CharField(max_length=20, choices=TYPES_OF_GUNS)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    caliber = models.CharField(max_length=20)
    owner = models.ForeignKey(Shooter, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.caliber})"

class Discipline(models.Model):
    name = models.CharField(max_length=100, verbose_name="Discipline Name")
    number_of_shots = models.IntegerField(verbose_name="Number of Shots")
    distance = models.IntegerField(verbose_name="Distance (m)")
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, verbose_name="Specialization")

    def __str__(self):
        return f"{self.name} - {self.distance}m ({self.number_of_shots} shots)"

class Category(models.Model):
    CATEGORIES = [
        ('muži', 'Muži'),
        ('junioři', 'Junioři'),
        ('dorostenci', 'Dorostenci'),
        ('ženy', 'Ženy'),
        ('juniorky', 'Juniorky'),
        ('dorostenky', 'Dorostenky'),
    ]
    name = models.CharField(max_length=20, choices=CATEGORIES, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return dict(self.CATEGORIES).get(self.name, self.name)

class Competition(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    disciplines = models.ManyToManyField(Discipline)
    categories = models.ManyToManyField(Category)
    organizer = models.ForeignKey(Club, on_delete=models.CASCADE, blank=True)
    referees = models.ManyToManyField(Referee, blank=True)

    def __str__(self):
        return f"{self.name} - {self.date}"
    
class Result(models.Model):
    shooter = models.ForeignKey(Shooter, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    series = models.JSONField(blank=True, null=True)
    score = models.IntegerField()
    center = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField()

    def __str__(self):
        return f"{self.shooter} - {self.competition} - {self.discipline} - {self.score}"