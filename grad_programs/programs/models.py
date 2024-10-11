from django.db import models

class GraduateProgram(models.Model):
    graduate_program = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    qualifications = models.JSONField(null=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.graduate_program} - {self.university}"

