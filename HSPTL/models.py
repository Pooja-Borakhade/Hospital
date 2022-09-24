

from django.db import models

# Create your models here.


class Hospital(models.Model):
    Name = models.CharField(max_length= 200)
    Phone_num = models.BigIntegerField() 
    esta_year = models.DateField()

    class Meta:
        db_table = 'Hospital'
    def __str__(self) -> str:
        return f'{self.Name}'
    
class Owner(models.Model):
    Name = models.CharField(max_length= 200)

    hospi = models.OneToOneField('Hospital',on_delete=models.CASCADE)
    class Meta:
        db_table = 'Owner'

    def __str__(self) -> str:
        return f'{self.Name}'
    

class Department(models.Model ):
    Name = models.CharField(max_length= 200)

    hospi = models.ForeignKey('Hospital',on_delete=models.CASCADE)
    Total_Staff =  models.IntegerField()
    class Meta:
        db_table = 'Dept'

    def __str__(self) -> str:
        return f'{self.Name}'
    

class Doctor(models.Model):
    Name = models.CharField(max_length= 200)

    No_of_Doctor = models.IntegerField()
    speciality = models.CharField(max_length=100)
    department = models.ManyToManyField('Department')
    hospi = models.ForeignKey('Hospital',on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'Doctor'
    
    def __str__(self) -> str:
        return f'{self.Name}'
    




    