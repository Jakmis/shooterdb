from django.db import models

# Create your models here.
class Klub(models.Model):
    nazev = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nazev

class Strelec(models.Model):
    jmeno = models.CharField(max_length=50)
    prijmeni = models.CharField(max_length=50)
    datum_narozeni = models.DateField()
    klub = models.ForeignKey(Klub, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

class Trener(models.Model):
    jmeno = models.CharField(max_length=50)
    prijmeni = models.CharField(max_length=50)
    licence = models.CharField(max_length=100)
    trenuje = models.ManyToManyField(Strelec, related_name='trenéři')

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"