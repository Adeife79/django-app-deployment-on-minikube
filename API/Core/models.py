from django.db import models

# Create your models here.
class State(models.Model):
    state_name = models.CharField(max_length=60)
    state_code = models.CharField(max_length=8)

    def __str__(self):
        return self.state_name

class Local_government(models.Model):
    name = models.CharField(max_length=60)
    code = models.CharField(max_length=10)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ward(models.Model):
    ward_name = models.CharField(max_length=60)
    ward_code = models.CharField(max_length=10)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True,
    blank=True)
    local_government = models.ForeignKey(Local_government, on_delete=models.CASCADE, null=True,
    blank=True)

    def __str__(self):
        return self.ward_name

class Unit(models.Model):
    unit_name = models.CharField(max_length=60)
    unit_code = models.CharField(max_length=10)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True,
    blank=True)
    local_government = models.ForeignKey(Local_government, on_delete=models.CASCADE, null=True,
    blank=True)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True,
    blank=True)

    def __str__(self):
        return self.unit_name
   
class Voter_Register(models.Model):
    first_name = models.CharField(max_length=10)
    middle_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.CharField(max_length=20)
    address = models.CharField(max_length=60)
    date_of_birth = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True,
    blank=True)
    local_government = models.ForeignKey(Local_government, on_delete=models.CASCADE, null=True,
    blank=True)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True,
    blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True,
    blank=True)

