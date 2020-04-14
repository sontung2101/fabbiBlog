from django.db import models


# Create your models here.
# Create your models here.

class DepartmentModel(models.Model):
    department_code = models.CharField(max_length=255, null=True, blank=True, unique=False)
    department_name = models.CharField(max_length=255, null=True, blank=True, unique=False)

    class Meta:
        verbose_name = 'Phong ban'
